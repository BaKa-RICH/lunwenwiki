---
type: concept
last_updated: 2026-04-28
source_pages: [wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging.md]
confidence: medium
---

# Integrated MINLP Merging Sequence and Trajectory

## 1. 概念定义

`EXTRACTED` P007 的 integrated approach 将 CAV 合流中的 merge-in gap 选择、合流序列、终端时间和连续轨迹统一为 MINLP，而不是先用 FIFO/MCTS 等方法确定序列再单独规划轨迹。

## 2. 核心机制

```text
RSU 触发一个 CAV batch
-> 对每辆匝道车枚举可选 merge-in gap
-> 每个候选 gap 下同时优化主线/匝道车辆连续轨迹
-> 轨迹成本反过来决定最优 gap / sequence
-> Bézier convex hull 保证任意时刻速度、加速度和车距约束
-> 基于最优性必要条件逐个确定匝道车 gap，降低搜索空间
```

## 3. 关键变量

- Binary merge-in gap vector `gamma_i`。
- Terminal time `t_f`。
- Cubic polynomial trajectory parameter `theta`。
- Cooperation zone length, desired terminal speed, minimum time gap, vehicle length and buffer distance。
- Mainline/on-ramp delay weights `w_m`, `w_r`。

## 4. 对本研究的启发

- `INFERRED` 该机制给“实时但优于 FIFO 的排序”提供了强参照：排序不应只看几何先后，也应看候选序列诱导出的轨迹质量。
- `INFERRED` Bézier / Bernstein continuous-time constraint 是补足离散规划安全漏洞的一条路线，可与 CBF safety layer 形成对比。
- `INFERRED` 多匝道车共享一个主线 gap 的设定，可能启发 dual-lane ramp 或 platoon-level merging sequencing。

## 5. 相关页面

- [[wiki/papers/P007-2024-Chen-Integrated-Approach-Optimal-Merging]]
- [[wiki/concepts/flexible-merging-positions]]
- [[wiki/concepts/flexible-control-barrier-function-merging]]
- [[wiki/comparisons/merging-control-baselines]]
- [[wiki/gaps/open-questions]]
