# Research Agenda

last_updated: 2026-05-03

## 当前阶段

状态：P001-P0022 的有效语料已完成初始化 ingest 和 source-quality cleanup。当前保留 21 个 paper cards / 21 个 raw papers；P0013 重复源、P0023 低质量 OCR 源和错名 raw 已处理。现在暂停继续导入新论文，进入中期整理阶段。

## 近期目标

1. 完成 `wiki/concepts/` 的 concept consolidation audit，防止概念页退化成“一篇论文一个 concept”。
2. 基于 P001-P0022 生成 `wiki/synthesis/mid-field-synthesis-P001-P0022.md`，把 21 篇有效论文压缩成中期领域地图。
3. 基于中期综合结果，判断是否需要：
   - 继续 ingest P0024-P0030；
   - 先生成 `idea-candidates`；
   - 先做 baseline / benchmark 设计；
   - 先清理或合并 concepts / open questions。
4. 暂不创建正式 HYP，除非用户明确选择某个 candidate 并要求推进。

## 当前问题队列

| 优先级 | 问题 | 状态 | 相关页面 |
| --- | --- | --- | --- |
| P0 | Source-quality cleanup | done | `wiki/synthesis/source-quality-audit-2026-04-29.md` |
| P0 | Concept consolidation audit | next | `wiki/concepts/`, `wiki/comparisons/merging-control-baselines.md` |
| P0 | Mid-field synthesis P001-P0022 | done | `wiki/synthesis/mid-field-synthesis-P001-P0022.md` |
| P1 | 检查 open questions 是否膨胀、重复或可合并 | pending | `wiki/gaps/open-questions.md` |
| P1 | 检查 confirmed gaps 是否需要拆分或降级 | pending | `wiki/gaps/confirmed-gaps.md` |
| P1 | 决定是否继续 P0024-P0030 ingest | pending | `raw/papers/` |

## 中期整理重点

1. Concepts 是否需要合并为更高层跨论文概念，例如 sequencing、safety-critical control、mixed-traffic modeling、lateral-longitudinal execution、flow-level gap creation、learning-based merging。
2. `wiki/field/field-map.md` 是否已经过胖，哪些内容应转移到 `wiki/comparisons/` 或 `wiki/synthesis/`。
3. `wiki/gaps/open-questions.md` 中 OQ-0001 至 OQ-0026 是否存在重复、层级过细或可以合并的问题。
4. GAP-0001 至 GAP-0004 是否仍成立；是否有 gap 需要拆成更可实验的子问题。
5. P001-P0022 是否已经足够支持第一轮 `idea-candidates`，还是还需要补 P0024-P0030。

## 导入节奏

```text
单篇 ingest
-> 每 3-5 篇 mini-synthesis
-> 每 8-10 篇 batch synthesis
-> 重开聊天窗口
-> 30 篇后 full field synthesis
-> 再 generate-idea-candidates
```

## 下次启动提示

普通 Codex workflow 先按 Codex-native 启动链读取：

- `AGENTS.md`
- `purpose.md`
- `research-agenda.md`
- `index.md`

`.wiki-schema.md` 仅作为 legacy / migration reference；不是 Codex-native 启动必读，只有在 legacy comparison 或 migration audit 时读取。

随后按任务需要读取最小必要的 wiki 页面：

- `wiki/field/field-map.md`
- `wiki/field/shared-assumptions.md`
- `wiki/gaps/confirmed-gaps.md`
- `wiki/gaps/open-questions.md`
- `wiki/comparisons/merging-control-baselines.md`
- `wiki/synthesis/mid-field-synthesis-P001-P0022.md`
- `wiki/synthesis/source-quality-audit-2026-04-29.md`
- `wiki/synthesis/concept-consolidation-audit-2026-04-29.md`
