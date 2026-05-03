---
type: paper
paper_id: P0016
title: "HCOMC: A Hierarchical Cooperative On-Ramp Merging Control Framework in Mixed Traffic Environment on Two-Lane Highways"
authors: "Tianyi Wang, Yangyang Wang, Jie Pan, Junfeng Jiao, Christian Claudel"
year: 2025
venue: "IEEE"
status: read
confidence: high
source_path: raw/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging.md
zotero_key:
doi:
tags: [CAV, HDV, mixed-traffic, HCOMC, two-lane-highway, virtual-vehicle, Stackelberg-game, NSGA-II, multi-objective-optimization]
last_updated: 2026-04-29
---

# P0016: HCOMC for Two-Lane Mixed-Traffic On-Ramp Merging

## 1. 一句话定位

这篇论文提出 HCOMC 分层协同合流框架，在两车道 mixed traffic 中结合改进 virtual vehicle、Stackelberg discretionary lane-changing game 和 NSGA-II 多目标优化，以决定匝道车合流位置/轨迹与主线协作车的纵向或横向协作模式。

## 2. 核心贡献

- `EXTRACTED` 构建 HDV/CAV 异质交通模型：HDV longitudinal IDM 加入反应时间和估计误差，CAV longitudinal IDM 融合 constant acceleration heuristic。
- `EXTRACTED` 使用 quintic polynomial curve 描述 HDV/CAV lateral lane-changing trajectories，并让 CAV lane-changing time 由 HCOMC 动态决定。
- `EXTRACTED` 提出 HCOMC 框架，包括 hierarchical cooperative planning、discretionary lane-changing decision 和 multi-objective optimization 三部分。
- `EXTRACTED` 在 cooperative planning 中使用改进 virtual vehicle model，分别处理 VR 在 Lane 1 的纵向合流协作和 VMC 到 Lane 2 的横向协作。
- `EXTRACTED` 用 Stackelberg game + Harsanyi transformation 建模 discretionary lane-changing 中 SV/FV 的交互。
- `EXTRACTED` 用 NSGA-II 优化 safety、fuel economy 和 efficiency，并从 Pareto set 中选取唯一方案。

## 3. 方法抓手

- Six-key-vehicle scenario：VR、VMC、VMF、VMR、VNF、VNR 表示 ramp、Lane 1 和 Lane 2 的关键交互车辆。
- Collision detection：用 quick rejection test 和 straddle test 快速判断 rear-end / side-impact collision risk。
- First-order longitudinal cooperation：当 VMC 纵向协作时，用 Lane 1 virtual vehicle 将 VR 映射到 mainline trajectory。
- Second-order lateral cooperation：当 VMC 横向协作时，用 Lane 2 virtual vehicle 规划 VMC 换道到 Lane 2，为 VR 释放 Lane 1 空间。
- Smooth lane-changing transition：用 hyperbolic tangent transition function 平滑 VMC 换道导致的 IDM leading vehicle 跳变。
- Optimization objectives：critical acceleration 代表 safety，fuel consumption 代表 economy，acceleration incentive model 代表 efficiency。
- Solution rule：若 `U_safe > 4` 优先选择最小 safety cost；否则对 efficiency 和 fuel economy 归一化求和选唯一解。

## 4. 关键实验结论

- `EXTRACTED` NSGA-II 与 PSO、SA 对比，几乎在所有工况下综合表现更优，尤其在 longitudinal cooperation mode 下优势明显。
- `EXTRACTED` Condition 1 / 3 中，NSGA-II 相比 PSO/SA 在 group vehicle safety 上分别约提升 5% 左右。
- `EXTRACTED` HCOMC 在所有工况下均提高 group vehicle safety；相比 FIFO 和 game theory，critical distance 平均提高 9.11% 和 5.13%。
- `EXTRACTED` Condition 2 中，HCOMC 采用 lateral cooperation，使 critical distance 最大提升率超过 46%。
- `EXTRACTED` Condition 2 中，HCOMC 相比 FIFO 和 game theory 将 merging stabilization time 缩短 54.79% 和 53.53%。
- `EXTRACTED` HCOMC 在不同 CAV penetration rates 下保持 superiority and stable，表明对 penetration 变化有一定鲁棒性。
- `EXTRACTED` HCOMC 的 fuel consumption 在多数工况优于 FIFO/game，但 Condition 2 因 VMC 额外 lateral cooperation 导致燃耗略高。

## 5. 局限与隐含假设

- 论文自述局限：
  - 结论中主要说明 HCOMC 的仿真有效性，未详细展开真实部署、通信延迟或 field validation。
- 你识别到的隐含假设：
  - 场景围绕六辆关键车，尚未验证连续交通流、大规模多车队或多匝道网络。
  - HDV 行为仍由改进 IDM + 反应/估计误差描述，未使用真实 human reaction 数据校准。
  - 虽然包含 lateral cooperation，但验证仍以仿真轨迹和指标为主，缺少 CarSim/vehicle dynamics 执行层。
  - Stackelberg game、NSGA-II 和多目标规则组合较复杂，实时性与参数敏感性未充分量化。
  - 通信延迟、packet loss、partial observability 和 perception noise 未作为扰动实验进入核心结果。

## 6. 关系线索

- complements: [[wiki/concepts/calibrated-gap-selection-lane-balance-control]]，P0015 用 vehicle bond / gap selection / lane balance，P0016 用 virtual vehicle + game + NSGA-II 处理两车道关键车协作。
- complements: [[wiki/concepts/integrated-longitudinal-lateral-dnmpc-merging]]，P0011 提供 vehicle dynamics execution，P0016 提供 higher-level longitudinal/lateral cooperation decision。
- contrasts: [[wiki/concepts/dual-module-ppo-heterogeneous-onramp-control]]，P0014 是 RL 双模块，P0016 是 model-based game + multi-objective optimization。
- uses: HCOMC two-lane mixed-traffic control paper-specific mechanism, modified virtual vehicle, Stackelberg game, Harsanyi transformation, NSGA-II, critical acceleration, LSRV, fuel consumption；原单篇 concept 已删除，核心信息保留在本 card、[[wiki/comparisons/merging-control-baselines]] 和 [[wiki/gaps/open-questions]]。
- suggests_gap: model-based integrated longitudinal/lateral cooperation 仍需真实 HDV reaction、delay robustness、执行层 tracking 和连续流验证。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P0016/`。

## 7. 对我研究的可能用途

- baseline: 可作为 two-lane mixed traffic 下的 model-based integrated cooperation baseline。
- mechanism_source: “VMC longitudinal cooperation vs lateral cooperation”是可解释的协作模式切换机制。
- proof_source: critical acceleration safety、Stackelberg game 和 Pareto selection 可作为多目标决策 proof 片段来源。
- experiment_design: Condition 1-5 提供 traffic density / CAV penetration / lane imbalance 的小规模对照模板。
- risk_source: 组合模型较复杂但真实扰动验证不足，提醒后续 idea 要解释实时性和 robustness。
- metric: critical distance、average acceleration、stabilization time、LSRV、fuel consumption、safety improvement、stability/rapidity。

## 8. 原文锚点

- raw: `raw/papers/P0016-2025-Wang-Hierarchical-Cooperative-On-Ramp-Merging.md`
- zotero:
- doi:
- keywords: HCOMC; mixed traffic; two-lane highways; cooperative on-ramp merging; NSGA-II.

## 9. 必要摘录

> `EXTRACTED` "This paper proposes a HCOMC framework, consisting of a hierarchical cooperative planning model based on the modified virtual vehicle model, a discretionary lane-changing model based on game theory, and a multi-objective optimization model"

> `EXTRACTED` "This paper modifies the longitudinal car-following models and lateral lane-changing models to capture the distinct driving characteristics of mixed traffic flow on two-lane highways."

> `EXTRACTED` "Compared to the FIFO model and the game theory model, the proposed HCOMC improves the critical distance by 9.11% and 5.13%, respectively."

> `EXTRACTED` "Under Condition 2 ... the maximum increase rate can reach over 46%."

> `EXTRACTED` "Under Condition 2 ... HCOMC model can shorten the time to stabilize after merging by 54.79% and 53.53%"

> `EXTRACTED` "Under Condition 2, the fuel consumption of the HCOMC is larger than that of the FIFO model and the game theory model, which is attributed to the additional lateral cooperation maneuvers of VMC."

## 10. 回查触发点

- proof：需要解释 modified virtual vehicle、hyperbolic tangent transition、Stackelberg lane-changing game 或 NSGA-II Pareto selection 时，回查 `III. Methodology`。
- 实验设计：需要复现 Condition 1-5、PSO/SA/NSGA-II 对比、FIFO/game/HCOMC 对比时，回查 `IV. Experiments`。
- baseline 复现：需要实现 heterogeneous IDM、quintic lane-changing、collision detection、critical acceleration、LSRV 或 fuel consumption 指标时，回查 `II. Problem Formulation` 和 `III.C`。
- 写作：需要论证“纵向协作和横向协作模式切换”在两车道 mixed traffic 中的价值时，回查 `III.A`、`III.B` 和实验 `Condition 2` 结果。
- citation audit：需要核对参考模型、作者、IEEE 会议/期刊元数据或 HCOMC 命名时，回查论文开头和 `References`。

## 11. 关键原文位置

- 题名、作者、摘要：开头。
- 研究动机、相关工作和贡献：`I. Introduction`。
- 两车道六车场景、HDV/CAV longitudinal/lateral model、collision detection：`II. Problem Formulation`。
- hierarchical cooperative planning：`III.A`。
- discretionary lane-changing game：`III.B`。
- multi-objective optimization and NSGA-II：`III.C`。
- 工况、PSO/SA/NSGA-II、FIFO/game/HCOMC 对比：`IV. Experiments`。
- safety、stability/rapidity、traffic efficiency、fuel consumption、discussion：`IV.A` 至 `IV.E`。
- 结论：`V. Conclusions`。
