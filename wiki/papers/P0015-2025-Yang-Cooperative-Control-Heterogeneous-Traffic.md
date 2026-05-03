---
type: paper
paper_id: P0015
title: "Cooperative Control Strategy for Heterogeneous Traffic Flow in Multi-Lane On-Ramp Areas with Connected and Automated Technology"
authors: "Wenzhang Yang, Changyin Dong, Ziqian Zhang, Hui Zhang, Hao Wang"
year: 2025
venue: "Transportation Research Part C: Emerging Technologies"
status: read
confidence: high
source_path: raw/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic.md
zotero_key:
doi:
tags: [CAV, AV, HDV, heterogeneous-traffic, gap-selection, lane-changing-control, capacity-drop, exiD, ramp-metering-comparison]
last_updated: 2026-04-29
---

# P0015: Calibrated Gap Selection and Lane Balance Control

## 1. 一句话定位

这篇论文提出一种非 RL 的可解释协同控制策略：在 HDV/AV/CAV 异质交通中，用 ramp gap selection 优化虚拟 platoon 的可靠 vehicle bonds，并用主线换道控制平衡 Inside/Outside Lane，从而同时改善安全、效率、舒适性和 capacity drop。

## 2. 核心贡献

- `EXTRACTED` 提出面向 multi-lane on-ramp 的 CAV cooperative control strategy，包含 merging control 和 lane-changing control 两个组件。
- `EXTRACTED` merging control 通过 right-of-way / gap selection 让 Outside Lane 与 ramp 车辆在 merging boundary 前形成更有序的 virtual platoon。
- `EXTRACTED` 引入 reliable / unreliable vehicle bond，用最小化 unreliable VBs 和序列变化程度来选择最优 gap selection scheme。
- `EXTRACTED` lane-changing control 通过速度均匀性和密度均匀性决定 CAV 是否换道，以平衡主线两车道交通流。
- `EXTRACTED` 构建包含 HDV/AV/CAV、多种 car-following model 和 exiD 数据校准的仿真框架。
- `EXTRACTED` 讨论 capacity drop，并与 ALINEA、PI-ALINEA ramp metering 方法对比。

## 3. 方法抓手

- Heterogeneous vehicle types：HDV、AV、CAV；CAV 具备自动驾驶和 V2X，AV 具备自动驾驶但不连通。
- Gap selection：先基于到达 merging boundary 时间确定 anticipated gap，再通过 Outside Lane CAV 或 ramp CAV 的主动减速扩展 feasible gaps。
- Vehicle bond：同车道前后关系或 subject 是 CAV 时为 reliable VB；跨车道且信息/控制不足时为 unreliable VB。
- Optimal scheme：第一层最小化 unreliable VB 数量，第二层最小化相对当前顺序的变化程度。
- Lane balance：计算 speed uniformity、density uniformity 及其乘积 `u`，只有换道后 `u_i' >= k_u * u` 才触发 lane-changing decision。
- Simulation calibration：用 exiD 校准 arrival headway distribution、lane-changing dissatisfaction threshold、TTC/distance lane-change thresholds。
- Safety/comfort rules：用 TTC/TET/TETMP/CPMR、emergency braking 和 ISO 2631-1 comfort levels 评价策略。

## 4. 关键实验结论

- `EXTRACTED` AV/CAV 相比 HDV 可显著改善 on-ramp 交通；在拥堵 Set 1 中，AV penetration 从 0.1 到 1 时，TET 降低超过 95%，delay 降低超过 98%。
- `EXTRACTED` CAV 相比 AV 优势更明显；在 Set 1 中，90% CAV 时 delay 为 1.87 s、TET 为 0.11 s，均低于 90% AV 场景的 25%。
- `EXTRACTED` cooperative control 在典型场景中使 TET、TETMP、CPMR 平均 reduction rates 超过 90%，delay 和 CD 最高降低约 40%。
- `EXTRACTED` 在 CAV penetration 0.3-0.6 的轻度拥堵区间，cooperative control 可降低 delay 15%-50%。
- `EXTRACTED` ablation 显示 merging control 是 merging safety 改善主因；lane-changing control 对轻度拥堵下 delay reduction 有明显贡献。
- `EXTRACTED` capacity drop 复现实验中，纯 HDV 合流瓶颈使下游 flow 从约 3056 veh/h 降至 2492 veh/h，drop 约 18.5%。
- `EXTRACTED` CAV penetration 0.5 时，非协同 capacity drop 为 15.9%，协同控制下为 11.2%；纯 CAV 时非协同 drop 为 22.7%，协同控制下为 9.9%。
- `EXTRACTED` 与 ALINEA / PI-ALINEA 对比显示，ramp metering 更易部署且拥堵下能降 delay，但 stop-and-go 可能提高 TET；本文策略在 0.5 penetration 下各指标优于 ramp metering，在纯 CAV 下安全/舒适性优势更明显。
- `EXTRACTED` speed update perturbation `[-10%, 10%]` 下，协同控制组指标仍低于非协同组，显示一定鲁棒性。

## 5. 局限与隐含假设

- 论文自述局限：
  - 未来将扩展到更广泛场景，并加入更多真实世界实验。
- 你识别到的隐含假设：
  - 需要 roadside control center 与高精度广域检测器，实时获取所有车辆位置/速度并向 CAV 下发指令。
  - 尽管使用 exiD 校准，核心验证仍是自建 Python 仿真，而非 SUMO/CarSim/field test。
  - lane-changing execution 被简化为满足条件即可在仿真步内完成，未验证横向动力学和舒适性。
  - communication delay、packet loss、perception error 只通过 speed perturbation 间接触及，未系统建模。
  - gap selection 和 lane balance 均依赖阈值/规则，跨道路几何和驾驶文化的泛化仍需验证。

## 6. 关系线索

- complements: [[wiki/concepts/dual-module-ppo-heterogeneous-onramp-control]]，P0014 用 PPO 学习双模块控制，P0015 用可解释规则、exiD 校准和 capacity-drop 分析替代 RL。
- complements: [[wiki/concepts/flow-level-multilane-comc]]，P0012 是流级 platoon/gap 周期控制，P0015 是车辆级 gap selection + lane balance，但两者都关注多车道与 capacity/stability。
- contrasts: [[wiki/concepts/consensus-based-mixed-traffic-merging]]，P003 有 stability proof，P0015 更偏规则化工程仿真和容量下降分析。
- uses: [[wiki/concepts/calibrated-gap-selection-lane-balance-control]], reliable VB, gap selection scheme, uniformity-based lane-changing, exiD calibration, capacity drop, ALINEA / PI-ALINEA。
- suggests_gap: 需要把 capacity-drop-aware cooperative control 与横向执行、通信延迟和真实/高保真验证统一。
- asset_todo: 原始 MinerU 文件含大量外链图片，后续如需写作审计，应本地化到 `raw/assets/P0015/`。

## 7. 对我研究的可能用途

- baseline: 可作为 non-RL / interpretable heterogeneous traffic baseline，与 P0014 PPO baseline 成对比较。
- mechanism_source: reliable/unreliable vehicle bond 是一个可解释的合流风险结构，可用于设计排序代价或 proof sketch。
- experiment_design: capacity drop reproduction、ALINEA/PI-ALINEA 对比、speed perturbation、merging-only vs lane-changing-only ablation 都可复用。
- counterexample: 只优化 ramp delay 的 ramp metering 可能提高 TET，提示新方法要同时报告 safety 和 comfort。
- metric: TET、TETMP、CPMR、delay、CD、capacity drop ratio、flow at observation points、speed update perturbation sensitivity。

## 8. 原文锚点

- raw: `raw/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic.md`
- zotero:
- doi:
- keywords: On-ramp; Cooperative control; Connected and automated technology; Heterogeneous traffic flow.

## 9. 必要摘录

> `EXTRACTED` "It consists of two primary components: merging control and lane-changing control."

> `EXTRACTED` "Several safety-related indicators show average reduction rates exceeding 90% for typical simulation scenarios."

> `EXTRACTED` "delays and cumulative discomfort index values can be reduced by up to 40%."

> `EXTRACTED` "the cooperative control approach mitigates the capacity drop phenomenon"

> `EXTRACTED` "In a pure HDV environment, the flow rate downstream of the congestion bottleneck decreased from approximately 3056 veh/h to around 2492 veh/h, a reduction of about 18.5%."

> `EXTRACTED` "At the 0.5 CAV penetration rate, the cooperative control strategy outperformed traditional ramp metering approaches across all performance metrics"

## 10. 回查触发点

- proof：需要解释 reliable/unreliable VB、gap selection scheme 或 lane uniformity objective 时，回查 `3. Cooperative control strategy for CAVs`。
- 实验设计：需要复现 exiD 参数校准、TET/TETMP/CPMR/CD 指标、capacity drop 或 ALINEA 对比时，回查 `4. Simulation modelling framework`、`5.4`、`5.5`。
- baseline 复现：需要实现 HDV/AV/CAV 多模型 car-following、gap selection、lane-changing control 或 speed perturbation 时，回查 `4.2`、`5.6`。
- 写作：需要论证“协同控制比 ramp metering 更能同时兼顾安全/效率/舒适性”时，回查 `5.5. Comparation to the ramp metering methods`。
- citation audit：需要核对 exiD、ALINEA、PI-ALINEA、capacity drop、Yang 2023b/P0014 关系时，回查 `References`。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头、`A R T I C L E I N F O`、`A B S T R A C T`。
- 研究动机、相关工作和 gap：`1. Introduction`。
- connected/automated heterogeneous scenario：`2. Research scenario`。
- merging control、gap selection、vehicle bond、lane-changing control：`3. Cooperative control strategy for CAVs`。
- 仿真框架、车辆行为模型、exiD 校准、评价指标：`4. Simulation modelling framework`。
- AV/CAV 优势、协同控制效果、ablation、flow sensitivity、trajectory：`5.2`、`5.3`。
- capacity drop：`5.4. Discussion on capacity drop`。
- ramp metering comparison：`5.5. Comparation to the ramp metering methods`。
- speed perturbation robustness 和 low-demand lane-changing：`5.6`、`5.7`。
- 结论：`6. Conclusions`。
