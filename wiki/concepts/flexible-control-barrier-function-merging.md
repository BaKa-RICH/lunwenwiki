---
type: concept
last_updated: 2026-04-28
source_pages: [wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging.md]
confidence: medium
---

# Flexible Control Barrier Function Merging

## 1. 概念定义

`EXTRACTED` P006 的 FCBF 是在 receding horizon 合流控制中，把递归更新的 expected merging position 作为非状态变量嵌入 CBF，使 flexible merging position 能转化为连续安全约束的机制。

## 2. 核心机制

```text
上层 PMP 计算 candidate / expected merging position
-> expected merging position 决定 variable time headway
-> time headway 将安全合流距离从“合流时刻约束”变为连续约束
-> FCBF 将连续安全约束转为 QP 控制约束
-> 下层 CBF-CLF-QP 同时追求安全、速度恢复和能耗/控制 effort
```

## 3. 关键变量

- Expected merging position `L_m^exp`, `L_s^exp`。
- Variable time headway `Phi_l-m`, `Phi_m-s`。
- Safe merging distance constraint and car-following constraint。
- QP control variables：traction force and CLF slack variable。
- Receding horizon sampling time and HDV disturbance state。

## 4. 对本研究的启发

- `INFERRED` FCBF 是把“合流位置自由度”落到安全约束层的一个可复用接口，比只把合流位置作为上层优化变量更接近可验证机制。
- `INFERRED` 该机制适合与横向 tracking、communication delay 或 stability constraints 结合，但当前 P006 尚未证明这些扩展。

## 5. 相关页面

- [[wiki/papers/P006-2023-Liu-Safety-Critical-and-Flexible-Cooperative-Merging]]
- [[wiki/concepts/flexible-merging-positions]]
- [[wiki/concepts/consensus-based-mixed-traffic-merging]]
- [[wiki/comparisons/merging-control-baselines]]
- [[wiki/gaps/open-questions]]
