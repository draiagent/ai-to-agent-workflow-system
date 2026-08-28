# VAC Template — Visual Agent Checklist

> 把模糊需求轉成「任何 LLM 都能執行」的規格合約。
> Copy this file, rename to `VAC-XXX-v1.0-<slug>.md`, fill in all 8 elements, validate, then hand to an LLM/Agent.

---

## How to use

1. **Copy** this file into your knowledge base as `VAC-<id>-v1.0-<short-name>.md`.
2. **Fill** all 8 elements below. Do not leave placeholders — an empty field means the spec is not ready.
3. **Validate** with the checklist at the bottom (or `tools/vac-validator.py`).
4. **Execute**: paste the whole VAC into Claude / GPT / Gemini with the run prompt in [CLAUDE.md](../CLAUDE.md).
5. **Learn**: after a successful run, fold lessons into `v1.1` and store it as a reusable Skill.

Routing hint (see [README](../README.md) → ROUTE):

| Situation | Model | Cost |
|-----------|-------|------|
| First time / unknown method | Opus / GPT-4 class | ¥50 |
| Known task, VAC exists | Haiku / mini class | ¥5 |
| Fully repeatable | Agent automation | ¥0.5 |

---

## Metadata

| Field | Value |
|-------|-------|
| VAC ID | `VAC-000` |
| Version | `v1.0` |
| Title | _one line, what this workflow produces_ |
| Owner | _name / team_ |
| Domain | _biotech / food service / short video / education / coaching / ops …_ |
| Created | `YYYY-MM-DD` |
| Last run | `—` |
| Status | `draft` → `validated` → `in-use` → `stable` |
| Reusable Skill | _link once created_ |

---

## ① GOAL — 最終想達成的狀態

_What is the finished, verifiable end state? One or two sentences. No process talk here — describe the destination, not the route._

- **Deliverable in one line:**
- **Why it matters (business trigger):**
- **Definition of done (plain language):**

> ✅ Good: "3 份完整菜單規格（含食譜、營養分析、每份成本），素食客滿意度預估 +20%"
> ❌ Bad: "做一下菜單"

---

## ② INPUT — 需要的資料與來源

_Everything the executor must be given. Name the source, the format, and where it is. If an input does not exist yet, that is a blocker — resolve it before running._

| # | Input | Format | Source / location | Ready? |
|---|-------|--------|-------------------|--------|
| 1 | | | | ☐ |
| 2 | | | | ☐ |
| 3 | | | | ☐ |

- **Attached with this VAC:**
- **Must be supplied at run time:**

---

## ③ ASSETS — 可用的資源與素材

_Reusable materials, people, systems, and prior work the executor may draw on. Distinct from INPUT: assets are capabilities/resources, inputs are the specific data for this run._

- **Reference material / examples / past outputs:**
- **Brand / style / templates:**
- **People or systems available (SME, test kitchen, API, DB):**
- **Existing VACs or Skills to build on:**

---

## ④ RULES — 限制與邊界

_Hard constraints. Anything that would make the output unacceptable if violated. Be specific and measurable._

- **Must:**
  -
- **Must not:**
  -
- **Budget / cost ceiling:**
- **Deadline / time box:**
- **Compliance / safety / legal:**
- **Tone / brand / format constraints:**

---

## ⑤ STEPS — 執行順序（含決策點與時程）

_The plan. Numbered, with owners, rough timing, and explicit branch points ("if X then …")._

| Step | Action | Owner | Timing | Decision point / branch |
|------|--------|-------|--------|-------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

- **Known risk points:**
- **Fallback if a step fails:**

---

## ⑥ TOOLS — 使用的模型與外部服務

_Which model tier, which external tools, and any MCP servers / scripts. Match the model to the task per the routing hint above._

| Purpose | Tool / model | Notes |
|---------|--------------|-------|
| Reasoning / drafting | | |
| Execution | | |
| Data / calculation | | |
| Validation | | |
| Automation (Agent) | | |

- **MCP servers / CLI / APIs:**
- **Output tooling (format conversion, publishing):**

---

## ⑦ OUTPUT — 交付物格式與標準

_Exact shape of what gets delivered. File type, structure, length, naming, where it lands._

- **Format:** _(md / pptx / xlsx / json / …)_
- **Structure / sections:**
- **Length or size target:**
- **File name & storage location:**
- **Example / reference of the desired result:**

---

## ⑧ ACCEPTANCE — 客觀驗收標準

_Objective, checkable signals — not "looks good". Each item is something a reviewer can mark pass/fail without asking the author. Mirror the 5-layer VERIFY model from the README._

| Layer | Criterion | Pass condition | Result |
|-------|-----------|----------------|--------|
| Logic | | | ☐ |
| Flow | | all STEPS complete, no gaps | ☐ |
| Visual / format | | matches OUTPUT spec & example | ☐ |
| Data | | numbers / calculations verified | ☐ |
| Business | | meets GOAL & RULES | ☐ |

**Sign-off:** _who approves, and by when_

---

## Pre-flight validation checklist

Run before handing the VAC to any model:

- [ ] GOAL is a specific end state, no vague words ("nice", "better", "some")
- [ ] Every INPUT row has a source and is marked ready — or listed as a run-time input
- [ ] ASSETS are real and reachable now
- [ ] RULES include at least one measurable constraint (cost, time, or spec)
- [ ] STEPS are numbered and have timing; branch points are explicit
- [ ] TOOLS name a specific model tier (not just "AI")
- [ ] OUTPUT names a file format, structure, and storage location
- [ ] ACCEPTANCE has at least one objective criterion per VERIFY layer
- [ ] A human sign-off owner is named

> If any box is unchecked → go back and fill it in. A weak VAC produces expensive iteration.

---

## Worked mini-example (60-second short video script)

```
① GOAL
一支 60 秒血糖管理短影音腳本，可直接進錄製，讓一般觀眾看完知道「餐後散步 10 分鐘」的作用。

② INPUT
- 目標受眾：注重健康的上班族（25–40）
- 語氣：教育但口語
- 平台：TikTok / Reels
- 現有 3 支影片模板（見 assets）

③ ASSETS
- 影片模板 3 款、品牌旁白指南、字幕樣式指南
- 過往表現最好的 2 支腳本

④ RULES
- 上限 60 秒（約 150 字）
- 結構必含 Hook → 說明 → CTA
- 2–3 個視覺轉場
- 不得宣稱療效

⑤ STEPS
1. 寫 Hook（前 5 秒）— 一個反直覺數據
2. 說明概念（40 秒）— 白話拆解
3. CTA（15 秒）— 明確下一步

⑥ TOOLS
- Claude Haiku（腳本生成，已有 VAC）
- 字數計算：腳本字數 ÷ 2.5 ≈ 秒數

⑦ OUTPUT
- Markdown、含時間戳
- 檔名：VAC-045-v1.0-short-video-60sec-output.md
- 存：Knowledge base → Short Video → Scripts

⑧ ACCEPTANCE
- Logic：資訊正確、無療效宣稱 ☐
- Flow：Hook/說明/CTA 三段齊全 ☐
- Visual：讀起來順、標了時間戳 ☐
- Data：字數換算 ≤ 60 秒 ☐
- Business：CTA 明確可執行 ☐
- Sign-off：內容負責人，錄製前一天
```

---

## Version history

| Version | Date | Change |
|---------|------|--------|
| v1.0 | `YYYY-MM-DD` | Initial |
| v1.1 | | Lessons from first run folded in |

---

**First time smart, every time after automatic. — ai-to-agent workflow system**
