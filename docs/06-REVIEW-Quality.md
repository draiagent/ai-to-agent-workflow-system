# Layer 6 — REVIEW：Multi-Perspective Quality Assurance（多角度品質審視）

> 用「全新脈絡」去看，抓自動測試漏掉的東西。
> 效果目標：**修改成本 -40%**（把返工擋在交付前）

---

## 為什麼需要這一層

VERIFY 回答「這個東西本身對不對」。REVIEW 回答一組不一樣的問題：

- 我們是不是**改對了地方**？
- 有沒有**過度設計**？
- 有沒有**副作用**弄壞別的東西？

這些問題自動測試常常抓不到，因為它們是關於**判斷與脈絡**，不是關於單一輸出。
關鍵字：**fresh context**——最好由沒有參與執行的人（或另開一個乾淨脈絡的模型）來審。

---

## 六個角度

| 角度 | 要問的問題 | 常見問題 |
|------|-----------|----------|
| **Scope 範圍** | 我們改的正好是該改的嗎？ | 改了功能 A，卻動到功能 B |
| **Complexity 複雜度** | 有沒有過度設計？ | 簡單問題套了三層抽象 |
| **Security 安全** | 有沒有漏洞 / 洩漏？ | 憑證被印到 console |
| **Edge Cases 邊界** | 什麼情況會壞？條件變了呢？ | 沒有資料時匯出直接失敗 |
| **Consistency 一致性** | 跟既有模式 / 風格一致嗎？ | 命名慣例和其他檔案不同 |
| **Regressions 迴歸** | 會不會弄壞別的東西？ | 更新模組讓相依程式壞掉 |

---

## 具體做法

1. **換人 / 換脈絡**：審的人不要是執行的人；用模型審時，開新對話、只給 VAC + 交付物 + `verify.json`。

2. **六個角度逐一過**：用上表的問題，逐項寫下發現與判斷（`verify-checklist.json` 的
   `review.perspectives[]` 已備好欄位）。

3. **分辨 blocking 與 non-blocking**：
   - blocking：Scope、Security、Regressions —— 有問題就退回。
   - non-blocking：Complexity、Edge Cases、Consistency —— 記錄成待辦 / 下版改。

4. **具體到可行動**：不是「感覺有點複雜」，而是「第 X 段的三層包裝可以拉平成一層」。

5. **給結論**：`approved` / `changes-requested`（附清單）/ `pending`（待補資訊）。

---

## 產出物

| 項目 | 說明 |
|------|------|
| 六角度審視結果 | 每個角度：發現 + 判斷 + blocking 與否 |
| 變更請求清單 | 若 `changes-requested`，逐條可行動 |
| 待辦 / 下版清單 | non-blocking 的改善點 |
| 最終決議 | approved / changes-requested / pending |

---

## 反模式 Anti-patterns

- ❌ **執行者自審**：看不到自己的盲點。
- ❌ **把 REVIEW 當第二次 VERIFY**：重覆檢查輸出對錯，卻沒問範圍 / 複雜度 / 副作用。
- ❌ **只給結論不給依據**：「覺得 OK」/「怪怪的」都不可行動。
- ❌ **blocking 和 nice-to-have 混在一起**：小建議卡住交付，或大問題被當小建議放掉。
- ❌ **審完不記錄**：同樣的問題下次再犯。

---

## 檢查清單

- [ ] 審視者不是執行者（或是全新脈絡的模型）
- [ ] 六個角度都逐一寫了發現與判斷
- [ ] Scope / Security / Regressions 任一有問題 → 標 blocking 並退回
- [ ] Complexity / Edge Cases / Consistency 的問題已記為待辦 / 下版
- [ ] 每條發現都具體到可行動
- [ ] 有明確最終決議
- [ ] non-blocking 的改善點已進 LEARN 的輸入清單

---

## 範例

**交付物**：把「客戶回饋分析」腳本從單檔擴成模組。

- Scope：只該動 analysis 模組，卻順手改了共用的 `io.py` 介面 → **blocking**，退回拆開。
- Complexity：新增了 3 層 strategy 抽象，但目前只有 1 種策略 → 記待辦，下版拉平。
- Security：回饋內含個資，log 有把姓名印出來 → **blocking**，改成遮罩。
- Edge Cases：回饋為 0 筆時會除以零 → 記待辦（附重現步驟）。
- Consistency：函式命名用 camelCase，專案其他都 snake_case → 記待辦。
- Regressions：`io.py` 介面改動會讓另外兩支腳本壞掉 → **blocking**。

決議：`changes-requested`，清單 2 條 blocking（Scope/`io.py`、Security/遮罩）。

---

## 與前後層的銜接

- **上游**：[Layer 5 — VERIFY](05-VERIFY-Validation.md) 通過的交付物 + 證據。
- **下游**：`approved` → 進 **[Layer 7 — LEARN](07-LEARN-Scaling.md)** 沉澱；
  `changes-requested` → 退回 [EXECUTE](04-EXECUTE-Tools.md) 或 [VAC](02-VAC-Specification.md)。
- **迴圈**：反覆出現的同類問題 → 寫進 VAC 的 RULES / STEPS，讓下次不會再發生。

---

## 延伸

- 一句話：**VERIFY 問「對不對」，REVIEW 問「該不該、會不會、值不值」。**
- 資料檔：[tools/verify-checklist.json](../tools/verify-checklist.json) 的 `review` 區塊。
