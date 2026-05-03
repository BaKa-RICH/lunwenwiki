---
type: paper
paper_id: P0010
title: "Cooperative Merging in Mixed Traffic Based on Strategic Influence of Connected Automated Vehicles on Human-Driven Vehicle Behavior"
authors: "Kyunghwan Choi, Seongjae Shin, Minseok Seo"
year: 2025
venue: "Advanced Intelligent Systems"
status: read
confidence: high
source_path: raw/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic.md
zotero_key:
doi: 10.1002/aisy.202400797
tags: [CAV, HDV, mixed-traffic, strategic-slowdown, arrival-time-optimization, dynamic-optimization, cooperative-merging]
last_updated: 2026-04-28
---

# P0010: Strategic CAV Influence on HDV Behavior

## 1. 一句话定位

这篇论文提出一种 mixed traffic 多 CAV 合流策略：不依赖精确预测 HDV，而是通过战略性减速 HDV 前方的 CAV 来影响 HDV 行为，让相邻道路的 CAV 更确定地插入 HDV 前方。

## 2. 核心贡献

- `EXTRACTED` 提出面向 control zone 内所有 CAV 的 optimization-based cooperative merging strategy，处理 HDV intentions 不确定的问题。
- `EXTRACTED` 引入 strategic influence / strategic slowdown：让 HDV 前方的 CAV 主动减速，迫使后随 HDV 为保持安全时距而减速，从而降低其他 CAV 合流不确定性。
- `EXTRACTED` 通过枚举 candidate slowdown patterns 并评估 CAV throughput / travel time delay，选择最优 cooperation pattern。
- `EXTRACTED` 每当新车辆进入 control zone 时执行 dynamic optimization，以适应 HDV 行为的实时变化。
- `EXTRACTED` 采用 hierarchical optimization：上层优化 CAV arrival times，下层用 energy-optimal control 求当前 CAV 控制输入。

## 3. 方法抓手

- Arrival-time domain：用 arrival time 约束 lateral collision 与 rear-end collision，优化所有车辆 TTD 平方和。
- Cooperation candidate set：识别两条道路上的连续 CAV 群，划分 cooperation group `C` 和 noncooperation group `N`。
- Strategic CAV：在 Mode 3 中，位于 HDV 前方且可影响后续 HDV 的 CAV 被选为 strategic CAV，其 slowdown pattern 决定哪些 CAV 可并入 cooperation group。
- Dynamic optimization：每次有新车进入控制区，重新初始化 arrival times、重排车辆优先级，并顺序优化 CAV。
- Lower-level control：给定上层 `T_i*` 后，求最小控制输入平方的能耗友好控制，并用输入约束与下一步 rear-end safety bound 修正。

## 4. 关键实验结论

- `EXTRACTED` 4 车案例中，proposed strategy 相比 DO strategy 将 ATTD 降低 16%，control cost 降低 65%。
- `EXTRACTED` 20 车组实验中，proposed strategy 在不同 CAV penetration 和 entry time gap 下通常低于 SO 的 ATTD；在 70% penetration、`T_g=2 s` 时 ATTD reduction 最高达 31%。
- `EXTRACTED` proposed strategy 的有效最低 penetration rate 约为 30%-50%，峰值收益出现在 60%-70% penetration；100% CAV 时各策略几乎相同。
- `EXTRACTED` proposed strategy 相比 DO 可在几乎相同 control cost 下获得更低 ATTD。
- `EXTRACTED` MATLAB 计算时间均值低于 80 μs，proposed strategy 最大计算时间为 9.04 ms，论文据此认为可实时实施。

## 5. 局限与隐含假设

- 论文自述局限：
  - 后续需要扩展到 multi-lane settings，并考虑 HDV 受到 strategic slowdown 时的详细 lane-change behavior。
  - HDV reaction 可进一步建模为 probabilistic behavior，并用 data-driven methods 学习后纳入优化。
- 你识别到的隐含假设：
  - 明确假设 CAV 无控制误差、无 communication delay 和 packet loss；这与 P009 的 field evidence 形成张力。
  - HDV 在仿真中由 IDM 描述，未使用实车或自然驾驶 HDV 数据验证 strategic influence。
  - arrival-time upper level 使用常速估计初始化 HDV 到达时间，虽然 dynamic optimization 可缓解但不能消除预测误差。
  - 合流区内 CAV/HDV 均由 IDM 平滑通过，横向换道细节和驾驶风格差异未充分建模。

## 6. 关系线索

- extends: [[wiki/concepts/mixed-traffic-multilane-cormc]] 和 [[wiki/concepts/flexible-control-barrier-function-merging]]，从“适应/预测 HDV”推进到“CAV 战略性影响 HDV”。
- complements: [[wiki/concepts/field-experimental-communication-delay-cav-merging]]，P0010 机制依赖无延迟/无丢包，P009 提供该假设的现实反证。
- contrasts: [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]]，P007 是纯 CAV 强一体化优化；P0010 是 mixed traffic 下的 strategic influence + dynamic arrival-time optimization。
- uses: strategic CAV influence on HDV paper-specific mechanism, strategic slowdown, cooperation candidate set, dynamic optimization, arrival time optimization, IDM；原单篇 concept 已删除，核心信息保留在本 card、[[wiki/comparisons/merging-control-baselines]] 和 [[wiki/gaps/open-questions]]。
- suggests_gap: strategic influence 是否在通信延迟、横向换道、真实 HDV 反应和低 CAV penetration 下仍有效，需要独立验证。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P0010/`。

## 7. 对我研究的可能用途

- idea_source: “影响 HDV 而不是只预测 HDV”是很强的机制线索，可转化为 candidate idea，但需要先补 proof 和反例。
- baseline: 可作为 mixed traffic multi-CAV arrival-time optimization baseline，与 P006 safety-critical control、P007 integrated sequencing、P008 adaptive weighting 对比。
- counterexample: 如果新方法仍假设 HDV 只作为外部扰动，P0010 提醒 CAV 可主动塑造 HDV 行为。
- risk_source: 与 P009 的通信延迟证据冲突，说明 strategic influence 类方法尤其需要 delay / packet loss robustness test。
- dataset_or_metric: ATTD、control cost、CAV penetration rate、entry time gap `T_g`、computation time、Carla reproduction。

## 8. 原文锚点

- raw: `raw/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic.md`
- zotero:
- doi: 10.1002/aisy.202400797
- keywords: connected and automated vehicles; cooperative control; human-driven vehicles; mixed traffic; on-ramp merging.
- open data / simulator: `https://github.com/GIST-MIC-Lab/Cooperative-merging-in-mixed-traffic`

## 9. 必要摘录

> `EXTRACTED` "A key innovation is the strategic influence of CAVs on HDV behavior by slowing down the CAV preceding HDVs, thereby allowing other CAVs on the adjacent road to merge in front of the HDVs with reduced uncertainty."

> `EXTRACTED` "All CAVs are controllable and free from control errors (e.g., communication delays and packet loss)."

> `EXTRACTED` "This strategic slowdown led the proposed strategy to achieve a 16% reduction in ATTD and a 65% reduction in control cost compared to the DO strategy."

> `EXTRACTED` "at a penetration rate of 70% with Tg = 2s, the proposed strategy achieved an ATTD reduction of up to 31%."

## 10. 回查触发点

- proof：需要解释 strategic slowdown、arrival-time optimization、cooperation candidate set、Mode 1/2/3 或 dynamic optimization 时，回查 `3.1. Solution to Arrival Time Optimization Problem`。
- 实验设计：需要设置 SO/DO/proposed 对比、20 车组、penetration sweep、`T_g` sweep、ATTD/control cost 指标时，回查 `4. Results`。
- baseline 复现：需要实现 lower-level energy-optimal control、input/safety bound、IDM HDV 仿真或 Matlab 计算时间时，回查 `2.2.2`、`3.2` 和 `4.1. Setup`。
- 写作：需要论证“CAV 可战略性塑造 HDV 行为”而不是只做 HDV prediction 时，回查 `1.3. Contribution of the Article`。
- citation audit：需要核对 DOI、Advanced Intelligent Systems 元数据、open-source Carla reproduction 和 supporting information 时，回查开头元数据、`Data Availability Statement` 和 `References`。

## 11. 关键原文位置

- 题名、作者、摘要、DOI、关键词：开头、`Keywords`。
- mixed traffic 多 CAV 协同问题定位：`1.1. Motivation`。
- related work 分类与本文缺口：`1.2. Literature Review`。
- 贡献：`1.3. Contribution of the Article`。
- 建模假设、arrival-time safety constraints：`2.1. Modeling Framework`。
- 上层 arrival time 与下层 energy-optimal control：`2.2. Optimization Problem Formulation`。
- strategic slowdown、cooperation modes 和 Algorithm 1：`3.1. Solution to Arrival Time Optimization Problem`。
- 输入/安全约束修正控制：`3.2. Solution to Energy-Optimal Control Problem`。
- 4 车与 20 车实验结果：`4.2`、`4.3`。
- 局限与未来工作：`5. Concluding Remarks`。
