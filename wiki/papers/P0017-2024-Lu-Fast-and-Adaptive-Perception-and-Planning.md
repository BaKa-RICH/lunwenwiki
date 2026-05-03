---
type: paper
paper_id: P0017
title: "FAPP: Fast and Adaptive Perception and Planning for UAVs in Dynamic Cluttered Environments"
authors: "Minghao Lu, Xiyu Fan, Han Chen, Peng Lu"
year: 2024
venue: "IEEE"
status: read
confidence: medium
source_path: raw/papers/P0017-2024-Lu-Fast-and-Adaptive-Perception-and-Planning.md
zotero_key:
doi:
tags: [UAV, dynamic-obstacle-avoidance, point-cloud-segmentation, adaptive-estimation, covariance-adaptation, trajectory-optimization, replanning]
last_updated: 2026-04-29
---

# P0017: FAPP for UAV Dynamic Cluttered Environments

## 1. 一句话定位

这篇论文提出 FAPP，将点云动态/静态分割、协方差自适应运动估计、MINCO 轨迹优化和失败时临时目标重规划组合成一个可在拥挤动态环境中实时运行的 UAV 感知-规划系统。

## 2. 核心贡献

- `EXTRACTED` 提出轻量点云分割策略，用当前聚类到历史点云集合的平均最近距离和归一化距离方差区分 moving / static / unknown objects。
- `EXTRACTED` 只对动态对象创建 tracker，并用 Mahalanobis distance + Hungarian algorithm 做动态聚类与 tracker 的关联，降低拥挤环境中的计算负担。
- `EXTRACTED` 提出 covariance adaptation，用 Kalman innovation sequence 在线更新过程噪声协方差 `Q_k`，以适应不同动态障碍的非匀速、急转向或突变运动。
- `EXTRACTED` 在 trajectory optimization 中直接纳入静态障碍、动态障碍预测和预测不确定性，不使用前端 path searching / safe corridor generation。
- `EXTRACTED` 提出 adaptive replanning：当到原目标的可行无碰轨迹不存在时，根据动态障碍相对速度投影生成临时目标点继续避障。
- `EXTRACTED` 用仿真和真实 UAV 室内/室外实验验证系统，报告 perception + planning 总迭代时间约 20 ms。

## 3. 方法抓手

- Dynamic segmentation：对当前点云 DBSCAN 聚类后，用 `T1` 表示点到历史点云的平均最近距离，用 `T2` 表示归一化距离方差；`T1 > h1` 且 `T2 < h2` 判为 moving object。
- Adaptive estimation：仍以 constant velocity Kalman filter 为基础，但用 innovation covariance matching 更新 `Q_k`，避免为每个动态障碍维护多模型滤波器。
- Uncertainty-aware dynamic avoidance：动态障碍安全距离 `D_d^i = r_0 + r^i + e^i`，其中 `e^i` 来自预测协方差传播，直接进入轨迹碰撞 penalty。
- Fast planning：采用 5 次分段多项式和 MINCO 参数化，优化中同时考虑 jerk/time、动力学可行性、静态障碍和动态障碍。
- Failure handling：当轨迹优化找不到通往目标点的可行解时，不让 UAV 原地等待，而是由动态障碍速度在相对位置方向上的投影生成 repulsion-like temporary target。

## 4. 关键实验结论

- `EXTRACTED` 动态感知对比中，FAPP perception 平均耗时 12.77 ms，低于对比方法的 29.52 ms、40.33 ms 和 40.52 ms；MOTA 为 84.10%。
- `EXTRACTED` covariance adaptation ablation 中，三类非匀速运动的 velocity MAE 明显降低，例如 Condition 3 从 2.39 m/s 降至 0.36 m/s。
- `EXTRACTED` 随机加速障碍撞向悬停 UAV 的 50 次仿真中，有 covariance adaptation 的避障成功率为 94%，去掉 adaptation 后仅 48%。
- `EXTRACTED` 三类动态拥挤仿真环境中，FAPP 成功率分别为 94%、88%、90%，规划耗时约 2.48 ms、3.12 ms、2.80 ms；第三类无直接可行路径场景只有 FAPP 能处理。
- `EXTRACTED` 真实抛箱实验中，带 covariance adaptation 的动态避障 10 次成功 9 次，不带 adaptation 只成功 2 次。
- `EXTRACTED` 室内多人搬箱和室外公园人行道实验显示，系统能在真实 UAV 平台上分割行人/工作人员并生成无碰轨迹。

## 5. 局限与隐含假设

- 论文自述局限：
  - 若 UAV 激烈机动时 onboard localization 失效，系统仍可能偶发失败；未来工作需要处理 localization failure。
- 你识别到的隐含假设：
  - 任务对象是 UAV 避障，不是 CAV 匝道合流；其方法价值主要是可迁移的动态障碍估计和失败时重规划机制。
  - 动态障碍预测仍以短时近似线性运动为主，covariance adaptation 提升响应速度，但不等于长期意图预测。
  - 动态障碍被视为外部物体，不建模博弈、协作、合流规则或驾驶人反应。
  - 实验重在安全通过和避碰，缺少交通流效率、通行能力、合流公平性或 CAV-HDV communication 维度。
  - 感知依赖 50 Hz Livox MID-360 + Fast-LIO2，在路侧感知或车载感知场景中的遮挡、尺度和噪声特性需重新验证。

## 6. 关系线索

- uses: covariance-adaptive dynamic obstacle planning paper-specific mechanism, point-cloud dynamic segmentation, covariance adaptation, uncertainty-aware dynamic obstacle penalty, adaptive temporary-target replanning；原单篇 concept 已删除，核心信息保留在本 card 与 [[wiki/gaps/open-questions]]。
- complements: [[wiki/concepts/field-experimental-communication-delay-cav-merging]]，P009 强调真实通信延迟，P0017 强调感知/预测估计延迟和不确定性。
- complements: [[wiki/concepts/flexible-control-barrier-function-merging]]，P006 给 CAV 合流提供 safety-critical layer，P0017 提供预测不确定性如何进入避障 penalty 的迁移线索。
- contrasts: [[wiki/papers/P0010-2025-Choi-Cooperative-Merging-Mixed-Traffic]]，P0010 主动影响 HDV，P0017 主要被动预测动态对象并绕行。
- suggests_gap: mixed traffic merging 中的 HDV/CAV 轨迹预测不应只用固定 IDM/CV 假设，还需显式处理快速变化运动、估计协方差和可行规划失败。
- asset_todo: 原始 MinerU 文件含大量外链图片，后续如需写作审计，应本地化到 `raw/assets/P0017/`。

## 7. 对我研究的可能用途

- method_source: covariance adaptation 可作为 HDV/CAV 短时运动预测不确定性建模的轻量候选机制。
- experiment_design: 可借鉴“有/无协方差自适应”的 ablation，检验 prediction uncertainty 是否真的影响合流安全或排序结果。
- risk_source: 提醒合流控制不能只假设预测状态准确，还要考虑估计收敛速度、预测协方差和 planner infeasibility。
- metric: MOTA、position/velocity MAE、convergence time、planning time、success rate、trajectory energy cost，可迁移为 prediction/planning 子模块指标。
- boundary_marker: 该文不是匝道合流 baseline，不能直接作为交通控制对比；更适合作为 perception-planning robustness 的外部机制证据。

## 8. 原文锚点

- raw: `raw/papers/P0017-2024-Lu-Fast-and-Adaptive-Perception-and-Planning.md`
- zotero:
- doi:
- video: https://youtu.be/4DXBuKpqQk4
- keywords: fast adaptive perception and planning; dynamic cluttered environments; covariance adaptation; point cloud segmentation; UAV obstacle avoidance.

## 9. 必要摘录

> `EXTRACTED` "This paper proposes Fast and Adaptive Perception and Planning (FAPP) for UAVs flying in complex dynamic cluttered environments."

> `EXTRACTED` "A novel covariance adaptation method is proposed to address multiple dynamic objects with different motions."

> `EXTRACTED` "The whole perception and planning process can be completed within a few milliseconds, which is highly efficient."

> `EXTRACTED` "To quickly and accurately estimate and predict the motion of the dynamic objects is vital for dynamic obstacle avoidance."

> `EXTRACTED` "In 50 tests, the UAV achieves a success rate of 94% with covariance adaptation, however, when the covariance adaptation is eliminated, the success rate is only 48%."

> `EXTRACTED` "Overall, the entire system only takes about 20 ms in each iteration."

## 10. 回查触发点

- proof：需要解释 covariance matching、innovation sequence 如何更新 `Q_k` 时，回查 `IV. Adaptive Estimation and Prediction`。
- 实验设计：需要设计 prediction uncertainty / estimation speed ablation 时，回查 `VI.C Evaluation of the Adaptive Perception with Covariance Adaptation`。
- baseline 复现：需要实现动态点云分割、Mahalanobis + Hungarian 数据关联、MINCO 动态障碍 penalty 或临时目标重规划时，回查 `III` 至 `V`。
- 写作：需要引用“动态障碍预测精度与收敛速度会决定避障/规划成败”时，回查 `II.B`、`IV` 和 `VI.C`。
- citation audit：需要核对 UAV 平台、传感器、视频链接、作者和参考方法时，回查论文开头、`VI.A` 与 `References`。

## 11. 关键原文位置

- 题名、作者、摘要和 supplementary video：开头。
- 研究动机、动态拥挤环境定义和贡献：`I. Introduction`。
- 相关工作和既有方法缺口：`II. Related Works`。
- 点云动态/静态分割和 tracking：`III. Fast and Adaptive Perception of Dynamic Cluttered Environments`。
- 协方差自适应估计：`IV. Adaptive Estimation and Prediction for Dynamic Cluttered Environments`。
- MINCO 轨迹优化、动态障碍不确定性 penalty 和 adaptive replanning：`V. Fast and Adaptive Planning`。
- 感知、协方差 ablation、仿真避障和真实 UAV 实验：`VI. Experiments and Evaluations`。
- 自述局限：`VII. Conclusion`。
