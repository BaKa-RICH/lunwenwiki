---
type: paper
paper_id: P004
title: "Cooperative control of CAVs in the merging area of multi-lane mainline and dual-lane ramps on freeways"
authors: "Yi Wang, Jian Xiang, Junliang Pan, Jie Wang, Tao Chen, Hao Wang"
year: 2025
venue: "Transportation Safety and Environment"
status: read
confidence: medium
source_path: raw/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging.md
zotero_key:
doi: 10.1093/tse/tdaf030
tags: [CAV, multilane-mainline, dual-lane-ramp, multi-area-control, virtual-platoon, trajectory-optimization]
last_updated: 2026-04-26
---

# P004: Multi-Area CAV Control for Multilane Mainline and Dual-Lane Ramp

## 1. 一句话定位

这篇论文面向多主线车道 + 双车道匝道的纯 CAV freeway merging 场景，把合流控制拆成主线提前换道、匝道虚拟车队速度控制和合流区滚动轨迹优化三个协作区域，以解决复杂几何下的合流效率与停车排队问题。

## 2. 核心贡献

- `EXTRACTED` 构建 multi-area cooperative merging control framework，将主线、匝道和合流区划分为六个控制区域。
- `EXTRACTED` 设计 velocity-benefit-orientated lane changing in advance strategy，引导主线外侧车道车辆提前向内侧换道，为匝道车创造 gap。
- `EXTRACTED` 针对 dual-lane ramp，基于 FIFO 和 virtual platoon 对匝道车辆进行速度控制，使两条匝道车流无冲突进入加速/合流区域。
- `EXTRACTED` 在合流区使用 cyclic rolling trajectory optimization，使匝道车辆可在加速车道任意位置完成合流，而不是固定在末端。

## 3. 方法抓手

- 主线提前换道：只有同时满足最小安全间距和换道后速度收益时，车辆才向相邻内侧车道移动。
- 匝道虚拟车队：根据车辆预测到达加速车道起点的时间，用 FIFO 确定双匝道车道进入顺序，再映射成单车道 virtual platoon。
- 匝道速度控制：最大化虚拟车队在控制周期内的速度，同时满足速度、加速度、加速度变化、最小安全距离和动力学约束。
- 合流区轨迹优化：以周期滚动方式最大化合流车辆速度，并约束同车道及跨车道车辆在周期末满足安全距离。

## 4. 关键实验结论

- `EXTRACTED` 仿真使用 SUMO + Python TraCI，场景为三条主线车道 + 双车道匝道，主线 1000 m，匝道 400 m，仿真 3600 s，步长 1 s。
- `EXTRACTED` 设计 16 组需求：主线 800/1200/1600/2000 veh/h/ln，匝道 400/500/600/700 veh/h/ln，每组 3 个随机种子取平均。
- `EXTRACTED` 相比 no control，trajectory optimization 提升速度并降低延误；cooperative control 进一步优于 trajectory-only，说明主线提前换道和匝道速度控制有额外价值。
- `EXTRACTED` 高需求下优势更明显：当主线和匝道均为高流量时，cooperative control 平均速度提升 49.1%，平均延误降低 70.2%。
- `EXTRACTED` no control 在 11 组中出现停车，trajectory-only 高需求下仍有少量停车，而 cooperative control 在测试场景中消除停车。
- `EXTRACTED` dual-lane ramp 在 cooperative control 下相对 single-lane ramp 有小幅速度/延误优势，并能避免匝道车辆停车等待。

## 5. 局限与隐含假设

- 论文自述局限：
  - 所有车辆均假设为 CAV，未来需要研究 CAV + HDV 混合交通，尤其是混合车队合流控制。
  - 未考虑换道过程的横向轨迹优化和 tracking，未来需要优化 lateral lane-changing trajectories。
- 你识别到的隐含假设：
  - V2V/V2I 通信无延迟，所有车辆完全服从 RSU 控制。
  - 主线提前换道和匝道速度调节相对独立，随后才在合流区进行联合轨迹优化。
  - 使用 FIFO 处理双车道匝道进入顺序，计算简单但可能牺牲全局最优排序。

## 6. 关系线索

- extends: P002/P003 的多车道与混合交通线索，但 P004 回到纯 CAV，更强调双车道匝道与多区域工程化控制。
- contrasts: no control、trajectory-only optimization、单车道匝道场景。
- uses: multi-area dual-lane ramp control paper-specific mechanism, mainline pre-lane-changing, virtual platoon, FIFO, rolling trajectory optimization, SUMO/TraCI；原单篇 concept 已删除，核心信息保留在本 card、[[wiki/field/field-map]] 和 [[wiki/comparisons/merging-control-baselines]]。
- suggests_gap: 混合交通双车道匝道、主线提前换道与匝道排序联合优化、横向轨迹 tracking 仍待研究。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P004/`。

## 7. 对我研究的可能用途

- baseline: 可作为复杂几何场景下 multi-area pure-CAV cooperative control baseline。
- idea_source: 可启发“主线提前换道 + 匝道虚拟队列 + 合流区滚动优化”的模块化方法故事。
- counterexample: 反驳只研究单匝道车道或只在合流区做轨迹优化足以覆盖实际复杂合流场景的设定。
- dataset_or_metric: average speed、average delay、stop counts、mainline/ramp demand matrix、single-vs-dual-ramp comparison。
- assumption: 纯 CAV、无通信延迟、完全服从、未优化横向轨迹、FIFO 匝道排序。

## 8. 原文锚点

- raw: `raw/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging.md`
- zotero:
- doi: 10.1093/tse/tdaf030
- keywords: intelligent network environment; ramp merging area; multi-area cooperative merging control; lane-changing strategy; vehicle trajectory optimization.

## 9. 必要摘录

> `EXTRACTED` The strategy integrates lane changing in advance tactics for upstream mainline vehicles and speed regulation for ramp vehicles into a structured control framework.

> `EXTRACTED` Vehicles can merge at any point along the acceleration lane, with the merging position being the trajectory position at the end of the cycle.

> `EXTRACTED` Under high demand on both mainline and ramp, cooperative control boosts average speeds by 49.1% and reduces delays by 70.2%.

## 10. 回查触发点

- proof：需要论证“多区域分治为何改善双车道匝道合流”时，回查 `3.2. Multi-areas collaborative control framework`、`3.3. Consider velocity-benefit-orientated lane changing in advance strategy`、`3.4. Virtual platoon-based speed optimization for CAVs on ramps`。
- 实验设计：需要设置三主线车道、双车道匝道、需求矩阵、stop counts 和 sensitivity analysis 时，回查 `4. Simulation analysis`、`4.1. Simulation scenario and parameter settings`、`4.2.3. Sensitivity analysis`。
- baseline 复现：需要复现 no control、trajectory-only、cooperative control 或 single-vs-dual ramp 对比时，回查 `4.2.1. Comparative analysis`、`4.2.2. Comparison of cooperative control method effects in single-lane and dual-lane ramp scenarios`。
- 写作：需要描述复杂几何、多车道匝道 gap、固定合流点不足和工程化多区域控制贡献时，回查 `1. Introduction`、`2. Literature review`、`5. Conclusions`。
- citation audit：需要核对 FIFO、virtual vehicle、rolling trajectory optimization、SUMO/TraCI 相关引用时，回查 `References`；具体页码需回 raw 或 Zotero 核查。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头、`Abstract`、`Keywords`。
- 研究动机、gap 与贡献：`1. Introduction`。
- rule-based / optimization-based / other approaches：`2. Literature review`。
- 场景和假设：`3.1. Scenario description and assumptions`。
- 多区域控制框架：`3.2. Multi-areas collaborative control framework`。
- 主线提前换道和速度收益：`3.3. Consider velocity-benefit-orientated lane changing in advance strategy`。
- 双车道匝道 virtual platoon 与速度控制：`3.4. Virtual platoon-based speed optimization for CAVs on ramps`。
- 合流区滚动轨迹优化：`3.5. Vehicle trajectory optimization`。
- 仿真设置与参数：`4.1. Simulation scenario and parameter settings`。
- 三种控制策略对比：`4.2.1. Comparative analysis of simulation results for different control strategies on dual-lane ramp`。
- 单/双匝道车道对比和敏感性：`4.2.2. Comparison of cooperative control method effects in single-lane and dual-lane ramp scenarios`、`4.2.3. Sensitivity analysis`。
- 局限与 future work：`5. Conclusions`。
