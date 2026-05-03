---
type: concept
last_updated: 2026-04-29
source_pages: [wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant.md]
confidence: high
---

# DCoMA Dynamic Cooperative Merging Assistant

## 1. 概念定义

`EXTRACTED` DCoMA 是一种面向 mixed traffic 的动态协同合流辅助策略：用宏观 FD 根据主线/匝道流量计算目标交通状态和 platoon/gap 结构，再把主线 gap 时空信息转为匝道车辆可用的 time-series，引导匝道车辆不停驶入主线。

## 2. 核心机制

```text
检测 mainline / on-ramp flow 与 CAV distribution
-> 用 FD 从 state A 计算 target state C
-> 根据 ramp demand 动态求解 v_C / h_C / gap length
-> 只选择 mainline CAV 作为 cooperative vehicles
-> 主线 CAV 减速形成 platoon，platoon 间产生 gap
-> platoon = red phase，gap = green phase
-> 匝道车辆根据 gap time-series 做速度规划
-> 与 ALINEA / X-ALINEA/Q / CoopMA 比较 efficiency, safety, emissions
```

## 3. 关键变量

- `state A`：无控制时主线初始交通状态。
- `state C`：主线 CAV 协同减速后形成更高密度、更短 headway 的目标状态。
- `state O`：车辆空白 gap，对应密度和流量为零。
- `v_C / h_C`：目标状态速度和 headway，由 ramp demand 与 minimum effective gap 共同决定。
- `n_p`：一个控制周期中主线 platoon size。
- `G / C_c`：gap duration 和 control cycle length。
- `PI`：platoon intensity，用于描述 CAV/HDV 空间分布。

## 4. 对本研究的启发

- `INFERRED` DCoMA 是 flow-level objective 与 vehicle-level execution 的强连接线索：gap size 不再固定，而是由实时 ramp/mainline demand 决定。
- `INFERRED` “platoon/gap 时空序列 = virtual traffic signal”可与 P0020 的 VTS-DRL 接口对照：一个是物理/FD 驱动，一个是学习驱动。
- `INFERRED` P0021 强化了多目标评价必要性：DCoMA 改善 on-ramp fuel/queue/safety，但会让 mainline 车辆承担额外减速和 fuel cost。
- `INFERRED` 方法可作为 candidate idea 的上层 flow plan，但要进入本研究，还需补足通信延迟、真实 FD、非保护 gap、多车道横向执行和 congested-state fallback。

## 5. 相关页面

- [[wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant]]
- [[wiki/concepts/flow-level-multilane-comc]]
- [[wiki/concepts/vts-drl-ocp-onramp-merging]]
- [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]]
- [[wiki/comparisons/merging-control-baselines]]
- [[wiki/gaps/open-questions]]
