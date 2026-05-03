---
type: comparison
last_updated: 2026-04-29
source_pages:
  - wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control.md
  - wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control.md
  - wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control.md
  - wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging.md
  - wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging.md
  - wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging.md
  - wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging.md
  - wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles.md
  - wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay.md
  - wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic.md
  - wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging.md
  - wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging.md
  - wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp.md
  - wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic.md
  - wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging.md
  - wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control.md
  - wiki/papers/P0020-2024-Muzahid-Optimizing-On-Ramp-Merging-DRL-OCP.md
  - wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant.md
  - wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging.md
  - wiki/synthesis/mid-field-synthesis-P001-P0022.md
confidence: medium
---

# Merging Control Baselines

本页用于承接 Batch 01 中出现的主要 baseline、排序机制和控制机制，避免 `field-map.md` 继续膨胀。它服务于后续 query、candidate idea 生成、proof 和实验设计。

## 1. 机制对比表

| 机制 | 代表论文 | 解决的问题 | 优势 | 局限 | 适合做什么 baseline | 可能启发的 idea |
| --- | --- | --- | --- | --- | --- | --- |
| FIFO / FCFS | [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]], [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] | 用进入顺序快速决定合流顺序 | 简单、可解释、实时性好 | 可能牺牲全局效率；P003 显示 MS 优于 FCFS | 低复杂度排序 baseline | 在双车道匝道或混合交通中设计优于 FIFO 但仍实时的排序策略 |
| Closed-form optimal control | [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]] | 在单主路单匝道中在线求解燃耗友好、安全的合流控制 | 解析、可解释、适合 proof | 几何和交通组成简化；约束激活时需额外处理 | 经典解析型 CAV merging baseline | 作为局部 proof module，为复杂排序策略提供可解释控制层 |
| MCTS-DA | [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]] | 在 flexible merging positions 下近似求解战术层复杂优化 | 扩大解空间同时控制计算复杂度 | 仍依赖纯 CAV、完美通信和非凸 MIQCP 结构 | Flexible merging position 的优化型 baseline | 用学习辅助搜索、线性化或滚动优化降低复杂度 |
| APS / CUC | [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]] | 在 mixed traffic multilane 场景中指定协作车辆并决定主线车辆是否换道 | 显式考虑 CHV compliance 和主线换道协作 | compliance 二值化，无通信延迟，仿真验证为主 | Mixed traffic + multilane cooperation baseline | 将协作车辆选择与 stability-aware controller 结合 |
| Shortest-path merging sequencing | [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]] | 将合流排序从 zero-one integer programming 转为固定起点 shortest-path search | 降低排序复杂度，优于 FCFS | 依赖成本函数设计；合流点固定 | 实时优化排序 baseline | 在 dual-lane ramp 或 flexible merging positions 中替换 FIFO |
| Consensus controller | [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]] | 在 mixed traffic platoon 中保证 local/string stability 和抗扰动 | 有稳定性 proof，可解释性强 | 横向控制简化，通信延迟和 HDV 模型仍理想化 | Stability-aware motion planning baseline | 将协作车辆选择、换道协作与稳定性约束统一 |
| Rolling trajectory optimization | [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] | 在合流区周期性优化轨迹，允许匝道车在加速车道任意位置合流 | 适合复杂几何和在线更新 | 纯 CAV，未优化横向 tracking，排序仍用 FIFO | 多区域复杂几何 baseline | 与 flexible merging positions、upstream gap shaping 结合 |
| Multi-area control | [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] | 将合流控制前移到主线上游、匝道上游和合流区多区域协同 | 工程结构清晰，高需求下减少停车和延误 | 混合交通和 lateral tracking 未解决 | Multi-lane mainline + dual-lane ramp baseline | 构建“上游塑形 + 合流位置 + 稳定性”的统一框架 |
| FPM-FCBF | [[wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging]] | 在 mixed traffic 中把 flexible merging position 与 safety-critical constraints 连接起来 | CBF/CLF-QP 实时性强，可把期望合流位置嵌入连续安全约束 | TCG 选择、排序、横向执行、HDV 预测和通信延迟仍未统一 | Safety-critical flexible merging baseline | 将 FCBF 与稳定性、横向 tracking 或协作车辆选择结合 |
| Integrated MINLP sequence + trajectory | [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]] | 同时决定 merge-in gap、合流顺序、终端时间和连续轨迹 | 避免先排序后规划造成不可行/低质量轨迹；NGSIM 上接近 MCTS-DA 延误但计算更快 | 100% CAV、单主线单匝道纵向控制；匝道车数量增加时搜索仍快增 | 强优化型 sequencing + trajectory baseline | 用轨迹质量驱动排序，并与 mixed traffic prediction / lateral control 结合 |
| BDM-AWM | [[wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles]] | 在 CAV/HV 与 car/truck 混合车辆中动态平衡安全和效率 | 分布式 MPC + Pareto + Transformer 权重选择，显式考虑 TIT/RTTC 和 truck penetration | 通信延迟忽略，理论鲁棒性不足，横向轨迹主要在附录扩展 | Mixed-vehicle multi-objective baseline | 将动态安全-效率权重接入 safety-critical 或 sequencing 框架 |
| Vehicle-in-the-loop delay assessment | [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]] | 用 field data 评估通信延迟对 CAV 合流控制、速度波动和能耗的影响 | 提供 ACM 实测 delay、能耗和 H-LSTM 证据，补足纯仿真假设 | 一辆真实 CAV + digital twin，侧重能耗/波动而非完整合流控制性能 | Delay-aware robustness evidence / field validation baseline | 将 delay 扰动加入 safety-critical、stability 或 energy-aware 实验 |
| Strategic CAV influence | [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]] | 通过减速 HDV 前方 CAV 来影响 HDV 到达时间，降低相邻 CAV 合流不确定性 | 不强依赖精确 HDV 预测；在 20 车 mixed traffic 中最高 ATTD 降低 31% | 假设无通信延迟/丢包，HDV 用 IDM，横向换道反应未充分建模 | Mixed traffic multi-CAV arrival-time baseline | 将“影响 HDV”与 delay robustness、probabilistic HDV reaction 或 safety layer 结合 |
| Integrated longitudinal-lateral DNMPC | [[wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging]] | 将上层纵向最优控制、横向轨迹规划和下层车辆动力学 tracking/避碰接起来 | CarSim/Simulink 近真实车辆动力学验证；DNMPC 每周期计算时间 < 0.02 s；三车 case 燃耗降低 21.9% | FIFO、纯 CAV、单主线单匝道；上层 comfort objective 与下层 acceleration/jerk tracking 存在断点 | Integrated lateral-longitudinal execution baseline | 将横向 DNMPC / driving safety field 接入 sequencing、safety-critical 或 mixed traffic 框架 |
| Flow-level multilane CoMC | [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]] | 在多车道主线中周期性创造外侧车道 gap，并以 ramp platoon 释放合流流量 | 显式处理连续交通流效率和 shockwave 稳定；2C 高需求场景 overall delay 降低 86.4% | 100% CAV、即时通信、精确控制；换道规则 compliance 和 vehicle-level execution 未充分解决 | Flow-level traffic-stability baseline | 将上层 `n/d/v_C` flow plan 与下层 DNMPC / CBF / mixed-traffic role assignment 结合 |
| Dual-module PPO cooperative control | [[wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp]] | 用 MC/LC 两个 PPO 模块分别处理 Lane 2/ramp 合流协作和主线换道协作 | 低 CAV penetration 仍有效；`p_C=0.2` delay 降低 26%，`p_C>=0.3` TET 约降 45%；有 transferability analysis | 缺少 safety/stability proof；lane-change execution 简化；通信/感知/网络扰动未进入实验 | Low-penetration heterogeneous traffic RL baseline | 将 RL proposal layer 与 CBF/DNMPC safety filter 或可解释权重机制结合 |
| Calibrated gap selection + lane balance | [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]] | 用 reliable/unreliable vehicle bonds 选择 ramp gap，并用速度/密度均匀性控制主线换道 | exiD 校准；典型场景 TET/TETMP/CPMR 降幅 >90%，delay/CD 最高降约 40%；缓解 capacity drop | 需要路侧高精度感知和控制中心；横向执行简化；delay/noise 仅弱测试 | Non-RL interpretable heterogeneous multi-lane baseline | 将 VB-based risk term 接入排序代价、safety filter 或 capacity-drop-aware objective |
| HCOMC model-based two-lane control | [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]] | 用 modified virtual vehicle、Stackelberg game 和 NSGA-II 联合决定合流轨迹、合流位置和 VMC 纵向/横向协作模式 | HCOMC critical distance 相比 FIFO/game 提高 9.11%/5.13%；Condition 2 稳定时间缩短 54.79%/53.53% | 六关键车小规模仿真；通信/感知扰动未测；模型组合复杂且实时性未充分量化 | Model-based integrated longitudinal-lateral cooperation baseline | 将协作模式切换与 delay-aware safety filter、continuous lateral tracking 或 flow-level objective 结合 |
| HCMCC MILP + LCMPC-PTO multilane control | [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]] | 在 mixed traffic 多车道合流中利用 Lane 0/1/2 CAV，规划合流、cut-in、Lane 2 assistance 和合流后车道均衡 | 2800 veh/h 下 average TT 改善约 16.32%-42.86%；3200 veh/h、PR=0.8 下 total ATF 提升约 10.28%-12.13%；LCMPC-PTO tracking error 明显小于 LCMPC | 无通信延迟；instant lane-changing；HV 采用 IDM+保守换道；依赖 RSU 完整状态和 Gurobi/SUMO 仿真 | Multi-lane mixed traffic + execution-layer baseline | 将 Lane 2 assistance 与真实 lane-change duration、delay/noise、prediction uncertainty 和 lateral tracking 结合 |
| VTS-DRL + OCP speed control | [[wiki/papers/P0020-2024-Muzahid-Optimizing-On-Ramp-Merging-DRL-OCP]] | 用 Yield/Green virtual traffic signal 简化 DRL 合流排序，再用 OCP/MPC 生成安全节能速度轨迹 | 相比 SUMO Krauss，mainline throughput 提升 12.5%，emergency braking 减少 28%，fuel efficiency 改善 31.66% | 100% CAV、理想通信与完美感知；mixed traffic 仅补充分析；baseline 较弱，缺 delay/noise 和强 CAV merging 对比 | Hybrid learning-proposal + model-based execution baseline | 加入 CBF/DNMPC safety filter、delay compensation、mixed traffic HDV reaction 和 stronger baselines 做 ablation |
| DCoMA dynamic macro-micro gap creation | [[wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant]] | 用 FD 动态计算目标状态 C 和 gap time-series，主线 CAV platooning 造 gap，匝道车辆不停驶入 | 高需求下 total travel time 相比 ALINEA/X-ALINEA/Q/CoopMA 降约 5.93%/5.68%/5.65%；overall fuel consumption 降 61%-66%；安全指标整体更优 | 单车道、free-flow、通信延迟忽略、created gap 被保护、FD 依赖 IDM 理想化；低 MPR 效果弱 | Dynamic-demand-aware flow-level merging baseline | 与 VTS-DRL、CBF/DNMPC、真实 FD、delay/noise 和 multi-lane lane-changing 结合 |
| HCA sequence + speed-adaptation timing | [[wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging]] | 战术层联合优化合流顺序和 on-ramp CAV speed-adaptation time，执行层 MPC 决定加速度与换道启动 | 135 场景无碰撞；单匝道车 equilibrium 场景 34/45 优于 FIFO；non-equilibrium 平均改善 33.01%；两匝道车平均改善 26.65% | 100% CAV、小规模单主线/单匝道；指标主要为内部 objective；计算随匝道车数快速增加；混合交通和横向执行有限 | Pure-CAV timing-aware sequence baseline | 将 `t^p` 接入 VTS/DCoMA/CBF/DNMPC，检验“何时开始调速”对安全与效率的边际贡献 |

## 2. 当前最关键的对比轴

| 对比轴 | 低复杂度端 | 高表达能力端 | 当前风险 |
| --- | --- | --- | --- |
| 合流排序 | FIFO / FCFS | shortest-path / MCTS / rolling optimization | 高表达能力可能牺牲实时性 |
| 合流位置 | fixed merge point | flexible / rolling merge position | flexible 收益可能依赖纯 CAV 和单车道设定 |
| 交通组成 | pure CAV | mixed CAV / CHV / HDV | mixed traffic 下 compliance 和 HDV stochasticity 难建模 |
| 车辆异质性 | passenger cars only | car/truck + CAV/HV mixed vehicles | truck penetration 会改变拥堵、安全和控制收益解释 |
| 控制层级 | 单层轨迹控制 | sequencing + tactical + motion planning | 层级越多，接口和稳定性越难证明 |
| 交通流尺度 | 局部 merging triplet | flow-level gap creation + ramp platooning | 局部收益可能无法防止连续流 shockwave 或 recurrent congestion |
| 验证目标 | efficiency | safety + comfort + robustness + stability | 多目标可能导致实验解释困难 |
| 学习策略 | rule / optimization / control-theory | PPO / multi-agent RL | 低渗透率收益强，但可解释性和安全可证明性不足 |
| 可解释规则 | vehicle-bond / gap-selection rule | data-calibrated + capacity-drop-aware rule | 工程透明，但跨场景泛化和执行层验证仍需补足 |
| 协作模式 | longitudinal facilitating only | longitudinal vs lateral cooperation switching | 横向协作收益大，但可能增加燃耗、复杂度和执行风险 |
| 安全约束 | 合流时刻离散约束 | continuous CBF / FCBF safety constraints | 约束可证明性与排序、横向控制、延迟鲁棒性尚未统一 |
| 排序-轨迹耦合 | 先排序再规划 | integrated sequence + trajectory optimization | 一体化模型更强，但更依赖纯 CAV 和求解规模假设 |
| 执行层验证 | 点质量/运动学仿真 | CarSim/Simulink vehicle dynamics co-simulation | 上层舒适性和安全目标可能无法被下层执行完全保真 |
| 证据类型 | simulation-only | field / vehicle-in-the-loop data | field data 更真实，但样本规模和可控性有限 |
| HDV 处理方式 | predict / treat as disturbance | strategically influence HDV through CAV actions | 影响机制需要真实 HDV 反应和延迟鲁棒性验证 |

## 3. 对后续 idea 的启发

- `Stability-aware cooperative vehicle selection`：P002 的 APS/CUC 与 P003 的 consensus controller 有互补性，但必须证明协作车辆选择会改善 string stability，而不是简单模块拼接。
- `Dual-lane ramp sequencing beyond FIFO`：P004 的 dual-lane ramp 仍用 FIFO，P003 提供实时优化排序线索，P005 提供解析型控制基线。
- `Flexible merging position + upstream gap shaping`：P001 的 flexible merging positions 与 P004 的 multi-area upstream shaping 可以结合，但需证明边际收益不是重复。
- `Safety-critical flexible merging`：P006 的 FPM-FCBF 使 flexible merging position 具备连续安全约束接口，可作为后续 integrated lateral-longitudinal control 或 stability-aware merging 的安全层。
- `Trajectory-quality-driven sequencing`：P007 显示最优合流顺序应由候选序列诱导出的轨迹成本决定，可作为替代 FIFO / FCFS 的强优化参照。
- `Adaptive safety-efficiency weighting`：P008 显示安全和效率权重可随交通状态动态变化，适合补足固定目标函数在 mixed vehicle 场景中的解释缺口。
- `Delay-aware field validation`：P009 表明 0.06 s 量级通信延迟已能影响速度波动和能耗，后续仿真实验应至少加入 delay sweep 或 vehicle-in-the-loop 对照。
- `Strategic HDV influence`：P0010 提供一个新机制，把 CAV 从被动适应 HDV 转为主动塑造 HDV 行为，但其无延迟和简化 HDV 反应假设需要重点审查。
- `Lateral-longitudinal execution validation`：P0011 提醒后续方法不能只报告上层轨迹收益，还要验证下层 tracking、yaw/lateral acceleration、计算时间和车辆动力学可执行性。
- `Flow-level gap shaping`：P0012 提供多车道流级控制参照，后续若只优化单车轨迹，需要额外证明不会在连续流中诱发 shockwave 或 recurrent congestion。
- `Dual-module RL control`：P0014 显示 RL 可在低 CAV penetration 的 mixed traffic 中同时改善效率和 TET，但后续需要可解释 safety layer 和真实通信/感知扰动验证。
- `Calibrated interpretable control`：P0015 提供 P0014 的非 RL 对照，把 gap selection、lane balance、exiD calibration、capacity drop 和 ramp metering comparison 统一到一个 baseline 中。
- `Mode-switching HCOMC`：P0016 提供 longitudinal cooperation 与 lateral cooperation 的可解释切换机制，适合检验横向协作是否真的值得其额外燃耗和执行复杂度。
- `Lane 2 assistance with execution tracking`：P0018 将内侧车道 CAV 辅助、MILP 战术层和 LCMPC-PTO 执行层连起来，是检验多车道空间是否真正被利用的强 baseline。
- `VTS as learning interface`：P0020 把合流排序压缩为 Yield/Green 信号相位，可作为 RL proposal 与 model-based execution 的轻量接口。
- `FD-driven dynamic gap signal`：P0021 把主线 platoon/gap 时空结构转成类信号序列，是 flow theory 驱动的 VTS 对照物。
- `Speed-adaptation timing`：P0022 提醒 sequence 不只是排序，还包括 on-ramp CAV 何时开始为目标 gap 调速/调位。

## 4. 使用建议

- 设计新实验时，先从本页选择最小 baseline 组合。
- 生成 candidate idea 时，先检查本页，避免提出已经等价于现有 baseline 的想法。
- 写 proof 时，优先明确目标机制位于“排序、合流位置、协作车辆选择、运动稳定性、横向跟踪、多目标评价”中的哪一层。
