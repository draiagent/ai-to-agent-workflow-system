# tools/

輔助腳本與資料檔。純標準函式庫，不需安裝套件，不呼叫外部 API。

| 檔案 | 用途 |
|------|------|
| `vac-validator.py` | 檢查一份 VAC 是否八要素齊全、可交給 LLM/Agent 執行 |
| `verify-checklist.json` | 機器可讀的驗收清單（五層 VERIFY ＋ 六角度 REVIEW） |
| `route-calculator.py` | _(待補)_ 依任務是否已知，估算模型層級與成本 |

---

## vac-validator.py

```bash
# 驗證一份填好的 VAC
python tools/vac-validator.py path/to/VAC-001-v1.0-example.md

# 檢查範本本身（空區塊只當警告）
python tools/vac-validator.py templates/VAC-Template.md --allow-template

# CI / 腳本用：JSON 輸出，error 時離開碼 1
python tools/vac-validator.py my-vac.md --json
```

檢查項目：

- 八個必要區塊（GOAL / INPUT / ASSETS / RULES / STEPS / TOOLS / OUTPUT / ACCEPTANCE）存在且非空
- 區塊不是只剩表格骨架或佔位符
- GOAL 無模糊字眼、RULES 至少一個數字、STEPS 有編號
- ACCEPTANCE 有可勾選 / pass-fail 條件
- TOOLS 指名具體模型層級

離開碼：`0` 通過、`1` 有 error、`2` 用法錯誤。

需求：Python 3.10+。

---

## verify-checklist.json

執行完 VAC 後，複製成 `<vac-id>-run-<n>.verify.json`，逐項填 `result`（`pass` / `fail` / `na` / `pending`）與 `evidence`。
所有 `blocking: true` 的項目都要 `pass`，`signoff.decision` 為 `approved`，才算 done。

結構對應 [README](../README.md) 的第 5 層 VERIFY 與第 6 層 REVIEW。
