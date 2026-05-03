# Research Wiki Index

last_updated: 2026-05-03

## 启动文件

| 页面 | 用途 |
| --- | --- |
| `AGENTS.md` | Codex core rule source / Codex-native 启动规则 |
| `purpose.md` | Codex-native 启动链：长期研究方向、边界和偏好 |
| `research-agenda.md` | Codex-native 启动链：当前阶段计划、优先级和近期问题 |
| `index.md` | Codex-native 启动链：定位最小必要 `wiki/` 页面 |
| `.wiki-schema.md` | legacy / migration reference；仅在 legacy comparison 或 migration audit 时读取 |
| `log.md` | append-only 操作日志 |

## Raw 输入层

| 路径 | 用途 | 写入原则 |
| --- | --- | --- |
| `raw/papers/` | MinerU 论文 Markdown | 原文层，只读 |
| `raw/notes/` | 想法、导师建议、会议记录、网页剪藏 | 原文层，只读 |
| `raw/articles/` | 博客、技术报告、调研文章 | 原文层，只读 |
| `raw/experiment-results/` | 实验原始回填 | 原文层，只读 |
| `raw/assets/` | 图片、表格、PDF、截图等附件 | 原文层，只读 |

## Wiki 编译层

| 路径 | 用途 |
| --- | --- |
| `wiki/papers/` | Paper Memory Card |
| `wiki/concepts/` | 方法、理论、机制 |
| `wiki/entities/` | 数据集、benchmark、关键系统、关键研究组 |
| `wiki/comparisons/` | 方法、论文、baseline 对比 |
| `wiki/field/field-map.md` | 方法谱系、研究路线、领域演化 |
| `wiki/field/shared-assumptions.md` | 共同隐含假设和脆弱点 |
| `wiki/field/research-frontier.md` | 当前前沿和可切入方向 |
| `wiki/gaps/confirmed-gaps.md` | 已确认或高可信 gap |
| `wiki/gaps/open-questions.md` | 待探索问题 |
| `wiki/idea-candidates/` | 候选 idea 批次 |
| `wiki/hypotheses/index.md` | HYP 状态看板 |
| `wiki/hypotheses/` | 正式 hypothesis 生命周期卡 |
| `wiki/proof-sketches/` | HYP 的理论依据 |
| `wiki/experiment-briefs/` | 给实验 Agent 或人类的任务书 |
| `wiki/experiment-reports/` | 实验事实和对 HYP 的影响 |
| `wiki/manuscripts/` | 文章级论证、章节草稿、投稿前材料 |
| `wiki/decisions/` | 继续、调整、暂停、放弃的研究决策 |
| `wiki/_archive/` | 暂停或否定 idea 的中间产物归档 |
| `wiki/synthesis/` | 高价值问答、多轮讨论、阶段综合 |

## Tooling / Skills / Schema

| 路径 | 用途 | 写入原则 |
| --- | --- | --- |
| `skills/research-wiki/` | repo-native workflow skill source：query、ingest、synthesis、candidate/HYP、proof/EXP/DEC、maintenance | 操作指南层，不是 compiled research memory |
| `skills/research-argumentation/` | repo-native argumentation skill source：机制论证、proof 写作、最强反对理由、claim 审计 | 只改善论证质量，不改变证据强度或研究事实 |
| `schema/` | lifecycle、frontmatter、citation/evidence policy 文档级规范 | 服务 lint 和 workflow 一致性 |
| `scripts/` | scan、rebuild index、lint、status 等机械辅助脚本 | 不自动创建 HYP、EXP brief、EXP report 或 DEC |
| `workspace/` | 自动生成 manifests、status/lint reports、cache | 可重建运行时层，不是正式研究结论 |

## 当前关键页面

- [[wiki/comparisons/merging-control-baselines]]
- [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]]
- [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]]
- [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]]
- [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]]
- [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]]
- [[wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging]]
- [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]]
- [[wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles]]
- [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]]
- [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]]
- [[wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging]]
- [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]]
- [[wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp]]
- [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]]
- [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]]
- [[wiki/papers/P0017-2024-Lu-Fast-and-Adaptive-Perception-and-Planning]]
- [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]]
- [[wiki/papers/P0019-2024-Pan-CAV-Impacts-Mixed-Traffic-Flow-Review]]
- [[wiki/papers/P0020-2024-Muzahid-Optimizing-On-Ramp-Merging-DRL-OCP]]
- [[wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant]]
- [[wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging]]
- [[wiki/concepts/flexible-merging-positions]]
- [[wiki/concepts/mixed-traffic-multilane-cormc]]
- [[wiki/concepts/consensus-based-mixed-traffic-merging]]
- [[wiki/concepts/closed-form-optimal-merging]]
- [[wiki/concepts/flexible-control-barrier-function-merging]]
- [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]]
- [[wiki/concepts/field-experimental-communication-delay-cav-merging]]
- [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]]
- [[wiki/concepts/flow-level-multilane-comc]]
- [[wiki/concepts/dual-module-ppo-heterogeneous-onramp-control]]
- [[wiki/concepts/calibrated-gap-selection-lane-balance-control]]
- [[wiki/concepts/cav-mixed-traffic-impact-review]]
- [[wiki/concepts/vts-drl-ocp-onramp-merging]]
- [[wiki/concepts/dcoma-dynamic-cooperative-merging-assistant]]
- [[wiki/concepts/hierarchical-sequence-speed-adaptation-control]]
- [[wiki/synthesis/source-quality-audit-2026-04-29]]
- [[wiki/synthesis/concept-consolidation-audit-2026-04-29]]
- [[wiki/synthesis/mid-field-synthesis-P001-P0022]]
- [[wiki/field/field-map]]
- [[wiki/field/shared-assumptions]]
- [[wiki/field/research-frontier]]
- [[wiki/gaps/confirmed-gaps]]
- [[wiki/gaps/open-questions]]
- [[wiki/hypotheses/index]]

## 最近更新

- 2026-04-29：执行减法型 concept consolidation：删除刚才新增的 concept consolidation plan 文件；删除 3 个 paper-specific concepts（P008 Transformer-AWM、P0017 covariance-adaptive UAV 外部机制、P0018 HCMCC 单篇方法页），并将引用改回 paper cards、field-map、baseline comparison 或 open questions；未新增 audit / synthesis / plan 文件，未创建正式 HYP、EXP 或 DEC。
- 2026-04-29：继续执行第二批减法型 concept consolidation：删除 3 个 paper-specific concepts（P004 multi-area dual-lane ramp、P0010 strategic HDV influence、P0016 HCOMC mode switching），并将引用改回 paper cards、baseline comparison 或 open questions；未新增 audit / synthesis / plan 文件，未创建正式 HYP、EXP 或 DEC。
- 2026-04-29：删除 8 个已被 [[wiki/synthesis/mid-field-synthesis-P001-P0022]] 吸收的中间 synthesis 文件（Batch 01-04 summary 与对应 mini-synthesis），将当前接力入口收敛到 mid-field synthesis；未创建正式 HYP、EXP 或 DEC。
- 2026-04-29：完成 [[wiki/synthesis/mid-field-synthesis-P001-P0022]]，基于当前有效编译层材料压缩 P001-P0022 方法谱系，复核推进关系、共同假设、confirmed gaps、open questions 和 candidate idea 线索；建议下一步优先做 baseline / benchmark design，再生成 idea-candidates，暂缓继续 P0024-P0030 大规模 ingest；未回读 raw，未创建正式 HYP、EXP 或 DEC。
- 2026-04-29：完成 [[wiki/synthesis/concept-consolidation-audit-2026-04-29]]，将 21 个 concepts 分为 core cross-paper concept、merge candidate、paper-specific mechanism 三类，并给出建议合并目标及对 field-map、comparisons、open-questions 的影响；本次未删除、合并或改写任何 concept，未创建正式 HYP、EXP 或 DEC。
- 2026-04-29：完成 source-quality cleanup，当前保留 21 个 paper cards / 21 个 raw papers；同步 P0019/P0020/P0021 的规范化 raw 路径，清理失效 paper、concept、field/gaps/comparison/synthesis 引用，更新 [[wiki/synthesis/source-quality-audit-2026-04-29]]；未创建正式 HYP、EXP 或 DEC。
- 2026-04-29：结束 Batch 04 初始化导入并已将中间 batch/mini synthesis 合并进 [[wiki/synthesis/mid-field-synthesis-P001-P0022]]；confirmed gaps 维持 GAP-0001 至 GAP-0004，OQ-0021 至 OQ-0026 保持 open，candidate idea 仅保留线索，未创建正式 HYP。
- 2026-04-29：完成 P0017-P0022 mini-synthesis，其内容后续已被 [[wiki/synthesis/mid-field-synthesis-P001-P0022]] 吸收；原 mini-synthesis 文件已删除。
- 2026-04-29：完成 [[wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging]] ingest，新增 [[wiki/concepts/hierarchical-sequence-speed-adaptation-control]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 HCA sequence + speed-adaptation timing baseline；记录 OQ-0026，未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant]] ingest，新增 [[wiki/concepts/dcoma-dynamic-cooperative-merging-assistant]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 DCoMA dynamic macro-micro gap creation baseline；记录 OQ-0025，未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0020-2024-Muzahid-Optimizing-On-Ramp-Merging-DRL-OCP]] ingest，新增 [[wiki/concepts/vts-drl-ocp-onramp-merging]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 VTS-DRL + OCP speed control baseline；记录 OQ-0024，未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0019-2024-Pan-CAV-Impacts-Mixed-Traffic-Flow-Review]] ingest，新增 [[wiki/concepts/cav-mixed-traffic-impact-review]]，记录 OQ-0023 与 multi-objective merging evaluation minimal set candidate 线索；未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]] ingest，记录 HCMCC MILP + LCMPC-PTO multilane control baseline 并在 [[wiki/comparisons/merging-control-baselines]] 增补；记录 OQ-0022，未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0017-2024-Lu-Fast-and-Adaptive-Perception-and-Planning]] ingest，记录 covariance adaptation / dynamic obstacle planning 外部机制源、OQ-0021 与 prediction-uncertainty-aware merging fallback candidate 线索；未创建正式 HYP。
- 2026-04-29：结束 Batch 03 初始化导入，其内容后续已被 [[wiki/synthesis/mid-field-synthesis-P001-P0022]] 吸收；原 batch/mini synthesis 文件已删除。
- 2026-04-29：完成 P0011-P0016 mini-synthesis，其内容后续已被 [[wiki/synthesis/mid-field-synthesis-P001-P0022]] 吸收；原 mini-synthesis 文件已删除。
- 2026-04-29：完成 [[wiki/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging]] ingest，并在 [[wiki/comparisons/merging-control-baselines]] 增补 HCOMC model-based two-lane control baseline；记录 OQ-0020，未创建正式 HYP。原 HCOMC 单篇 concept 已在后续减法型 consolidation 中删除。
- 2026-04-29：完成 [[wiki/papers/P0015-2025-Yang-Cooperative-Control-Heterogeneous-Traffic]] ingest，新增 [[wiki/concepts/calibrated-gap-selection-lane-balance-control]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 calibrated gap selection + lane balance baseline；记录 OQ-0019，未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp]] ingest，新增 [[wiki/concepts/dual-module-ppo-heterogeneous-onramp-control]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 dual-module PPO cooperative control baseline；记录 OQ-0018，未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0012-2022-Zhu-Flow-level-Coordination-Multilane-Merging]] ingest，新增 [[wiki/concepts/flow-level-multilane-comc]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 flow-level multilane CoMC baseline；记录 OQ-0017，未创建正式 HYP。
- 2026-04-29：完成 [[wiki/papers/P0011-2022-Jing-Integrated-Longitudinal-Lateral-Merging]] ingest，新增 [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 integrated longitudinal-lateral DNMPC baseline；记录 OQ-0016，未创建正式 HYP。
- 2026-04-28：结束 Batch 02 初始化导入，其内容后续已被 [[wiki/synthesis/mid-field-synthesis-P001-P0022]] 吸收；原 batch/mini synthesis 文件已删除。
- 2026-04-28：完成 P006-P0010 mini-synthesis，其内容后续已被 [[wiki/synthesis/mid-field-synthesis-P001-P0022]] 吸收；原 mini-synthesis 文件已删除。
- 2026-04-28：完成 [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]] ingest，并在 [[wiki/comparisons/merging-control-baselines]] 增补 strategic CAV influence baseline；未创建正式 HYP。原 strategic CAV influence 单篇 concept 已在后续减法型 consolidation 中删除。
- 2026-04-28：完成 [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]] ingest，新增 [[wiki/concepts/field-experimental-communication-delay-cav-merging]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 vehicle-in-the-loop delay assessment 证据线索；未创建正式 HYP。
- 2026-04-28：完成 [[wiki/papers/P008-2025-Zhang-Cooperative-Control-Mixed-Vehicles]] ingest，记录 BDM-AWM mixed-vehicle baseline 并在 [[wiki/comparisons/merging-control-baselines]] 增补；未创建正式 HYP。
- 2026-04-28：完成 [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]] ingest，新增 [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 integrated sequence + trajectory baseline；未创建正式 HYP。
- 2026-04-28：完成 [[wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging]] ingest，新增 [[wiki/concepts/flexible-control-barrier-function-merging]]，并在 [[wiki/comparisons/merging-control-baselines]] 增补 FPM-FCBF baseline；未创建正式 HYP。
- 2026-04-28：新增 [[wiki/comparisons/merging-control-baselines]]，将 Batch 01 的 FIFO/FCFS、closed-form、MCTS-DA、APS/CUC、shortest-path、consensus、rolling optimization 和 multi-area control 从 field-map 中分离为 baseline/机制对比页。
- 2026-04-28：更新 `research-agenda.md`，标记 Batch 01 完成，并明确 Batch 02 重点审查方向。
- 2026-04-28：更新 [[wiki/gaps/confirmed-gaps]]，为 GAP-0001 增加后续拆解方向；未创建正式 HYP。
- 2026-04-26：结束 Batch 01 初始化导入，其内容后续已被 [[wiki/synthesis/mid-field-synthesis-P001-P0022]] 吸收；原 batch/mini synthesis 文件已删除。
- 2026-04-26：按 P001-P005 cards/concepts/field/gaps 复核 mini-synthesis；补充推进/互补/矛盾关系，收紧 confirmed gaps，并将统一框架问题降级为 open question。
- 2026-04-26：完成 P001-P005 mini-synthesis，更新 `wiki/field/field-map.md`、`wiki/field/shared-assumptions.md`、`wiki/gaps/confirmed-gaps.md`、`wiki/gaps/open-questions.md`。
- 2026-04-26：完成 [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]] ingest，新增 closed-form optimal merging 经典基线线索。
- 2026-04-26：完成 [[wiki/papers/P004-2025-Wang-Cooperative-Control-CAVs-Merging]] ingest，新增 multi-area dual-lane ramp control 线索。
- 2026-04-26：完成 [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]] ingest，新增 consensus-based mixed-traffic merging 与稳定性线索。
- 2026-04-26：完成 [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]] ingest，新增 mixed traffic + multilane CORMC 线索。
- 2026-04-26：补充 [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]] 的回查触发点和关键原文位置，服务 proof、实验设计、baseline 复现、写作和 citation audit。

## 当前状态

- Paper cards：21
- Concepts：15
- Confirmed gaps：4
- Idea candidate batches：0
- Hypotheses：0
- Experiment briefs：0
- Experiment reports：0
- Decisions：0
- Synthesis：11
