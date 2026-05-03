---
type: concept
title: Dual-Module PPO Heterogeneous On-Ramp Control
status: active
confidence: medium
source_pages: [wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp.md]
last_updated: 2026-04-29
---

# Dual-Module PPO Heterogeneous On-Ramp Control

## 1. 概念定义

`Dual-module PPO heterogeneous on-ramp control` 指在 CAV-HDV 异质交通中，将匝道合流协作和主线换道协作拆成两个 RL 控制模块，并用规则约束过滤 RL action 的 on-ramp cooperative control 路线。

## 2. 双模块结构

| 模块 | 控制对象 | 关键状态 | 关键动作 | 奖励 |
| --- | --- | --- | --- | --- |
| MC module | Lane 2 与 ramp CAV | subject / preceding / virtual preceding / virtual rear 的速度与距离 | 有界 acceleration | speed reward + TTC/TET safety penalty |
| LC module | Lane 1/Lane 2 mainline CAV lane-changing cooperation | MC 状态 + `U` lane imbalance indicator | 有界 acceleration，辅助 Lane 2 -> Lane 1 换道 | speed reward + 条件化 safety penalty |

最终控制不是直接执行 PPO 输出，而是由 agent action、车辆动力学约束、TTC braking、lane-changing safety conditions 和 traffic rules 共同决定。

## 3. 机制价值

- 把合流冲突和主线换道冲突同时纳入控制，避免 Lane 2/ramp 冲突向 Lane 1 和上游传播。
- 在低 CAV penetration 下仍有收益，P0014 报告 `p_C=0.2` 时 delay 降低 26%。
- 把 transferability 作为实验对象，检查 agent 在不同 penetration、speed、flow、control length 下是否仍有效。

## 4. 局限边界

- RL reward 和状态设计主要是经验工程，缺少稳定性或安全可证明性。
- 横向换道执行被简化，缺少车辆动力学 tracking。
- 通信延迟、感知误差、网络安全和真实驾驶员反应未进入核心实验。
- 高渗透率训练到低渗透率迁移表现较好，但低渗透率训练到高渗透率较弱，说明 policy 泛化方向并不对称。

## 5. 与本研究的连接

- baseline：可作为 low-penetration mixed traffic RL baseline。
- module：MC/LC 双模块结构可为后续“上游 lane-change shaping + ramp merging control”提供架构参考。
- gap evidence：强化 RL 类方法需要 safety layer、execution validation 和 communication robustness。
- candidate clue：把 PPO policy 作为 proposal layer，再由 CBF/DNMPC safety filter 约束执行，但当前只保留为 candidate 线索，不创建 HYP。

## 6. 回查入口

- Paper card: [[wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp]]
- Raw source: `raw/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp.md`
