---
type: field-map
last_updated: 2026-04-29
source_pages: [wiki/synthesis/mid-field-synthesis-P001-P0022.md, wiki/comparisons/merging-control-baselines.md]
confidence: medium
---

# Field Map

## 1. 领域范围

当前初始化范围聚焦自动驾驶匝道合流场景中的协同规划与合流轨迹优化。当前保留 21 篇 paper cards，覆盖从 closed-form / flexible position / mixed-traffic sequencing 到 safety-critical control、integrated sequence-trajectory、field delay evidence、strategic HDV influence、longitudinal-lateral execution、flow-level coordination、dual-module RL、calibrated interpretable gap/lane control、HCOMC mode switching、multi-lane HCMCC、VTS-DRL+OCP、DCoMA macro-micro gap creation 和 speed-adaptation timing 的主要路线。

## 2. 方法谱系

| 路线 | 代表论文 | 核心机制 | 优势 | 局限 |
| --- | --- | --- | --- | --- |
| Closed-form optimal CAV merging | [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]] | FIFO 队列 + 安全时间递归 + Hamiltonian 闭式解 | 在线解析、燃耗与旅行时间改善明显 | 单主路单匝道、纯 CAV、合流区单车占用、约束激活时需额外处理 |
| Flexible merging position system optimization | [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]] | 合流位置、顺序与关键状态进入系统优化；MCTS-DA 降低复杂度 | 相比固定合流点显著降低延误 | 纯 CAV、单车道、完美通信、总延误单目标 |
| Mixed-traffic multilane cooperation | [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]] | APS/CUC 指定协作车辆并决定主线换道/纵向协作 | 覆盖 CAV/CHV、多车道、compliance | compliance 二值化，无通信延迟 |
| Stability-aware mixed-traffic merging | [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]] | shortest-path sequencing + delayed consensus controller | 有 local/string stability proof | 横向控制简化，合流点固定 |
| Multi-area dual-lane ramp control | [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] | 主线提前换道、匝道 virtual platoon、合流区滚动优化 | 覆盖三主线车道 + 双匝道复杂几何 | 纯 CAV、无通信延迟、排序仍 FIFO |
| Safety-critical flexible merging | [[wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging]] | PMP expected merging position + FCBF/CBF/CLF-QP | 将 flexible position 落到连续安全约束 | TCG 选择、排序、横向执行和 delay 未统一 |
| Integrated sequence-trajectory optimization | [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]] | MINLP 同时优化 merge-in gap、sequence、terminal time 和连续轨迹 | 避免先排序后规划导致低质量轨迹；NGSIM 验证 | 100% CAV、单主线单匝道；匝道车数增加时复杂度快增 |
| Mixed-vehicle adaptive safety-efficiency control | [[wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles]] | BDM + NSGA-II Pareto + Transformer-AWM + CAV 迭代协商 | 覆盖 CAV/HV 与 car/truck，显式优化 safety/efficiency | 忽略通信延迟，鲁棒性缺少理论支持，横向轨迹非主线 |
| Field delay and energy evidence | [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]] | ACM vehicle-in-the-loop + delay estimation + H-LSTM | 提供通信延迟影响速度波动/能耗的实证证据 | 一辆真实 CAV + digital twin，侧重能耗/波动 |
| Strategic CAV influence on HDV | [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]] | strategic slowdown 影响后随 HDV，到达时间动态优化 | 不强依赖精确 HDV 预测；最高 ATTD 降低 31% | 假设无通信延迟/丢包，HDV 用 IDM，横向换道反应未充分建模 |
| Integrated longitudinal-lateral execution | [[wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging]] | 纵向最优控制 + sigmoid 横向轨迹 + DNMPC + driving safety field | CarSim/Simulink 验证车辆动力学和横向 tracking | FIFO、纯 CAV、单主线单匝道；上层 comfort 与下层执行可能脱节 |
| Flow-level multilane coordination | [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]] | 主线外侧造 gap + ramp platoon + 单向换道限制 | 关注连续交通流、shockwave 和 recurrent congestion；2C delay 降低 86.4% | 100% CAV、即时通信、换道规则强执行 |
| Dual-module PPO heterogeneous control | [[wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp]] | PPO merging control + lane-changing control | 低 CAV penetration 仍改善 delay/TET；有 transferability analysis | 缺少 safety/stability proof，横向执行和通信扰动简化 |
| Calibrated gap selection and lane balance | [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]] | reliable/unreliable vehicle bond + 主线速度/密度均匀性 + exiD 校准 | 可解释、非 RL、capacity-drop-aware，并与 ALINEA/PI-ALINEA 对比 | 需要路侧高精度感知；横向执行和 delay robustness 不足 |
| HCOMC mode-switching control | [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]] | modified virtual vehicle + Stackelberg game + NSGA-II | 明确切换纵向协作/横向协作；Condition 2 稳定时间缩短超 53% | 六关键车小规模仿真，实时性和通信扰动未充分验证 |
| External prediction-uncertainty planning | [[wiki/papers/P0017-2024-Lu-Fast-and-Adaptive-Perception-and-Planning]] | covariance adaptation + prediction uncertainty + infeasible-planner fallback | 为 HDV/CAV 短时预测不确定性和 fallback 提供外部机制源 | 非交通合流论文，缺少驾驶规则/交互/流级目标 |
| HCMCC multilane mixed traffic control | [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]] | MILP tactical layer + Lane 2 CAV assistance + LCMPC-PTO execution | 多车道 mixed traffic 下平衡主线/匝道利益，PR=0.8 时 ATF 提升约 10%-12% | 无延迟、instant lane-changing、HV 保守换道和完整 RSU 状态假设 |
| VTS-DRL + OCP merging | [[wiki/papers/P0020-2024-Muzahid-Optimizing-On-Ramp-Merging-DRL-OCP]] | Yield/Green VTS action + CAE state compression + OCP speed control | 将 RL proposal 与 model-based execution 分层，throughput/safety/fuel 指标均改善 | 100% CAV、理想通信，mixed traffic 仅补充分析，baseline 较弱 |
| DCoMA macro-micro gap creation | [[wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant]] | FD-derived target state C + CAV platooning + gap time-series + ramp motion planning | 动态适配 ramp/mainline flow，同时改善 travel time、SSM 和 fuel | free-flow、protected gap、IDM-derived FD、低 MPR 效果弱 |
| Speed-adaptation timing HCA | [[wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging]] | 合流顺序 + `t^p` speed-adaptation time + operational MPC | 揭示“何时开始调速/调位”是 sequence 之外的重要决策 | pure CAV、小规模、内部 objective，计算随匝道车数增加 |

## 3. 研究路线演化

- 早期路线从 P005 的 fixed merge point / FIFO / closed-form control 出发，以解析性和实时性换取简单场景假设。
- P001-P004 扩展了解空间、交通组成、稳定性和道路几何：flexible position、mixed traffic、多车道、多区域、dual-lane ramp。
- P006-P007 将 Batch 01 的两条断点向前推进：P006 把 flexible position 接入 continuous safety layer，P007 把 sequencing 与 trajectory quality 一体化。
- P008-P0010 将 mixed traffic 进一步现实化：车辆异质性、动态安全-效率权重、通信延迟 field evidence、CAV 对 HDV 的 strategic influence。
- P0011-P0016 将问题继续推到三个新层级：车辆级横向执行、连续交通流/capacity drop、以及低渗透率异质交通中的可解释规则或 RL 控制。
- P0017-P0022 将问题进一步推到接口层：prediction uncertainty、multi-lane assistance、system-level multi-objective evaluation、VTS learning interface、FD-driven dynamic gap creation 和 speed-adaptation timing。
- 当前前沿不再是单一“更优轨迹”，而是多接口统一：排序、合流位置、安全约束、HDV 行为、通信延迟、横向执行、流级稳定、capacity drop 和实证验证。

## 4. 推进、互补与矛盾关系

| 类型 | 关系 | 解释 |
| --- | --- | --- |
| 推进 | P001 -> P006 | P001 证明 flexible merging position 的效率价值；P006 用 FCBF 将该自由度嵌入 safety-critical constraints。 |
| 推进 | P003/P005 -> P007 | P003/P005 给出排序基线与实时性权衡；P007 进一步要求排序由候选轨迹质量共同决定。 |
| 推进 | P002 -> P008/P0010 | P002 引入 mixed traffic compliance；P008 加入 car/truck 异质性和动态目标权重，P0010 进一步主动影响 HDV。 |
| 推进 | P009 -> all | P009 将通信延迟从假设层拉到 field evidence 层，要求后续方法加入 delay robustness。 |
| 互补 | P006 + P007 | P006 可作为 continuous safety layer，P007 可作为 sequence-trajectory optimizer。 |
| 互补 | P008 + P0010 | P008 的 adaptive weighting 可服务 P0010 strategic slowdown 的安全/效率取舍。 |
| 矛盾 | 无延迟假设 vs field evidence | P006/P008/P0010 多处忽略 delay，P009 显示 0.06 s 量级 delay 已影响速度波动和能耗。 |
| 矛盾 | 强一体化优化 vs mixed traffic 可部署性 | P007 优化强但纯 CAV；P008/P0010 更现实但依赖预测、协商或 HDV 反应假设。 |
| 矛盾 | 横向行为是核心 vs 横向模型常简化 | P002/P004/P006/P007/P008/P0010 都触及 lane changing，但很少把 lateral tracking 作为同等重要的验证对象。 |
| 推进 | P0011 -> GAP-0002 | P0011 把横向 DNMPC 和车辆动力学执行纳入验证，直接强化 lateral tracking 维度。 |
| 推进 | P0012 -> P0015 | P0012 提出 flow-level CoMC，P0015 进一步复现 capacity drop 并与 ALINEA/PI-ALINEA 比较。 |
| 推进 | P0014 -> P0015 | P0014 提供 dual-module PPO，P0015 提供同类任务的可解释规则和 exiD 校准对照。 |
| 推进 | P0016 -> P0011/P0015 | P0016 显式化 longitudinal vs lateral cooperation switching，但仍需要 P0011 的执行验证和 P0015 的连续流验证。 |
| 互补 | P0011 + P0012 | P0011 解决 vehicle-level execution，P0012 解决 flow-level stability，二者构成多尺度组合线索。 |
| 互补 | P0014 + P0015 | P0014 学习型低渗透率策略与 P0015 可解释/校准策略可作为 paired baselines。 |
| 矛盾 | 横向协作收益 vs 执行/燃耗成本 | P0016 横向协作提升 safety/stabilization，但可增加燃耗；P0011 提醒需验证下层 tracking 与舒适性。 |
| 矛盾 | RL 性能 vs 可解释 safety guarantee | P0014 性能强但 proof 弱；P0015/P0016 更可解释但依赖规则、阈值和小规模仿真。 |
| 互补 | P0020 + P0021 | P0020 用 VTS-DRL 学习 Yield/Green window，P0021 用 FD 显式计算 gap time-series，可作为 learning vs physics/rule paired baselines。 |
| 互补 | P0018 + P0021 | P0018 提供多车道 Lane 2 assistance 与执行层，P0021 提供动态需求下的宏观 gap size，两者共同指向 multi-lane macro-micro coordination。 |
| 互补 | P0017 + P0022 | P0022 依赖 sequence search 和短时预测，P0017 提供 prediction covariance 与 infeasibility fallback 的外部机制。 |
| 矛盾 | 理想通信/感知 vs robust deployment | P0018/P0020/P0021 多处假设无延迟或完整感知，P0017/P009/P0019 共同提醒 prediction/communication/cyber risk 不能被忽略。 |

## 5. 关键对比维度

- 问题设定：固定合流点 vs 可变/滚动合流位置；纯 CAV vs mixed CAV/CHV/HDV；passenger cars only vs car/truck mixed vehicles。
- 控制对象：单车/三车 TCG、多 CAV batch、主线/匝道 stream、CAV-HDV interaction、vehicle-in-the-loop real CAV。
- 优化层级：arrival time、merge-in gap、trajectory、safety barrier、adaptive weighting、strategic influence。
- 安全机制：terminal time gap、continuous Bézier constraints、CBF/FCBF、TIT/RTTC、delay robustness。
- 证据类型：MATLAB/SUMO/VISSIM/Carla 仿真、NGSIM/exiD-driven simulation、CarSim/Simulink vehicle dynamics、ACM vehicle-in-the-loop field data、自建 Python 仿真。
- metrics：delay/ATTD/TTT/TD、fuel/energy/control cost、TIT/RTTC/TET/TETMP/CPMR、speed volatility、time gap、computation time、stability、capacity drop、CD、LSRV。

## 6. 与本研究的关系

- baseline：P005 closed-form、P006 FPM-FCBF、P007 integrated sequencing、P008 BDM-AWM、P0010 strategic influence、P0011 DNMPC execution、P0012 flow-level CoMC、P0014 dual-module PPO、P0015 calibrated VB/lane-balance、P0016 HCOMC、P0018 HCMCC、P0020 VTS-DRL+OCP、P0021 DCoMA、P0022 timing-aware HCA 是当前 baseline 池。
- idea_source：可组合机制包括 FCBF safety layer、trajectory-quality-driven sequencing、adaptive weighting、delay-aware robustness、strategic HDV influence、DNMPC lateral execution、flow-level gap shaping、VB risk term、longitudinal/lateral cooperation switch、prediction covariance、Lane 2 assistance、VTS interface、FD-driven gap time-series 和 speed-adaptation timing。
- counterexample：P009 对“无通信延迟可忽略”形成实证反例；P0010 对“HDV 只能被预测/规避”形成机制反例；P0011 对“上层轨迹可直接执行”形成执行反例；P0015 对“只看 delay 足够”形成 safety/comfort/capacity drop 反例。
- assumption：完美或高质量通信/感知、HDV 可模型化、横向执行可简化、仿真可外推、CAV penetration 足够、强优化或 RL 可实时。

## 7. 待核查

- [x] P006-P0010 是否完成中间综合：内容已吸收进 [[wiki/synthesis/mid-field-synthesis-P001-P0022]]。
- [x] 是否已有论文强化通信延迟 gap：P009 提供 field / vehicle-in-the-loop evidence。
- [x] 是否已有 integrated sequence + trajectory 强 baseline：P007 已覆盖纯 CAV 版本。
- [x] 是否已有主动影响 HDV 的 mixed traffic 机制：P0010 提供 strategic slowdown。
- [ ] 是否存在同时覆盖 mixed traffic、multi-lane、lateral tracking、communication delay 和 stability 的统一框架。
- [ ] P0010 strategic influence 在真实 HDV reaction 和通信延迟下是否仍有效。
- [ ] P006 FCBF 与 P007 integrated sequence search 能否实时结合。
- [x] P0011-P0016 是否完成中间综合：内容已吸收进 [[wiki/synthesis/mid-field-synthesis-P001-P0022]]。
- [ ] Flow-level / capacity-drop objective 与 vehicle-level DNMPC / CBF safety filter 能否统一。
- [ ] P0014 RL 与 P0015/P0016 可解释规则谁贡献主要收益，需要 ablation。
- [x] P0017-P0022 是否完成中间综合：内容已吸收进 [[wiki/synthesis/mid-field-synthesis-P001-P0022]]。
- [ ] VTS-DRL、FD-driven gap time-series 和 speed-adaptation timing 能否统一到同一最小 benchmark。
