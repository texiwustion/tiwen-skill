# Calibration Examples

Use these only to calibrate tone and output shape. Do not paste them blindly.

## Example 1: Skill install confusion

Raw:
“蒸馏具体怎么用啊？如果用手机的话。skill 吧，具体怎么弄呀，必须用电脑？”

Pressure question:
“你现在把蒸馏、小模型、skill 混在一锅里了；先说清楚你要装的是哪个 agent 系统里的 skill，以及你手机上能不能访问那个 agent 环境。”

Possible final:
“我想问：如果我只有手机，想安装并使用某个 agent 的 `.skill`，这个流程是否必须依赖电脑或本地 CLI？（背景：我现在不确定它属于哪个 agent 系统，也没分清 skill 和模型蒸馏是不是一回事）”

## Example 2: Finding a research harness skill

Raw:
“我想找一个偏科研项目，轻量级的 harness 相关 skill。”

Pressure question:
“‘harness 相关’现在只是个摆设词；你到底要的是实验评测 harness、LLM eval harness，还是项目脚手架里的测试 harness？”

Possible final:
“我想问：有没有适合小型科研项目的轻量级 LLM eval harness 类 skill，用来快速组织实验输入、运行评测并记录结果？（背景：我更在意低配置和可复现，不需要完整平台化方案）”

## Example 3: Model and reasoning-level choice

Raw:
“Win10 桌面版软件开发类似网约车的项目，选择哪个模型比较合适？推理等级呢？我不懂模型，希望一个模型一个推理等级干到底。”

Pressure question:
“你想一个模型干到底可以理解，但你没说这个‘类似网约车’到底是 UI 原型、业务 Demo，还是要接近真实派单系统；这三种失败代价不是一个量级。”

Possible final:
“我想问：我在做一个 Win10 桌面端、类似网约车业务流程的开发项目，如果希望尽量固定一个模型和一个推理等级以减少上下文风格漂移，应该按什么项目复杂度和失败代价来选？（背景：我不熟模型参数，更想要稳定推进而不是频繁切换）”

## Wounded-mode example

Raw after user says “别问了，带伤放行。”

Possible final:
“我想问：我想在手机上尽量低门槛地使用某个 `.skill`，一般需要满足哪些环境条件？（背景：我还没确认它属于哪个 agent 系统，也没确认手机端是否支持安装流程，所以答案可能会偏到错误平台）”
