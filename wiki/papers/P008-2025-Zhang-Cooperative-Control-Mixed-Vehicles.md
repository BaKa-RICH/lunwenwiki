---
type: paper
paper_id: P008
title: "A traffic control strategy for freeway merging zones cooperating safety and efficiency in the intelligent connected environment of mixed vehicles"
authors: "Lang Zhang, Heng Ding, Zeyang Cheng, Xiaoyan Zheng, Weihua Zhang"
year: 2025
venue: "Transportation Research Part C: Emerging Technologies"
status: read
confidence: high
source_path: raw/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles.md
zotero_key:
doi: 10.1016/j.trc.2025.105298
tags: [mixed-vehicles, CAV, HV, trucks, MPC, NSGA-II, Transformer, multi-objective-control, safety-efficiency]
last_updated: 2026-04-28
---

# P008: Transformer-Adaptive Safety-Efficiency Control for Mixed Vehicles

## 1. 一句话定位

这篇论文面向 car/truck 与 CAV/HV 共存的混合车辆匝道合流区，用分布式 MPC、NSGA-II Pareto 行为决策和 Transformer adaptive weighting 动态平衡安全与效率。

## 2. 核心贡献

- `EXTRACTED` 提出 mixed-vehicle traffic flow 的 distributed CAV behavioural decision model（BDM），车辆类型包括 CAV car、CAV truck、HV car、HV truck。
- `EXTRACTED` 在 CAV 行为决策中同时优化 traffic efficiency 和 safety，效率用行驶距离/停车延误等指标体现，安全用 RTTC/TIT 风险指标体现。
- `EXTRACTED` 用 NSGA-II 直接生成 Pareto frontier，避免线性加权无法覆盖非凸 Pareto 区域的问题。
- `EXTRACTED` 用 Transformer 预测不同控制权重下的系统状态，并由 adaptive weighting model（AWM）从 Pareto frontier 中选择当前交通状态下的最优方案。
- `EXTRACTED` 通过 CAV 间迭代协商和控制中心评价，把单车分布式决策推向系统级优化。

## 3. 方法抓手

- Scenario：two-lane mainline + single-lane on-ramp，控制区由通信半径和加速/合流区定义。
- BDM：每辆 CAV 在 MPC 框架下求解 multi-objective nonlinear mixed-integer planning，决策变量包括加速度和左右换道二元变量。
- HV prediction：纵向用改进 IDM，匝道 HV mandatory lane-changing 用概率模型和安全约束；主线 HV 自由换道在决策阶段被忽略以降低复杂度。
- AWM：输入车辆状态、控制权重、CAV/truck penetration、局部密度/均速/速度标准差，输出下一时刻局部交通状态，用于选择安全-效率权重。
- Iterative cooperation：CAV 逐车基于其他车辆预测轨迹调整自身行为，控制中心用系统级 `F1/F2` 检查收敛并选择最终轨迹。

## 4. 关键实验结论

- `EXTRACTED` 摘要报告：即使在 20% CAV penetration 下，BDM-AWM 也可将 total parking delay 降低 48.7%，TIT 降低 72.2%。
- `EXTRACTED` NGSIM I-80 5:00-5:30 数据的 feasibility validation 中，15% CAV 场景下 BDM-AWM 相比 NC 将 total parking delay 降低 57.4%，TIT 降低 6.7%。
- `EXTRACTED` 在 20%、60%、100% CAV penetration 与 0%、5%、15% truck penetration 的 27 个场景中，BDM-AWM 的 total stopping delay 均低于 NC 和 BDM。
- `EXTRACTED` BDM-AWM 相比 NC 的平均 TIT reduction 为 67.8%，高于 BDM 的 59.7%，说明 adaptive weighting 对安全提升有额外贡献。
- `EXTRACTED` 100% CAV penetration 下，BDM-AWM 平均降低 TTT 29.2%、TD 59%、RTTC 92%。

## 5. 局限与隐含假设

- 论文自述局限：
  - 系统扰动和模型不确定性主要依赖 MPC rolling optimization 处理，缺少理论鲁棒性支持。
  - HV trajectory prediction 精度不足，限制了 CAV 行为决策的解空间。
- 你识别到的隐含假设：
  - 假设 CAV-to-CAV、CAV-to-HV、CAV-to-infrastructure communication 可用，且不考虑通信延迟。
  - 假设 CAV car 与 CAV truck 物理性能不同，但驾驶行为无差异。
  - 主文不显式建模 lane-changing trajectory，虽然附录给出扩展，横向动态仍不是主控制闭环核心。
  - HVW / OVM-HV 鲁棒性分析仍依赖简化感知和预测假设，例如未感知 HVW 的速度在预测域内保持不变。

## 6. 关系线索

- extends: [[wiki/concepts/mixed-traffic-multilane-cormc]]，从 CAV/CHV compliance 扩展到 CAV/HV + car/truck 的混合车辆异质性。
- complements: [[wiki/concepts/flexible-control-barrier-function-merging]]，P006 强调局部 safety-critical control，P008 强调系统级安全-效率权重自适应。
- contrasts: [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]]，P007 在纯 CAV 中做强一体化优化，P008 在混合车辆中牺牲全局最优，换取分布式可扩展与动态权重。
- uses: BDM-AWM paper-specific mechanism, BDM, AWM, NSGA-II, Pareto frontier, Transformer, TIT, RTTC；原单篇 concept 已删除，核心信息保留在本 card 与 [[wiki/comparisons/merging-control-baselines]]。
- suggests_gap: mixed vehicle heterogeneity、adaptive safety-efficiency weighting、communication delay、lateral trajectory 和理论鲁棒性尚未统一。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P008/`。

## 7. 对我研究的可能用途

- baseline: 可作为 mixed vehicle + multi-objective safety-efficiency 控制 baseline，尤其适合检验只优化效率的方法是否牺牲安全。
- idea_source: Transformer-AWM 提供一种“根据交通状态动态选择安全/效率偏好”的机制，可作为 candidate idea 的权重选择模块。
- counterexample: 即便考虑 mixed vehicles 和安全指标，通信延迟、横向轨迹、理论鲁棒性仍可能是薄弱点。
- dataset_or_metric: NGSIM I-80、CAV penetration、truck penetration、total parking delay、TTT、TD、TIT、RTTC、mandatory lane-changing ratio。
- assumption: 可通信、可预测 HV、CAV 具备独立求解能力、MPC rolling optimization 可吸收扰动。

## 8. 原文锚点

- raw: `raw/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles.md`
- zotero:
- doi: 10.1016/j.trc.2025.105298
- keywords: Freeway; merging zone; mixed-vehicle traffic flow; cooperative control; model predictive control.

## 9. 必要摘录

> `EXTRACTED` "Even at 20% CAV penetration rates, this strategy reduces total parking delays by 48.7% and time-integrated time-to-collision (TIT) by 72.2%."

> `EXTRACTED` "The mixed traffic flow consists of four types of vehicles: the CAV truck, the CAV car, the HV truck and the HV car."

> `EXTRACTED` "Transformer is used to establish the relationship between individual CAV behaviours and the system state."

> `EXTRACTED` "The BDM-AWM scenario yields an average TIT reduction rate of 67.8%, whereas the BDM scenario yields an average reduction rate of 59.7%."

## 10. 回查触发点

- proof：需要讨论多目标 Pareto、NSGA-II、adaptive weighting 或 Transformer 预测系统状态时，回查 `3.3. Model solving algorithm` 和 `4. Transformer-based adaptive efficiency and safety weighting model`。
- 实验设计：需要设置 CAV/truck penetration、NGSIM I-80、TIT/RTTC/TTT/TD、BDM vs BDM-AWM vs NC 对比时，回查 `6. Case analysis`。
- baseline 复现：需要 vehicle-level BDM、AWM 输入输出、迭代协作流程、参数表或控制域设置时，回查 `3. CAV behavioural decision model`、`5. Control process`、`Table 2`。
- 写作：需要强调 mixed vehicle heterogeneity、truck moving bottleneck 或安全-效率动态权衡时，回查 `1. Introduction` 与 `6.3. Result analysis`。
- citation audit：需要核对 DOI、TR-C 元数据、supplementary material 和相关 mixed vehicle / NSGA-II / Transformer 引用时，回查开头元数据、`Appendix B` 与 `References`。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头、`A B S T R A C T`。
- mixed-vehicle 问题定位、研究缺口和贡献：`1. Introduction`。
- 控制场景、车辆类型和通信假设：`2. Control scenario and framework`。
- BDM、HV prediction、目标函数和约束：`3. CAV behavioural decision model`。
- Transformer-AWM：`4. Transformer-based adaptive efficiency and safety weighting model`。
- CAV 迭代协商与控制流程：`5. Control process`。
- NGSIM、penetration、truck、TIT/RTTC/TTT/TD 结果：`6. Case analysis`。
- 鲁棒性和未来工作：`7. Conclusion`。
- 横向轨迹扩展：`Appendix A. Expansion of BDM on vehicle lateral motion`。
