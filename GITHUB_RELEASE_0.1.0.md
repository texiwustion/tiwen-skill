# 提问.skill v0.1.0

把小白问题拷打成能发给真人的成熟提问。  
不回答，不教学，先把问题问明白。

## 这是什么

`提问.skill` 是一个专门处理低质量技术/项目问题的 skill：

- 先做一次内部 friction scan
- 再用 2～6 个短问题追打缺失前提
- 默认硬门槛：前提不够，不给成熟问题
- 最终只输出一句能发给真人的问题

## v0.1.0 内容

- 加入 v1 作用域：技术 / 产品 / 工具 / 科研 / 项目决策
- 加入私有 friction scan
- 加入 2～6 问的苏格拉底追问循环
- 加入默认硬门槛
- 加入 `--wounded` 带伤放行
- 加入 `--agent` 目标改写
- 加入 `--cold` 冷刀模式
- 加入高风险题材安全卡口
- 加入公开自测样例与手工测试记录

## 安装

```bash
npx skills install texiwustion/tiwen-skill
```

也可以直接下载 Release asset: `tiwen-skill.skill`

## 已知限制

- 当前更适合技术/项目类问题
- 对特别短的输入，语气可能仍偏硬
- 当前测试以手工 prompt-walk 为主，不是自动化 harness
