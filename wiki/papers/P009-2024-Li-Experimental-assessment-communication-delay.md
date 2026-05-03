---
type: paper
paper_id: P009
title: "Experimental assessment of communication delay's impact on connected automated vehicle speed volatility and energy consumption"
authors: "Wan Li, Jackeline Rios-Torres, Boyu Wang, Zulqarnain H. Khattak"
year: 2024
venue: "Communications in Transportation Research"
status: read
confidence: high
source_path: raw/papers/P009-2024-Li-Experimental-assessment-communication-delay.md
zotero_key:
doi:
tags: [CAV, communication-delay, field-experiment, vehicle-in-the-loop, merging-control, energy-consumption, H-LSTM]
last_updated: 2026-04-28
---

# P009: Field Evidence on Communication Delay in CAV Merging

## 1. 一句话定位

这篇论文用 ACM Smart City Test Center 的 vehicle-in-the-loop 合流实验和 H-LSTM 模型，量化通信延迟对 CAV 速度波动与能耗的影响。

## 2. 核心贡献

- `EXTRACTED` 在真实 ACM 测试场和 VISSIM digital twin 中部署 CAV merging control algorithm，生成 vehicle-in-the-loop field experimental data。
- `EXTRACTED` 提出基于发送/接收消息时间戳与速度差阈值的 communication delay 估计与验证方法。
- `EXTRACTED` 用 Bollinger bands 和 K-means 将 CAV speed volatility 分成 high / low volatility 场景。
- `EXTRACTED` 构建 Hybrid LSTM（H-LSTM），同时建模 speed、acceleration、yaw rate、communication delay 的线性项和历史序列的非线性时间依赖。
- `EXTRACTED` 基于实测数据分析 delay、speed volatility 与 energy consumption 的关系，强调通信延迟对高速度波动下能耗影响更强。

## 3. 方法抓手

- Test bed：ACM 500-acre test track，DSRC、Drive-by-Wire、ROS、BSM，真实 CAV 与 VISSIM digital twin 中的虚拟车辆闭环交互。
- Merging controller：沿用 Rios-Torres / Malikopoulos closed-loop optimal merging，先计算 desired arrival time，再用 Hamiltonian closed-form control 最小化加速度平方。
- Delay estimation：用 transmission / receiving message pair 匹配，条件是时间差和速度差分别小于阈值 `epsilon_t`、`epsilon_v`。
- Speed volatility：用 Bollinger bands 计算速度波动，再用 K-means 分成 high-speed volatility 与 low-speed volatility。
- Energy model：H-LSTM 将当前 speed、delay、acceleration、yaw rate 作为线性因子，将历史序列交给 LSTM 捕获 temporal dependencies。

## 4. 关键实验结论

- `EXTRACTED` 4 天 field experiment 中完成 21 次测试运行，控制区 400 m、merge zone 100 m，包含 slow merging traffic 与 high traffic density 两类场景。
- `EXTRACTED` 估计得到平均 communication delay 为 0.06 s，标准差为 0.01 s。
- `EXTRACTED` closed-loop optimal merging control 相比 open-loop baseline 的平均单车能耗更低；open-loop 平均能耗 0.00036 kWh，比 closed-loop 0.00032 kWh 高 12.5%。
- `EXTRACTED` H-LSTM 的 MAPE 为 9.36%，优于 ARIMA、linear regression、partial least squares regression 和 2/3-layer LSTM。
- `EXTRACTED` speed volatility 估计中 delay 系数为 0.28；energy estimation 中 delay 系数在 high-speed volatility 下为 0.70，在 low-speed volatility 下为 0.63。
- `EXTRACTED` acceleration 是能耗最主要影响因子，high-speed volatility 下系数 1.44，low-speed volatility 下系数 1.16。

## 5. 局限与隐含假设

- 论文自述局限：
  - 需要更多 controlled analytical experiments，以建立因果关系而不仅是相关性。
  - communication delay 对 freeway platoon 的影响和不同 merging control algorithms 的性能差异仍需评估。
  - 原始 ACM 数据受 sponsor restrictions，derived data 需向作者合理请求，demo data 另有 GitHub。
- 你识别到的隐含假设：
  - vehicle-in-the-loop 中只有一辆真实 CAV，其余交通主要由 digital twin 虚拟车辆提供。
  - 分析重点是 speed volatility / energy consumption，不是完整安全性、吞吐或合流顺序性能。
  - delay 估计依赖 message pairing 阈值和速度一致性假设，仍可能受缺失数据与异步采样影响。
  - 结论中关于“delay 增加 0.01 s 可节省 0.007 kWh”的表述与“减少 delay 提升能效”的主张方向不一致，后续引用需回查原文语义。

## 6. 关系线索

- strengthens_gap: [[wiki/gaps/confirmed-gaps]] 中“完美通信假设不足”的证据，P009 给出 field data 而非仿真假设。
- extends: [[wiki/concepts/closed-form-optimal-merging]]，将 closed-loop optimal merging controller 放入真实 vehicle-in-the-loop 测试。
- complements: [[wiki/concepts/flexible-control-barrier-function-merging]] 和 [[wiki/concepts/consensus-based-mixed-traffic-merging]]，为通信延迟和能耗敏感性提供实证约束。
- uses: [[wiki/concepts/field-experimental-communication-delay-cav-merging]], ACM test track, digital twin, DSRC, H-LSTM, Bollinger bands, K-means。
- suggests_gap: 合流控制论文需要从“假设无延迟”转向 delay-aware design，并区分 delay 对安全、能耗、稳定性和控制算法的不同影响。
- asset_todo: 原始 MinerU 文件含多处外链图片，后续如需写作审计，应本地化到 `raw/assets/P009/`。

## 7. 对我研究的可能用途

- evidence: 可作为“完美通信假设过强”的强实证证据，支撑研究问题从理想 CAV 合流转向 delay-aware robust merging。
- baseline_context: 可用 closed-loop optimal merging field test 作为实车/车辆在环验证参照。
- metric_source: communication delay、speed volatility、energy consumption、H-LSTM MAPE、Bollinger band volatility、high/low volatility 分组。
- counterexample: 仿真中忽略 0.06 s 量级 delay 可能低估能耗和速度波动，尤其在高速度波动场景。
- caution: 当前证据更适合支撑 gap 和实验设计，不宜直接当作某个新控制算法的性能证明。

## 8. 原文锚点

- raw: `raw/papers/P009-2024-Li-Experimental-assessment-communication-delay.md`
- zotero:
- doi:
- keywords: Communication delay; Connected and autonomous vehicles; Merging control; Field experimental data; Vehicle-in-the-loop testing.
- demo data: `https://github.com/wanli3301114/Communication Delay.git`

## 9. 必要摘录

> `EXTRACTED` "To our knowledge, this is one of the first attempts at evaluating the impacts of communication delays on CAV merging operational control with field data."

> `EXTRACTED` "Based on field data, the average communication delay is 0.06 s and standard deviation is 0.01 s."

> `EXTRACTED` "the mean energy consumption per vehicle of the open-loop control is 12.5% higher ... compared to the closed-loop control."

> `EXTRACTED` "The coefficient of 0.28 in communication delay suggests that even modest delays in information transmission can lead to noticeable increase in speed volatility."

## 10. 回查触发点

- proof：需要论证 communication delay 影响速度波动、能耗或 temporal dependency 时，回查 `4. Methodology` 与 `5. Results and discussion`。
- 实验设计：需要设置 vehicle-in-the-loop、digital twin、ACM 场景、slow merging traffic / high traffic density、控制区和合流区长度时，回查 `3. Field experiment`。
- baseline 复现：需要复现 closed-loop optimal merging controller、arrival time 递推、Hamiltonian control law 或 open-loop/closed-loop 对比时，回查 `3.1. Optimal merging control algorithm` 与 `Fig. 7-8`。
- 写作：需要强调仿真无延迟假设与 field test 差距时，回查 `1. Introduction` 和 `2. Literature review`。
- citation audit：需要核对 venue、DOI、demo data、ACM/DSRC/ROS/BSM 细节时，回查开头元数据、`Replication and data sharing` 与 `References`。

## 11. 关键原文位置

- 题名、作者、摘要、关键词：开头、`A B S T R A C T`。
- 动机、通信延迟 gap 和贡献：`1. Introduction`。
- 仿真研究不足与 field test 价值：`2. Literature review`。
- 合流控制算法：`3.1. Optimal merging control algorithm`。
- ACM 测试场、digital twin 和 vehicle-in-the-loop：`3.2. ACM test track and vehicle-in-the-loop testing`。
- 场景设置与 21 次测试：`3.3. Experiment setup`。
- delay estimation、speed volatility、H-LSTM：`4. Methodology`。
- closed-loop 能耗、H-LSTM MAPE、delay 系数：`5. Results and discussion`。
- 局限与未来工作：`6. Conclusions`。
