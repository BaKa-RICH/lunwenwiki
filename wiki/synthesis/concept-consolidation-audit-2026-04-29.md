---
type: concept-consolidation-audit
last_updated: 2026-04-29
status: proposed-no-merge-applied
source_pages:
  - .wiki-schema.md
  - purpose.md
  - research-agenda.md
  - index.md
  - wiki/concepts/
  - wiki/field/field-map.md
  - wiki/comparisons/merging-control-baselines.md
  - wiki/synthesis/mid-field-synthesis-P001-P0022.md
  - wiki/synthesis/source-quality-audit-2026-04-29.md
confidence: medium
---

# Concept Consolidation Audit: 2026-04-29

## 1. 总体判断

当前 `wiki/concepts/` 已经明显接近“一篇论文一个 concept”的状态：有效语料为 21 篇 paper cards，当前 concepts 也是 21 个；除 `consensus-based-mixed-traffic-merging` 曾被重复源回用外，多数 concept 的 `source_pages` 仍是单篇论文。

这不代表这些页面没有价值。问题在于页面标题和归档层级多为“某篇论文的方法名”，而不是跨论文复用的研究概念。后续如果继续按每篇论文创建一个 concept，`wiki/concepts/` 会逐渐退化为 paper card 的方法摘要副本，真正的跨论文轴线会散落在 `field-map`、`comparisons` 和 `open-questions` 中。

本次审计只给出整理建议，不删除、不合并、不移动任何 concept 文件。未创建 HYP、EXP brief 或 DEC。

## 2. 判定标准

| 类别 | 判定标准 | 建议动作 |
| --- | --- | --- |
| core cross-paper concept | 能组织多篇论文的机制、baseline、gap 或评价轴；即使原始来源单篇，也已被 field/comparison/open questions 跨论文复用 | 保留或强化，必要时改写为高层概念页 |
| merge candidate | 页面内容有价值，但当前标题和边界过窄，更像某篇论文方法；应并入更高层概念或作为该概念的 paper-specific subsection | 等用户确认后再合并，保留原页面证据和链接迁移计划 |
| paper-specific mechanism | 机制主要服务单篇论文或外部迁移线索，暂不足以成为跨论文概念；但作为 baseline/evidence 仍有保留价值 | 保留，标注为窄概念或 paper-specific mechanism |

## 3. Core Cross-Paper Concepts

| Concept | 判断 | 建议 |
| --- | --- | --- |
| [[wiki/concepts/closed-form-optimal-merging]] | 经典解析 baseline，支撑 FIFO、optimal control、proof module 和后续方法动机 | 保留为 historical / analytical baseline anchor，不强行合并 |
| [[wiki/concepts/flexible-merging-positions]] | 可变合流位置是 P001/P004/P006/P007 等多条路线的共同自由度 | 强化为 `merge-position freedom and gap assignment` 高层概念 |
| [[wiki/concepts/mixed-traffic-multilane-cormc]] | mixed traffic、compliance、主线换道协作和多车道协同是多篇论文共同轴线 | 保留并扩展为 `mixed-traffic multilane cooperative merging` |
| [[wiki/concepts/consensus-based-mixed-traffic-merging]] | stability-aware sequencing / consensus proof 是跨方法理论轴 | 保留，强化与 GAP-0003、string stability、delay robustness 的连接 |
| [[wiki/concepts/field-experimental-communication-delay-cav-merging]] | 虽源自 P009，但已成为 GAP-0004 的实证锚点，约束多篇无延迟假设 | 保留为 `delay robustness and field evidence` anchor |
| [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]] | 横向 tracking、车辆动力学执行和上/下层目标失真是跨论文缺口 | 保留为 execution-layer anchor，可吸收部分安全/执行相关机制 |
| [[wiki/concepts/flow-level-multilane-comc]] | flow-level gap creation、capacity drop、shockwave 与局部轨迹方法形成跨尺度对照 | 保留并强化为 `flow-level gap creation and capacity control` |
| [[wiki/concepts/cav-mixed-traffic-impact-review]] | 综述页提供 multi-objective evaluation、cyber/communication risk 和 policy 背景 | 保留为 evaluation / deployment context anchor，不作为算法机制页扩写过多 |

## 4. Merge Candidates

| Concept | 建议合并目标 | 合并理由 |
| --- | --- | --- |
| [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] 的 multi-area dual-lane ramp 机制 | `flow-level gap creation and upstream/multi-area coordination`，可并入强化后的 [[wiki/concepts/flow-level-multilane-comc]] 或新高层页 | 已在第二批减法型 consolidation 中删除原单篇 concept；核心信息保留在 paper card、field-map 和 baseline comparison |
| [[wiki/concepts/flexible-control-barrier-function-merging]] | `safety-critical and execution-layer merging constraints`，与 [[wiki/concepts/flexible-merging-positions]] 和 [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]] 建立上下层关系 | FCBF 的价值是把合流位置自由度转成连续安全约束，适合作为高层 safety/execution concept 的 subsection |
| [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]] | `sequencing-gap-trajectory-timing interface` | P007 是强 baseline，但其核心应服务更高层问题：sequence、target gap、terminal time 与轨迹质量如何耦合 |
| [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]] 的 strategic influence 机制 | `HDV interaction and influence mechanisms in mixed traffic` | 已在第二批减法型 consolidation 中删除原单篇 concept；核心信息保留在 paper card、baseline comparison 和 open questions |
| [[wiki/concepts/dual-module-ppo-heterogeneous-onramp-control]] | `learning proposal with constrained / interpretable execution` | P0014 的 PPO 双模块适合与 P0020 的 VTS-DRL、P006/P0011 的 safety/execution layer 对照 |
| [[wiki/concepts/calibrated-gap-selection-lane-balance-control]] | `interpretable gap selection, lane balance, and capacity-drop-aware control` | P0015 是非 RL 可解释对照，适合承担 learning-vs-rule / capacity-drop 轴的一部分 |
| [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]] 的 HCOMC mode switching 机制 | `longitudinal-vs-lateral cooperation switching` | 已在第二批减法型 consolidation 中删除原单篇 concept；核心信息保留在 paper card、baseline comparison 和 open questions |
| [[wiki/concepts/vts-drl-ocp-onramp-merging]] | `learning-based sequencing interface and model-based execution` | VTS Yield/Green 是合流机会表达接口，可与 P0014、P0022、P007 对照 |
| [[wiki/concepts/dcoma-dynamic-cooperative-merging-assistant]] | `flow-level dynamic gap signal / gap time-series` | DCoMA 的 FD-driven gap time-series 应与 [[wiki/concepts/flow-level-multilane-comc]] 共同构成流级 gap creation 轴 |
| [[wiki/concepts/hierarchical-sequence-speed-adaptation-control]] | `sequencing-gap-trajectory-timing interface` | P0022 的 `t^p` 不是独立大方向，而是 sequence/gap 决策中被忽略的 timing 变量 |

## 5. Paper-Specific Mechanisms

| Concept | 判断 | 建议 |
| --- | --- | --- |
| [[wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles]] 的 BDM-AWM 机制 | BDM-AWM、Transformer 权重选择和 truck penetration 目前主要服务 P008 | 已在减法型 consolidation 中删除原单篇 concept；核心信息保留在 paper card 与 [[wiki/comparisons/merging-control-baselines]] |
| [[wiki/papers/P0017-2024-Lu-Fast-and-Adaptive-Perception-and-Planning]] 的 covariance-adaptive planning 机制 | 外部 UAV 动态避障机制源，不是合流论文 | 已在减法型 consolidation 中删除原单篇 concept；核心信息保留在 paper card 与 [[wiki/gaps/open-questions]] |
| [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]] 的 HCMCC 机制 | HCMCC 是 P0018 的强 baseline，但 MILP + Lane 2 assistance + LCMPC-PTO 组合仍高度 paper-specific | 已在减法型 consolidation 中删除原单篇 concept；核心信息保留在 paper card、[[wiki/field/field-map]]、[[wiki/comparisons/merging-control-baselines]] 和 [[wiki/gaps/open-questions]] |

## 6. 建议的高层合并目标

后续若用户确认执行合并，优先不要把所有内容塞进一个巨型 concept，而是整理为 5-6 个高层概念轴：

| 高层目标 | 可吸收的当前 concepts | 用途 |
| --- | --- | --- |
| `sequencing-gap-trajectory-timing interface` | integrated MINLP、VTS-DRL、HCA `t^p`，并引用 closed-form / FIFO baseline | 统一讨论 sequence、target gap、VTS window、speed-adaptation time 和轨迹质量 |
| `safety-critical and execution-layer merging` | FCBF、DNMPC、HCMCC execution 部分 | 统一讨论 CBF/FCBF、DNMPC、LCMPC-PTO、车辆动力学 tracking 与 feasibility fallback |
| `mixed-traffic multilane cooperative merging` | CORMC、strategic HDV influence、HCOMC、HCMCC Lane 2 assistance | 统一讨论 compliance、HDV influence、协作车辆选择、纵向/横向协作和多车道空间 |
| `flow-level gap creation and capacity control` | flow-level CoMC、DCoMA、multi-area control、calibrated lane balance 的 capacity-drop 部分 | 统一讨论上游 gap shaping、ramp platoon、FD gap time-series、shockwave 和 capacity drop |
| `learning proposal vs interpretable control` | dual-module PPO、VTS-DRL、calibrated gap/lane control、Transformer AWM | 组织 RL、数据驱动权重、规则控制和 safety filter 的对比 |
| `robustness and evaluation interface` | field delay evidence、CAV mixed-traffic impact review、covariance external mechanism | 组织 delay、prediction uncertainty、cyber risk、multi-objective evaluation 和 field/VIL evidence |

## 7. 对 Field Map 的影响

如果执行合并，`wiki/field/field-map.md` 不应继续保留 21 条近似逐论文路线。建议改为：

- 方法谱系按高层轴组织：`sequence/gap/timing`、`safety/execution`、`mixed-traffic/multilane interaction`、`flow-level/capacity`、`learning-vs-rule`、`robustness/evaluation`。
- 代表论文仍保留在每条轴内，但不让每篇论文自动成为一条 field route。
- `field-map` 的“与本研究关系”可从 baseline 列表改为 baseline pool + mechanism axes，避免与 `merging-control-baselines.md` 重复。
- P0017 这种外部机制源应在 field-map 中标注为 robustness / prediction interface evidence，而不是与合流算法同级。

## 8. 对 Comparisons 的影响

`wiki/comparisons/merging-control-baselines.md` 可以继续保留更细的 paper-level baseline 行，因为 baseline 复现实验需要具体方法名。合并 concepts 后，comparison 页的角色会更清楚：

- concepts 负责跨论文概念轴；
- comparisons 负责 paper-level baseline、优劣、适合做什么实验对照；
- 每个 baseline 行可增加 `concept_axis` 字段或分组标题，例如 `sequencing/gap/timing`、`flow-level gap creation`、`learning proposal`；
- FCBF、DNMPC、VTS-DRL、DCoMA 等不需要从 comparison 删除，只需要把它们从“独立概念”降为“某概念轴下的代表 baseline”。

## 9. 对 Open Questions 的影响

合并后，`wiki/gaps/open-questions.md` 可以减少重复和层级过细的问题。建议先不删除 OQ，而是建立归并关系：

| 高层问题簇 | 可归并的 OQ | 影响 |
| --- | --- | --- |
| Sequence / gap / timing 是否能统一 | OQ-0003, OQ-0007, OQ-0011, OQ-0024, OQ-0026 | 把 FIFO、MCTS、MINLP、VTS、`t^p` 统一成一个 sequencing interface 问题 |
| Flow-level plan 能否被车辆级安全执行 | OQ-0017, OQ-0019, OQ-0025 | 把 CoMC、capacity drop、DCoMA、CBF/DNMPC 接口统一 |
| Mixed-traffic interaction 和 HDV 不确定性 | OQ-0004, OQ-0005, OQ-0012, OQ-0021 | 把 compliance、HDV influence、prediction covariance、delay 下的 reaction 放在同一簇 |
| 横向执行与多车道协作收益边界 | OQ-0008, OQ-0020, OQ-0022 | 把 lateral tracking、longitudinal/lateral cooperation switch、Lane 2 assistance 统一 |
| Learning / adaptive methods 的收益来源 | OQ-0013, OQ-0018, OQ-0024 | 把 Transformer AWM、PPO、VTS-DRL 的 ablation 问题统一 |
| Robustness and evaluation minimal set | OQ-0014, OQ-0023 | 把 field delay、multi-objective metrics、cyber/communication risk 作为评估协议问题 |

这些归并会降低 open questions 的数量，但不会削弱证据；原 OQ 可以先保留为子问题，等用户确认后再改写。

## 10. 建议执行顺序

1. 先确认本审计中的三类归档是否接受。
2. 再决定是否创建或强化 5-6 个高层 concept 目标页。
3. 对 merge candidate 逐个迁移内容，保留原页面为 redirect/stub 或在 index 中降级标注。
4. 更新 `field-map` 的方法谱系，使其按高层轴组织。
5. 更新 `merging-control-baselines.md` 的分组或 `concept_axis` 标注，但保留 paper-level baseline 行。
6. 最后整理 `open-questions.md`，先标注归并关系，再决定是否真正合并 OQ。

本轮不执行上述合并动作，等待用户确认。
