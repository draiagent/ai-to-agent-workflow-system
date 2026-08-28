# Layer 7 — LEARN：Knowledge Consolidation & Organizational Scaling（知識沉澱與組織擴展）

> 把每一次成功，變成組織的資產。
> 效果目標：**重複成本 -90%**（第 10 次只要第 1 次的一小部分）

---

## 為什麼需要這一層

一次性完成任務，價值是線性的：做一件、得一件。
把方法沉澱下來，價值才會複利：做一件、下次快 10 倍、再下次自動。

沒有 LEARN：
- 每個人的訣竅留在自己腦裡，離職就流失
- 新人每次都從零學
- 同一類任務永遠是 ¥50 + 2 小時

有 LEARN：
- 訣竅寫進 VAC v1.1，變成可複製的規格
- 再抽象成 Skill，任何人 / 任何模型都能套
- 穩定後交給 Agent，變成 ¥0.5 + 自動

---

## 三步（其實是四動作）學習循環

```
1. Extract  從這次執行萃取「有效的方法」
2. Update   把心得 folded 進 VAC → 產出 v1.1
3. Store    抽象成可複用的 Skill，存進知識庫
4. Automate 步驟穩定後，接上低成本 Agent，下次自動跑
        ↓
   下一個同類任務：用 v1.1 + 便宜模型（或 Agent）
```

---

## 具體做法

1. **Extract — 萃取（做完當下就做，別拖）**
   - 這次哪一步比預期順 / 卡？為什麼？
   - VERIFY / REVIEW 抓到什麼？根因是什麼？
   - 有沒有可重用的片段（提示詞、檢查點、資料表結構）？

2. **Update — 更新 VAC → v1.1**
   - 把新的邊界寫進 `④ RULES`
   - 把踩過的坑寫進 `⑤ STEPS` 的決策點 / fallback
   - 把 REVIEW 常見問題寫進 `⑧ ACCEPTANCE`
   - metadata：版本 `v1.1`、更新日期、變更摘要

3. **Store — 抽象成 Skill**
   - 命名：`SKILL-<id>-v1.0-<slug>.md`
   - 內容：適用情境、觸發時機、輸入輸出、步驟骨架、常見錯誤
   - 存進知識庫對應領域，並在索引登記一行

4. **Automate — 接 Agent**
   - 判準：VAC 穩定、步驟固定、跑過多次都通過驗收
   - 動作：把 `⑥ TOOLS` 改成 Agent，接排程 / webhook
   - 保留降級路徑：Agent 連續失敗 → 轉回人工帶跑一次並再更新 VAC

---

## 產出物

| 項目 | 說明 |
|------|------|
| VAC `v1.1` | 心得已 folded，版本紀錄更新 |
| `SKILL-<id>-v1.0-<slug>.md` | 可複用技能卡，已進知識庫索引 |
| 自動化設定（若適用） | Agent 觸發方式 + 降級規則 |
| 學習筆記 | Extract 的原始觀察（供日後回溯） |

---

## 反模式 Anti-patterns

- ❌ **做完就下一件**：最有價值的一步被跳過。
- ❌ **心得留在腦裡 / 聊天記錄裡**：沒進 VAC 就等於沒沉澱。
- ❌ **只更新這一份 VAC，不抽象成 Skill**：換個相近任務又要重寫。
- ❌ **步驟還不穩就自動化**：Agent 把不穩定的流程放大成規模化的錯誤。
- ❌ **自動化後沒有降級路徑**：Agent 壞掉時整條線停擺。
- ❌ **Skill 不進索引**：存了等於沒存，沒人找得到。

---

## 檢查清單

- [ ] 執行後**當下**就做了 Extract，記下原始觀察
- [ ] VAC 已更新為 `v1.1`，RULES / STEPS / ACCEPTANCE 都吸收了心得
- [ ] 版本紀錄有這次的變更摘要
- [ ] 已產出 `SKILL-<id>-v1.0-<slug>.md` 並登記進知識庫索引
- [ ] 若已自動化：判準（穩定 + 多次通過）成立，且有降級規則
- [ ] 成本與次數已回填 VAC metadata（給 ROUTE 下次判斷用）

---

## 範例

**任務**：第 3 次做「blog 封面說明圖」，這次終於順。

- Extract：卡點是「AI 產的圖字太多」；解法是提示詞加「圖上文字 ≤ 6 字」。
- Update：`VAC-072` → `v1.4`，`④ RULES` 增一條「封面文字 ≤ 6 字」，
  `⑧ ACCEPTANCE` 的 Visual 增一條「無多餘說明文字」。
- Store：`SKILL-072-v1.0-blog-cover-explainer.md`，寫明「何時用、輸入是文章標題+重點、
  輸出是 1200×630 PNG、常見錯誤是文字過多」。索引加一行。
- Automate：已跑過 3 次且都通過 → `⑥ TOOLS` 改 Agent，接 CMS 發文 webhook；
  降級規則：連續 2 張 Visual 不過 → 轉 Haiku 人工一次並更新 VAC。

結果：第 4 次起，¥0.5 + 自動。

---

## 與前後層的銜接

- **上游**：[Layer 6 — REVIEW](06-REVIEW-Quality.md) 標為 `approved` 的交付，加上 VERIFY/REVIEW 的發現。
- **下游 / 迴圈**：更新後的 VAC + 新 Skill 回到 **[Layer 1 — VAD](01-VAD-Visual-Design.md)** /
  **[Layer 3 — ROUTE](03-ROUTE-Intelligent-Routing.md)**，讓下一輪更快、更便宜。
- 完整迴圈說明見 **[08 — Complete Loop](08-Complete-Loop.md)**。

---

## 延伸

- 一句話：**做完不是終點，沉澱才是。第一次聰明，之後自動。**
- 相關：[templates/VAC-Template.md](../templates/VAC-Template.md) 的版本紀錄區塊。
