#!/usr/bin/env python3
"""
vac-validator.py — 檢查一份 VAC 是否「可交給 LLM/Agent 執行」。

用法:
    python tools/vac-validator.py path/to/VAC-001-v1.0-example.md
    python tools/vac-validator.py templates/VAC-Template.md --allow-template
    python tools/vac-validator.py my-vac.md --json

規則對應 templates/VAC-Template.md 的八要素與飛行前檢查清單。
只用 Python 標準函式庫，無需安裝任何套件，也不呼叫任何外部 API。

離開碼:
    0  通過（沒有 error）
    1  有 error（VAC 尚未就緒）
    2  用法錯誤 / 找不到檔案
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# 八個必要區塊：接受 "① GOAL"、"1. GOAL"、"GOAL" 等寫法
REQUIRED_SECTIONS = [
    ("GOAL", ["①", "1"]),
    ("INPUT", ["②", "2"]),
    ("ASSETS", ["③", "3"]),
    ("RULES", ["④", "4"]),
    ("STEPS", ["⑤", "5"]),
    ("TOOLS", ["⑥", "6"]),
    ("OUTPUT", ["⑦", "7"]),
    ("ACCEPTANCE", ["⑧", "8"]),
]

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$", re.MULTILINE)

# 佔位符 / 尚未填寫的訊號
PLACEHOLDER_HINTS = [
    "_one line", "_name / team", "yyyy-mm-dd", "todo", "tbd", "fixme",
    "填寫", "待填", "placeholder", "xxx", "<id>", "vac-000",
]

# GOAL 常見的空話
VAGUE_WORDS = ["nice", "better", "good", "some", "improve", "更好", "優化一下", "做一下", "處理一下"]


def find_sections(text: str) -> dict[str, str]:
    """回傳 {正規化區塊名: 該區塊的內容文字}。"""
    headings = list(HEADING_RE.finditer(text))
    sections: dict[str, str] = {}
    for i, m in enumerate(headings):
        title = m.group(1).strip()
        start = m.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        body = text[start:end].strip()
        key = normalize_heading(title)
        if key:
            sections[key] = body
    return sections


def normalize_heading(title: str) -> str | None:
    upper = title.upper()
    for name, _prefixes in REQUIRED_SECTIONS:
        # 去掉編號符號後比對開頭字
        stripped = re.sub(r"^[\s\d.、①②③④⑤⑥⑦⑧()\-—–:：]+", "", upper).strip()
        if stripped.startswith(name):
            return name
    return None


def looks_empty(body: str) -> bool:
    """區塊是否實質為空（只剩表格骨架 / 佔位符 / 破折號）。"""
    meaningful = []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith(("|", ">", "<!--")):
            # 表格分隔列或引用範例，略過
            if set(s) <= set("|-: "):
                continue
        # 純骨架：| | | |
        if re.fullmatch(r"[|\-:\s]+", s):
            continue
        # 空的清單項
        if s in {"-", "*", "- **Must:**", "-"}:
            continue
        meaningful.append(s)
    joined = " ".join(meaningful).lower()
    if not meaningful:
        return True
    if len(joined) < 12:
        return True
    if any(h in joined for h in PLACEHOLDER_HINTS):
        # 若整段幾乎只有佔位符
        non_ph = re.sub("|".join(re.escape(h) for h in PLACEHOLDER_HINTS), "", joined)
        if len(non_ph.strip()) < 12:
            return True
    return False


def validate(text: str, *, allow_template: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    sections = find_sections(text)

    for name, _ in REQUIRED_SECTIONS:
        if name not in sections:
            errors.append(f"缺少必要區塊: {name}")
            continue
        body = sections[name]
        if looks_empty(body):
            if allow_template:
                warnings.append(f"{name}: 尚未填寫（--allow-template，僅警告）")
            else:
                errors.append(f"{name}: 區塊是空的或只有骨架 / 佔位符")

    # GOAL 額外檢查：不要出現空話、至少一句話
    if "GOAL" in sections and not looks_empty(sections["GOAL"]):
        g = sections["GOAL"].lower()
        hit = [w for w in VAGUE_WORDS if re.search(rf"(^|\W){re.escape(w)}(\W|$)", g)]
        if hit:
            warnings.append(f"GOAL 含模糊字眼: {', '.join(sorted(set(hit)))} — 換成可驗收的結果")

    # RULES 至少一個可量化限制（數字 / 日期 / 幣別 / 百分比）
    if "RULES" in sections and not looks_empty(sections["RULES"]):
        if not re.search(r"\d", sections["RULES"]):
            warnings.append("RULES 沒有任何數字 — 建議加入可量化的成本 / 時間 / 規格上限")

    # STEPS 應該有編號
    if "STEPS" in sections and not looks_empty(sections["STEPS"]):
        if not re.search(r"(^|\n)\s*(\d+[.)、]|\|\s*\d+\s*\|)", sections["STEPS"]):
            warnings.append("STEPS 看起來沒有編號步驟")

    # ACCEPTANCE 應該有可勾選項或 pass 條件
    if "ACCEPTANCE" in sections and not looks_empty(sections["ACCEPTANCE"]):
        if "☐" not in sections["ACCEPTANCE"] and not re.search(
            r"\[[ xX]\]|pass|通過|驗收", sections["ACCEPTANCE"]
        ):
            warnings.append("ACCEPTANCE 沒有可勾選 / pass-fail 條件 — 驗收會變主觀")

    # TOOLS 應指名模型層級
    if "TOOLS" in sections and not looks_empty(sections["TOOLS"]):
        if not re.search(
            r"opus|haiku|sonnet|gpt|gemini|claude|agent|模型|mini",
            sections["TOOLS"], re.IGNORECASE,
        ):
            warnings.append("TOOLS 沒有指名具體模型層級（只寫 'AI' 不夠）")

    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="驗證一份 VAC 是否可執行")
    ap.add_argument("path", help="VAC markdown 檔路徑")
    ap.add_argument("--allow-template", action="store_true",
                    help="把空區塊降級為警告（用於檢查範本本身）")
    ap.add_argument("--json", action="store_true", help="以 JSON 輸出結果")
    args = ap.parse_args(argv)

    p = Path(args.path)
    if not p.is_file():
        print(f"找不到檔案: {p}", file=sys.stderr)
        return 2

    text = p.read_text(encoding="utf-8")
    errors, warnings = validate(text, allow_template=args.allow_template)
    ok = not errors

    if args.json:
        print(json.dumps(
            {"file": str(p), "ok": ok, "errors": errors, "warnings": warnings},
            ensure_ascii=False, indent=2,
        ))
    else:
        print(f"VAC 驗證: {p}")
        print("-" * 48)
        for e in errors:
            print(f"  ✗ ERROR   {e}")
        for w in warnings:
            print(f"  ! WARN    {w}")
        if ok and not warnings:
            print("  ✓ 八要素齊全，沒有發現問題。可以交給 LLM/Agent 執行。")
        elif ok:
            print(f"\n  通過（{len(warnings)} 個警告）— 建議修掉警告再執行。")
        else:
            print(f"\n  未通過：{len(errors)} 個 error，{len(warnings)} 個警告。")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
