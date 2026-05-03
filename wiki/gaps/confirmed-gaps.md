---
type: confirmed-gaps
last_updated: 2026-04-29
source_pages: [wiki/synthesis/mid-field-synthesis-P001-P0022.md]
confidence: medium
---

# Confirmed Gaps

## 1. 已确认或高可信 gap

| ID | Gap | 证据 | 影响 | 状态 |
| --- | --- | --- | --- | --- |
| GAP-0001 | 纯 CAV、完美通信、完全服从控制的设定不足以支撑近期可部署合流控制 | P001/P004/P005/P007 依赖纯 CAV 或强可控；P002/P003/P006/P008/P0010 转向 mixed traffic 但仍保留通信、预测或执行假设；P009 以 field data 显示 delay 会影响速度波动和能耗 | 任何新 idea 若只在纯 CAV 或无延迟下提升，论文说服力有限 | confirmed |
| GAP-0002 | 横向换道轨迹和 tracking 常被简化，未与合流排序/纵向控制共同验证 | P003/P004 明确简化；P006/P007/P0010 主要纵向/arrival-time 控制；P008 主文简化横向轨迹，附录才扩展；P0011 提供 CarSim/DNMPC 证据但仍是纯 CAV 小场景，P0014/P0015/P0016 继续简化 lane-change execution 或缺 vehicle dynamics validation | 安全性和舒适性可能被高估，实验复现需要补足 lateral 维度 | confirmed |
| GAP-0003 | 实时排序机制仍在全局最优、低复杂度和鲁棒性之间摇摆 | P005/P004 使用 FIFO；P001 用 MCTS-DA；P003 用 shortest-path；P007 用 integrated MINLP + sequential search；P0010 用 strategic slowdown pattern search | 可形成“实时可解释排序 + 安全/稳定/鲁棒约束”的方法空间 | confirmed |
| GAP-0004 | Delay-aware robustness 和 field / vehicle-in-the-loop validation 不足 | P006/P008/P0010 忽略通信延迟或丢包；P009 是少数 vehicle-in-the-loop evidence，且只含一辆真实 CAV 和侧重能耗/速度波动；P0011/P0014/P0015/P0016 多数仍未系统测试 delay/packet loss/partial observability，P0015 仅做 speed perturbation | 新方法需要至少在仿真中加入 delay sweep，并尽量设计 VIL/field-aware benchmark | confirmed |

### P0017-P0022 复核结论

本轮不新增 confirmed gap。P0017-P0022 强化了既有 GAP-0001 至 GAP-0004，但新增问题仍更适合作为 open questions / candidate 线索：

- GAP-0001 被 P0018/P0020/P0021 继续强化：强方法仍常依赖无通信延迟、完整感知、100% CAV 或高 MPR。
- GAP-0002 被 P0018/P0021/P0022 继续强化：多车道或换道执行常以 instant lane occupation、gap time-series 或多项式横向轨迹近似。
- GAP-0003 被 P0020/P0022 强化：VTS-DRL 和 `t^p` 枚举都说明排序机制仍在表达能力、实时性和可解释性之间取舍。
- GAP-0004 被 P0017/P0019/P0020/P0021 强化：prediction covariance、communication/cyber risk、delay compensation 和 fallback planning 尚未形成统一合流 benchmark。

暂不新增 confirmed gap 的原因：

- `Prediction uncertainty as first-class input` 目前主要由 P0017 外部 UAV 论文迁移而来，合流内证据不足。
- `VTS / gap time-series / speed-adaptation timing` 是接口设计问题，尚未证明存在跨 baseline 的系统性失败。
- `Multi-objective minimal evaluation set` 更像评估协议候选，需要先证明能区分现有方法失败模式。

### GAP-0001 后续拆解方向

GAP-0001 当前仍是高层 gap，适合作为研究边界提醒，但后续需要拆成更可实验的子问题：

- HDV / CHV compliance 不确定时，CAV advisory control 如何保持收益和安全边界？
- 通信延迟、丢包或部分可观测状态下，中心化合流控制应如何降级或转为分布式协同？
- mixed traffic 下，HDV 轨迹预测、信息补全和 CAV 控制是否应统一建模，而不是作为外部前处理？
- 纯 CAV 结果在什么 CAV penetration 阈值后才开始接近可部署收益？

后续处理原则：

- Batch 02 继续检查是否已有论文解决上述子问题。
- 若某个子问题有跨论文证据和最小验证方式，再单独拆成新的 confirmed gap。
- 若证据不足，保留在 `wiki/gaps/open-questions.md`，不要直接创建 HYP。

### GAP-0004 后续拆解方向

GAP-0004 由 P009 明确强化，但仍需要拆成可实验子问题：

- 延迟对 safety-critical FCBF / CBF-QP 控制可行域的影响。
- 延迟对 strategic CAV influence 的影响：CAV 减速是否仍能及时塑造 HDV 到达时间？
- 延迟对 integrated sequencing 的影响：候选 sequence 的轨迹成本是否随 delay 改变排序。
- field / vehicle-in-the-loop benchmark 如何从单车扩展到多 CAV、多 HDV。

这些仍是 gap / candidate 线索，未创建正式 HYP。

### P0011-P0016 复核结论

本轮不新增 confirmed gap。P0011-P0016 更强地拆解了既有 GAP-0001/GAP-0002/GAP-0004，并将 capacity drop、flow-level control、RL safety guarantee、longitudinal-vs-lateral cooperation switch 等问题推入 `wiki/gaps/open-questions.md`。

暂不升为 confirmed gap 的原因：

- `Flow-level + vehicle-level execution` 统一不足已有多篇线索，但现有证据仍分散在 P0011、P0012、P0015、P0016 的不同平台和指标中。
- `RL safety guarantee` 主要来自 P0014 与 P0015/P0016 的对照线索，尚缺统一实验或 proof。
- `Capacity-drop-aware merging` 由 P0015 明确提出，但是否跨道路几何、通信延迟和真实驾驶行为成立仍需复验。

## 2. 证据要求

每个 confirmed gap 至少需要说明：

- 来自哪些论文、实验结果或综合页面。
- 现有方法为什么没有解决。
- 它是否可能只是指标、数据或设定差异造成的假 gap。
- 它可能支持哪些 candidate idea 或 HYP。

## 3. 待验证

- [ ] 第一批论文 ingest 后，从 `wiki/gaps/open-questions.md` 中筛选高可信 gap。
- [ ] 对每个 gap 检查是否已有近年论文解决。
- [ ] 后续每 5-8 篇论文复查 confirmed gap 是否被新文献解决或削弱。
- [x] Batch 01 已复核 confirmed gaps，未将证据不足的统一框架问题写入 confirmed gap。
- [x] Batch 02 已复核 confirmed gaps，新增 GAP-0004；未创建正式 HYP。
- [x] Batch 02 summary 已复核 confirmed gaps，维持 GAP-0001 至 GAP-0004；未创建正式 HYP。
- [x] P0011-P0016 mini-synthesis 已复核 confirmed gaps：维持 GAP-0001 至 GAP-0004；强化 GAP-0002/GAP-0004；未新增 confirmed gap；未创建正式 HYP。
- [x] Batch 03 summary 已复核 confirmed gaps：维持 GAP-0001 至 GAP-0004；未新增 confirmed gap；未创建正式 HYP。
- [x] P0017-P0022 mini-synthesis 已复核 confirmed gaps：维持 GAP-0001 至 GAP-0004；强化 GAP-0001/GAP-0003/GAP-0004；未新增 confirmed gap；未创建正式 HYP。
- [x] Batch 04 summary 已复核 confirmed gaps：维持 GAP-0001 至 GAP-0004；未新增 confirmed gap；未创建正式 HYP。
