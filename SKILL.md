---
name: local-browser-human-handoff
description: 在浏览器任务被登录、扫码或验证码阻塞时组织人工交接，并在用户返回后核验原任务。
license: MIT
---

# 浏览器人工交接

先确认具体目标页面、原任务与当前阻塞。只请求用户完成当前所需的登录、MFA 或 CAPTCHA，不索要密码、Cookie、令牌或浏览器档案。

使用 examples/handoff.md 的交接表达与 templates/HANDOFF_STATUS.json 记录状态。用户返回后先确认目标页面能否访问，再验证原任务结果。页面加载、登录成功与业务动作完成分别记录。

同一账号在另一会话登录，不证明当前工具会话也已登录。仍受限时保留 BLOCKED 和具体原因，只请求必要的页面信息或用户提供的链接，不绕过访问限制或降低浏览器安全设置。

## 上手示例与当前限制

先读 [README.md](README.md) 的快速开始、输入输出和未完成项；可运行例子在 examples/，本次修订见 CHANGELOG.md。不要把合成演示或离线检查当成真实平台验证。

## 扩展能力

增加可运行的交接状态检查器：登录后页面可见只能恢复原任务，声明任务完成必须附时间、结果链接和观察结果。 使用前阅读 [README.md](README.md) 的“第二轮”命令和当前限制。不要把本地检查、人工声明或模拟响应解释为实时平台验证。

## 面向使用者的说明

解释用途、适用人群、下载和第一次运行时，读 [USER_GUIDE.md](USER_GUIDE.md)；需要中文对外介绍时参考 [INTRODUCTION.md](INTRODUCTION.md)，不要把介绍稿等同于已发布。
