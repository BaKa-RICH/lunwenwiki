---
type: concept
last_updated: 2026-04-29
source_pages: [wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control.md]
confidence: medium
---

# Consensus-Based Mixed-Traffic Merging

## 1. 概念定义

`EXTRACTED` P003 将混合交通合流转化为 virtual-platoon 下的运动规划问题，用考虑通信延迟的 decentralized consensus controller 调整 CAV 纵向运动，并分析 local stability 与 string stability。

## 2. 核心机制

```text
merging sequencing 给出 leader-follower 顺序
-> CAV 根据虚拟 platoon 识别前车和期望间距
-> consensus controller 使用周围车辆状态误差生成控制输入
-> 稳定性条件约束控制增益
-> 提升抗扰动、鲁棒性和交通流稳定性
```

## 3. 与其他路线的区别

- 相比 P001 的系统最优可变合流位置，P003 更强调固定合流点前的排序效率和 platoon stability。
- 相比 P002 的 APS/CUC 主线换道协作，P003 更强调 HDV stochasticity、通信延迟和控制器稳定性。

## 4. 对本研究的启发

- `INFERRED` 如果未来 idea 涉及 proof，P003 的稳定性条件可作为理论依据来源。
- `INFERRED` 只优化宏观效率指标不够，扰动是否被放大可能是合流控制方法能否成立的关键机制。

## 5. 相关页面

- [[wiki/papers/P003-2025-Jing-Hierarchical-Cooperative-Merging-Control]]
- [[wiki/concepts/mixed-traffic-multilane-cormc]]
- [[wiki/gaps/open-questions]]
