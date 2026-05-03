---
type: concept
title: Calibrated Gap Selection and Lane Balance Control
status: active
confidence: medium
source_pages: [wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic.md]
last_updated: 2026-04-29
---

# Calibrated Gap Selection and Lane Balance Control

## 1. 概念定义

`Calibrated gap selection and lane balance control` 是一种面向 multi-lane on-ramp 异质交通的可解释协同控制路线：通过 gap selection 让 ramp 与 Outside Lane 车辆形成可靠 virtual platoon，并通过主线换道控制平衡 Inside/Outside Lane 的速度和密度。

## 2. 核心机制

| 组件 | 目标 | 关键变量 | 评价 |
| --- | --- | --- | --- |
| Merging control | 在 merging boundary 前降低 ramp/Outside Lane 冲突 | feasible gaps、reliable/unreliable vehicle bonds、sequence change | TETMP、CPMR |
| Lane-changing control | 平衡主线两车道交通状态 | speed uniformity、density uniformity、`u_i' >= k_u * u` | delay、CD、TET |
| Simulation calibration | 让仿真参数更接近真实数据 | exiD arrival intervals、lane-change dissatisfaction、TTC/distance thresholds | 参数可追溯 |
| Capacity-drop analysis | 检查瓶颈形成后的吞吐下降 | observation points、downstream flow drop | capacity drop ratio |

## 3. 与 P0014 的区别

- P0014 使用 PPO 学习 MC/LC 双模块策略，强调低 CAV penetration 下的 RL 收益和 transferability。
- P0015 使用规则化 gap selection、vehicle bond、lane uniformity 和 exiD 校准，强调可解释性、容量下降和 ramp metering 对比。
- 两者适合成对作为 learning baseline 与 interpretable baseline。

## 4. 局限边界

- 需要 roadside control center 和高精度广域检测器。
- 横向换道执行仍被简化为满足条件即完成。
- 通信延迟、感知噪声和 packet loss 没有系统进入核心实验。
- exiD 校准提高可信度，但仍未替代高保真仿真或实车验证。

## 5. 与本研究的连接

- baseline：non-RL interpretable mixed-traffic multi-lane baseline。
- idea_source：reliable/unreliable VB 可转化为合流排序代价、risk term 或 proof 中的结构变量。
- gap evidence：capacity drop 与 TET/comfort 共同说明单一效率指标不足。
- candidate clue：将 VB-based gap selection 与 safety-critical filter、delay robustness 或 lateral tracking 结合；当前仅保留线索，不创建 HYP。

## 6. 回查入口

- Paper card: [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]]
- Raw source: `raw/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic.md`
