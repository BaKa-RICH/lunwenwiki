---
type: concept
last_updated: 2026-04-26
source_pages: [wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging.md]
confidence: high
---

# Closed-Form Optimal Merging

## 1. 概念定义

`EXTRACTED` P005 的 closed-form optimal merging 指在 CAV 合流控制中，将每辆车的纵向控制表述为最优控制问题，并通过 Hamiltonian analysis 得到可在线计算的解析加速度轨迹。

## 2. 核心机制

```text
车辆进入 control zone 后进入 FIFO 队列
-> 控制器递归指定每辆车进入/离开 merging zone 的安全时间
-> 每辆车单独求解最小控制输入平方的 optimal control
-> Hamiltonian 给出 u*(t)=a t + b 的闭式解
-> 减少加减速波动、燃耗和旅行时间
```

## 3. 关键限制

- `EXTRACTED` 如果车辆进入控制区时已有速度/控制约束激活，闭式 unconstrained 解不一定可行。
- `EXTRACTED` 高速场景可能需要很长 control zone 才能满足安全约束。
- `INFERRED` FIFO 顺序和合流区单车占用简化了问题，但限制了解空间和容量。

## 4. 对本研究的启发

- P005 可作为最经典的解析型 baseline，用于支撑“为什么后续方法需要可变合流位置、多车道、多目标和混合交通”。
- 对 proof 有价值：它把燃耗优化、碰撞约束和在线控制之间的关系讲得很清楚。

## 5. 相关页面

- [[wiki/papers/P005-2017-Rios-Torres-Automated-Cooperative-Merging]]
- [[wiki/concepts/flexible-merging-positions]]
- [[wiki/field/field-map]]
