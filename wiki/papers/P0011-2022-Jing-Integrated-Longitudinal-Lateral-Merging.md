---
type: paper
paper_id: P0011
title: "Integrated Longitudinal and Lateral Hierarchical Control of Cooperative Merging of Connected and Automated Vehicles at On-Ramps"
authors: "Shoucai Jing, Fei Hui, Xiangmo Zhao, Jackeline Rios-Torres, Asad J. Khattak"
year: 2022
venue: "IEEE Transactions on Intelligent Transportation Systems"
status: read
confidence: high
source_path: raw/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging.md
zotero_key:
doi: 10.1109/TITS.2022.3204033
tags: [CAV, cooperative-merging, longitudinal-lateral-control, hierarchical-control, DNMPC, CarSim-Simulink, driving-safety-field]
last_updated: 2026-04-29
---

# P0011: Integrated Longitudinal-Lateral Hierarchical Merging

## 1. 一句话定位

这篇论文把 CAV 匝道合流从纵向 arrival-time / speed planning 推到车辆级执行层，提出纵向最优控制 + 横向 DNMPC 追踪避碰的分层框架，并用 CarSim/Simulink 近真实车辆动力学验证。

## 2. 核心贡献

- `EXTRACTED` 提出 integrating traffic management and vehicle-level control 的 hierarchical cooperative coordination framework，用于 on-ramp CAV merging。
- `EXTRACTED` 上层纵向控制用 optimal control 在输入约束下优化燃耗和舒适性，目标函数同时惩罚 acceleration 和 jerk。
- `EXTRACTED` 设计 lateral trajectory planning start time decision strategy，用 sigmoid 轨迹生成横向参考。
- `EXTRACTED` 下层横向控制提出基于 nonlinear model predictive control 的 decentralized unified algorithm，同时追踪轨迹并通过 driving safety field 避免横向碰撞。
- `EXTRACTED` 用 CarSim/Simulink co-simulation 验证 integrated longitudinal and lateral control，而不只停留在点质量模型或纯纵向仿真。

## 3. 方法抓手

- Traffic management：单主线 + 单匝道，进入控制区后按 FIFO 分配合流顺序、合流时间和终端状态。
- Longitudinal upper-level：三阶点质量模型，状态为 position / speed / acceleration，控制输入为 jerk；用 Pontryagin maximum principle 推导最优控制并处理输入约束。
- Lateral trajectory：用 sigmoid 函数生成从当前车道到目标车道的平滑横向参考，并搜索合适的横向规划启动时间。
- Lower-level longitudinal：CarSim 中 PI 控制器跟踪上层最优速度。
- Lower-level lateral：DNMPC 以 lateral tracking error、steering input increment 和 driving safety index 为代价，在车辆动力学和转角约束下滚动求解。
- Safety representation：driving safety field 同时描述空间风险和时间风险，用于横向避碰目标而非仅靠合流点安全时距。

## 4. 关键实验结论

- `EXTRACTED` 三车 case 中，轨迹在时空上不相交，速度曲线平滑、无 stop-and-go，DNMPC tracking error 最终趋近 0。
- `EXTRACTED` 三车 case 的每车每控制周期计算时间小于 0.02 s，论文据此认为 DNMPC 可实时实现。
- `EXTRACTED` 三车 case 相比 baseline 总燃耗降低 21.9%。
- `EXTRACTED` 六车 case 在 CarSim 支持上限内验证了多车合流，结果显示 DNMPC 可安全有效控制横向合流。
- `EXTRACTED` 六车 case 相比 baseline 总燃耗降低 3.9%，论文指出收益与车辆进入/退出控制区状态有关。

## 5. 局限与隐含假设

- 论文自述局限：
  - 上层最优加速度/jerk 未能直接作为下层输入，实际舒适性由下层控制器决定，lower-level acceleration / jerk tracking 仍需验证。
  - 未考虑 unreliable communication、information interference、communication delay 和 disturbance。
  - 未来需要研究 mixed traffic 条件下不同 CAV penetration 的合流效率。
- 你识别到的隐含假设：
  - 合流顺序仍是 FIFO，方法重点是执行与横向控制，不解决排序最优性。
  - 场景是单主线单匝道、纯 SAE Level 4/5 CAV，未覆盖 HDV/CHV 行为和 compliance。
  - 横向碰撞由 driving safety field + DNMPC 处理，但上层横向启动策略仍基于简化粒子模型。
  - CarSim 单次联合仿真最多六车，规模化交通影响主要依赖推断而非仿真证据。

## 6. 关系线索

- extends: [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]] 的 closed-form / optimal longitudinal control，把车辆动力学、横向 tracking 和 CarSim validation 接入合流控制。
- complements: [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]]，P007 强在 sequence + trajectory 一体化，P0011 强在 lateral tracking 与 vehicle dynamics execution。
- complements: [[wiki/concepts/flexible-control-barrier-function-merging]]，P006 给 safety-critical longitudinal/flexible-position layer，P0011 提供横向 DNMPC + driving safety field 的执行层线索。
- uses: [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]], FIFO, optimal control, sigmoid lateral trajectory, PI speed tracking, DNMPC, driving safety field。
- suggests_gap: 上层 comfort objective 与下层实际 acceleration/jerk tracking 脱节，可能成为 integrated control 的隐藏断点。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P0011/`。

## 7. 对我研究的可能用途

- baseline: 可作为 integrated longitudinal-lateral execution baseline，专门对照“只做纵向合流排序/arrival-time planning”的方法。
- mechanism_source: driving safety field + DNMPC 可作为横向 tracking / collision avoidance 模块，补足 GAP-0002。
- experiment_design: CarSim/Simulink co-simulation 提供比纯 SUMO/MATLAB 更接近车辆动力学的验证路径。
- risk_source: 如果新方法在上层优化 comfort，却没有验证下层 acceleration/jerk tracking，P0011 的 discussion 可作为反例依据。
- metric: tracking error、computation time per control cycle、fuel consumption、speed/acceleration/yaw/lateral acceleration profiles。

## 8. 原文锚点

- raw: `raw/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging.md`
- zotero:
- doi: 10.1109/TITS.2022.3204033
- keywords: Connected and automated vehicles; cooperative merging control; on-ramp merging; hierarchical decentralized framework; CarSim/Simulink.

## 9. 必要摘录

> `EXTRACTED` "This paper addresses the problem of integrated longitudinal and lateral cooperative merging control with practical implications for CAVs approaching on-ramps."

> `EXTRACTED` "To the best of the authors’ knowledge, an integrated cooperative longitudinal and lateral control method for merging CAVs at on-ramps has not been reported yet."

> `EXTRACTED` "For each vehicle, the computation time is less than 0.02 s in a control cycle, suggesting that the proposed system can be implemented in real-time."

> `EXTRACTED` "Compared to baseline, the proposed method reduces overall fuel consumption by 21.9%."

> `EXTRACTED` "Compared to the baseline, the proposed method reduces overall fuel consumption by 3.9%."

> `EXTRACTED` "This framework does not consider the influence of uncertainties such as unreliable communication and information interference."

## 10. 回查触发点

- proof：需要解释纵向最优控制、PMP 推导、输入约束或 acceleration/jerk comfort objective 时，回查 `III.A Longitudinal Upper-Level Controller`。
- 实验设计：需要设置 CarSim/Simulink、三车/六车 case、tracking error、燃耗和计算时间指标时，回查 `V. Simulation Experiments`。
- baseline 复现：需要实现 FIFO final time、sigmoid lateral trajectory、DNMPC cost function、driving safety field 或 PI speed tracking 时，回查 `II.A`、`III.B`、`IV.A`。
- 写作：需要论证横向 tracking / vehicle dynamics validation 是现有合流控制短板时，回查 `I. Introduction` 后半部分。
- citation audit：需要核对 DOI、TITS 元数据、作者机构和关键词时，回查论文开头元数据。

## 11. 关键原文位置

- 题名、作者、摘要、DOI、关键词：开头、`Index Terms`。
- related work 与问题缺口：`I. Introduction`。
- hierarchical framework、FIFO 与合流终端状态：`II. Merging Problem Formulation and Hierarchical Control Framework`。
- 纵向上层 optimal control 与 PMP 解法：`III.A Longitudinal Upper-Level Controller`。
- sigmoid 横向轨迹与横向启动时机策略：`III.B Lateral Vehicle Trajectory Planning for On-Ramp Merging`。
- lower-level PI speed tracking、driving safety field、DNMPC：`IV. Vehicle Lower-Level Control`。
- CarSim/Simulink 三车和六车实验：`V. Simulation Experiments`。
- 下层舒适性与通信不确定性局限：`VI. Discussion`、`VII. Conclusion`。
