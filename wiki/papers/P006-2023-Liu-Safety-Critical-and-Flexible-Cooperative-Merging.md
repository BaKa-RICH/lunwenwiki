---
type: paper
paper_id: P006
title: "Safety-Critical and Flexible Cooperative On-Ramp Merging Control of Connected and Automated Vehicles in Mixed Traffic"
authors: "Haoji Liu, Weichao Zhuang, Guodong Yin, Zhaojian Li, Dongpu Cao"
year: 2023
venue: "IEEE Transactions on Intelligent Transportation Systems"
status: read
confidence: high
source_path: raw/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging.md
zotero_key:
doi: 10.1109/TITS.2022.3224592
tags: [CAV, mixed-traffic, flexible-merging-position, CBF, CLF, receding-horizon, safety-critical-control]
last_updated: 2026-04-28
---

# P006: Safety-Critical Flexible Merging with FCBF

## 1. 一句话定位

这篇论文把 mixed traffic 中的 flexible merging position 和 safety-critical control 接起来：用上层 PMP 规划期望合流位置，下层 CBF-CLF QP 保证安全约束，并通过 receding horizon 应对 HDV 扰动。

## 2. 核心贡献

- `EXTRACTED` 提出两层 hierarchical cooperative on-ramp merging control：上层求 flexible expected merging position，下层求 safety-critical CAV 轨迹。
- `EXTRACTED` 将上层期望合流位置嵌入下层可变 time headway，提出 Flexible Control Barrier Function（FCBF）以同时支持 FPM policy 和安全约束。
- `EXTRACTED` 将含多重状态/控制约束的非线性 OCP 转换为 QP，使每个递归步可实时求解。
- `EXTRACTED` 使用 receding horizon 持续更新期望合流位置和牵引力，处理 leading HDV 不确定行为造成的扰动。

## 3. 方法抓手

- Three-vehicle coordination group（TCG）：leading vehicle 可为 CAV 或 HDV，其轨迹作为 disturbance；assisted CAV 为匝道 CAV 创造 gap；merging CAV 调整纵向速度完成合流。
- 上层 planner：简化为 free-terminal OCP，用 PMP 得到 candidate merging position，并与 acceleration lane 末端 `L` 取最小得到 expected merging position。
- 下层 controller：把速度限制、car-following、安全合流距离等约束通过 CBF/FCBF 转为控制约束，再和 CLF 速度跟踪目标组成 QP。
- FCBF：把递归更新的 expected merging position 作为非状态变量嵌入 barrier function，用连续 time headway 避免只在合流时刻施加离散安全约束。

## 4. 关键实验结论

- `EXTRACTED` 单 TCG 场景中，FPM-FCBF 相比 PPM-CBF 将合流持续时间压缩 49.28%，CAV2/CAV1 行驶距离分别缩短 49.98% 和 45.90%，两车总燃耗降低 32.33%。
- `EXTRACTED` 每个递归步计算时间小于 0.06 s，低于 0.1 s sampling time，论文据此主张可实时实施。
- `EXTRACTED` 多 HDV mixed traffic 场景中，FPM-FCBF 缓解 leading vehicle 引入的 shock wave，并提升瓶颈处交通速度和效率。
- `EXTRACTED` 仅 leading vehicle 为 HDV 的多 CAV 场景中，FPM-FCBF 比 PPM-CBF 的速度波动更小，并在 1000 m 范围内降低超过 10% 平均燃耗。

## 5. 局限与隐含假设

- 论文自述局限：
  - 尚未研究 CAV penetration 和 traffic density 的影响。
  - 合流序列优化未纳入当前框架，后续需要结合 proposed control strategy 继续挖掘优化潜力。
  - 未来需要考虑 inter-vehicle interactions，例如 nudge maneuvers。
  - HDV 轨迹预测仍待用 data-driven trajectory prediction model 改进。
- 你识别到的隐含假设：
  - 只控制 TCG 中两个 CAV 的纵向运动，横向合流/换道执行被简化为满足条件后的 maneuver。
  - leading HDV 作为外部扰动处理，而不是与 CAV 决策统一博弈或预测。
  - TCG 中 leading/assisted vehicle 的选择规则超出本文范围，多车场景仍使用 FIFO。

## 6. 关系线索

- extends: [[wiki/concepts/flexible-merging-positions]]，将 flexible merging position 从系统优化线索推进到 mixed traffic + safety-critical lower-level control。
- extends: [[wiki/concepts/closed-form-optimal-merging]]，继承 PMP/optimal control 的解析规划思路，但不再固定合流点。
- complements: [[wiki/concepts/consensus-based-mixed-traffic-merging]]，P006 保证局部安全约束，P003 强调 platoon stability 和 communication delay。
- uses: [[wiki/concepts/flexible-control-barrier-function-merging]], PMP, CBF, CLF, QP, receding horizon, TCG。
- suggests_gap: flexible merging position 与合流排序、HDV 预测、横向 tracking 和 stability proof 仍未统一。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P006/`。

## 7. 对我研究的可能用途

- baseline: 可作为 safety-critical flexible merging position 的强 baseline，尤其适合对比 fixed merging point / PPM-CBF。
- idea_source: FCBF 提供一种把“动态合流位置”嵌入安全约束的机制，可用于后续 integrated lateral-longitudinal 或 stability-aware 版本。
- proof_source: CBF/CLF-QP 和 time-varying headway 是构造安全约束 proof 的可复用模块。
- counterexample: 仅有 flexible merging position 仍不能解决排序、横向执行、通信延迟和 HDV 预测问题。
- dataset_or_metric: merging duration、travel distance、fuel consumption、speed wave、recursive-step computation time。

## 8. 原文锚点

- raw: `raw/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging.md`
- zotero:
- doi: 10.1109/TITS.2022.3224592
- keywords: Connected and automated vehicle; on-ramp merging; cooperative control; mixed traffic; control barrier function.

## 9. 必要摘录

> `EXTRACTED` "there still remains a research gap between flexible merging position planning and safetycritical control of cooperative on-ramp merging in mixed traffic."

> `EXTRACTED` "the flexible non-state time-varying variable, i.e., expected merging position, is integrated into the CBF, which is called Flexible Control Barrier Function (FCBF)."

> `EXTRACTED` "FPM-FCBF strategy compresses 49.28% merging duration ... and the corresponding total consumption is saved by 32.33%."

> `EXTRACTED` "Computation time for each recursive step is less than 0.06s, which is within the sampling time 0.1s."

## 10. 回查触发点

- proof：需要引用 FCBF、CBF/CLF-QP、安全集合、time-varying headway 或 mixed state-control constraints 时，回查 `III. COOPERATIVE MERGING CONTROL STRATEGY DESIGN`。
- 实验设计：需要复现 FPM-FCBF vs PPM-CBF / PPM-OC、single TCG、multi-HDV 或 multi-CAV 场景时，回查 `IV. SIMULATION RESULTS AND DISCUSSION`。
- baseline 复现：需要参数、fuel model、0.1 s sampling time、400 m acceleration lane 或 QP 求解时间时，回查 `TABLE II`、`TABLE III`、`Case A` 和 `Case B`。
- 写作：需要论证 fixed merging point 在 mixed traffic 下会错过 transient optimal opportunity 时，回查 `I. INTRODUCTION`。
- citation audit：需要核对 DOI、TITS 发表信息、PMP/CBF/CLF 引用链和 related work 时，回查开头元数据与 `REFERENCES`。

## 11. 关键原文位置

- 题名、作者、摘要、DOI、关键词：开头、`Abstract`、`Index Terms`。
- mixed traffic、PPM/FPM 对比和研究 gap：`I. INTRODUCTION`。
- TCG、车辆动力学、安全约束和整体 OCP：`II. PROBLEM FORMULATION AND CONTROL FRAMEWORK`。
- 上层 expected merging position planning：`III-A. Upper-Level Merging Position Planning`。
- FCBF、time-varying headway 和 CBF/CLF-QP：`III-B. Lower-Level Safe Optimal Control`。
- 单 TCG 对比实验和核心百分比结果：`IV-A. Case A: Single TCG`。
- 多车 mixed traffic 和 multi-CAV 结果：`IV-B. Case B: Multiple Merging Vehicles`。
- 局限与未来工作：`V. CONCLUSION`。
