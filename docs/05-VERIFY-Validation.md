# Layer 5 — VERIFY：Objective Signal Validation（客觀信號驗證）

> 不要問「你做完了嗎」，要問「證據是什麼」。
> 效果目標：**錯誤成本 -50%**（在交付前攔下錯誤，而不是上線後）

---

## 為什麼需要這一層

AI 很會說「我覺得完成了」。但「覺得」不是驗收標準。

- 模型的信心 ≠ 結果正確
- 人工肉眼掃一遍 ≠ 系統化檢查
- 沒有客觀信號 → 錯誤被帶到下游 → 修復成本翻好幾倍

VERIFY 把「做完了嗎」換成五個可查的問題，每個都要有**證據**，不是感覺。

---

## 五層驗證模型

| 層 | 驗什麼 | 通過條件 | 證據範例 |
|----|--------|----------|----------|
| **Logic 邏輯** | 內容站得住、無矛盾 | 單元測試 / 型別檢查通過；事實正確 | 測試輸出、事實查核註記 |
| **Flow 流程** | STEPS 全做完、無缺口 | 每個 STEP 有對應產出，順序正確 | 步驟對照表、整合測試 |
| **Visual / 格式** | 外觀 / 格式符合規格 | 符合 `⑦ OUTPUT`，與參考範例一致 | 截圖、回歸比對、Vision 評分 |
| **Data 數據** | 數字對、算式驗過 | 獨立驗算一致；schema 驗證通過 | 驗算表、schema 驗證輸出 |
| **Business 商業** | 達成 GOAL、符合 RULES | `definition of done` 全滿足；關係人簽核 | KPI 數據、簽核紀錄、客戶回饋 |

---

## 具體做法

1. **打開 VAC 的 `⑧ ACCEPTANCE`**：那就是這次的驗收清單。

2. **套用 [tools/verify-checklist.json](../tools/verify-checklist.json)**：
   複製成 `<vac-id>-run-<n>.verify.json`，逐項填 `result`（pass/fail/na/pending）與 `evidence`。

3. **逐層要證據，不接受「應該可以」**：
   - Logic：把測試 / 查核結果貼上
   - Flow：列出每個 STEP 對到哪個產出
   - Visual：附截圖或比對結果
   - Data：附獨立驗算（不是複述模型的數字）
   - Business：對照 GOAL 的每一條 done 定義

4. **任何 `blocking` 項目 fail → 整體不算 done**：退回 [EXECUTE](04-EXECUTE-Tools.md) 修，
   或若是規格問題，退回 [VAC](02-VAC-Specification.md) 改。

5. **通過後**：`signoff.decision = approved`，連同證據包交給 REVIEW。

---

## 產出物

| 項目 | 說明 |
|------|------|
| 已填的 `*.verify.json` | 五層結果 + 證據連結 + 六角度 REVIEW（下一層用） |
| 驗算 / 測試附件 | 獨立產生的證據，不是模型自述 |
| 簽核狀態 | approved / changes-requested / pending |

---

## 反模式 Anti-patterns

- ❌ **信心當證據**：「我已仔細檢查，沒問題」——沒有附件就是沒驗。
- ❌ **只驗 Logic**：程式跑得動，但數字錯 / 不符 GOAL。
- ❌ **Data 用模型自己的數字**：要獨立驗算，不能請它「再算一次」就當驗過。
- ❌ **Visual 靠口頭**：「排版看起來 OK」→ 附截圖或回歸比對。
- ❌ **blocking fail 卻放行**：把已知缺陷帶到下游。
- ❌ **驗收標準是驗的時候才想**：那叫事後合理化，不叫驗收。

---

## 檢查清單

- [ ] 用的是 VAC `⑧ ACCEPTANCE` + `verify-checklist.json`，不是臨時想的標準
- [ ] Logic：有測試 / 型別 / 事實查核的實際輸出
- [ ] Flow：每個 STEP 都能對到一個產出，無跳步
- [ ] Visual：有截圖 / 回歸比對 / 格式比對，符合 `⑦ OUTPUT`
- [ ] Data：有**獨立**驗算，數字與算式一致
- [ ] Business：GOAL 的每條 done 定義都滿足，未違反 RULES
- [ ] 所有 `blocking` 項目為 pass
- [ ] `signoff.decision` 已明確設定
- [ ] 證據包完整，可交給 REVIEW

---

## 範例

**交付物**：一份「每份成本 ≤ ¥35」的新菜單規格。

- Logic：食材 → 分量 → 單價 的對應表沒有漏項、單位一致 ✅（附對應表）
- Flow：STEP 1–4（分析偏好 / 草擬 / 試做 / 定版）都有對應文件 ✅
- Visual：規格書格式符合範本，欄位齊全 ✅（附截圖）
- Data：**用試算表獨立重算**每份成本 = ¥31.8，與規格書一致 ✅（附試算表）
- Business：素食客滿意度預估 +22%，達 GOAL 的 +20%；成本 ¥31.8 未破 ¥35 上限 ✅

blocking 全 pass → approved → 交 REVIEW。

---

## 與前後層的銜接

- **上游**：[Layer 4 — EXECUTE](04-EXECUTE-Tools.md) 的交付物 + 執行證據。
- **下游**：通過驗證的結果 + `verify.json` → **[Layer 6 — REVIEW](06-REVIEW-Quality.md)** 換人用新脈絡審。
- **迴圈**：常常 fail 的那一層，通常代表 VAC 的 ACCEPTANCE 或 STEPS 要補強 → [Layer 7 — LEARN](07-LEARN-Scaling.md)。

---

## 延伸

- 一句話：**每一條「通過」後面都要掛得出一個附件。**
- 資料檔：[tools/verify-checklist.json](../tools/verify-checklist.json)
