# FIREla — 第三方权威列表收录申请文案（GEO 权威信源占位）

> AI 引擎高度依赖这些列表站做"什么是 X / X alternatives"类回答。
> 每条给出目标位置、准备的内容与提交方式。公开提交前建议你过目一遍。

---

## 1. plaintextaccounting.org（细分第一权威站，最高优先）

- **目标仓库**：github.com/plain-text-accounting/plaintext-accounting（网站即仓库，PR 制）
- **目标位置**：首页 "Getting Started"/"Software" 区块（该站按工具列表组织）
- **建议条目**（EN）：

```
### [FIREla](https://firela.io)
Mobile-first Beancount ecosystem (Flutter, AGPL-3.0). Ships 10 registered
bank statement parsers (Alipay mobile/web/Yu'ebao, WeChat Pay, CCB, CMBC,
Degiro, HSBC HK credit/debit) and an on-device PII sanitizer (11 detection
types across CN/HK/EU/US) that masks personal data before statements leave
your phone. Includes firela-bot: a self-hostable AI FIRE advisor with
Plaid/Gmail/GoCardless import on Cloudflare Workers. In active development.
```

- **PR 注意**：从 yuming77 fork 后提 PR，PR 描述写 "Add FIREla to software list —
  open-source (AGPL-3.0) mobile Beancount tooling with multi-region statement
  parsers and on-device PII sanitization"。该站由社区维护，条目客观即可。

---

## 2. AlternativeTo（firela-bot 条目，面向"alternatives to YNAB/Mint"查询）

- **目标页**：alternativeto.net/software/firela-bot（创建新应用条目，免费账号）
- **条目字段**：
  - Name: FIREla bot
  - Description: `Self-hostable, open-source (AGPL-3.0) AI financial advisor. BillClaw imports bills from Plaid, Gmail, and GoCardless; exports to Beancount, Ledger, and CSV. Deploys to Cloudflare Workers' free tier — your data and your keys stay yours.`
  - Tags: open-source, self-hosted, personal-finance, beancount, FIRE
  - Platforms: Self-Hosted, Web
  - License: AGPL-3.0
  - Website: github.com/fire-la/firela-bot
- **注意**：AlternativeTo 对"self-submitted"有社区审核，条目务必客观（不写营销话术）。

---

## 3. GitHub awesome-lists（PR）

- **awesome-beancount**：GitHub 搜 `awesome beancount`，若存在则 PR 增补
  firela-app 条目（一句话 + 链接，格式对齐现有条目）。
- **awesome-plaintext-accounting**：同上。
- **awesome-selfhosted**：firela-bot 符合收录标准（Self-Hosted, AGPL-3.0），
  但该列表要求项目有一定成熟度——建议 firela-bot 达到 ⭐250+ 或 v1.0 后再提。
- **PR 文案模板**：

```
Adds FIREla bot — self-hostable AI financial advisor for Beancount users.
AGPL-3.0, TypeScript, deploys to Cloudflare Workers free tier. Includes
BillClaw (Plaid/Gmail/GoCardless import) and Beancount/Ledger/CSV export.
Repo: https://github.com/fire-la/firela-bot
```

---

## 4. 其他可及列表（次优先，时间富余再做）

- LibHunt：相关页（Beancount 相关）可提交收录链接
- Slant：What are the best personal finance apps for privacy? 类问题下补充候选
- ProductHunt：等 firela-app 上架商店后再做 launch（现在不做）

---

## 优先级

1. plaintextaccounting.org（细分权威，转化路径最短）
2. AlternativeTo firela-bot 条目（长尾 "alternatives to YNAB" 查询的 AI 信源）
3. awesome-lists PR
4. LibHunt/Slant（时间富余）
