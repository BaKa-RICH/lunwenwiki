---
type: paper
paper_id: P005
title: "Automated and Cooperative Vehicle Merging at Highway On-Ramps"
authors: "Jackeline Rios-Torres, Andreas A. Malikopoulos"
year: 2017
venue: "IEEE Transactions on Intelligent Transportation Systems"
status: read
confidence: high
source_path: raw/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging.md
zotero_key:
doi: 10.1109/TITS.2016.2587582
tags: [CAV, cooperative-merging, optimal-control, Hamiltonian, closed-form, fuel-consumption]
last_updated: 2026-04-26
---

# P005: Closed-Form Optimal Cooperative Merging

## 1. 一句话定位

这篇论文是 CAV on-ramp cooperative merging 的经典优化基线：在单主路 + 单匝道合流区中，用集中式 FIFO 队列和 Hamiltonian 分析推导在线闭式最优控制，以降低燃耗和旅行时间并满足碰撞约束。

## 2. 核心贡献

- `EXTRACTED` 将 CAV 合流道路协调问题表述为 optimal control problem，目标包括最小化控制输入平方和缩小车辆进入合流区的时间间隔。
- `EXTRACTED` 在 rear-end collision 和 lateral collision 约束下，通过递归定义车辆离开合流区时间，保证同路和异路车辆安全。
- `EXTRACTED` 用 Hamiltonian analysis 推导闭式解，使每辆车在线计算最优加速度/减速度。
- `EXTRACTED` 用 MATLAB 仿真展示相对“主路优先、匝道停车等待”基线的燃耗和旅行时间改善。

## 3. 方法抓手

- FIFO queue：车辆进入 control zone 后由集中式控制器赋予唯一编号，编号对应进入控制区的 FIFO 顺序。
- 安全约束：同一路车辆保持最小安全距离 `delta`；不同道路车辆避免同时占用 merging zone。
- 燃耗目标：用 polynomial metamodel 表示燃耗，核心上通过最小化加速度平方减少 transient engine operation。
- 闭式控制：最优控制输入为时间的一次函数 `u_i*(t)=a_i t + b_i`，速度和位置分别为二次和三次函数。

## 4. 关键实验结论

- `EXTRACTED` MATLAB 仿真中 control zone 长度为 400 m，merging zone 长度为 30 m，初始默认速度为 13.4 m/s。
- `EXTRACTED` case study 包括 4 车协调、30 车协调、主/匝道不同初始速度、以及 29 m/s 高速进入控制区场景。
- `EXTRACTED` 相比主路优先、匝道车停车等待的 baseline，case study 2 燃耗改善 52.7%，旅行时间改善 7.1%；case study 3 燃耗改善 48.1%，旅行时间改善 13.5%。
- `EXTRACTED` 在 29 m/s 场景中，原控制区长度和速度限制下无法满足安全约束，需将控制区增至 1200 m，暴露该方法的应用边界。

## 5. 局限与隐含假设

- 论文自述局限：
  - 主要求解 unconstrained optimal control；若车辆进入控制区时已有约束激活，需要额外分析。
  - 未来需要更复杂交通仿真模型、更高级车辆模型、车辆多样性，以及燃耗与拥堵之间的 trade-off。
  - 高速进入控制区时可能需要过长控制区或更高速度限制，存在现实可行性问题。
- 你识别到的隐含假设：
  - 单主路 + 单匝道、纯 CAV、集中式控制器、FIFO 顺序。
  - 合流区同一时刻只允许一辆车占用，长合流区时可能浪费容量。
  - 车辆被点质量二阶动力学近似，横向运动和 lane-changing 细节基本不建模。

## 6. 关系线索

- extends: 早期自动合流、virtual platoon 和集中式优化控制路线。
- contrasts: 后续 P001 的可变合流位置、P002/P003 的 mixed traffic、P004 的多车道和双匝道几何。
- uses: [[wiki/concepts/closed-form-optimal-merging]], FIFO, Hamiltonian analysis, fuel consumption metamodel, collision constraints。
- suggests_gap: 固定 FIFO 顺序、单车占用合流区、unconstrained arcs、控制区长度可行性、车辆异质性与混合交通。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P005/`。

## 7. 对我研究的可能用途

- baseline: 可作为经典 closed-form optimal control baseline，尤其适合说明早期方法如何处理燃耗和安全约束。
- idea_source: 可启发把“可解析控制 + 递归安全时间约束”作为轻量 proof 或实验 baseline。
- counterexample: 高速场景需要 1200 m 控制区，说明闭式最优并不自动等于现实可部署。
- dataset_or_metric: fuel consumption、travel time、control zone length、merging zone length、safety feasibility。
- assumption: 纯 CAV、单车道合流、集中式 FIFO、无通信延迟、二阶动力学、合流区单车占用。

## 8. 原文锚点

- raw: `raw/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging.md`
- zotero:
- doi: 10.1109/TITS.2016.2587582
- keywords: Connected and automated vehicles; cooperative driving; cooperative merging control; highway on-ramps; merging highways; vehicle coordination.

## 9. 必要摘录

> `EXTRACTED` The paper formulates optimal vehicle coordination at merging roadways in terms of fuel consumption under the hard constraint of collision avoidance.

> `EXTRACTED` The optimal control input is given by `u_i*(t)=a_i t + b_i`, allowing online closed-form coordination.

> `EXTRACTED` Optimal vehicle coordination improves overall fuel consumption by 52.7% and 48.1% in case studies 2 and 3, respectively, compared to the baseline scenario.

## 10. 回查触发点

- proof：需要推导闭式最优控制、Hamiltonian 条件或燃耗目标时，回查 `II. PROBLEM FORMULATION`、`III. ANALYTICAL SOLUTION`、`B. Hamiltonian Analysis`。
- 实验设计：需要设置经典单主路单匝道 baseline、control zone / merging zone 长度、主路优先 baseline、燃耗和旅行时间指标时，回查 `IV. SIMULATION RESULTS`。
- baseline 复现：需要复现 FIFO queue、递归安全时间约束、4 车/30 车 case study 或 29 m/s 可行性边界时，回查 `A. Vehicle Coordination`、`A-D. Case Study`、`E. Case Study 4`。
- 写作：需要介绍早期 CAV merging closed-form optimal control、燃耗优化和经典局限时，回查 `I. INTRODUCTION`、`C. Contribution of the Paper`、`V. CONCLUDING REMARKS`。
- citation audit：需要核对 DOI、IEEE TITS 元数据、燃耗模型和早期 merging control 文献链时，回查 `REFERENCES`；具体页码需回 raw 或 Zotero 核查。

## 11. 关键原文位置

- 论文题名、作者、DOI、摘要、关键词：开头、`Abstract`、`Index Terms`。
- 研究动机和 related work：`I. INTRODUCTION`、`A. Motivation`、`B. Literature Review`。
- 贡献：`C. Contribution of the Paper`。
- 建模框架、车辆动力学和优化问题：`II. PROBLEM FORMULATION`、`A. Modeling Framework`、`B. Optimization Problem Formulation`。
- 车辆协调和安全时间递归：`III. ANALYTICAL SOLUTION`、`A. Vehicle Coordination`。
- Hamiltonian 闭式解：`B. Hamiltonian Analysis`。
- 仿真实验与基线：`IV. SIMULATION RESULTS`。
- 4 车、30 车、不同初始速度、高速可行性：`A-D. Case Study`、`E. Case Study 4`。
- 燃耗和旅行时间结果：`D. Fuel Consumption and Travel Time Results`。
- 局限与 future work：`V. CONCLUDING REMARKS`。
