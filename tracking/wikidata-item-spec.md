# FIREla — Wikidata 实体创建规格（网页操作 ~10 分钟）

> 目标：在 wikidata.org 创建 FIREla 实体（Q 编号），让 AI 引擎做实体消歧时
> 能把 "FIREla" 与官网/GitHub/许可证绑定。开源项目**无知名度门槛**，可创建。
> 需要一个 Wikidata 账号（注册即用，无审批）。

## 操作步骤

1. 登录 wikidata.org → Create a new item
2. 按下表填写 Label / Description / Aliases

## 顶层字段

| 字段 | 语言 | 值 |
|---|---|---|
| Label | en | FIREla |
| Label | zh-hans | FIREla |
| Description | en | Open-source Beancount ecosystem for privacy-first personal finance |
| Description | zh-hans | 开源的 Beancount 个人财务生态，主打隐私优先 |
| Aliases | en | FIREla app, FIREla project, firela-bot |

## Statements（声明）

| 属性 | 值 | 限定 |
|---|---|---|
| P31 (instance of) | Q341 (free software) | — |
| P31 (instance of) | Q21128366 (open-source software) | — |
| P856 (official website) | https://firela.io | — |
| P1324 (source code repository) | https://github.com/fire-la/firela-app | — |
| P1324 (source code repository) | https://github.com/fire-la/firela-bot | — |
| P275 (copyright license) | Q7603 (GNU AGPL-3.0) | — |
| P178 (developer) | （创建 Firela 开发者实体或先留空） | — |
| P407 (language of work) | Q7033 (Dart)？——语言为表述属性，可选 | — |
| P306 (operating system) | Android / iOS（pending，app 未上架可不填） | — |
| P571 (inception) | 2026-02-07（首 commit） | — |
| P2002 (Twitter) / P2037 (GitHub username) | fire-la（org）；GitHub org username 属性 P2037 用于个人，org 用 P1124 或 sameAs | — |

## sameAs / 外部标识

- 官网 P856 = firela.io（主）
- GitHub 组织：P1830? 建议用 sat (P1896)? ——最简：在「官方」页面的 sameAs 由
  firela.io 网站反向声明（JSON-LD sameAs 已含 Wikidata 创建后的 Q 编号，双向互指）

## 之后

- firela.io 的 JSON-LD（organization.jsonld）`sameAs` 数组加入：
  `https://www.wikidata.org/wiki/<Q编号>`
- 上线 docs.firela.io/faq 后，Wikidata 增补 P973 (described at URL)
