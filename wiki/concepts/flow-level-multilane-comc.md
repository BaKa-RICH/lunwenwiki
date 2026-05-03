---
type: concept
title: Flow-Level Multilane CoMC
status: active
confidence: medium
source_pages: [wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging.md]
last_updated: 2026-04-29
---

# Flow-Level Multilane CoMC

## 1. 概念定义

`Flow-level multilane CoMC` 是一种面向多车道高速匝道合流瓶颈的 CAV 协调路线：不直接优化每辆车的完整轨迹，而是在流级周期性创造主线 gap、组织匝道 platoon，并用换道规则保护 gap，以改善连续交通流的效率和稳定性。

## 2. 核心机制

| 机制 | 作用 | P0012 中的表达 |
| --- | --- | --- |
| Proactive gap creation | 主线外侧车道 facilitating vehicle 减速，压缩后续车流，形成大 gap | speed-change position、cooperative speed `v_C` |
| Ramp platooning | 匝道等待车辆成组释放，减少零散合流扰动 | merging platoon size `n` |
| Cooperative distance | 决定减速开始位置和上游影响范围 | `d` |
| One-sided lane-change prohibition | 防止内侧车道车辆占用外侧 gap，同时允许外侧车道车辆向内侧疏散 | control segment 内禁止 inner -> outer |
| Shockwave / stability constraint | 避免协调频率过高导致主线 breakdown | `n / lambda >= (d + d') / omega` 等约束 |

## 3. 与车辆级方法的区别

- 车辆级方法关注合流 triplet、merge-in gap、trajectory、tracking 和局部安全。
- Flow-level CoMC 关注 ramp/mainline 两股交通流、周期性协调、shockwave、bottleneck stability 和 recurrent congestion。
- 它适合作为上层 traffic management layer，但需要下层车辆级控制来保证执行可行、安全与舒适。

## 4. 适用边界

- 高需求、近容量的多车道主线 + 单车道匝道场景最能体现收益。
- 需要 100% CAV 或至少足够多可控车辆来担任 facilitating vehicle / platoon leader。
- 依赖即时通信、精确控制和换道规则服从。
- 对 mixed traffic、通信延迟和执行层横向轨迹仍需额外机制。

## 5. 与本研究的连接

- baseline：可作为 flow-level traffic stability baseline，与 P0011 的 execution baseline 和 P007 的 sequence-trajectory baseline 分层对照。
- idea_source：上游 gap shaping 不一定要逐车精细规划，可以通过流级周期性控制先塑造合流机会。
- gap evidence：强化“局部最优轨迹不等于连续流稳定”这一风险，提示后续实验要看 speed contour / shockwave / recurrent congestion。
- candidate clue：将 flow-level CoMC 的 `n/d/v_C` 上层计划与下层 DNMPC/CBF 执行层结合，但当前只作为线索，不创建 HYP。

## 6. 回查入口

- Paper card: [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]]
- Raw source: `raw/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging.md`
