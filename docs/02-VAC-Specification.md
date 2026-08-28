# Layer 2 — VAC：Visual Agent Checklist（可執行規格合約）

> 把模糊需求，變成「任何 LLM 都能照著做」的規格。
> 效果目標：**學習成本 -70%**（重複任務不必每次重新摸索）

---

## 為什麼需要這一層

VAD 讓大家看到終點，但「看得到」不等於「做得出」。
AI 需要的是**結構化、無歧義、可驗收**的指令，而不是一段對話。

沒有 VAC 的世界：
- 每次交辦都要重講一遍背景
- 換一個人 / 換一個模型，知識就流失
- 「這次為什麼跟上次不一樣？」——因為沒有規格

有 VAC 的世界：
- 規格寫一次，之後複製、改 10%、再執行
- 規格是**組織資產**，不是某個人腦裡的默契
- 規格可以被 [tools/vac-validator.py](../tools/vac-validator.py) 自動檢查

---

## 核心觀念

**Structure beats conversation.**

一份 VAC = 8 個要素。缺一個，執行者就得猜；一猜，就開始來回。

| # | 要素 | 回答的問題 |
|---|------|-----------|
| ① | GOAL | 最終想達成的狀態是什麼？ |
| ② | INPUT | 需要哪些資料？來源與格式？ |
| ③ | ASSETS | 有哪些現成資源可用？ |
| ④ | RULES | 限制與邊界是什麼？ |
| ⑤ | STEPS | 怎麼執行？順序與決策點？ |
| ⑥ | TOOLS | 用哪些模型 / 外部服務？ |
| ⑦ | OUTPUT | 交付物長什麼樣？存哪裡？ |
| ⑧ | ACCEPTANCE | 怎樣算驗收通過（客觀）？ |

---

## 具體做法

1. **複製範本**：把 [templates/VAC-Template.md](../templates/VAC-Template.md) 另存為
   `VAC-<id>-v1.0-<slug>.md`。

2. **從 VAD 搬料**：
   - VAD 的「一句話 deliverable」→ `① GOAL`
   - VAD 的「參考正反例」→ `③ ASSETS`
   - VAD 的「成功定義」→ `⑧ ACCEPTANCE` 的雛形

3. **逐格填，不留佔位符**：空格 = 尚未想清楚 = 執行時會出事。

4. **RULES 要可量化**：至少一個數字（成本上限 / 頁數 / 時限 / 百分比）。

5. **STEPS 標決策點**：「如果 X 就 A，否則 B」要寫出來，別讓模型臨場發揮。

6. **TOOLS 指名層級**：不是「用 AI」，而是「Opus 探索 / Haiku 執行 / Agent 自動化」。

7. **ACCEPTANCE 對齊五層 VERIFY**：Logic / Flow / Visual / Data / Business 各至少一條，
   每條要能被別人不問作者就標 pass/fail。

8. **驗證**：
   ```bash
   python tools/vac-validator.py VAC-001-v1.0-xxx.md
   ```
   有 error 就回去補，通過再交給模型。

---

## 產出物

| 項目 | 說明 |
|------|------|
| `VAC-<id>-v1.0-<slug>.md` | 8 要素完整、通過 validator |
| 存放位置 | 團隊知識庫的對應領域資料夾 |
| 狀態 | `draft` → `validated` → `in-use` → `stable` |

---

## 反模式 Anti-patterns

- ❌ **把對話當規格**：「你知道我意思」——模型不知道。
- ❌ **GOAL 寫成流程**：「先做 A 再做 B」是 STEPS，不是 GOAL。GOAL 是終點狀態。
- ❌ **ACCEPTANCE 主觀**：「看起來要專業」→ 無法驗收。
- ❌ **RULES 沒有數字**：「要快、要便宜」→ 多快？多便宜？
- ❌ **一份 VAC 想涵蓋所有情況**：拆成多份小 VAC，各自可複用。
- ❌ **填完就丟，不跑 validator**：弱規格會在執行階段用 10 倍成本反噬。

---

## 檢查清單

- [ ] 8 個要素都有，且非骨架 / 非佔位符
- [ ] GOAL 是可驗收的終點狀態，沒有「優化一下 / 更好」這類空話
- [ ] 每個 INPUT 標了來源與格式，且標記 ready 或「執行時提供」
- [ ] RULES 至少一個可量化限制
- [ ] STEPS 有編號、有時程、決策點寫成 if/else
- [ ] TOOLS 指名具體模型層級
- [ ] OUTPUT 指定檔型、結構、命名、存放位置
- [ ] ACCEPTANCE 每層 VERIFY 至少一條、可 pass/fail
- [ ] `vac-validator.py` 無 error
- [ ] 指定了人工簽核負責人

---

## 範例

見 [templates/VAC-Template.md](../templates/VAC-Template.md) 末尾的「60 秒短影音」完整實例，
以及 [case-studies/](../case-studies/) 的各行業 VAC。

---

## 與前後層的銜接

- **上游**：[Layer 1 — VAD](01-VAD-Visual-Design.md) 的一頁視覺稿。
- **下游**：VAC 完成後進入 **[Layer 3 — ROUTE](03-ROUTE-Intelligent-Routing.md)**，
  決定這次要用哪個成本層級的模型。
- **迴圈**：每次執行後的心得，folded 進 `v1.1`（見 [Layer 7 — LEARN](07-LEARN-Scaling.md)）。

---

## 延伸

- 一句話：**規格寫一次，之後只改 10%。**
- 版本命名：`VAC-045-v1.0-...` → `v1.1`（小改）→ `v2.0`（大改）。
