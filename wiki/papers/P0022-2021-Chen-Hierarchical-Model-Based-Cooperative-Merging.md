---
type: paper
paper_id: P0022
title: "A Hierarchical Model-Based Optimization Control Approach for Cooperative Merging by Connected Automated Vehicles"
authors: "Na Chen, Bart van Arem, Tom Alkim, Meng Wang"
year: 2021
venue: "IEEE Transactions on Intelligent Transportation Systems"
status: read
confidence: high
source_path: raw/papers/P0022-2021-chen-cooperative-merging-cavs.md
zotero_key:
doi: "10.1109/TITS.2020.3007647"
tags: [CAV, on-ramp-merging, hierarchical-control, merging-sequence, speed-adaptation-time, MPC, model-based-control, FIFO]
last_updated: 2026-04-29
---

# P0022: Hierarchical Model-Based Cooperative Merging

## 1. 一句话定位

这篇论文提出一个纯 CAV 分层合流控制框架，战术层同时优化合流顺序和匝道车开始速度/位置适应的时间，执行层用 MPC 和三阶车辆动力学决定加速度与换道启动时刻。

## 2. 核心贡献

- `EXTRACTED` 设计 hierarchical control architecture：roadside tactical layer 负责 gap/sequence 和 speed-adaptation time，vehicle operational layer 负责 acceleration trajectory 和 lane-changing initiation time。
- `EXTRACTED` 战术层使用 second-order car-following model，并区分 car-following mode 与 cooperative merging mode。
- `EXTRACTED` 将 on-ramp CAV 的 speed-adaptation time `t^p` 纳入战术决策，允许匝道车先以期望速度行驶一段时间，再开始适应目标 gap。
- `EXTRACTED` 执行层使用 third-order vehicle dynamics 与 MPC，考虑 actuator lag，并基于当前和预测 time gaps 判断 lane-changing acceptability。
- `EXTRACTED` 在 135 个不同 initial conditions、desired time gaps 和 on-ramp vehicle 数量的场景中，与 FIFO sequence + same operational controller benchmark 对比。
- `EXTRACTED` 给出何时可以合理使用 FIFO 的经验建议：当匝道车初速接近主线且相对位置在两辆主线车中部时，FIFO 更可能接近最优。

## 3. 方法抓手

- Tactical decision variable：`(f_r, t^p)`，其中 `f_r` 是合流后的车辆顺序，`t^p` 是匝道车开始为目标 gap 调速/调位的时间。
- Tactical model：second-order dynamics + Helly car-following + cooperative merging mode，用较粗时间步降低计算量。
- Objective：加权惩罚 gap error、relative speed 和 acceleration，同时加入 terminal gap / relative speed error。
- Operational decision：desired accelerations、lane-changing acceptability `xi_r` 和 lane-changing initiation time `t^l`。
- Operational model：third-order longitudinal dynamics with actuator lag，MPC horizon `T_p = 6 s`。
- Safety gate：匝道车当前和预测 inter-vehicle time gaps 对未来前车/后车都满足阈值后，才允许换道。
- Rejection/fallback：若 operational layer 找不到可行解，可拒绝 tactical command 并请求新决策；若靠近加速车道末端，则直接选择下一个 gap。

## 4. 关键实验结论

- `EXTRACTED` 135 个场景中，两种控制方法均未发生 collision。
- `EXTRACTED` 单匝道车、主线 equilibrium 的 45 个场景中，HCA 在 34 个场景优于 FIFO，在 11 个场景表现相同。
- `EXTRACTED` 当匝道车初速为 15 m/s 时，HCA 在表 I 所列场景中改善均高于 14.92%，部分场景改善超过 80%。
- `EXTRACTED` 主线 non-equilibrium 场景中，HCA 在 29/45 个场景优于 FIFO，平均改善 33.01%。
- `EXTRACTED` 两辆匝道车场景中，HCA 在 34/45 个场景改善，平均改善 26.65%，4 个场景平均恶化约 1.2%。
- `EXTRACTED` 示例中，两辆匝道车时 HCA 将 objective function 从 FIFO 的 5732.25 降至约 3473.94，改善 39.40%。
- `EXTRACTED` 计算时间：单匝道车战术层约 0.32 s；两辆匝道车全枚举约 4.8 s；执行层 6/7 辆车约 0.91 s / 1.12 s。

## 5. 局限与隐含假设

- 论文自述局限：
  - 当前研究假设 100% CAV；未来需扩展到 multiple main lanes、outermost main lane courtesy lane change 和 mixed traffic。
  - 当 on-ramp vehicles 增多时，战术层枚举计算时间显著上升，需要更高效的 mixed-integer programming 或限制候选。
  - 对 HDV 扩展需要合理 car-following/lane-changing model，并在 operational layer 处理效率与碰撞风险权衡。
- 你识别到的隐含假设：
  - 车辆状态估计基本准确，仅考虑 0.2 s fixed feedback delay，没有系统通信延迟、packet loss 或 perception noise sweep。
  - 横向换道由多项式轨迹表达，缺少车辆动力学级横向 tracking 和舒适性验证。
  - 性能指标主要是内部 objective function，而不是直接 travel time、fuel、TTC/DRAC 或 throughput。
  - 只覆盖单主线/单匝道小规模 CAV platoon，未验证连续交通流、capacity drop 或大规模网络。
  - 权重手动调参，最优 sequence 与性能指标强相关，泛化到多目标评价需谨慎。

## 6. 关系线索

- uses: [[wiki/concepts/hierarchical-sequence-speed-adaptation-control]], merging sequence, speed-adaptation time, tactical MIQP, operational MPC, lane-changing acceptability。
- complements: [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]]，P007 同时优化 sequence/trajectory，P0022 强调在 sequence 之外加入 `t^p` 以避免匝道车过早调速。
- complements: [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]]，P0011 更重车辆动力学横向执行，P0022 更重 sequence + speed-adaptation timing。
- complements: [[wiki/concepts/vts-drl-ocp-onramp-merging]]，P0020 用 VTS-DRL 决定合流窗口，P0022 用模型优化枚举 sequence 与 `t^p`。
- contrasts: [[wiki/concepts/dcoma-dynamic-cooperative-merging-assistant]]，P0021 从宏观流级造 gap，P0022 在局部 CAV platoon 内优化进入哪个 gap 以及何时开始适应。
- suggests_gap: speed-adaptation time 是被忽视的决策维度，但仍需在 mixed traffic、延迟、真实横向执行和多目标指标下验证。
- asset_todo: 原始 MinerU 文件含外链图片和作者照片，后续如需写作审计，应本地化到 `raw/assets/P0022/`。

## 7. 对我研究的可能用途

- baseline: 可作为 pure CAV sequence + speed-adaptation timing 的经典 model-based baseline。
- mechanism_source: `t^p` 提醒后续方法不应只问“合流到哪个 gap”，还应问“何时开始为该 gap 调速/调位”。
- proof_source: tactical/operational model mismatch、command rejection 和 next-gap fallback 是分层控制可行性 proof 的有用素材。
- experiment_design: 135 场景设计可改造成最小 benchmark：initial speed、relative position、desired time gap、one/two ramp vehicles。
- risk_source: objective-function-based improvement 不等于交通效率直接改善，后续需要统一到 travel time/safety/fuel/comfort 指标。

## 8. 原文锚点

- raw: `raw/papers/P0022-2021-chen-cooperative-merging-cavs.md`
- zotero:
- doi: `10.1109/TITS.2020.3007647`
- keywords: connected automated vehicles; on-ramp merging; merging sequence; optimization control.

## 9. 必要摘录

> `EXTRACTED` "A tactical layer controller employs a second-order car-following model with a cooperative merging mode to represent a cooperative merging process and generates an optimal vehicle merging sequence and time instants when on-ramp CAVs start to adapt their speeds and positions"

> `EXTRACTED` "An operational layer controller is designed based on Model Predictive Control (MPC). It uses a third-order vehicle dynamics model"

> `EXTRACTED` "The performance ... is demonstrated under 135 scenarios with different initial conditions, desired time gap settings, and numbers of on-ramp vehicles."

> `EXTRACTED` "The experimental results show the superiority of the hierarchical control approach."

> `EXTRACTED` "The proposed hierarchical control approach brings pronounced improvements ... when the initial speed of the on-ramp vehicle is significantly lower than the mainline traffic"

> `EXTRACTED` "When one on-ramp vehicle exists and five mainline vehicles exist ... the computation time of the tactical layer controller is 0.32s."

## 10. 回查触发点

- proof：需要解释 `t^p`、two-mode tactical model、lane-changing acceptability 或 command rejection/fallback 时，回查 `III` 和 `IV`。
- 实验设计：需要复现 135 场景、FIFO 使用建议、single/two ramp vehicles 或 feedback delay 时，回查 `V` 与 `VI`。
- baseline 复现：需要实现 tactical enumeration of `k` and `t^p`、operational MPC 或 polynomial lateral motion 时，回查 `IV` 和 Appendix A。
- 写作：需要论证“合流排序不应在匝道车进入控制区时立即固定，而应允许 speed-adaptation delay”时，回查 `VI.D Discussion` 和 `VII`。
- citation audit：需要核对 TITS 元数据、DOI、参数值和作者时，回查论文开头、`V.C` 和 references。

## 11. 关键原文位置

- 题名、作者、摘要、DOI：开头。
- merging sequence 文献综述：`II`。
- 分层控制架构、command rejection、lane-changing logic：`III`。
- tactical layer `f_r/t^p` 与 operational MPC：`IV`。
- 135 场景、benchmark、参数和指标：`V`。
- no-collision、improvement、FIFO 建议和 computation time：`VI`。
- 结论与 future mixed/multilane direction：`VII`。
- 横向换道多项式：Appendix A。
