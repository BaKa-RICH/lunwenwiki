---
type: concept
last_updated: 2026-04-29
source_pages: [wiki/papers/P0019-2024-Pan-CAV-Impacts-Mixed-Traffic-Flow-Review.md]
confidence: medium
---

# CAV Mixed-Traffic Impact Review

## 1. 概念定义

`EXTRACTED` P0019 将 CAV 对 mixed traffic flow 的影响概括为一个多目标系统问题：CAV 不只改变 traffic efficiency 和 congestion，也同时影响 traffic stability、safety、environment/energy、cybersecurity 和 policy。

## 2. 核心机制

```text
CAV penetration / automation level / connectivity
-> 更短反应时间、更强协同控制、更小车头时距
-> traffic efficiency、capacity、speed 与 congestion 改变
-> traffic oscillation、string stability 与 phantom congestion 改变
-> safety conflict、cybersecurity、privacy 与 latency 风险出现
-> emissions / energy 的短期收益与长期诱导需求权衡
-> policy、dedicated lane、testing regulation 与 public acceptance 约束部署
```

## 3. 关键变量

- Market penetration rate (MPR)。
- Automation level and vehicle type。
- Connectivity / V2X mode: V2V, V2I, V2C, V2P, V2N。
- Traffic flow, average speed, vehicle count, road capacity, travel time。
- Stability / traffic oscillation / phantom congestion。
- Safety, cyberattack, latency, communication failure。
- Energy consumption, emissions, environmental impacts。

## 4. 对本研究的启发

- `INFERRED` on-ramp merging 研究可把 P0019 作为宏观动机：合流局部效率提升需要放入 mixed traffic 的 stability/safety/environment/policy 背景中解释。
- `INFERRED` 后续实验不宜只扫 CAV penetration，还应同时报告或讨论 MPR 与 safety/stability/energy 指标的交互。
- `INFERRED` CAV dedicated lane 和 policy 结论提示：多车道合流控制若依赖专用车道或特定 lane-use 规则，需要说明低渗透率下是否会牺牲整体 throughput。
- `INFERRED` cyberattack、communication failure 和 high latency 是 GAP-0004 的宏观支撑，但 P0019 本身不提供合流控制层面的定量证据。

## 5. 相关页面

- [[wiki/papers/P0019-2024-Pan-CAV-Impacts-Mixed-Traffic-Flow-Review]]
- [[wiki/field/shared-assumptions]]
- [[wiki/gaps/confirmed-gaps]]
- [[wiki/gaps/open-questions]]
- [[wiki/concepts/field-experimental-communication-delay-cav-merging]]
- [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]]
