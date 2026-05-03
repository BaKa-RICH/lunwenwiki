---
type: shared-assumptions
last_updated: 2026-04-29
source_pages: [wiki/synthesis/mid-field-synthesis-P001-P0022.md]
confidence: medium
---

# Shared Assumptions

## 1. 已识别共同假设

| 假设 | 证据 | 影响 | 脆弱点 |
| --- | --- | --- | --- |
| 控制区状态可被完整获取，CAV 可按控制器执行 | P001/P004/P005/P007/P0010 依赖集中或半集中调度；P006/P008 也要求 CAV 可解算/执行控制 | 支撑 system-level optimization、arrival-time planning、trajectory planning | mixed traffic 中 HDV 不可控；P009 显示通信延迟会影响速度波动和能耗 |
| 单主线 + 单匝道仍是机制验证主场景 | P001/P005/P006/P007/P009/P0010 均主要围绕单主线或简化合流道路；P008 扩展到 two-lane mainline | 便于比较排序、合流位置和安全约束 | 多车道 lane-changing、dual-lane ramp 和 lateral tracking 的耦合仍不足 |
| HDV 行为可被预测、约束或影响 | P006 将 leading HDV 视为 disturbance；P007 用常速/回放处理 HDV；P008 用 IDM/概率换道预测；P0010 用 strategic slowdown 影响 HDV | 使 mixed traffic 控制可计算 | 真实 HDV 反应、aggressive lane change、partial observability 和模型偏差仍会破坏策略 |
| 优化目标可用 delay / travel time / control effort 表征主要收益 | P001/P005/P007/P0010 强调 delay/control effort；P006/P009 强调 fuel/energy；P008 加入 safety | 便于建立 baseline 和复现实验 | 舒适性、排放、鲁棒性、稳定性和安全权重未形成统一目标体系 |
| 实时性可通过分解、滚动优化或搜索剪枝获得 | P001 MCTS-DA、P006 QP、P007 sequential search + iterative LP、P0010 dynamic arrival-time optimization | 让复杂合流控制具备在线可能 | 扩展到多车道、混合车辆、delay robustness 后计算复杂度可能重新上升 |
| 横向行为可被简化或延后处理 | P003/P004/P006/P007/P0010 主要纵向控制；P008 主文简化 lateral trajectory，附录才扩展 | 降低模型复杂度 | 合流安全和舒适性可能被高估，尤其在 mixed traffic 和 strategic influence 场景 |
| 仿真改善可代表方法有效性 | P001-P008/P0010 主要依赖仿真或数据驱动仿真；P009 提供 vehicle-in-the-loop 补充 | 为早期筛选提供证据 | 平台、驾驶模型、通信栈和真实车辆动力学差异会影响外推 |
| 横向执行可以由简化换道规则、轨迹函数或单步完成近似 | P0012/P0014/P0015/P0016 都涉及主线换道或横向协作，但多以规则/函数/仿真步简化；P0011 是少数进入 DNMPC/CarSim tracking 的工作 | 让 mixed traffic + multilane 仿真可控 | 横向舒适性、yaw/lateral acceleration、tracking error 和真实 lane-change reaction 可能改变收益 |
| 流级改善可以由局部控制外推 | P0012/P0015 用 flow-level/capacity-drop 指标；P0011/P0016 偏关键车或车辆级执行 | 有助于把单车控制与瓶颈效率连接 | flow-level objective 与 vehicle-level safety/execution 之间仍缺统一接口 |
| 学习型或规则型策略的收益可以由仿真指标证明 | P0014 依赖 PPO reward 和 transferability；P0015/P0016 依赖规则、阈值、NSGA-II 和小规模/自建仿真 | 快速形成 strong baselines | reward shaping、阈值校准、真实泛化和 safety guarantee 仍不足 |
| 预测均值足够支撑合流决策 | P0022 依赖短时车辆状态/轨迹预测；P0017 提醒动态对象估计收敛速度和协方差会改变规划成败 | 让 sequence search、gap selection 和 safety filter 可计算 | prediction covariance、遮挡、HDV 意图变化和 planner infeasibility 仍未系统进入合流 benchmark |
| Gap/time-series 或 VTS 抽象足以表达合流机会 | P0020 用 Yield/Green VTS，P0021 用 platoon/gap time-series，P0022 用 `t^p` | 将复杂 sequence-trajectory problem 压缩成可操作接口 | 高密度、多车道、mixed traffic 下可能丢失 gap ownership、横向执行和公平性信息 |
| 高层多目标评价可由少数指标代表 | P0019 提出 efficiency/stability/safety/environment/cybersecurity/policy 联动；P0021 同时报告 travel time、SSM 和 fuel | 有助于避免只优化 travel time | 多目标最小指标集尚未统一，指标权重可能决定“最优”方法排序 |

## 2. 可能脆弱的前提

- 完美通信假设被 P009 明确削弱：平均 0.06 s delay 已与速度波动和能耗相关。
- 纯 CAV 或高 CAV penetration 假设仍使 P007/P0010 的收益边界偏乐观，P0010 自述有效最低 penetration 约 30%-50%。
- HDV 预测/影响机制缺少真实 human reaction 验证，P0010 的 strategic slowdown 尤其需要 lane-change reaction 数据。
- 多目标权重的可解释性不足：P008 的 AWM 有性能收益，但机制 proof 仍弱。
- continuous safety constraints 不等于完整安全：P006/P007 的安全约束主要是纵向/时间间隔，未完整覆盖 lateral tracking。
- P0011 暴露了上层 comfort objective 与下层 actuator / tracking 的断点；P0014-P0016 多数仍未充分验证执行层。
- P0012/P0015 说明 capacity drop 和 continuous flow stability 可能改变“局部合流最优”的解释。
- P0014 的 PPO 与 P0015/P0016 的规则/优化路线存在可解释性和泛化性张力。
- P0018/P0020/P0021/P0022 继续暴露理想通信、完整感知、简化横向执行和仿真平台依赖；P0017/P0019 将预测不确定性与 cyber/communication risk 推到同等重要位置。
- P0021 的 dynamic gap creation 和 P0022 的 speed-adaptation timing 说明“何时造 gap / 何时开始调速”可能与“选哪个 gap”同样重要。

## 3. 与 gap 的关系

| 假设 | 可能暴露的 gap | 相关页面 |
| --- | --- | --- |
| 完美通信或低延迟可忽略 | Delay-aware robust merging 与 field validation 不足 | [[wiki/gaps/confirmed-gaps]] |
| HDV 可预测或可被影响 | mixed traffic 中 HDV prediction、probabilistic reaction 和 CAV influence 需要统一 | [[wiki/gaps/open-questions]] |
| 纵向控制主导合流效果 | lateral tracking / lane-changing 与 longitudinal sequencing 尚未共同验证 | [[wiki/gaps/confirmed-gaps]] |
| 固定或人工设定目标权重足够 | safety-efficiency-emission-robustness 多目标权重如何自适应且可解释 | [[wiki/gaps/open-questions]] |
| 仿真足够证明有效性 | vehicle-in-the-loop / field data benchmark 仍稀缺 | [[wiki/gaps/open-questions]] |
| 局部合流指标足够 | capacity-drop-aware / flow-level objective 与 vehicle-level execution 的统一不足 | [[wiki/gaps/open-questions]] |
| RL 或规则策略可由单平台仿真确认 | learning policy、rule layer、safety filter 的贡献拆分不足 | [[wiki/gaps/open-questions]] |
| 预测均值足够 | prediction uncertainty / covariance 与 fallback planning 未进入合流排序和安全层 | [[wiki/gaps/open-questions]] |
| VTS/gap time-series 足够表达合流机会 | timing-aware sequence、flow-level gap plan 和 vehicle-level execution 的接口尚不统一 | [[wiki/gaps/open-questions]] |

## 4. 需要反例审查的问题

- [x] 是否有真实轨迹数据或实验车验证仿真假设：P009 提供 vehicle-in-the-loop delay evidence，但规模有限。
- [ ] 是否有真实 HDV reaction 数据支持 P0010 strategic influence。
- [ ] delay、packet loss、partial observability 是否会推翻 P006/P008/P0010 的收益。
- [ ] FCBF / Bézier continuous safety 在加入 lateral tracking 后是否仍实时。
- [ ] 动态权重方法是否只是经验调参，还是能形成可解释机制。
- [ ] Flow-level gap creation / capacity drop 控制是否会被 vehicle-level tracking 或 communication delay 削弱。
- [ ] P0014 的 PPO 收益是否来自学习策略本身，还是来自规则约束和 TTC/TET reward shaping。
- [ ] P0016 的 lateral cooperation 在真实横向执行和燃耗/舒适性约束下是否仍优于 longitudinal cooperation。
- [ ] P0020 的 VTS-DRL 收益是否来自 action abstraction、state compression、reward shaping，还是 OCP execution。
- [ ] P0021 的 FD-derived state C 在真实 FD、非保护 gap 和通信延迟下是否仍可执行。
- [ ] P0022 的 `t^p` 是否能扩展到 mixed traffic 和多车道，而不造成不可接受的搜索复杂度。
- [x] Batch 04 summary 已复核 shared assumptions：最脆弱假设仍是无延迟/完整感知、横向执行简化、gap/VTS 抽象充分和单目标效率评价。
