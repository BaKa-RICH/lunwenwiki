---
type: open-questions
last_updated: 2026-04-29
source_pages: [wiki/synthesis/mid-field-synthesis-P001-P0022.md]
confidence: medium
---

# Open Questions

## 1. 待探索问题

| ID | 问题 | 来源 | 下一步 | 状态 |
| --- | --- | --- | --- | --- |
| OQ-0001 | 固定合流点限制解空间这一问题，在混合交通或多车道场景中是否仍是主要瓶颈？ | [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]] | 继续读取后续 SO-CMC、mixed traffic、multilane merging 论文交叉验证 | open |
| OQ-0002 | 如何在可变合流位置控制中同时优化效率、舒适性、排放和扰动衰减，而不是只优化总延误？ | [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]] | 查找多目标 CAV merging / robustness / emission-aware control 论文 | open |
| OQ-0003 | 可变合流位置带来的计算复杂度，是否可以通过线性化、学习辅助搜索或分布式控制进一步降低？ | [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]] | 对比 MIQP/MILP、MPC、MCTS、RL 和 distributed control 路线 | open |
| OQ-0004 | 混合交通中 HDV 轨迹预测和信息补全如何与 CAV 合流优化统一，而不是作为外部前处理？ | [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]] | 查找 HDV prediction、trajectory reconstruction、mixed CAV-HDV merging 论文 | open |
| OQ-0005 | CHV/HDV compliance 低或部分执行时，协同合流控制如何保持收益和安全边界？ | [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]] | 查找 driver compliance、human factors、advisory control 相关论文 | open |
| OQ-0006 | 是否能把 P003 的 stability-aware consensus controller 与 P002/P004 的主线提前换道/协作车辆选择结合？ | [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]], [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]], [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] | 先做机制级 proof，再设计最小仿真实验 | open |
| OQ-0007 | 双车道匝道汇入是否存在优于 FIFO、又足够实时可解释的排序策略？ | [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]], [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]] | 对比 FIFO、shortest-path、MCTS、rolling optimization | open |
| OQ-0008 | 横向换道轨迹 tracking 与纵向合流排序分开优化时，是否会隐藏安全或舒适性问题？ | [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]], [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]], [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] | 后续查找 integrated lateral-longitudinal control 文献 | open |
| OQ-0009 | 多车道主线、双车道匝道、可变合流位置、mixed traffic 和稳定性是否已有统一框架？ | [[wiki/synthesis/mid-field-synthesis-P001-P0022]] | 继续检查 integrated / safety-critical / flexible mixed-traffic merging 文献；证据不足，暂不升 confirmed gap | open |
| OQ-0010 | P002/P003/P004 的机制组合是否只是模块缝合，还是能形成可证明的新因果链？ | [[wiki/synthesis/mid-field-synthesis-P001-P0022]] | 先写 proof-sketch 级机制链，再决定是否生成 candidate idea batch | open |
| OQ-0011 | FCBF safety layer 能否与 integrated sequence-trajectory optimization 结合，并保持实时性？ | [[wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging]], [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]] | 小规模场景比较 P007 sequence、P006 FCBF safety filter 和组合版本 | open |
| OQ-0012 | Strategic CAV influence 在 communication delay、packet loss 和真实 HDV lane-change reaction 下是否仍有效？ | [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]], [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]] | 在 P0010 setup 中加入 P009 delay 参数和 probabilistic HDV reaction | open |
| OQ-0013 | Adaptive safety-efficiency weighting 是机制性改进，还是数据驱动调参？ | [[wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles]] | 设计固定权重、规则权重、AWM 权重对照，比较 TIT/TD/control effort 与失败条件 | open |
| OQ-0014 | Vehicle-in-the-loop delay evidence 能否迁移到多 CAV、多 HDV 和不同 merging controllers？ | [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]] | 先用 delay/volatility 参数构造仿真 benchmark，再决定是否做 VIL 扩展 | open |
| OQ-0015 | Mixed vehicle heterogeneity 中 truck penetration 与 CAV penetration 如何共同改变合流控制收益边界？ | [[wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles]] | 将 truck penetration 纳入后续 baseline sweep，避免只扫 CAV penetration | open |
| OQ-0016 | 上层合流优化中的 comfort / jerk objective 能否被下层车辆动力学控制器真实实现？ | [[wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging]] | 对比只跟踪速度、同时跟踪速度+加速度/jerk、不同 actuator delay 的 CarSim 或简化动力学实验 | open |
| OQ-0017 | Flow-level gap creation 如何与 vehicle-level trajectory tracking / safety constraints 统一，避免流级收益在执行层损失？ | [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]], [[wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging]] | 用 CoMC 上层 `n/d/v_C` 作为计划输入，对接 DNMPC/CBF 执行层做小规模仿真 | open |
| OQ-0018 | RL 合流控制如何在保持低渗透率收益的同时提供可解释 safety guarantee 和真实通信/感知扰动鲁棒性？ | [[wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp]] | 用 PPO policy 作为 proposal，与 CBF/DNMPC safety filter、delay/noise sweep 和 rule-based ablation 对照 | open |
| OQ-0019 | Capacity-drop-aware cooperative merging 能否同时纳入 gap selection、lane balance、safety/comfort 和通信延迟鲁棒性？ | [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]], [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]] | 复现 P0015 capacity drop setup，加入 delay/noise、lateral execution 和 ALINEA/PI-ALINEA 对照 | open |
| OQ-0020 | 两车道 mixed traffic 中，主线协作车应何时纵向减速让 gap，何时横向换道释放 lane？ | [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]], [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]] | 对比 longitudinal-only、lateral-only、mode-switching 三组，在 fuel/comfort/safety/delay 与 delay/noise 下评估 | open |
| OQ-0021 | Mixed traffic merging 中，HDV/CAV 短时运动预测是否应显式输出协方差并参与排序、safety filter 或 fallback planning？ | [[wiki/papers/P0017-2024-Lu-Fast-and-Adaptive-Perception-and-Planning]], [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]], [[wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging]] | 先把 P0017 的 covariance adaptation 作为外部机制线索，设计 prediction-uncertainty ablation；不创建正式 HYP | open |
| OQ-0022 | Lane 2 CAV assistance 在加入真实换道持续时间、通信延迟、感知误差和非保守 HV 行为后，是否仍能稳定改善 multi-lane mixed traffic 合流？ | [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]], [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]], [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]] | 复现 P0018 Lane 2 assistance ablation，加入 lane-change duration、delay/noise 和 aggressive HV cut-in；不创建正式 HYP | open |
| OQ-0023 | 匝道合流方法如何同时报告 efficiency、stability、safety、energy/environment 和 communication/cybersecurity 风险，而不是只优化局部 travel time？ | [[wiki/papers/P0019-2024-Pan-CAV-Impacts-Mixed-Traffic-Flow-Review]], [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]], [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]] | 将 P0019 作为宏观指标框架，先整理最小指标集；不创建正式 HYP | open |
| OQ-0024 | VTS-DRL 合流排序的收益来自 Yield/Green 信号抽象、CAE state compression、reward shaping，还是低层 OCP/MPC 执行？ | [[wiki/papers/P0020-2024-Muzahid-Optimizing-On-Ramp-Merging-DRL-OCP]], [[wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp]], [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]] | 设计 rule-VTS、raw-state DRL、CAE-DRL、OCP-only、DRL+OCP 五组 ablation；不创建正式 HYP | open |
| OQ-0025 | FD-driven dynamic gap creation 能否在真实 FD、communication delay、非保护 gap、congested state 和 multi-lane lane-changing 下保持收益？ | [[wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant]], [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]], [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]] | 复现 DCoMA 后逐步替换 IDM-derived FD、加入 delay/noise、允许主线车辆切入 gap、扩展多车道；不创建正式 HYP | open |
| OQ-0026 | 合流排序中是否应显式优化 speed-adaptation time，而不是只确定 target gap / sequence？ | [[wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging]], [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]], [[wiki/papers/P0020-2024-Muzahid-Optimizing-On-Ramp-Merging-DRL-OCP]] | 在既有 sequence baseline 中加入固定/优化 `t^p` 对照，检查对 comfort、安全和 fuel 的边际贡献；不创建正式 HYP | open |

## 2. 问题分层

### 机制问题

- `INFERRED` 可变合流位置改善效率的关键机制是扩大 gap assignment 和合流时空选择空间，减少匝道车在固定点前等待以及主线车为固定点强行减速。
- `INFERRED` 当匝道占比升高时，可变合流位置可能把一部分合流提前到合流段前部，导致低速并入并影响主线。
- `INFERRED` P002/P004 显示，提前塑造主线 gap 可能与合流区内轨迹优化同等重要。
- `INFERRED` P003 显示，方法是否有效不仅取决于瞬时合流成功，还取决于扰动是否沿 platoon 放大。
- `INFERRED` P006/P007 显示，合流位置/顺序的收益需要与连续安全约束共同评估，而不是只看 terminal state。
- `INFERRED` P0010 显示，HDV 不一定只能被预测；可控 CAV 的战略动作可能改变 HDV 反应。
- `INFERRED` P0017 虽不是合流论文，但说明快速变化动态对象的估计收敛速度和预测协方差会直接影响规划成败。

### 实证问题

- P001 的 64% 延误改善是否依赖纯 CAV、完美通信和单车道设定？
- 在不同合流段长度、不同安全时距 `beta`、不同主线/匝道流量占比下，收益边界在哪里？
- 不同论文仿真平台和场景差异较大，后续需要统一 SUMO / Python 最小复现实验。
- P004 的 dual-lane ramp 高需求收益是否在 mixed traffic 下仍成立？
- P009 的 field delay evidence 规模有限：需要判断 0.06 s 量级 delay 对不同控制器是否都显著。
- P008/P0010 的收益是否依赖特定 IDM / HV prediction / driver reaction 设定？
- P0012 的 86.4% delay reduction 是否依赖 100% CAV、即时通信、换道限制强执行和 VISSIM lane-changing 模型？
- P0014 的低渗透率收益是否依赖特定 IDM / lane-changing dissatisfaction 模型和 reward shaping？
- P0015 的 exiD 校准规则在其他道路几何、驾驶文化和通信延迟下是否仍能缓解 capacity drop？
- P0016 的 lateral cooperation 是否在加入车辆动力学、横向舒适性和通信延迟后仍优于纵向协作？
- P0017 的 covariance adaptation 迁移到路侧/车载交通感知时，遮挡、尺度和 HDV 行为模型偏差是否会削弱收益？
- P0018 的 Lane 2 assistance 在高流量低 PR 下收益明显，但是否依赖 instant lane-changing、保守 HV lane-change 和完整 RSU 状态仍需复验。
- P0019 提醒 CAV mixed traffic 评价天然多目标；单一 travel time improvement 可能掩盖 safety、stability、network security 或 long-term energy trade-off。
- P0020 报告 VTS-DRL+OCP 的 throughput/fuel/safety 收益，但其理想通信、100% CAV 和 SUMO Krauss baseline 可能高估可部署性。
- P0021 说明动态 gap creation 可同时改善效率、安全和排放，但依赖 free-flow、protected gap 与较高 CAV MPR。
- P0022 显示匝道车初始速度低或与主线车同时进入控制区时，允许其先调速/调位再合流可显著改善 objective。

### 理论问题

- 战术层非凸 MIQCP 是否能被等价或近似线性化，并保持可解释的安全约束？
- MCTS-DA 的 optimality gap 在大规模、混合交通和多车道条件下如何变化？
- 合流排序的目标函数能否同时纳入效率、安全、舒适性、稳定性和驾驶风格，而不导致实时性崩溃？
- P005 的闭式控制能否作为局部 proof module，而排序与协作车辆选择由更高层模型决定？
- FCBF、Bézier continuous safety、arrival-time constraints 三种 safety 表达能否统一，还是各自适合不同层级？
- Strategic slowdown 是否能形成可证明的因果链：CAV action -> HDV response -> gap formation -> improved ATTD/safety？
- 上层 optimal control 的舒适性指标是否会在 lower-level PI / DNMPC / actuator dynamics 中失真？
- Flow-level 的 shockwave / bottleneck stability 约束能否转译为 vehicle-level controller 可执行的局部约束？
- PPO policy 的 action 经过规则/约束过滤后，收益到底来自学习策略、规则层，还是二者耦合？
- Reliable/unreliable vehicle bond 能否形式化为可证明的 conflict-risk surrogate，并与 CBF/FCBF 类安全约束兼容？
- HCOMC 的 NSGA-II + Stackelberg game 组合能否给出实时性上界，还是只适合小规模关键车决策？
- Prediction covariance 能否被形式化为合流排序代价或 CBF/FCBF safety margin，而不仅是感知模块诊断指标？
- HCMCC 的 MILP 战术层能否与真实横向轨迹/执行层连续约束结合，而不退化为难以实时求解的混合整数非线性问题？
- 效率、稳定性、安全、环境和 cyber risk 是否存在可用于合流控制的最小统一评价函数，还是只能作为分层指标分别报告？
- Yield/Green VTS 是否足以表达合流排序的关键决策，还是会在高密度、多车道、mixed traffic 下丢失必要的 gap assignment 信息？
- FD-derived state C 能否作为可证明的流级约束传递给 vehicle-level CBF/DNMPC，还是只能作为宏观启发式调度目标？
- Speed-adaptation time `t^p` 是否能被纳入可解释 sequence cost，还是只适合小规模枚举搜索？

### 写作与定位问题

- 如果后续研究继续沿“合流位置/顺序/关键状态联合优化”走，P001 很可能是核心 related work 和 baseline。
- 需要区分“优化型强 baseline”和“可部署实时控制方法”的定位，避免只在纯 CAV 理想条件下讲故事。
- 第一批论文已经能形成一条清晰叙事：closed-form baseline -> flexible merging position -> mixed traffic / multilane -> stability -> complex dual-lane ramp。
- 下一步写作需要警惕“模块缝合”问题：必须说明新方法解决的是哪一个明确断点，而不是把 P002/P003/P004 机械相加。
- Batch 02 之后，写作叙事可升级为：flexible position -> safety-critical constraints -> integrated sequencing -> mixed-vehicle adaptive objectives -> field delay evidence -> strategic HDV influence。
- 如果后续主打 mixed traffic，可优先围绕“HDV prediction / influence + delay robustness + safety layer”构造故事，而不是继续堆叠优化模块。
- P0011-P0016 后，写作叙事可以进一步升级为：mixed traffic + multilane 不只需要预测/排序，还需要 execution validation、flow-level / capacity-drop evidence、learning-vs-rule baseline 和 longitudinal/lateral cooperation switch。

## 3. Candidate Idea 线索

| 线索 | 来源 | 暂存原因 | 下一步 |
| --- | --- | --- | --- |
| Stability-aware cooperative vehicle selection：把 P002 的 APS/CUC 与 P003 的 consensus stability 结合 | P002, P003 | 机制看起来有互补性，但尚未证明协作车选择会改善 string stability | 写机制级 proof，不创建 HYP |
| Dual-lane ramp sequencing beyond FIFO：为 P004 的双车道匝道设计优于 FIFO 的实时排序 | P004, P005, P003 | P004 用 FIFO，P003 显示 optimized sequencing 有收益，但未验证双匝道场景 | 设计最小 SUMO 实验，不创建 HYP |
| Flexible merging position + upstream gap shaping：结合 P001 的合流位置自由度和 P004 的主线上游换道/匝道速度控制 | P001, P004 | 可能只是模块组合，需明确因果链和失败条件 | 先写反对理由和最小实验 |
| Delay-aware strategic HDV influence：在 P0010 strategic slowdown 中加入 P009 的 delay/volatility evidence | P0010, P009 | 通信延迟可能使 CAV 对 HDV 的影响滞后，收益消失甚至变差 | 做 delay sweep 和 aggressive HDV reaction ablation，不创建 HYP |
| FCBF-constrained trajectory-quality sequencing：用 P006 safety layer 约束 P007 integrated sequencing | P006, P007 | 一体化优化已复杂，加入 safety layer 可能牺牲实时性 | 小规模仿真对比 FIFO、P007、P007+FCBF，不创建 HYP |
| Adaptive safety-efficiency strategic merging：把 P008 AWM 用于 P0010 的 slowdown pattern 选择 | P008, P0010 | AWM 可能只是经验调权，缺少可解释机制 | 先比较固定权重和 AWM 权重的失败条件，不创建 HYP |
| Execution-aware merging objective：把 P0011 的下层 tracking 失真纳入上层合流目标或约束 | P0011 | 当前只是执行层风险线索，尚未证明会系统性改变排序/合流收益 | 先做速度-only 与速度+加速度/jerk tracking 对照，不创建 HYP |
| Flow-level CoMC + safety-critical execution：用 P0012 生成上层 gap/platoon 计划，用 P0011/P006 约束车辆级执行 | P0012, P0011, P006 | 可能只是层级拼接，尚未证明流级 stability 与车辆级 safety 能一致优化 | 先构造 1 个 high-demand two-lane VISSIM/SUMO 场景，不创建 HYP |
| RL proposal + safety filter for low-penetration merging：用 P0014 PPO 负责效率/换道 proposal，用 P006/P0011 类 safety layer 负责可执行约束 | P0014, P006, P0011 | RL 收益可能来自 reward shaping，且组合后可能牺牲实时性 | 做 PPO-only、rule-only、PPO+safety filter 三组 ablation，不创建 HYP |
| Capacity-drop-aware VB gap selection：把 P0015 reliable/unreliable VB 作为排序代价，并加入 P0012 flow-level stability 指标 | P0015, P0012 | 需要证明 VB 风险能预测 capacity drop，而不只是解释仿真结果 | 先复现 P0015 capacity drop 和 merging-only/lane-changing-only ablation，不创建 HYP |
| Longitudinal-vs-lateral cooperation switch：基于 P0016 的 HCOMC 判断 VMC 该减速还是换道协作 | P0016, P0011, P0015 | 横向协作收益可能被 fuel、comfort、tracking error 和 delay 吃掉 | 做三组 mode ablation，并加入车辆动力学/延迟扰动，不创建 HYP |
| Multi-scale merging controller benchmark：统一比较 P0011 vehicle dynamics、P0012 flow-level CoMC、P0015 capacity drop 和 P0016 mode switching | P0011, P0012, P0015, P0016 | 当前证据跨平台跨指标，尚不能说明哪个层级是主要瓶颈 | 先定义统一 SUMO/Python + 简化动力学 benchmark，不创建 HYP |
| Prediction-uncertainty-aware merging fallback：将 P0017 的 covariance adaptation 和 temporary-target replanning 迁移为 mixed traffic 合流中的预测不确定性排序/降级控制 | P0017, P0010, P006 | P0017 来自 UAV 避障，缺少交通规则、HDV 博弈和合流效率目标，需要先证明迁移合理 | 做有/无 prediction covariance 的排序与 safety filter ablation，不创建 HYP |
| Lane-2-assistance with realistic lateral execution：以 P0018 的 Lane 2 CAV assistance 为上层机制，加入 P0011/P0016 式横向执行、燃耗/舒适性和 delay/noise ablation | P0018, P0011, P0016 | P0018 的多车道收益可能被真实换道时间、tracking error 和通信扰动削弱 | 先复现 P0018 degradation experiment，再替换 instant lane-changing，不创建 HYP |
| Multi-objective merging evaluation minimal set：基于 P0019 整理合流实验中 efficiency/stability/safety/energy/cyber risk 的最小报告指标 | P0019, P009, P0015, P0018 | 目前更像评估协议而非方法 idea，需要先证明该指标集能区分现有 baseline 的失败模式 | 先从既有 cards 抽取指标并做对照矩阵，不创建 HYP |
| VTS-DRL proposal + safety-critical execution：以 P0020 的 VTS-DRL 输出合流窗口，用 P006/P0011 类 safety/execution layer 替代或约束 OCP speed profile | P0020, P006, P0011 | 需要证明 Yield/Green 抽象没有丢失关键排序信息，并且组合后仍实时 | 先做 VTS-rule、VTS-DRL、VTS-DRL+CBF/DNMPC ablation，不创建 HYP |
| FD-driven gap plan + vehicle-level safety filter：用 P0021 DCoMA 生成动态 gap time-series，再用 P006/P0011 类 safety/execution layer 约束匝道车和主线协作 CAV | P0021, P006, P0011, P0012 | 可能只是宏观计划与微观安全层拼接，需证明 state C / gap time-series 能被执行层稳定实现 | 先复现 DCoMA，再加入 CBF/DNMPC 和 delay/noise ablation，不创建 HYP |
| Timing-aware merging sequence：在 P007/P0020/P0021 的 target gap 或 VTS/gap time-series 上显式加入 P0022 的 speed-adaptation time `t^p` | P0022, P007, P0020, P0021 | 新变量可能增加搜索复杂度，且收益可能只出现在低匝道初速或特殊相对位置 | 做 fixed t^p、optimized t^p、no t^p 三组小规模对照，不创建 HYP |

Batch 04 summary 已复核上述 open questions，维持 OQ-0016 至 OQ-0026 为 open；candidate 线索仅作为机制迁移/复验/评估协议/ablation 线索，不创建正式 HYP。

## 4. 晋升为 confirmed gap 的条件

- 有明确证据说明现有方法不足。
- 能说明该不足与研究目标有关。
- 已检查最接近的已有工作。
- 能提出最小验证方式或 candidate idea。
