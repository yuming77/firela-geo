# FIREla — GEO 周运营循环 SOP（weekly-ops-loop）

> 版本 v1.0 · 2026-09-20 · 时间盒：每周 2-3 小时（周一集中 1.5h + 周中碎片 1h）
> 目标：让 GEO 从"一次性建设"变成**每周可执行的迭代循环**——测量 → 缺口分析 → 补内容 → 复盘

---

## 循环总览

```
周一（~1.5h）
 ├─ ① 测量：tracking/measurement-worksheet.html 打开 → 50 提示词 × 4 引擎逐条查（~30-40 分钟）
 ├─ ② 记录：结果填入表内 → 导出 geo-measurement-wN.csv → 与上周对比
 ├─ ③ 缺口分析：连续 2 周未命中的提示词 → 查 AI 实际引用了谁的什么页面（~20 分钟）
 └─ ④ 产出 1-3 条补内容任务（docs 页 / Medium / Reddit 回答 三选一通道）→ 进本周任务
周中（碎片 ~1h）
 └─ ⑤ 执行补内容任务（写一篇/答一帖/改一页）
周五（~0.5h）
 └─ ⑥ 复盘：命中增量记入 KPI → 飞书周报 GEO 段（命中 X/50 · 新增引用 Y · 动作 Z）
```

---

## ① 测量（每周一，30-40 分钟）

- 工具：`tracking/measurement-worksheet.html`（浏览器直接打开，本地自动保存，可导出 CSV）
- 输入：`tracking/prompt-baseline.csv` 的 50 条提示词（品牌 8 / 品类 15 / 用例 15 / 对比 7 / 中文 5）
- 每条点 4 个引擎按钮 → 人工判定：FIREla 被提及？引用了我们的 URL？引用了竞品？
- 判定口径：**提及品牌名或任何 fire-la 域名链接 = Y**；只提品类不提品牌 = N（但记入备注，作为"品类可见"信号）

## ② 缺口分析（每周一，20 分钟）

对每个连续 2 周未命中的提示词：
1. 打开引用了竞品的答案 → 记录竞品被引的**页面 URL**（这就是要超越的具体内容）
2. 分类缺口：**缺内容**（我们没写过）/ **内容弱**（写过但深度/结构不如竞品）/ **无机会**（提示词本身价值低）
3. 产出补内容任务：`写一篇 <标题> 发 <通道>`，优先级 = 提示词商业价值 × 缺口大小

## ③-④ 补内容三通道

| 通道 | 适用 | 动作 |
|---|---|---|
| **docs.firela.io** | 教程/FAQ 类 | 新页answer-first 结构：结论在前、统计数字（10 解析器/11 类检测/29 国 IBAN）、来源标注、FAQPage JSON-LD |
| **Medium** | 深度长文 | 周更一篇；标题含查询关键词；文末附 fact-sheet 链接与 GitHub |
| **Reddit** | 社区讨论类 | 个人号 90/10 真实回答，披露开发者身份；不贴链接先立信任 |

**写前必读**：`fact-sheet-en/cn.md`（事实红线：基线外数字/未上架声明禁止）。

---

## ⑤ KPI 与节奏

| 指标 | 基线（首轮测出） | 30 天 | 90 天 |
|---|---|---|---|
| 品类+用例词 FIREla 被提及率 | ≈0% | ≥20% | ≥50% |
| 品牌词回答准确率（事实一致） | 未测 | ≥80% | ≥95% |
| 用例词引用 firela 域名 | 0 | ≥1 词 | ≥3 词 |
| 第三方权威位 | 0 | 2 | 3+ |

---

## 工具指针

- 测量工作表：`tracking/measurement-worksheet.html`（浏览器打开即用）
- 提示词源：`tracking/prompt-baseline.csv`（50 行）→ tracker 导出：`tracking/prompts.ts`
- 仪表盘（可选，需 Bright Data key）：`~/workspace/geo-aeo-tracker`（`npm run dev`）
- Wikidata 规格：`tracking/wikidata-item-spec.md`
- 列表申请文案：`listings/third-party-listings.md`
- 内容原料：`../fact-sheet-en/cn.md` + `../geo-faq.md`

## 升级路径

人工周测跑顺后（约 4 周），可选升级：geo-aeo-tracker 接 Bright Data key 自动批量测量（免费试用额度），或 elmo 开源平台托管——触发条件：人工测量累计 ≥4 轮且稳定产生可执行缺口。
