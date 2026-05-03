---
type: paper
paper_id: P0018
title: "Hierarchical cooperative constrained control for multi-lane merging process under mixed traffic scenario"
authors: "Xiaoyu Liu, Min Zhao, Liuping Wang, Dihua Sun"
year: 2025
venue: "Springer Nature"
status: read
confidence: high
source_path: raw/papers/P0018-2025-liu-hcmcc-multi-lane-merging.md
zotero_key:
doi:
tags: [CAV, HV, mixed-traffic, multi-lane-merging, HCMCC, MILP, LCMPC-PTO, lane-changing, SUMO]
last_updated: 2026-04-29
---

# P0018: HCMCC for Multi-Lane Mixed-Traffic Merging

## 1. 一句话定位

这篇论文提出 HCMCC 分层协同约束控制框架，在 mixed traffic 的多车道匝道合流中用 MILP 战术层协调 Lane 0/1/2 的 CAV 合流、切入与辅助，再用 LCMPC-PTO 执行轨迹并抵抗外部扰动。

## 2. 核心贡献

- `EXTRACTED` 构建 decentralized hierarchical framework：Tactical layer 用 MILP 规划 CAV lane-occupation sequence 与 longitudinal acceleration profile，Operational layer 用 LCMPC-PTO 执行。
- `EXTRACTED` 将 Lane 2 内侧 CAV 纳入协同合流：低 CAV penetration 或 Lane 1 无可用 CAV 时，Lane 2 CAV 可切入 Lane 1，或通过 conditional assistance 为等待车辆释放空间。
- `EXTRACTED` 区分 CAV/HV car-following heterogeneity：CAV 可用更小 headway 和速度一致性释放道路空间，HV 用 IDM + conservative lane-change model 表示。
- `EXTRACTED` 提出 HCMCC-L1、HCMCC-L0、SHCMCC-L0 三类模型，覆盖未规划 CAV 位于 Lane 1、Lane 0 以及无协作车时的非协作切入情形。
- `EXTRACTED` 引入 continuation cooperative utility (CCU) model，在 Velocity Regulating Area 继续平衡各车道密度，缓解合流后 Lane 1 拥堵。
- `EXTRACTED` 在执行层将 nonlinear third-order vehicle dynamics、external disturbance、Laguerre-function MPC 和 prescribed-time observer 结合，以减少在线变量并补偿扰动。

## 3. 方法抓手

- Road partition：Control Area 包括 Pre-Merging Area、Organizing Area、Preparing Area、Merging Area 和 Velocity Regulating Area，并考虑末端速度限制下降。
- Data set construction：CAV 通过 V2X 获取 CAV 状态/已规划轨迹，通过 RSU 接收 HV 状态，并用 IDM/CLCM 预测周边 HV。
- MILP tactical variables：使用 `kappa`、`gamma`、`alpha`、`beta`、`chi`、`Lambda` 等辅助变量描述旅行时间、合流完成、空间释放、切入完成等离散事件。
- Lane 2 assistance：当 `Phi_WV` 中存在无法完成合流的车辆时，Lane 2 CAV 可保持与 Lane 1 CAV 类似轨迹来创造连续换道空间；必要时 Lane 2 CAV 先 cut-in 到 Lane 1。
- Operational execution：LCMPC 用 Laguerre functions 将未来控制输入压缩为少量正交基系数，PTO 在 prescribed time 内估计外部扰动并补偿到控制律中。

## 4. 关键实验结论

- `EXTRACTED` SUMO 仿真设置为两条主线 + 一条匝道，Control Area 位于下游 300 m，速度限制从 60 km/h 降至 40 km/h，流量测试覆盖 2800/3200/3600 veh/h 与多种主线/匝道流量分布。
- `EXTRACTED` 2800 veh/h 下，HCMCC 在不同流量分布和 PR 下将 all-vehicle average travel time 改善约 16.32% 至 42.86%。
- `EXTRACTED` 3200 veh/h 且 PR=0.8 时，total actual traffic flow 提升约 10.28% 至 12.13%，并更好平衡主线与匝道车辆利益。
- `EXTRACTED` Lane 2 assistance degradation experiment 显示，启用 Lane 2 CAV 辅助后，main lane 和 merging lane 的 average TT 改善分别达到 3.09% 至 8.63% 和 8.21% 至 31.44%。
- `EXTRACTED` LCMPC-PTO 相比 LCMPC 显著降低轨迹跟踪误差；选定测试中 maximum position tracking error 平均值约 0.042，而 LCMPC 约 0.849。
- `EXTRACTED` 与 CORMC 对比时，HCMCC+CCU 在 PR=0.8、2800 veh/h 下使主线/匝道 average TT 差值约 0.34 至 0.52 s，小于 CORMC 的 0.95 至 2.61 s，并使合流区车辆数波动更平滑。

## 5. 局限与隐含假设

- 论文自述局限：
  - 结论主要强调仿真优势和执行层扰动补偿，未展开真实道路、通信延迟、感知误差或实车验证。
- 你识别到的隐含假设：
  - Tactical layer 明确假设 CAV V2X 无通信延迟，HV 状态可由 RSU 获取。
  - CAV lane-change 在模型中按 lane occupation sequence 离散更新，存在 instant lane-changing 简化。
  - HV lane-change 用 conservative lane-change model，且禁止 HV 从内侧车道向外侧车道换道，驾驶行为假设较强。
  - MILP 使用固定安全换道距离预筛 feasible lane-change spaces，复杂真实换道风险在战术层仍被简化。
  - 仿真依赖 SUMO、Gurobi 和 Python；实时性更多来自模型结构与 LMPC 论证，缺少大规模在线计算时间统计。
  - 外部扰动主要作用于 CAV 执行层，尚未系统测试通信延迟、packet loss、partial observability 或 aggressive HV cut-in。

## 6. 关系线索

- uses: HCMCC paper-specific mechanism, HCMCC-L1, HCMCC-L0, SHCMCC-L0, CCU, MILP tactical layer, LCMPC-PTO operational layer；原单篇 concept 已删除，核心信息保留在本 card、[[wiki/field/field-map]]、[[wiki/comparisons/merging-control-baselines]] 和 [[wiki/gaps/open-questions]]。
- extends: [[wiki/concepts/mixed-traffic-multilane-cormc]]，P0018 直接对比 P002/CORMC，并放松“所有 HV 愿意协作”的前提，引入 Lane 2 CAV 辅助。
- complements: [[wiki/concepts/flow-level-multilane-comc]]，P0012 是 flow-level gap/platoon 控制，P0018 是 vehicle-level MILP + execution tracking 的 multi-lane mixed traffic 框架。
- complements: [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]]，P0011 验证横向/纵向执行层，P0018 提供多车道战术层和 LCMPC-PTO 扰动补偿。
- contrasts: [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]]，P0016 小规模关键车 mode switching，P0018 更偏多车道连续交通流和 CAV penetration 敏感性。
- suggests_gap: multi-lane mixed traffic 的 Lane 2 assistance 很有价值，但需要加入真实 lane-change duration、通信延迟、感知误差和 HV 非保守行为验证。
- asset_todo: 原始 MinerU 文件含大量外链图片，后续如需写作审计，应本地化到 `raw/assets/P0018/`。

## 7. 对我研究的可能用途

- baseline: 可作为 multi-lane mixed traffic 下带 inner-lane CAV assistance 的强 baseline。
- mechanism_source: Lane 2 CAV cut-in / conditional assistance 为“上游/内侧车道释放合流空间”提供可解释机制。
- proof_source: MILP 约束、PTO prescribed-time disturbance estimation 和 Laguerre-function MPC 可作为战术层-执行层闭环 proof 片段。
- experiment_design: 可复用 PR、traffic flow level、flow distribution、Lane 2 assistance ablation、LCMPC-PTO vs LCMPC、HCMCC vs CORMC 的对照结构。
- risk_source: 提醒后续方法如果使用多车道空间，必须说明是否牺牲主线利益、如何保持公平，以及是否真实可执行。
- metric: average travel time、actual traffic flow、main/merging lane TT difference、vehicle count fluctuation、cut-in count、position tracking error。

## 8. 原文锚点

- raw: `raw/papers/P0018-2025-liu-hcmcc-multi-lane-merging.md`
- zotero:
- doi:
- keywords: mixed traffic scenario; CAV longitudinal trajectory optimization; lane-change behavior; merging problem; model predictive control.

## 9. 必要摘录

> `EXTRACTED` "this paper proposes a hierarchical cooperative merging constrained control (HCMCC) algorithm-based decentralized framework under the mixed traffic scenario."

> `EXTRACTED` "The multi-lane merging problem is solved in the Tactical layer using a Mixed Integer Linear Programming (MILP) optimization model"

> `EXTRACTED` "CAVs at the inner lane are permitted to either cut into the outer lane to complete the cooperative merging or provide assistance to create more spaces for the cooperative merging."

> `EXTRACTED` "Any CAV ... can share the real-time state through vehicle-to-everything (V2X) without communication delay"

> `EXTRACTED` "the HCMCC model focuses on reducing the average TT of all vehicles at this traffic flow level (about 16.32% ~ 42.86%)."

> `EXTRACTED` "The total ATF of all lanes can achieve an increase of 10.28% ~ 12.13% at 3200 veh/h and PR of 0.8."

## 10. 回查触发点

- proof：需要解释 HCMCC MILP 辅助变量、Lane 2 conditional assistance、PTO prescribed-time stability 或 LCMPC 降维机制时，回查 `3 Tactical layer` 与 `4 Operational layer`。
- 实验设计：需要设置 PR、traffic flow level、flow distribution、Lane 2 assistance degradation、CORMC/SUMO baseline 时，回查 `6 Simulation results`。
- baseline 复现：需要实现 HCMCC-L1/HCMCC-L0/SHCMCC-L0、CCU、LCMPC-PTO 或 SUMO-Gurobi 闭环时，回查 `3.2`、`5` 和 `6.1`。
- 写作：需要论证“多车道 mixed traffic 需要利用内侧车道 CAV 平衡主线/匝道利益”时，回查 `1 Introduction`、`Remark 1`、`6.4` 和 `6.5.3`。
- citation audit：需要核对作者、Springer 出版信息、参数表或 CORMC 引用关系时，回查论文开头、`Table 1` 与 `References`。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头。
- 研究 gap 与贡献：`1 Introduction`。
- 道路区域、信息结构、分层框架：`2 Problem description and overview of proposed solutions`。
- HV conservative lane-change、CAV feasible lane-change spaces 与 kinematics：`3.1`。
- HCMCC-L1、HCMCC-L0、SHCMCC-L0 约束模型：`3.2.2` 至 `3.2.4`。
- 车辆动力学、PTO 和 LCMPC-PTO：`4 Operational layer`。
- CCU、terminal conditions 和 trajectory programming process：`5 The algorithm framework`。
- SUMO setup、benefits、degradation、sensitivity 和 CORMC 对比：`6 Simulation results`。
- 总结性性能数字：`7 Conclusion`。
