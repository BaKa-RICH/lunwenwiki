---
type: concept
last_updated: 2026-04-26
source_pages: [wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control.md]
confidence: medium
---

# Mixed-Traffic Multilane CORMC

## 1. 概念定义

`EXTRACTED` P002 的 CORMC 是面向多车道 freeway on-ramp 的混合交通协同合流框架，显式区分 CAV、compliant CHV 和 non-compliant CHV，并允许主线协作车辆通过换道或保持纵向运动来给匝道车创造合流空间。

## 2. 核心机制

```text
APS 提前预测匝道车到达合流区时的 lane 2 车辆位置
-> 指定 CLV / CFV 作为 cooperative vehicles
-> CUC 在换道协作与留在本车道之间做 utility choice
-> 下层纵向/换道/CMC 模型执行安全合流
-> 缓解合流区 congestion wave propagation
```

## 3. 关键变量

- CAV penetration rate。
- CHV compliance rate。
- on-ramp flow ratio。
- cooperative zone / merging zone。
- average flow and speed。

## 4. 对本研究的启发

- `INFERRED` 如果研究目标是近期可部署的混合交通合流，driver compliance 可能比纯优化目标更接近真实瓶颈。
- `INFERRED` 在多车道场景中，主线换道协作本身就是可设计变量，不能只把主线车辆当作纵向 gap creator。

## 5. 相关页面

- [[wiki/papers/P002-2023-Hou-Cooperative-On-Ramp-Merging-Control]]
- [[wiki/concepts/flexible-merging-positions]]
- [[wiki/gaps/open-questions]]
