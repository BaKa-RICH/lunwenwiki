---
type: paper
paper_id: P001
title: "A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization"
authors: "Zhixian Tang, Hong Zhu, Xin Zhang, Miho Iryo-Asano, Hideki Nakamura"
year: 2022
venue: "Transportation Research Part C: Emerging Technologies"
status: read
confidence: medium
source_path: raw/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control.md
zotero_key:
doi:
tags: [CAV, on-ramp-merging, cooperative-merging-control, flexible-merging-position, MCTS]
last_updated: 2026-04-26
---

# P001: Flexible-Position Hierarchical Cooperative Merging Control

## 1. 一句话定位

这篇论文提出 CMC-FMP：在纯 CAV、单主线单匝道合流瓶颈中，把传统 system-optimal cooperative merging control 的固定合流点扩展为可变合流位置，并用“上层战术规划 + 下层运动规划 + MCTS 分解”控制计算复杂度。

## 2. 核心贡献

- `EXTRACTED` 提出分层系统最优合流控制：上层 tactical planning 同时优化合流顺序和关键状态，下层 motion planning 生成可执行轨迹和下一步动作。
- `EXTRACTED` 用 MCTS-based decomposition algorithm 近似求解非凸 MIQCP，报告相对直接求解的优化 gap 多数低于 5%，且低于 10%。
- `EXTRACTED` 相比固定合流点 CMC-SMP，CMC-FMP 在多种需求水平和主线/匝道流量占比下显著降低平均延误，最高报告整体延误降低 64%。

## 3. 方法抓手

- 可变合流位置：匝道车不必在合流段末端固定点并入，而是在合流段内选择更合适的合流位置。
- 关键状态建模：不一次性优化所有完整轨迹，而优化进入合流段、执行合流、被切入、离开控制区等关键状态，再连接成轨迹。
- 运动规划：优先用最小速度波动的 optimal control 连接关键状态，若违反安全车头距约束，则启用 modified Newell car-following model。
- 实时化思路：战术层用 MCTS-DA 分解求解，运动层每 0.5s 快速更新；另提出 batch-based scheme 作为在线控制实现方式。

## 4. 关键实验结论

- `EXTRACTED` 仿真平台为 SUMO 1.7.0 + MATLAB + Gurobi 9.1，场景是单车道主线与单车道匝道，控制区覆盖合流段及上下游。
- `EXTRACTED` CMC-FMP 与同结构但固定合流点的 CMC-SMP 对比，测试 1200/1400/1600/1800 veh/h 和 20-80、35-65、50-50 三种流量占比。
- `EXTRACTED` 在高需求场景中，CMC-FMP 对匝道车辆延误改善尤其明显；整体合流瓶颈延误改善范围可达 26%-64%。
- `EXTRACTED` 安全合流附加时距 `beta` 增大会降低输出流量并增加延误；合流段越短，CMC-FMP 的可用解空间越小，效率越差。

## 5. 局限与隐含假设

- 论文自述局限：
  - 只优化总延误，未同时优化舒适性、排放等指标。
  - 战术层非凸、非线性约束仍带来求解困难，未来需要线性化。
  - 仅讨论单主线单匝道、纯 CAV、纵向控制场景。
  - 混合交通下 HDV 行为不可完全控制、部分可观测，统一合流控制框架仍是开放问题。
- 你识别到的隐含假设：
  - V2I 通信无延迟和丢包，控制中心掌握控制区内所有车辆状态与未来动作。
  - 车辆同质，且严格执行控制中心规划轨迹。
  - 安全性主要由车头距和紧急制动约束刻画，对扰动衰减能力考虑不足。

## 6. 关系线索

- extends: 固定合流点的 SO-CMC / CMC-SMP。
- contrasts: FIFO / virtual mapping / rule-based merging sequence；RL-based lane-changing controllers。
- uses: [[wiki/concepts/flexible-merging-positions]], optimal control, modified Newell car-following, MCTS, SUMO, Gurobi。
- suggests_gap: `wiki/gaps/open-questions.md` 中的混合交通、舒适性/排放多目标、扰动衰减和多车道扩展问题。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P001/`。

## 7. 对我研究的可能用途

- baseline: 可作为“可变合流位置 + 系统最优合流控制”的强优化型 baseline。
- idea_source: 可启发把合流位置、合流顺序和关键状态作为高层离散/连续联合决策变量。
- counterexample: 可反驳“固定合流点已经足够”的简单设定，尤其在低匝道占比、高需求场景下。
- dataset_or_metric: 延误、输出流量、主线速度轮廓、轨迹平滑性、time headway/traffic voids。
- assumption: 纯 CAV、单车道、完美通信、车辆同质、严格执行中心规划。

## 8. 原文锚点

- raw: `raw/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control.md`
- zotero:
- doi:
- keywords: Connected and automated vehicle; Merging bottleneck; System optimal cooperative merging control; Flexible merging positions; Monte Carlo tree search.

## 9. 必要摘录

> `EXTRACTED` Current SO-CMC models commonly assume a single fixed merging point to simplify model structures, but this limits the solution space and may underutilize the merging section.

> `EXTRACTED` CMC-FMP optimizes both merging sequence and critical states, then uses motion planning to connect those states into feasible trajectories.

> `EXTRACTED` The paper reports that CMC-FMP can reduce average delay compared with CMC-SMP, with the largest total delay reduction reaching 64% under 1800 veh/h and 20-80 split.

## 10. 回查触发点

- proof：需要论证“可变合流位置为什么能降低延误/traffic voids”时，回查 `3.1.2. Model framework`、`3.3. Tactical planning model`、`5.3.3. Trajectory maps`、`5.3.4. Time headway distribution (traffic voids)`。
- 实验设计：需要确定仿真场景、需求水平、流量占比、控制区长度、评价指标时，回查 `5.1. Simulation framework`、`5.3. Comparison between CMC-FMP and CMC-SMP`、`5.4. Sensitivity analysis`。
- baseline 复现：需要复现 CMC-FMP / CMC-SMP、MCTS-DA、batch-based scheme 或安全约束时，回查 `3.3. Tactical planning model`、`3.4. Motion planning model`、`4. Monte Carlo tree search-based decomposition algorithm`、`5.2. Computational efficiency and real-time application`、`Appendix B. Tactical planning model for CMC-SMP`。
- 写作：需要描述研究 gap、贡献、局限和 future work 时，回查 `1. Introduction`、`2. Literature review`、`6. Conclusions and future work`。
- citation audit：需要核对 fixed merging point、MCTS、modified Newell、SUMO/Gurobi、混合交通 future work 等引用链时，回查 `2. Literature review`、`5.1. Simulation framework`、`References`；具体 DOI 和 venue 元数据需回 raw 或 Zotero 核查。

## 11. 关键原文位置

- 论文题名、作者、关键词：`ARTICLEINFO`、`ABSTRACT`。
- 研究动机与贡献：`1. Introduction`。
- 相关工作与固定合流点 gap：`2. Literature review`。
- 问题设定、假设和整体框架：`3.1. Problem description and model framework`。
- 上层战术规划、合流顺序和关键状态：`3.3. Tactical planning model`、`3.3.1. Merging sequence`、`3.3.2. Critical states`。
- 下层运动规划、安全车头距和 modified Newell 模型：`3.4. Motion planning model`、`3.4.1. Optimal control model`、`3.4.2. Safe spacing requirement`、`3.4.3. Modified Newell's car-following model`。
- MCTS-DA 分解算法：`4. Monte Carlo tree search-based decomposition algorithm`、`4.1. Determining the next vehicle`、`4.2. Solving critical states`。
- 仿真设置和复现实验参数：`5.1. Simulation framework`。
- 计算效率、optimality gap 和实时 batch 方案：`5.2. Computational efficiency and real-time application`。
- 与 CMC-SMP 的对比结果：`5.3. Comparison between CMC-FMP and CMC-SMP`。
- 延误、速度轮廓、轨迹、traffic voids：`5.3.1. Average delay`、`5.3.2. Mainline speed contours`、`5.3.3. Trajectory maps`、`5.3.4. Time headway distribution (traffic voids)`。
- 参数敏感性：`5.4. Sensitivity analysis`、`5.4.1. Impacts of beta`、`5.4.2. Impacts of the merging section length`。
- 局限与 future work：`6. Conclusions and future work`。
- CMC-SMP 具体公式：`Appendix B. Tactical planning model for CMC-SMP`。
- DOI、期刊卷期、页码/文章号：需回 raw 核查或从 Zotero 核查。
