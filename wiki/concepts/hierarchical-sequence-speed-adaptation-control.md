---
type: concept
last_updated: 2026-04-29
source_pages: [wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging.md]
confidence: high
---

# Hierarchical Sequence and Speed-Adaptation Control

## 1. 概念定义

`EXTRACTED` P0022 将 CAV 匝道合流中的战术决策定义为合流顺序 `f_r` 与 speed-adaptation time `t^p` 的联合优化；执行层再用 MPC 判断换道启动时间 `t^l` 并生成加速度轨迹。

## 2. 核心机制

```text
roadside tactical layer 收集 CAV 状态
-> 枚举/优化 on-ramp CAV 合流顺序 k
-> 同时选择 speed-adaptation time t^p
-> operational MPC 检查 command feasibility
-> 若可行，生成 desired acceleration 与 lane-changing initiation t^l
-> 若不可行，拒绝 tactical command 或选择 next gap fallback
```

## 3. 关键变量

- `f_r`：on-ramp CAV 合流后的车辆顺序。
- `t^p`：on-ramp CAV 开始适应速度和位置以准备进入 target gap 的时间。
- `t^l`：on-ramp CAV 实际开始横向换道的时间。
- `t_g`：随加速车道位置变化的 acceptable time gap。
- `T / T_p`：战术层和执行层 prediction horizon。
- Objective terms：gap error、relative speed、acceleration/control effort、terminal gap/relative speed error。

## 4. 对本研究的启发

- `INFERRED` 许多合流方法只优化“哪个 gap / 什么 sequence”，P0022 显示“何时开始调速进入该 gap”本身就是关键决策变量。
- `INFERRED` tactical layer 与 operational layer 模型可以不同，但需要显式 feasibility rejection 和 fallback，否则分层计划可能失效。
- `INFERRED` `t^p` 可与 P0020 的 VTS window、P0021 的 gap time-series 或 P006 的 safety filter 结合，形成 timing-aware sequence proposal。
- `INFERRED` 该机制目前仍是 pure CAV 小规模 baseline，迁移到 mixed traffic 时必须加入 HDV prediction、delay/noise 和横向执行验证。

## 5. 相关页面

- [[wiki/papers/P0022-2021-Chen-Hierarchical-Model-Based-Cooperative-Merging]]
- [[wiki/concepts/integrated-minlp-merging-sequence-trajectory]]
- [[wiki/concepts/vts-drl-ocp-onramp-merging]]
- [[wiki/concepts/dcoma-dynamic-cooperative-merging-assistant]]
- [[wiki/comparisons/merging-control-baselines]]
- [[wiki/gaps/open-questions]]
