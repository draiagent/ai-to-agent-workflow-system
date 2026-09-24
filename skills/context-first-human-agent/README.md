# Context-First Human Agent

**AI to Agent 上位決策治理 Skill**

> **Context over Dogma · Problems over Benchmarks · People over Models · Outcome over Complexity**

## 核心主張

世界不存在一條適用所有人的標準道路。

Agent 應先理解**人、任務、情境、限制、時間與風險**，再決定該使用 Rule、Code、Search、RAG、LLM、Agent 或 Human-in-the-loop。

這個 Skill 的目的不是讓 Agent 更會「展示聰明」，而是讓它更會：

- 找出真正問題。
- 選擇最小充分複雜度。
- 根據使用者與任務動態調整。
- 避免 Benchmark Worship、Model Worship、Agent Everywhere。
- 將 AI 能力轉換成可理解、可執行、可驗證的人類成果。

## 四大原則

1. **Context over Dogma｜情境高於教條**
2. **Problems over Benchmarks｜問題高於跑分**
3. **People over Models｜人高於模型**
4. **Outcome over Complexity｜結果高於複雜度**

## 核心哲學

> **AI 的目的，不是證明機器有多聰明，而是讓更多人有能力把事情做好。**

## 與 AI to Agent 的關係

```text
Human Need
 ↓
Context
 ↓
VAD
 ↓
VAC
 ↓
Task Router
 ↓
Rule / Code / Search / Model / Agent
 ↓
Verify
 ↓
Human Outcome
```

## 與 Radical Hacker Persona 的關係

- `context-first-human-agent`：決定**怎麼思考與選路徑**。
- `radical-hacker-persona`：決定**用什麼視角挑戰假設與架構**。

因此 Context-First 應位於更上層，避免「為反骨而反骨」。


## 視覺圖卡導讀｜Visual Card Guide

本系列 4 張圖卡把 `context-first-human-agent` 從抽象原則轉成可教、可記、可執行的視覺流程。

### 01 / 04｜讓 AI 回歸人的問題

**主旨：People over Models。**

AI 的價值不在於炫耀模型有多聰明，而在於是否能讓更多人：

- **看得懂**：降低理解門檻。
- **用得起**：讓成本與工具門檻合理。
- **做得到**：把知識轉成可執行成果。

中心的「人的需求」代表本 Skill 的最終最佳化目標不是模型能力，而是 **Human Outcome**。

> 對應章節：People over Models、Broad Human Problems First、Human Context Adaptation。

---

### 02 / 04｜先理解人，再決定方法

**主旨：Context over Dogma。**

在選擇方法前，先理解五個條件：

1. **誰使用** → Person
2. **做什麼** → Task
3. **什麼環境** → Context
4. **有何限制** → Constraints
5. **目前階段** → Time / Stage

因此沒有一條技術路線適合所有人。應保持原則穩定，讓方法依情境調整。

圖卡底部四句即為本 Skill 的四大治理原則：

- 情境高於教條。
- 問題高於跑分。
- 人高於模型。
- 結果高於複雜度。

> 對應章節：Core Principles、Human Context Adaptation、Adaptive Depth。

---

### 03 / 04｜選擇足夠好用的工具

**主旨：Minimum Sufficient Intelligence。**

不要把所有問題都交給最大的模型或 Agent。先判斷任務性質，再選擇最低合理複雜度：

- 固定規則 → Rule
- 數值計算 → Code
- 即時資訊 → Search
- 複雜推理 → LLM / Model
- 跨工具執行 → Agent
- 高風險決策 → Human-in-the-loop

這張圖是完整版 Task Routing 的**教學收斂版**；完整規格另包含 Structured Processing、Retrieval / RAG、Choice、Score、Extract 等路由。

> 對應章節：Minimum Sufficient Intelligence、Task Routing、Outcome over Complexity。

---

### 04 / 04｜把人的需求，變成可驗證成果

**主旨：VAD / VAC → Execution → Verification。**

本 Skill 不停在「理解人」，而是把需求轉成可驗證成果：

```text
理解需求
   ↓
VAD：讓人看懂任務
   ↓
VAC：把任務說成可執行規格
   ↓
執行工具
   ↓
驗證成果
```

同時只保存完成當前任務所需的狀態，不把全部歷史塞回 Context：

```text
History ≠ State
Events → Semantic State → Relevant Context → Decision
```

最後用三個問題驗收：

- 問題解決了嗎？
- 使用者能行動嗎？
- 成本與風險合理嗎？

> 對應章節：VAD / VAC Integration、History ≠ State、Final Decision Rule。

---

## 圖卡與 Skill 一致性檢查

整體概念與 `SKILL.md` **高度一致，沒有核心邏輯衝突**。四張圖的敘事順序也成立：

```text
人的需求
  ↓
理解情境
  ↓
選擇工具
  ↓
VAD / VAC
  ↓
執行
  ↓
驗證結果
```

### 建議修正／統一

| 項目 | 現況 | 建議 |
|---|---|---|
| 第 3 張「複雜理解 → 模型」 | 意義正確但較寬 | 改成「複雜推理 → LLM」可與 SKILL 完全一致 |
| 第 3 張工具路由 | 為視覺精簡版 | 保留即可，但文件應註明完整版另含 RAG / Structured Processing / Choice / Score / Extract |
| 圖卡署名 | `AI Coach x CGM Coach｜2026 AI to Agent` | 若要與 GitHub 作者資訊完全一致，建議統一為 `AI Coach 益力康陳董 x CGM Coach 血糖教練｜2026 AI to Agent` |
| 第 1 張「讓 AI 回歸人的問題」 | 概念正確 | 若追求語意更自然，可改「讓 AI 回歸人的真實問題」；原句不構成邏輯錯誤 |
| 第 4 張 VAD / VAC 文案 | 「VAD 看懂任務・VAC 說清規格」 | 與方法論一致，適合作為教學短句；正式定義仍以 SKILL.md 為準 |

### 一致性結論

四張圖卡可視為同一 Skill 的四層視覺摘要：

> **People → Context → Routing → Verified Outcome**

核心邏輯保持一致：

> **先理解人，再理解任務；先選對方法，再增加智慧；最後用結果驗證。**


## 檔案

- [SKILL.md](./SKILL.md) — Agent 可直接讀取的完整技能規格。
- [CHANGELOG.md](./CHANGELOG.md) — 版本更新紀錄。

## Version

**v1.0.0 — 2026-09-25**

**AI Coach 益力康陳董 x CGM Coach 血糖教練 | 2026 AI to Agent**
