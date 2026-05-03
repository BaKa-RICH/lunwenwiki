---
type: concept
title: Integrated Longitudinal-Lateral DNMPC Merging
status: active
confidence: medium
source_pages: [wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging.md]
last_updated: 2026-04-29
---

# Integrated Longitudinal-Lateral DNMPC Merging

## 1. 概念定义

`Integrated longitudinal-lateral DNMPC merging` 指把上层合流时间/纵向速度规划与下层车辆动力学执行、横向轨迹追踪和横向避碰统一起来的 CAV 匝道合流控制路线。

P0011 中，这一路线不是优化合流顺序本身，而是解决“上层合流计划能否被车辆级控制器安全、平滑、实时执行”的问题。

## 2. 机制结构

| 层级 | 输入 | 机制 | 输出 |
| --- | --- | --- | --- |
| Traffic management | 控制区车辆状态、FIFO 顺序 | 分配合流时间、终端速度/加速度和安全时距 | `IN_i(t)` |
| Longitudinal upper-level | 初始状态、终端状态、输入约束 | PMP optimal control，惩罚 acceleration 和 jerk | 最优速度/加速度轨迹 |
| Lateral planning | 纵向轨迹、周车轨迹 | sigmoid 横向参考 + 启动时间搜索 | 横向参考轨迹 |
| Lower-level longitudinal | 上层最优速度 | PI controller in CarSim | throttle/brake tracking |
| Lower-level lateral | 横向参考、周车状态、车辆动力学 | DNMPC + driving safety field | steering control / collision avoidance |

## 3. 为什么重要

- 它直接补足多数合流论文把横向控制和车辆动力学简化掉的问题。
- 它提示“上层 objective”与“下层实际执行”可能不一致：上层优化 jerk/comfort，不代表下层车辆一定实现同等舒适性。
- 它提供了 CarSim/Simulink 级验证路线，可作为从纯算法仿真走向车辆动力学验证的中间台阶。

## 4. 局限边界

- 排序仍是 FIFO，不能替代 sequence optimization baseline。
- 仍是纯 CAV、单主线单匝道，未覆盖 mixed traffic 和 compliance。
- 未处理通信延迟、信息干扰、disturbance。
- DNMPC 规模只在三车/六车 case 中验证；交通流层面的拥堵传播和稳定性仍需额外模型。

## 5. 与本研究的连接

- baseline：可作为 `integrated lateral-longitudinal execution` baseline。
- module：可作为横向 tracking / collision avoidance 执行层，连接 P006 的 safety-critical layer 或 P007 的 sequence-trajectory optimizer。
- gap evidence：强化 GAP-0002，即纵向合流控制、横向换道 tracking 和车辆动力学验证尚未形成统一可扩展框架。
- candidate clue：在后续 idea 中检查上层 comfort/safety objective 是否真的能被下层 actuator-level controller 实现。

## 6. 回查入口

- Paper card: [[wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging]]
- Raw source: `raw/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging.md`
