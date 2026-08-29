# 08 — The Complete Loop（完整迴圈）

> 七層不是一條直線，是一個會越跑越快的迴圈。

---

## 全貌

```
企業需求 / 使用者請求
        ↓
① VAD ──── 視覺化、對齊目標           （溝通成本 -80%）
        ↓
② VAC ──── 寫成 8 要素可執行規格       （學習成本 -70%）
        ↓
③ ROUTE ── 依「是否已知」分流模型層級   （人工成本 -60%）
        ↓
④ EXECUTE ─ 掛真實工具完成、留證據      （概念→產出以秒計）
        ↓
⑤ VERIFY ─ 五層客觀信號 + 證據         （錯誤成本 -50%）
        ↓
⑥ REVIEW ─ 換脈絡、六角度審視          （修改成本 -40%）
        ↓
⑦ LEARN ── 更新 VAC v1.1 + 抽 Skill + 自動化（重複成本 -90%）
        ↓
   ↺ 回到 ① / ③：下一輪更快、更便宜
```

---

## 企業價值軸（最底層）

```
VAD          →  VAC          →  Agent        →  Verify       →  Knowledge
降低溝通成本      降低學習成本      降低人工成本      降低錯誤成本      降低重複成本
```

**收斂為一句：**

```
企業導入 AI to Agent
= 增效 × 提速 × 降學習曲線 × 降錯誤 × 降返工 × 可複製
```

---

## 方法論哲學（最上層）

> 底層模型持續進化，我們不重造巨人；
> 用 VAD 看得更遠、VAC 站得更穩、AI to Agent 飛得更快。
> ——站在巨人肩膀上的「開源老鷹視野」。

模型會一直變強，這一層不與它競爭；它把模型的能力**收斂成可交付、可複製、可規模化**的組織資產。

---

## 執行閉環與工具綁定

七層在實際執行時收斂成一個帶工具綁定的閉環。Orchestrator 依任務把工作分派給
專業 Agent，每支 Agent 綁定當代最好的工具；Verify 對 VAC 規格驗收，Reuse 把
成功能力寫回企業 Know-how。

```
                 企業 KNOW-HOW
                      │
                      ↓
             ┌────── VAD ──────┐
             │ 讓需求被看見     │
             │ 讓資料被看懂     │
             │ 讓流程被理解     │
             └────────┬────────┘
                      ↓
                     VAC
             能力規格・執行方法
             工具規則・驗收標準
                      ↓
                ORCHESTRATOR
                      │
         ┌────────────┼────────────┐
         ↓            ↓            ↓
      UI Agent     Data Agent   Process Agent
         │            │            │
       Figma       Flint Chart    Mermaid
         │            │            │
         └────────────┼────────────┘
                      ↓
                   VERIFY
              結果是否符合規格？
                      ↓
                    REUSE
               成功能力持續重用
                      ↓
                 KNOW-HOW ↑
                      │
                      └────── ↺
```

對應七層：VAD＝①、VAC＝②、ORCHESTRATOR＝③ ROUTE、三支 Agent＋工具＝④ EXECUTE、
VERIFY＝⑤＋⑥、REUSE＝⑦ LEARN。工具（Figma／Flint／Mermaid …）是可替換的實作，
換工具不動閉環。

### 分層視角：上層一直換，底層持續累積

```
大模型持續升級   Claude / GPT / Gemini / ...   ↑ 一直換
工具持續升級      Figma / Flint / Mermaid / ...  ↑ 一直換
Agent 持續升級                                   ↑ 一直換
════════════════════════════════════════════════
企業能力治理層
        │
  VAD → VAC → VERIFY → REUSE → KNOW-HOW           ← 持續累積、不換
════════════════════════════════════════════════
```

**核心主張：**

> VAD 讓需求、資料與流程被看見；VAC 讓成功方法被保存；專業 Agent 負責執行；
> Verify 確保正確；Reuse 讓企業能力持續複利。
>
> 模型會換、工具會換、Agent 會換；企業真正不能換掉的，是自己的 Know-how。

---

## 迴圈為什麼會加速

| 第 N 次 | 走哪幾層 | 模型層級 | 成本 / 時間（示意） |
|---------|----------|----------|---------------------|
| 第 1 次 | ①→⑦ 全走，重點在 VAD/VAC/探索 | Opus 級 | ¥50 + 2 小時 |
| 第 2–10 次 | 直接從 ③ 進，用現成 VAC | Haiku 級 | ¥5 + 30 秒 |
| 第 11 次起 | ③ 判定「可重複」→ Agent | Agent | ¥0.5 + 自動 |

差異來源：**每一次的 ⑦ LEARN 都把「未知」沉澱成「已知 / 可重複」**，
於是下一輪 ③ ROUTE 可以合法地選更便宜的層級。

---

## 每一層的交接物（一眼看懂銜接）

| 層 | 吃什麼（上游） | 吐什麼（下游） |
|----|----------------|----------------|
| ① VAD | 模糊的一句話需求 | 一頁需求視覺稿（deliverable + 正反例 + Before/After + 成功定義） |
| ② VAC | 需求視覺稿 | `VAC-*.md`，8 要素齊全、過 validator |
| ③ ROUTE | 已驗證的 VAC | 模型層級決策（寫入 `⑥ TOOLS`）+ 升降級規則 |
| ④ EXECUTE | 層級決策 + VAC | 符合 `⑦ OUTPUT` 的交付物 + 執行證據包 |
| ⑤ VERIFY | 交付物 + 證據 | 已填的 `*.verify.json`，blocking 全 pass |
| ⑥ REVIEW | 通過驗證的交付物 | 六角度結果 + 決議（approved / changes-requested） |
| ⑦ LEARN | approved 交付 + 發現 | VAC `v1.1` + `SKILL-*.md` + （選用）Agent 自動化 |

---

## 迴圈的三個入口

1. **全新任務**：從 ① VAD 開始。
2. **相近任務（已有 VAC）**：從 ③ ROUTE 開始，複製 VAC 改 10%。
3. **可重複任務（VAC 穩定）**：由 Agent 在 ④ 觸發，⑤⑥ 縮成自動檢查 + 抽樣人工。

---

## 常見卡點與對應

| 症狀 | 多半是哪一層沒做好 | 對策 |
|------|--------------------|------|
| 交付後才發現方向錯 | ① VAD | 補正反例與成功定義，先對齊再動手 |
| 每次都要重講背景 | ② VAC | 把默契寫成規格，跑 validator |
| 成本失控 | ③ ROUTE | 建立「是否已知」判準與升降級閥值 |
| 模型說做完了其實沒做 | ④ EXECUTE | 要求每步留證據，禁止假執行 |
| 上線後才爆錯 | ⑤ VERIFY | 五層都要附件，Data 要獨立驗算 |
| 改 A 壞 B | ⑥ REVIEW | 換脈絡審 Scope / Regressions |
| 同一題永遠 ¥50 | ⑦ LEARN | 做完當下就沉澱 VAC + Skill |

---

## 相關文件

- 各層深入：[01 VAD](01-VAD-Visual-Design.md)、[02 VAC](02-VAC-Specification.md)、
  [03 ROUTE](03-ROUTE-Intelligent-Routing.md)、[04 EXECUTE](04-EXECUTE-Tools.md)、
  [05 VERIFY](05-VERIFY-Validation.md)、[06 REVIEW](06-REVIEW-Quality.md)、
  [07 LEARN](07-LEARN-Scaling.md)
- 規格範本：[templates/VAC-Template.md](../templates/VAC-Template.md)
- 驗收清單：[tools/verify-checklist.json](../tools/verify-checklist.json)
- 上手：[QUICKSTART.md](../QUICKSTART.md)｜對 AI 下規格：[CLAUDE.md](../CLAUDE.md)

---

**First time smart, every time after automatic. — ai-to-agent workflow system**
