---
type: paper
paper_id: P0021
title: "DCoMA: A dynamic coordinative merging assistant strategy for on-ramp vehicles with mixed traffic conditions"
authors: "Linheng Li, Chen Qian, Jing Gan, Dapeng Zhang, Xu Qu, Feng Xiao, Bin Ran"
year: 2024
venue: "Transportation Research"
status: read
confidence: high
source_path: raw/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant.md
zotero_key:
doi:
tags: [CAV, HDV, mixed-traffic, DCoMA, on-ramp-merging, fundamental-diagram, gap-creation, platoon-formation, ramp-metering, emissions]
last_updated: 2026-04-29
---

# P0021: DCoMA Dynamic Coordinative Merging Assistant

## 1. 一句话定位

这篇论文提出 DCoMA，把宏观交通流基本图驱动的主线 platoon/gap creation 与匝道车辆微观速度规划结合起来，在 mixed traffic 中根据主线和匝道需求动态调整可合流 gap。

## 2. 核心贡献

- `EXTRACTED` 指出传统 micro-level cooperative merging 往往只优化局部车辆，忽略高流量下 shockwave 和 on-ramp queue；传统 macro-level RM/VSL 又缺少个体车辆控制粒度。
- `EXTRACTED` 提出 DCoMA：利用 mainline/on-ramp 实时流量和 FD 计算目标交通状态 C，使主线车辆形成 platoon，从而周期性创造 gap。
- `EXTRACTED` 将主线 platoon 占用时空区类比为 red phase，将 platoon 间 gap 类比为 green phase，并转成 time-series 发送给匝道车辆。
- `EXTRACTED` 在 mixed traffic 中只向 CAV 发送控制指令，通过 CAV deceleration 间接影响 HDV 分布和 gap 形成。
- `EXTRACTED` 在匝道侧用能耗/舒适性目标进行 motion planning，使车辆尽量不停驶入 gap。
- `EXTRACTED` 与 ALINEA、X-ALINEA/Q、CoopMA 对比，评估效率、安全和环境性能。

## 3. 方法抓手

- Macro desired state：用 FD 描述 state A 到 state C 的转换；state C 具有更高密度、更短 headway，从而在 platoon 之间形成 state O gap。
- Dynamic `v_C` resolve：根据 on-ramp flow、mainline state A、minimum merge headway 和最小有效 platoon 条件，动态求解目标状态 C 的速度 `v_C`。
- Platoon optimization：将 Detection area B2 中 CAV/HDV 分布编码为 binary string，只选择 CAV 为 cooperative vehicle，用类遗传算法最小化 mainline/ramp total delay。
- Cycle planning：计算 cooperative vehicle 到达合流点时间、gap 到达时间和 cycle end time，将主线 gap/platoon 时空信息转换为匝道可用时间序列。
- Ramp motion planning：根据 cycle data 决定匝道 CAV 到达合流点时间，再用 PMP/解析解生成兼顾 energy efficiency 与 comfort 的纵向速度轨迹。
- Evaluation dimensions：average travel time、speed spatio-temporal distribution、FD scatter、TTC/DRAC/conflict rate、fuel consumption。

## 4. 关键实验结论

- `EXTRACTED` 仿真使用 2000 m 上游主线、1250 m 下游、300 m 匝道和 250 m 加速车道；mainline flow 1000/1500/2000 veh/h，ramp flow 100-500 veh/h，MPR 30%/60%/100%。
- `EXTRACTED` DCoMA 会随 ramp flow 增加动态增加总 gap length；100% MPR 下，ramp flow 100 veh/h 时总 gap 约 84.6 s，500 veh/h 时增至 766.4 s，而 CoopMA 固定约 392 s。
- `EXTRACTED` 在 mainline 2000 veh/h、ramp 500 veh/h 时，DCoMA 相比 ALINEA、X-ALINEA/Q、CoopMA 的 total travel time 分别降低约 5.93%、5.68%、5.65%；on-ramp travel time 相比 ALINEA 降低 36.70%。
- `EXTRACTED` MPR 从 30% 增至 60% 时，overall 和 on-ramp travel times 在相同流量下下降，说明更高 CAV 比例提升策略效果。
- `EXTRACTED` safety analysis 中，DCoMA 在 DRAC、TTC 和 conflict rate 上整体优于其他策略，尤其高 on-ramp flow 时能保持较高 TTC 和较低冲突率。
- `EXTRACTED` 环境性能方面，DCoMA overall fuel consumption 相比 CoopMA、ALINEA、X-ALINEA/Q 分别降低 66.51%、61.27%、62.84%；on-ramp fuel consumption 分别降低 80.01%、77.29%、78.37%。
- `EXTRACTED` DCoMA 对 mainline fuel consumption 反而高于其他策略，因为主线车辆需要为 gap creation 减速，体现 mainline/ramp/environment 之间的权衡。

## 5. 局限与隐含假设

- 论文自述局限：
  - 当前研究场景是 single-lane highway，未来应引入 multi-lane 和 active lane-changing。
  - DCoMA 通过 CAV 间接控制 HDV，低 MPR 下效果变弱，更适合 MPR 高于 60% 的环境。
  - 依赖 IDM-derived FD，较理想化；未来需要用真实数据构建 FD，以捕捉随机驾驶行为。
- 你识别到的隐含假设：
  - 明确假设 communication delays negligible，和 GAP-0004 的 delay robustness 需求冲突。
  - 假设 created gap 被保护，除匝道车辆外其他车辆不能换道进入 gap，现实 mixed traffic 中可能较难保证。
  - 只研究 free-flow scenario，拥堵状态下需要其他控制先恢复自由流。
  - HDV 行为由 Krauss/LC2013 等仿真模型表达，缺少真实驾驶人对 gap 和 platoon 的反应验证。
  - 宏观 FD 与微观 SUMO/车辆控制之间的接口依赖标定，跨道路几何和驾驶文化泛化仍不确定。

## 6. 关系线索

- uses: [[wiki/concepts/dcoma-dynamic-cooperative-merging-assistant]], dynamic `v_C`, FD-based target state C, CAV binary distribution, platoon optimization, gap time-series, ramp PMP motion planning。
- extends: [[wiki/concepts/flow-level-multilane-comc]]，P0012 用 flow-level CoMC 周期性创造 gap；P0021 用 DCoMA 将 gap size 动态适配 ramp/mainline flow，并显式比较 ALINEA/X-ALINEA/Q/CoopMA。
- complements: [[wiki/papers/P0018-2025-Liu-Hierarchical-Cooperative-Constrained-Control]]，P0018 偏 multi-lane mixed traffic tactical MILP，P0021 偏 macro FD + micro speed planning 的 single-lane dynamic demand。
- complements: [[wiki/concepts/cav-mixed-traffic-impact-review]]，P0019 的 efficiency/safety/environment 多目标框架在 P0021 得到更具体的合流实验指标。
- contrasts: [[wiki/concepts/vts-drl-ocp-onramp-merging]]，P0020 用 VTS-DRL 学习合流窗口，P0021 用 FD 和动态流量显式计算 gap time series。
- suggests_gap: macro-micro gap creation 需要进一步加入真实 FD、通信延迟、非保护 gap、拥堵状态和 multi-lane lane-changing。
- asset_todo: 原始 MinerU 文件含大量外链图片，后续如需写作审计，应本地化到 `raw/assets/P0021/`。

## 7. 对我研究的可能用途

- baseline: 可作为 dynamic demand-aware macro-micro gap creation baseline，尤其适合对比固定 gap / 固定 signal / fixed platoon 方法。
- mechanism_source: “platoon = red phase, gap = green phase”的时空序列化机制可与 VTS、CBF 或 DNMPC 结合。
- experiment_design: 可复用 mainline/ramp flow sweep、MPR sweep、platoon intensity、ALINEA/X-ALINEA/Q/CoopMA baselines、TTC/DRAC/fuel 多指标。
- proof_source: FD-derived `v_C` 和 headway/gap equations 可作为流级 gap creation 的机制推导片段。
- risk_source: 主线 fuel/efficiency sacrifice 与匝道收益之间存在权衡，后续 idea 需要明确公平性或权重选择。
- metric: total/average gap length、average travel time、speed contour、FD scatter、TTC、DRAC、conflict rate、fuel consumption。

## 8. 原文锚点

- raw: `raw/papers/P0021-2024-Li-DCoMA-Dynamic-Coordinative-Merging-Assistant.md`
- zotero:
- doi:
- keywords: cooperative merging control; connected and autonomous vehicles; on-ramp metering; mixed traffic flow.

## 9. 必要摘录

> `EXTRACTED` "we innovatively introduce the Dynamic Cooperative Merging Assistance (DCoMA) strategy, a traffic management approach designed to enhance merging operations under variable traffic demands."

> `EXTRACTED` "The algorithm adaptively adjusts the size of platoons based on the volumes of both the mainline and the on-ramp."

> `EXTRACTED` "The spatio-temporal dynamics of these platoons function as the 'red phase' of traffic signals, with the intervals between platoons analogous to the 'green phase'."

> `EXTRACTED` "Communication delays are considered negligible due to the advancement in 5G communication technologies"

> `EXTRACTED` "DCoMA achieves travel time reductions of 5.93% (ALINEA), 5.68% (X-ALINEA/Q), and 5.65% (CoopMA)."

> `EXTRACTED` "DCoMA strategy reduces fuel consumption by 80.01% (CoopMA), 77.29% (ALINEA), and 78.37% (X-ALINEA/Q)"

## 10. 回查触发点

- proof：需要解释 FD state A/C/O、动态 `v_C`、gap duration 或 mainline/ramp delay objective 时，回查 `3.1` 和 `3.2`。
- 实验设计：需要复现 ALINEA/X-ALINEA/Q/CoopMA/DCoMA 对比、MPR/PI/flow sweep 或 fuel/TTC/DRAC 指标时，回查 `4` 与 `5`。
- baseline 复现：需要实现 Detection areas、CAV binary platoon optimization、cycle planning 或 ramp motion planning 解析解时，回查 `3.2` 至 `3.4`。
- 写作：需要论证“宏观流级 gap creation 与微观车辆控制必须统一”时，回查 `1 Introduction`、`3 DCoMA` 和 `6 Conclusions`。
- citation audit：需要核对 CoopMA、ALINEA、X-ALINEA/Q 参数或 DCoMA 命名时，回查 `4.1`、Tables 2-4 和 References。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头。
- macro/micro gap 与贡献：`1 Introduction`。
- assumptions、通信、free-flow 和 protected gap：`2 Optimization objectives and assumptions`。
- DCoMA 信息流、desired state C、platoon optimization、cycle planning、ramp motion planning：`3`。
- SUMO 仿真设计、MPR/flow/PI、baseline 参数：`4.1`。
- gap length、travel time、speed distribution、FD、vehicle trajectory：`4.2` 至 `4.3`。
- efficiency/safety/environment results：`5`。
- 自述局限：`6 Conclusions and future work`。
