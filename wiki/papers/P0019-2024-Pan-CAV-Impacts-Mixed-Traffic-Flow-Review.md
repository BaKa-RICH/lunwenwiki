---
type: paper
paper_id: P0019
title: "The impacts of connected autonomous vehicles on mixed traffic flow: A comprehensive review"
authors: "Yuchen Pan, Yu Wu, Lu Xu, Chengyi Xia, David L. Olson"
year: 2024
venue: "Review article"
status: read
confidence: medium
source_path: raw/papers/P0019-2024-Pan-CAV-Impacts-Mixed-Traffic-Flow-Review.md
zotero_key:
doi:
tags: [CAV, mixed-traffic-flow, review, traffic-efficiency, stability, safety, environment, policy, cybersecurity]
last_updated: 2026-04-29
---

# P0019: CAV Impacts on Mixed Traffic Flow Review

## 1. 一句话定位

这篇综述从 traffic efficiency、stability、safety、environment 和 policy 五个维度总结 CAV 对 mixed traffic flow 的系统性影响，适合作为本 wiki 的宏观背景和研究边界校准材料。

## 2. 核心贡献

- `EXTRACTED` 将 CAV 影响从单一交通效率扩展到效率、稳定性、安全、环境/能耗和政策建议的综合视角。
- `EXTRACTED` 梳理 AV/CAV 技术发展、自动驾驶等级、V2X/DSRC/C-V2X 通信以及主要企业/国家政策背景。
- `EXTRACTED` 总结 mixed traffic flow 中 CAV penetration rate、车辆控制、dedicated lane、road planning 等因素对交通效率的影响。
- `EXTRACTED` 综述 CAV 对 traffic oscillation、phantom congestion、string stability、safety conflict、cyberattack risk 和 emissions 的影响。
- `EXTRACTED` 提出未来研究应扩展控制框架，纳入 multimodal technologies、communication failures、network attacks、weather/noise 和 human-induced operations。

## 3. 方法抓手

- Review scope：围绕 CAV 在 mixed traffic 中对 efficiency/congestion 的核心影响，同时覆盖 stability、safety、environment 和 policy。
- Metric framing：traffic flow、average speed、vehicle count、road capacity、travel time、MPR、automation level、vehicle connectivity、safety 和 energy/emissions。
- Control taxonomy：longitudinal control、lateral lane-changing、intersection control、dedicated lane policy、DRL/distributed control、model predictive control。
- Risk taxonomy：communication delay/failure、cyberattack、privacy leakage、network security、HDV uncertainty、adverse weather、signal interference。
- Policy framing：美国、中国、日本、德国等政策文件对 AV/CAV 测试、运营、安全和监管的不同侧重。

## 4. 关键实验结论

- `EXTRACTED` 这是一篇综述，不提供新的仿真实验；其结论来自既有文献汇总。
- `EXTRACTED` 多篇研究表明 CAV penetration rate 增加通常提升 traffic efficiency、road capacity 和 mixed traffic stability，但影响可能是非线性的。
- `EXTRACTED` 有研究指出 CAV 对 traffic efficiency/safety 的最大收益可能出现在 20% 至 40% MPR 区间。
- `EXTRACTED` 低 MPR 下设置 CAV dedicated lane 可能不改善甚至降低整体 throughput，政策与 lane-use 规则需要依赖 penetration 条件。
- `EXTRACTED` cyberattack、high latency、communication failure 和 low penetration rate 可能引发危险交通行为或破坏安全距离。
- `EXTRACTED` 自动化对能耗和排放既可能有正效应，也可能因诱导需求、车速提升和出行群体扩大而产生负效应，长期净效应仍不确定。

## 5. 局限与隐含假设

- 论文自述局限：
  - 综述强调四个影响领域和政策建议，但没有对特定合流控制方法做可复现实验或统一 benchmark。
- 你识别到的隐含假设：
  - 综述范围很宽，和 on-ramp merging 的直接机制距离较远，不能直接作为合流算法 baseline。
  - 文献汇总中不同场景、自动化等级、CAV 定义、通信技术和仿真平台差异较大，结论不能简单横向比较。
  - 对交通效率、稳定性、安全和环境的关系多为概念级综合，缺少统一因果模型。
  - 政策建议对具体轨迹规划、合流排序或执行层控制的落地约束较弱。

## 6. 关系线索

- uses: [[wiki/concepts/cav-mixed-traffic-impact-review]], mixed traffic flow impact framing, MPR, traffic efficiency, stability, safety, environment, cybersecurity, policy。
- supports: [[wiki/gaps/confirmed-gaps]]，从宏观层面强化 GAP-0001 中 mixed traffic、communication/security 和部署条件的重要性。
- complements: [[wiki/concepts/field-experimental-communication-delay-cav-merging]]，P009 提供 delay field evidence，P0019 提供通信故障/网络攻击/安全监管的综述背景。
- complements: [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]]，P0018 是具体多车道控制方法，P0019 提供 MPR、policy、dedicated lane 和 system impact 背景。
- suggests_gap: 后续合流研究若只报告效率提升，可能不足以覆盖 CAV mixed traffic 的安全、稳定、环境、网络安全和政策约束。
- asset_todo: 原始 MinerU 文件含图片外链，后续如需写作审计，应本地化到 `raw/assets/P0019/`。

## 7. 对我研究的可能用途

- background_source: 可作为论文 introduction 中说明 mixed traffic transition、CAV penetration 和 traffic efficiency/stability/safety 耦合的背景综述。
- scope_guard: 提醒研究不能只优化 local merging delay，还要说明 safety、stability、environment、communication/cybersecurity 等边界。
- metric_source: 可用于整理 efficiency/stability/safety/environment 的评价指标池。
- risk_source: network attack、communication failure、high latency、privacy 和 policy risk 可转化为鲁棒性实验或讨论段落。
- not_baseline: 不是算法型 baseline，不应放入合流控制实验对比表作为方法。

## 8. 原文锚点

- raw: `raw/papers/P0019-2024-Pan-CAV-Impacts-Mixed-Traffic-Flow-Review.md`
- zotero:
- doi:
- keywords: automated vehicles; mixed traffic flow; connected vehicles; energy usage; safety.

## 9. 必要摘录

> `EXTRACTED` "This paper endeavors to conduct an extensive review concerning the effects of CAVs on mixed traffic flows, with a primary emphasis on their impact on traffic efficiency and congestion."

> `EXTRACTED` "The primary contribution of this paper lies in shifting focus away from solely examining specific subsets of CAVs' impact on mixed traffic flow."

> `EXTRACTED` "CAVs influence traffic efficiency in multiple ways, including CAV penetration rates, vehicle control, dedicated lane design, and road planning."

> `EXTRACTED` "the greatest benefits occurring at MPR ranges of 20 to 40%."

> `EXTRACTED` "Given the susceptibility of CAV communications to disruptions, attention must be directed towards vehicle control technologies in scenarios involving network attacks, communication failures, and human-induced operations."

> `EXTRACTED` "traffic efficiency, stability, safety, and environment impact are intricately interlinked"

## 10. 回查触发点

- proof：需要宏观论证 CAV penetration、stability、safety、emissions 之间并非单目标关系时，回查 `3`、`4` 和 `7`。
- 实验设计：需要选择 mixed traffic 评价维度或 MPR sweep 时，回查 `3.1`、`3.2` 和表 2/3。
- baseline 复现：不适用；该文是综述，不提供可直接复现的合流控制算法。
- 写作：需要 introduction / related work 中说明 CAV mixed traffic 的系统性影响、网络安全和政策背景时，回查 `1`、`4.2`、`5` 和 `6`。
- citation audit：需要核对正文题名、作者、年份和综述范围时，回查论文开头和 raw/PDF 元数据。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头。
- CAV/AV 历史、自动驾驶等级和 V2X 技术：`2 Overview of connected autonomous vehicles`。
- mixed traffic efficiency、metrics、MPR 和 control strategies：`3 Impacts of connected autonomous vehicles on alleviating congestion and traffic efficiency`。
- stability、safety、cybersecurity、environment 和 energy：`4 Impacts of connected self-driving cars on stability, safety and environment`。
- 政策建议与国家政策对比：`5 Policy recommendations of CAV`。
- future research directions：`6 Future research directions`。
- 总结性系统影响表述：`7 Conclusions`。
