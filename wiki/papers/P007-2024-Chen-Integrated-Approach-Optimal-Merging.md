---
type: paper
paper_id: P007
title: "An Integrated Approach to Optimal Merging Sequence Generation and Trajectory Planning of Connected Automated Vehicles for Freeway On-Ramp Merging Sections"
authors: "Jieming Chen, Yue Zhou, Edward Chung"
year: 2024
venue: "IEEE Transactions on Intelligent Transportation Systems"
status: read
confidence: high
source_path: raw/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging.md
zotero_key:
doi: 10.1109/TITS.2023.3315650
tags: [CAV, on-ramp-merging, MINLP, merging-sequence, trajectory-planning, Bezier, NGSIM]
last_updated: 2026-04-28
---

# P007: Integrated Merging Sequence and Trajectory Optimization

## 1. 一句话定位

这篇论文把 CAV on-ramp 合流中的 merge-in gap 选择、合流顺序、终端时间和连续轨迹放进同一个 MINLP，并用基于最优性必要条件的顺序搜索降低计算复杂度。

## 2. 核心贡献

- `EXTRACTED` 提出 integrated MINLP，同时优化多辆主线/匝道 CAV 的 merging sequence 和 trajectories，而不是先固定合流顺序再规划轨迹。
- `EXTRACTED` 模型不强制“一辆主线 facilitating vehicle 对一辆匝道车”，而是决定需要多少主线车参与，以及哪些主线车为匝道车创造 gap。
- `EXTRACTED` 用 cubic polynomial / Bernstein basis 描述连续轨迹，并利用 Bézier convex hull property 保证速度、加速度、车距等约束在任意时刻成立。
- `EXTRACTED` 证明一个 merge-in gap 顺序搜索的 optimality necessary condition，并用 iterative LP 求解每个候选序列下的轨迹子问题。

## 3. 方法抓手

- Decision variables：terminal time `t_f`、每辆车 trajectory polynomial 参数 `theta`、匝道车 merge-in gap binary vector `gamma_i`。
- Objective：最小化主线和匝道车辆相对期望速度的累计 delay，可等价理解为最小化合作区内总旅行时间。
- Continuous safety：终端 CTH gap、合流位置在 cooperation zone 内、同车道任意时刻防碰撞、速度/加速度任意时刻边界。
- Search algorithm：从最下游匝道车开始逐个确定最优 merge-in gap；每个候选 gap 下重规划已纳入车辆的轨迹，直到最后一个匝道车确定。

## 4. 关键实验结论

- `EXTRACTED` SUMO 中测试 12 个 demand / mainline-ramp ratio 场景；有 ramp metering 时，匝道占比高的 2:1、2082 veh/h 场景中 delay improvement 达 51.4%。
- `EXTRACTED` 无 ramp metering 时，proposed approach 在所有可比条件下相对 VROCP 至少有 11% delay improvement；2:1 场景下 VROCP 发生 failure，而 proposed 仍可求解。
- `EXTRACTED` cooperation zone 缩短到 300 m 时，proposed 仍保持 1.50 s mean time gap，VROCP failure，说明硬安全约束对短合流区有效。
- `EXTRACTED` NGSIM I-80 数据验证中，proposed 与 MCTS-DA 达到相同总延误 469 s，但总计算时间为 13.9 s，远低于 MCTS-DA 的 441 s。
- `EXTRACTED` 计算时间随匝道车数增长较快：20 辆主线 + 3 辆匝道时约 1.8 s。

## 5. 局限与隐含假设

- 论文自述局限：
  - 未来需要扩展到 multiple-lane scenarios，将 mainline lane changing 纳入 cooperative merging。
  - 当前 100% CAV 假设需要放宽，通过 human driver trajectory prediction 适配 mixed traffic。
  - microscopic trajectory generation 与 flow-based merging control 的结合仍值得研究。
- 你识别到的隐含假设：
  - 主线换道已在合流前完成，模型只处理 one mainline lane + one on-ramp lane 的纵向运动。
  - 虽有 HDV 扰动回放实验，但未来 HDV 速度用“保持当前速度”预测，未形成完整混合交通预测控制框架。
  - 搜索空间仍随匝道车数量指数增长，实际可实时性依赖每个 control cycle 的匝道车批量较小。

## 6. 关系线索

- extends: [[wiki/concepts/flexible-merging-positions]]，把 flexible merging time/location 从单车或层级设置推进到 sequence + trajectory 的一体化优化。
- contrasts: [[wiki/concepts/flexible-control-barrier-function-merging]]，P006 用 CBF/CLF-QP 做 safety-critical local control；P007 用 Bézier convex hull 在 MINLP 层保证 continuous-time safety。
- contrasts: [[wiki/comparisons/merging-control-baselines]] 中的 FIFO、VROCP、FTOCP、MCTS-DA，P007 通过必要条件减少搜索空间并保持最优序列。
- uses: [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]], MINLP, merge-in gap, Bernstein basis, iterative LP, NGSIM I-80。
- suggests_gap: integrated optimal sequencing 仍与 mixed traffic prediction、multilane lane-changing、lateral tracking 和 flow-level ramp control 脱节。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P007/`。

## 7. 对我研究的可能用途

- baseline: 可作为“排序与轨迹一体化优化”的强 baseline，尤其适合反驳 FIFO/先排序后规划的低质量轨迹问题。
- idea_source: merge-in gap 可多匝道车共享的设计，为“群组合流”或 dual-lane ramp sequencing 提供机制线索。
- proof_source: Proposition 1 和 sequential search 可作为排序搜索剪枝的理论参考。
- counterexample: 即便 integrated optimization 能提高效率，它仍未解决 mixed traffic、横向换道和多车道协作。
- dataset_or_metric: SUMO one-hour simulation、NGSIM I-80、total delay、mainline delay、speed variation、time gap distribution、computation time。

## 8. 原文锚点

- raw: `raw/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging.md`
- zotero:
- doi: 10.1109/TITS.2023.3315650
- keywords: Connected automated vehicles; on-ramp merging; optimal merging sequence; trajectory planning.

## 9. 必要摘录

> `EXTRACTED` "The proposed model simultaneously optimizes multiple vehicles' trajectories and their merging sequence to improve traffic efficiency and ensure safety."

> `EXTRACTED` "the proposed model determines the optimal number of facilitating vehicles and which mainline vehicles should serve as the facilitating vehicles."

> `EXTRACTED` "The convex hull property of the Bernstein basis is incorporated to ensure that all constraints ... are guaranteed at any time."

> `EXTRACTED` "the proposed approach achieves the same total travel delay as MCTS-DA ... however, the proposed approach requires way less computation time than MCTS-DA."

## 10. 回查触发点

- proof：需要引用 sequential search optimality、Proposition 1、搜索空间缩减或 integrated vs hierarchical 的理论依据时，回查 `III. AN INTEGRATED SOLUTION ALGORITHM`。
- 实验设计：需要设置 SUMO demand ratio、cooperation zone、ramp metering / no metering、VROCP/FTOCP/MCTS-DA baselines 时，回查 `V. NUMERICAL EXPERIMENTS`。
- baseline 复现：需要复现 MINLP、Bézier continuous constraints、iterative LP、NGSIM I-80 实验时，回查 `II. MATHEMATICAL MODELING`、`Algorithm 1`、`Algorithm 2` 和 `V-H`。
- 写作：需要批评“先定顺序再做轨迹”的 hierarchical drawback 时，回查 `I-A. Literature Review` 和 `I-B. Summary of Highlights and Contributions`。
- citation audit：需要核对 DOI、TITS 元数据、VROCP/FTOCP/MCTS-DA 引用链和 NGSIM 来源时，回查开头元数据与 `REFERENCES`。

## 11. 关键原文位置

- 题名、作者、摘要、DOI、关键词：开头、`Abstract`、`Index Terms`。
- integrated vs hierarchical 的问题定位：`I. INTRODUCTION`、`A. Literature Review`。
- 贡献列表：`B. Summary of Highlights and Contributions`。
- 场景、merge-in gap、trajectory representation：`II-A. Preliminaries`。
- MINLP 目标、约束和 continuous safety：`II-B. Model Formulation`。
- sequential search、optimality proof、iterative LP：`III. AN INTEGRATED SOLUTION ALGORITHM`。
- feedback loop：`IV. RECURSIVE IMPLEMENTATION FOR FEEDBACK`。
- SUMO、NGSIM、短 cooperation zone、HDV lane change 实验：`V. NUMERICAL EXPERIMENTS`。
- 局限与未来工作：`VI. CONCLUSION`。
