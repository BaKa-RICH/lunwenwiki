---
type: paper
paper_id: P003
title: "A hierarchical cooperative merging control strategy for the mixed traffic of CAVs and HDVs"
authors: "Dian Jing, Rongsheng Chen, Enjian Yao, Monica Menendez"
year: 2025
venue: "Transportation Research Part C: Emerging Technologies"
status: read
confidence: medium
source_path: raw/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control.md
zotero_key:
doi: 10.1016/j.trc.2025.105230
tags: [CAV, HDV, mixed-traffic, merging-sequencing, consensus-controller, platoon-stability]
last_updated: 2026-04-26
---

# P003: Mixed-Traffic Hierarchical Merging With Consensus Stability

## 1. 一句话定位

这篇论文提出面向 CAV/HDV 混合交通的分层合流控制：上层把 merging sequencing 转化为低复杂度 shortest-path search，下层用考虑通信延迟的 consensus controller 做运动规划，并给出 local stability 与 string stability 条件。

## 2. 核心贡献

- `EXTRACTED` 构建 merging sequencing layer + motion planning layer 的分层控制策略，用于混合交通中 CAV 的平滑合流。
- `EXTRACTED` 将合流排序建模为 zero-one integer programming，并重构为 fixed-start shortest-path search，用 Dijkstra 求解，复杂度为 `O((Nm + Nr)^2)`。
- `EXTRACTED` 在 mixed-traffic platoon 中用 2D-IDM 建模 HDV 随机性，并为 CAV 设计带 communication delays 的 decentralized consensus controller。
- `EXTRACTED` 推导 local stability 与 string stability 条件，为控制增益设置提供可检查准则。

## 3. 方法抓手

- 合流排序：用 directed graph 表示车辆之间的 leader-follower 关系，边成本由效率、舒适性和安全性组成。
- HDV 预测：用 2D-IDM 随机调整期望时距，并通过重复仿真选取分位轨迹来估计 HDV 运动。
- 运动规划：采用 virtual-platoon 思路，把合流问题转化为 car-following / consensus control 问题。
- 稳定性设计：控制器显式考虑通信延迟 `theta`，并通过 local/string stability 分析选择 `kp, kv, ka`。

## 4. 关键实验结论

- `EXTRACTED` 实验包括 MATLAB 数值仿真和 MATLAB + SUMO 联合仿真，场景含 two-lane merging zone 与 multi-lane merging zone。
- `EXTRACTED` 多车 platoon 数值实验显示 CAV penetration 越高，达到稳定所需时间越短，控制输入峰值越小。
- `EXTRACTED` time-varying platoon leader 实验显示，提高装备该控制器的 CAV penetration 能增强 anti-disturbance performance 和 robustness。
- `EXTRACTED` 交通流仿真比较 FCFS+CF、FCFS+CC、MS+CF、MS+CC，提出的 MS+CC 在速度、延误、吞吐和较低加速度方面表现最好。
- `EXTRACTED` 与 Zhou and Ahn、Sun et al.、Han et al. 等算法对比，P003 方法在高 CAV penetration 下保持最高速度、最低延误和最高吞吐。
- `EXTRACTED` 用 IDM、2D-IDM、Krauss、GM 四种 HDV 模型检验，对不同 HDV 行为有一定鲁棒性。

## 5. 局限与隐含假设

- 论文自述局限：
  - 需回 raw 核查是否在结论中列出更具体 future work；当前结论主要强调算法和仿真结果。
- 你识别到的隐含假设：
  - RSU/V2I 能收集合流区所有车辆实时状态，CAV 可接收必要信息。
  - 合流点由道路几何预设，所有匝道车必须在该点前进入主线。
  - 横向控制被简化为满足间隙后以固定横向速度换道，研究重点实际偏纵向排序与稳定性。
  - 稳定性推导依赖线性化、Taylor 近似和给定通信延迟假设，真实噪声和异质反应还需验证。

## 6. 关系线索

- extends: P001/P002 的分层合流控制主线，但把重点转向 HDV stochasticity、communication delay 和 platoon stability。
- contrasts: FCFS merging sequence、传统 car-following controller、RL-based controllers。
- uses: [[wiki/concepts/consensus-based-mixed-traffic-merging]], 2D-IDM, shortest-path search, Dijkstra, Lyapunov-Razumikhin, string stability, SUMO。
- suggests_gap: 横向控制简化、通信延迟与 HDV 不确定性的联合鲁棒性、排序目标权重与驾驶风格匹配仍值得深入。
- asset_todo: 原始 MinerU 文件含大量外链图片，后续如需写作审计，应本地化到 `raw/assets/P003/`。

## 7. 对我研究的可能用途

- baseline: 可作为 mixed traffic 下“优化排序 + 稳定 consensus controller”的强机制型 baseline。
- idea_source: 可启发把排序层的 edge cost 与驾驶风格、风险偏好或学习到的 HDV 不确定性结合。
- counterexample: 反驳只优化合流顺序但不检查 platoon stability 的方法。
- dataset_or_metric: average speed、acceleration、delay、throughput、anti-disturbance、robustness、local/string stability。
- assumption: RSU 完整感知、固定合流点、横向运动简化、CAV 执行控制、HDV 由 car-following model 表示。

## 8. 原文锚点

- raw: `raw/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control.md`
- zotero:
- doi: 10.1016/j.trc.2025.105230
- keywords: Connected and automated vehicles; Mixed traffic; Freeway merging zones; Merging sequencing; Consensus controller; Platoon stability.

## 9. 必要摘录

> `EXTRACTED` The strategy consists of a merging sequencing layer and a motion planning layer to facilitate smooth merging of CAVs in freeway merging zones.

> `EXTRACTED` A zero-one integer programming model is built to convert merging sequencing into a shortest-path search problem, enhancing the solving efficiency.

> `EXTRACTED` Increasing the penetration rates of CAVs can improve the anti-disturbance performance, robustness, and stability of traffic flow in the merging zone.

## 10. 回查触发点

- proof：需要证明 consensus controller 稳定性或通信延迟下的 string stability 时，回查 `3.4. Stability analysis`、`3.4.1. Local stability`、`3.4.2. String stability`。
- 实验设计：需要设计 two-lane / multi-lane、900/1200 vph/lane、CAV penetration、HDV 行为鲁棒性实验时，回查 `4. Experiments and results`、`4.2. Traffic-flow simulations`。
- baseline 复现：需要复现 MS、CC、FCFS+CF、FCFS+CC、MS+CF、MS+CC 对比时，回查 `3.2. Merging sequencing`、`3.3. Motion planning`、`4.2. Traffic-flow simulations`。
- 写作：需要描述 mixed traffic、HDV stochasticity、排序实时性、RL 可解释性不足或稳定性贡献时，回查 `1. Introduction`、`2. Literature review`、`5. Conclusions`。
- citation audit：需要核对 2D-IDM、Dijkstra、Lyapunov-Razumikhin、string stability、对比算法引用时，回查 `References`；具体卷期页码需回 raw 或 Zotero 核查。

## 11. 关键原文位置

- 论文题名、作者、关键词、摘要：开头、`A R T I C L E I N F O`、`A B S T R A C T`。
- 研究动机、gap 与贡献：`1. Introduction`。
- centralized/decentralized、virtual platoon、RL 相关工作：`2. Literature review`。
- 问题设定和分层框架：`3.1. Problem description`。
- 合流排序、成本函数、复杂度：`3.2. Merging sequencing`、`3.2.2. Cost function`、`3.2.4. Algorithm complexity`。
- 运动规划、通信网络、spacing policy、dynamics、consensus controller：`3.3. Motion planning`。
- local/string stability 推导：`3.4. Stability analysis`。
- 数值仿真、抗扰动、SUMO 交通流仿真：`4. Experiments and results`。
- two-lane / multi-lane 场景、对比算法和 HDV 鲁棒性：`4.2.1. Two-lane scenario`、`4.2.2. Multi-lane scenario`、`4.2.3. Comparison with other algorithms`、`4.2.4. Robustness against different HDV behavior`。
- 结论：`5. Conclusions`。
