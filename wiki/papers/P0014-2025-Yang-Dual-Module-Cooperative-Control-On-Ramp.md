---
type: paper
paper_id: P0014
title: "A Dual-Module Cooperative Control Method for On-Ramp Area in Heterogeneous Traffic Flow Using Reinforcement Learning"
authors: "Wenzhang Yang, Changyin Dong, Ziqian Zhang, Xu Chen, Hao Wang"
year: 2025
venue: "Engineering Applications of Artificial Intelligence"
status: read
confidence: high
source_path: raw/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp.md
zotero_key:
doi:
tags: [CAV, HDV, heterogeneous-traffic, reinforcement-learning, PPO, dual-module-control, merging-control, lane-changing-control, TET]
last_updated: 2026-04-29
---

# P0014: Dual-Module PPO Control for Heterogeneous On-Ramp Traffic

## 1. 一句话定位

这篇论文提出面向 CAV-HDV 异质交通的双模块 RL 合流控制：用 PPO 同时学习 ramp/Lane 2 合流协作和主线 Lane 1/Lane 2 换道协作，在低 CAV 渗透率下也降低延误和 TET 风险。

## 2. 核心贡献

- `EXTRACTED` 提出 dual-module cooperative control method，包括 merging control module 和 lane-changing control module。
- `EXTRACTED` MC module 协调 Lane 2 与 ramp CAV，LC module 帮助 mainline CAV 做换道决策并协调 Lane 1 车辆。
- `EXTRACTED` 两个模块均使用 PPO agent，并将 agent action 与基础交通规则/车辆动力学约束结合，而不是直接执行无约束 RL 输出。
- `EXTRACTED` reward 同时包含 efficiency reward 和 safety penalty，其中 safety 使用 TTC / TET 相关指标覆盖前车、虚拟前车和虚拟后车冲突。
- `EXTRACTED` 做了 penetration rate、maximum speed、flow rate、flow rate ratio、control area length 等 transferability analysis。

## 3. 方法抓手

- 场景：一条 ramp、两条 mainline lanes；Lane 2 与 ramp 直接发生合流冲突，Lane 1 可吸收部分 Lane 2 车辆。
- MC state：subject vehicle、preceding vehicle、virtual preceding vehicle、virtual rear vehicle 的速度和距离信息。
- LC state：在 MC state 基础上加入 `U`，表示 Lane 1 与 Lane 2+ramp 平均速度是否触发 Lane 2 -> Lane 1 换道需求。
- Action：PPO 输出连续有界 acceleration，但最终加速度还要经过速度、加速度、TTC braking 等约束。
- HDV model：IDM car-following + 基于 cumulative dissatisfaction 的 lane-changing probability。
- Baseline：CAV 对照组使用 PATH CACC/ACC，lane-changing 行为与 HDV 规则一致。

## 4. 关键实验结论

- `EXTRACTED` 两个 PPO agents 在不同 CAV penetration 下均收敛，平均 reward 通常在 100-200 episodes 后稳定到峰值。
- `EXTRACTED` CAV penetration 为 0.2 时，dual-module control 相比 comparison group 平均车辆 delay 降低 26%。
- `EXTRACTED` CAV penetration 大于等于 0.3 时，TET reduction 约为 45%。
- `EXTRACTED` 分车道结果显示，Lane 1、Lane 2、ramp 平均 delay 分别降低 16.9%、24.9%、11.5%，Lane 2 获益最大。
- `EXTRACTED` 分车型结果显示，CAV delay 平均降低 22.7%，HDV delay 平均降低 15.9%；TET 对 CAV/HDV 均约降低 41%。
- `EXTRACTED` trajectory case 显示 dual-module control 可避免 40-60 s 高输入阶段的 Lane 2/ramp 合流冲突向上游与 Lane 1 蔓延。
- `EXTRACTED` transferability analysis 表明，在异质交通中建议用较高 CAV penetration rate 训练 agents，因为高渗透率训练的 agents 可迁移到低渗透率，反之较弱。

## 5. 局限与隐含假设

- 论文自述局限：
  - 未处理更高层的 vehicle right-of-way allocation。
  - 真实 CAV 协同控制面临技术、基础设施、法律和社会接受度挑战。
  - 当前主要依赖仿真，未来需通过 VR / driving simulator / enclosed field tests 逐步过渡到真实实验。
- 你识别到的隐含假设：
  - 控制中心可由路侧感知实时获取所有车辆速度和位置，并稳定下发 CAV 控制命令。
  - lane-change execution 被简化为满足条件后在某一时间步完成，重点是决策而非横向轨迹跟踪。
  - RL reward 由经验设计，缺少可证明 safety / stability guarantee。
  - HDV 行为由 IDM 与 lane-changing dissatisfaction 模型表示，真实驾驶风格、compliance 和 aggressive merging 未充分验证。
  - communication delay、packet loss 和网络安全只在局限中讨论，未进入实验扰动。

## 6. 关系线索

- complements: [[wiki/concepts/mixed-traffic-multilane-cormc]]，P002/P0014 都处理 mixed traffic + mainline lane-changing，但 P0014 用 RL 同时学习合流和换道控制。
- complements: [[wiki/concepts/flow-level-multilane-comc]]，P0012 做流级 gap/platoon 控制，P0014 做车辆级 RL 决策和异质交通低渗透率控制。
- contrasts: [[wiki/concepts/consensus-based-mixed-traffic-merging]]，P003 有稳定性 proof，P0014 有强仿真和 transferability，但理论可解释性较弱。
- uses: [[wiki/concepts/dual-module-ppo-heterogeneous-onramp-control]], PPO, MC module, LC module, TTC/TET reward, IDM, PATH CACC/ACC baseline。
- suggests_gap: RL 合流控制需要可解释 safety layer、真实通信/感知扰动测试和 lane-change execution 验证。
- asset_todo: 原始 MinerU 文件含大量外链图片，后续如需写作审计，应本地化到 `raw/assets/P0014/`。

## 7. 对我研究的可能用途

- baseline: 可作为 low-penetration heterogeneous traffic RL baseline，尤其适合和 P008 adaptive weighting、P0010 strategic influence 对比。
- idea_source: 双模块结构提示可把 ramp merging 与 mainline lane-changing 分开建模，再通过共享安全指标和规则层耦合。
- experiment_design: penetration transfer、speed transfer、flow transfer、control-area length transfer 是检验学习策略泛化性的有用模板。
- risk_source: 如果采用 RL，需要补足 safety guarantee、可解释性和真实执行层，否则容易被质疑只是仿真调参。
- metric: average delay、TET、lane-specific delay、CAV/HDV-specific delay、reward convergence、transferability across penetration / speed / flow。

## 8. 原文锚点

- raw: `raw/papers/P0014-2025-Yang-Dual-Module-Cooperative-Control-On-Ramp.md`
- zotero:
- doi:
- keywords: On-ramp; Reinforcement learning; Cooperative control; Heterogeneous traffic flow.

## 9. 必要摘录

> `EXTRACTED` "The approach comprises two key modules: the merging control module and the lane-changing control module."

> `EXTRACTED` "With a CAV penetration rate of just 0.2, average vehicle delay is reduced by 26%."

> `EXTRACTED` "when the CAV penetration rate reaches or exceeds 0.3, the time-exposed time-to-collision decreases by approximately 45%."

> `EXTRACTED` "Generally, after training for 100 to 200 episodes, the average reward stabilizes at a maximum level."

> `EXTRACTED` "agents trained in high penetration rate settings also excel in low penetration rate scenarios, whereas those trained under low penetration rate conditions struggle"

> `EXTRACTED` "the current research does not address higher-level vehicle right-of-way allocation"

## 10. 回查触发点

- proof：需要说明 PPO objective、action/state/reward 设计或为何 agent 输出还需规则约束时，回查 `3. Dual-module cooperative control method`。
- 实验设计：需要复现 400 training rounds、100 testing rounds、delay/TET、penetration sweep 或 transferability analysis 时，回查 `5. Results and discussions`。
- baseline 复现：需要实现 PATH CACC/ACC comparison group、IDM HDV、lane-changing dissatisfaction model 或 TTC lane-change restrictions 时，回查 `4. Simulation experimental design`。
- 写作：需要论证“合流控制 + 主线换道控制应联合考虑”时，回查 `1.3. Contribution and organization` 与 `5.4. Vehicle trajectory analysis`。
- citation audit：需要核对作者、期刊、关键词、PPO、PATH CACC/ACC 和 Yang 2023b gap selection 对比时，回查开头元数据和 `References`。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头、`A R T I C L E I N F O`、`A B S T R A C T`。
- 背景、文献综述和贡献：`1. Introduction`。
- on-ramp 场景和控制目标：`2. On-ramp scenario`。
- PPO、MC module、LC module：`3. Dual-module cooperative control method`。
- HDV car-following/lane-changing、车辆约束、baseline 和指标：`4. Simulation experimental design`。
- reward 收敛、典型仿真、分车道/车型、trajectory 和 transferability：`5. Results and discussions`。
- 结论、局限和 future works：`6. Conclusions, limitations and future works`。
