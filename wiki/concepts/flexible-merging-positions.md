---
type: concept
last_updated: 2026-04-26
source_pages: [wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control.md]
confidence: medium
---

# Flexible Merging Positions

## 1. 概念定义

`EXTRACTED` 可变合流位置指匝道车辆不被限制在合流段末端的单一固定点并入主线，而是在合流段范围内选择更合适的合流位置。

## 2. 为什么重要

`INFERRED` 在合流控制中，固定合流点简化了优化模型，但也压缩了可行解空间。P001 的核心证据是：合流位置可变时，匝道车能更早或更晚利用可接受间隙，主线车也有更多方式形成间隙，从而减少等待、低速滞留和 traffic voids。

## 3. 机制链

```text
更大的合流位置选择空间
-> 更灵活的 gap assignment 和 merging sequence
-> 匝道车更少在固定点前低速等待
-> 主线车更少被迫急减速创造固定点间隙
-> 延误下降、轨迹更平滑、输出流更紧凑
```

## 4. 关键限制

- `EXTRACTED` 当匝道流量占比很高时，部分车辆可能在合流段前部以较低速度并入，仍会对主线速度产生明显影响。
- `EXTRACTED` 合流段过短会削弱可变合流位置的收益。
- `EXTRACTED` 较大的安全合流附加时距 `beta` 会减少可用合流机会并增加延误。

## 5. 相关页面

- [[wiki/papers/P001-2022-Tang-A-novel-hierarchical-cooperative-merging-control]]
- [[wiki/field/field-map]]
- [[wiki/gaps/open-questions]]
