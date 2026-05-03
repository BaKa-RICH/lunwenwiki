---
type: concept
last_updated: 2026-04-28
source_pages: [wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay.md]
confidence: medium
---

# Field Experimental Communication Delay in CAV Merging

## 1. 概念定义

`EXTRACTED` P009 将 CAV 合流中的 communication delay 从仿真假设转为 vehicle-in-the-loop field data 问题，通过 ACM 测试场、digital twin 和 H-LSTM 量化 delay 对速度波动与能耗的影响。

## 2. 核心机制

```text
真实 CAV + VISSIM digital twin 闭环运行
-> controller 与 CAV 通过 BSM/ROS/DSRC 交换消息
-> transmission / receiving message pairing 估计 delay
-> Bollinger bands + K-means 划分速度波动场景
-> H-LSTM 建模 speed / acceleration / yaw rate / delay 与能耗
-> 比较 high / low speed volatility 下 delay 的边际影响
```

## 3. 关键变量

- Average communication delay and delay standard deviation。
- Speed volatility high / low cluster。
- Speed, acceleration, yaw rate。
- Energy consumption per vehicle。
- H-LSTM MAPE and linear term coefficients。

## 4. 对本研究的启发

- `INFERRED` P009 是 confirmed gap 的实证支撑：合流控制中的“无通信延迟”假设不只是理论简化，而会影响能耗和速度稳定。
- `INFERRED` delay 的影响与 speed volatility 交互，说明鲁棒性实验不应只扫 delay，还应扫扰动/速度波动状态。
- `INFERRED` field / vehicle-in-the-loop 证据可作为论文写作中的现实动机，但现阶段不应替代机制 proof。

## 5. 相关页面

- [[wiki/papers/P009-2024-Li-Experimental-assessment-communication-delay]]
- [[wiki/concepts/closed-form-optimal-merging]]
- [[wiki/concepts/consensus-based-mixed-traffic-merging]]
- [[wiki/gaps/confirmed-gaps]]
- [[wiki/gaps/open-questions]]
