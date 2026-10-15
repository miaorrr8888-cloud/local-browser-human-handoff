# AI网页任务的人工验证交接：用户使用指南

## 它能帮你做什么

用交接模板记录目标、原任务和本人动作；检查完成记录是否具备页面观察和结果证据。

## 适合谁

让AI协助处理网页任务，但需要自己登录、扫码或验证的使用者。

## 具体解决什么问题

AI停在登录或验证处，回来后忘了原任务；把页面可见误当成业务已完成。

**不适合这些目标：**代过验证码、自动登录、自动操作浏览器或独立判断平台上的业务已完成。

## 下载与准备

- [打开独立仓库](https://github.com/miaorrr8888-cloud/local-browser-human-handoff)
- [直接下载源码ZIP](https://github.com/miaorrr8888-cloud/local-browser-human-handoff/archive/refs/heads/main.zip)

也可在仓库页面点 Code → Download ZIP。解压后打开包含 SKILL.md、README.md、USER_GUIDE.md 的那层文件夹。不要停在外层目录或只复制一个脚本。

建议使用Windows电脑和Python 3.12；这是本次验证环境。先在该文件夹打开PowerShell，再执行：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe --version
```

这里直接使用虚拟环境里的Python，不需要运行激活脚本或修改系统执行策略。安装步骤及其他系统说明见[通用安装说明](https://github.com/miaorrr8888-cloud/agent-skills-worklog/blob/main/INSTALLATION.md)。

本指南的基础示例只用Python标准库，无需安装第三方Python包。

## 第一次使用：先跑自带示例

运行自带交接记录，先得到需要本人处理的状态；理解登录后还要继续原任务并记录结果。

```powershell
.\.venv\Scripts\python.exe scripts/check_handoff.py templates/HANDOFF_STATUS.json
```

## 结果怎么看

示例返回 HUMAN_ACTION_REQUIRED。页面可见但原任务未核实时返回 RESUME_ORIGINAL_TASK；记录完成只表示 TASK_REPORTED_COMPLETE，独立验证仍为false。

## 换成自己的资料

JSON记录 target_url、requested_task、page_visible_after_return、original_task_verified 和 evidence。不要填密码、验证码或浏览器登录数据。

复制模板到自己的任务文件，写清原业务动作。本人在原页面完成验证后，只更新已观察到的事实；有真实结果时再填写时间、结果链接与观察结果。

## 不想手动敲命令：给AI助手的任务

以下任务适用于能读取所选目录、执行本地命令的助手。WorkBuddy需要先确认当前版本的权限与技能启用状态；本项目未完成WorkBuddy实际导入验收。

```text
请先读取我选定文件夹中的 SKILL.md 和 USER_GUIDE.md，只在该项目范围内处理。
先解释自带交接模板的每一项，再运行状态检查示例。若我之后遇到登录或验证码，请明确需要我在页面做什么；我回来后继续核对原业务任务。不要索取密码或验证码，也不要把登录成功当成业务完成。
缺少依赖时先说明用途，优先放进本项目虚拟环境；不要读取其他目录中的密码、密钥或浏览器登录数据。
```

## 常见问题

**完成状态被拒绝**

检查是否有页面可见、观察时间、结果链接和实际结果描述；没有证据就保留未完成。

**换个浏览器仍未登录**

不同浏览器或会话可能不共享登录状态，回到原任务所用会话核对。

**找不到文件或脚本**

确认终端当前目录就是包含SKILL.md的技能根目录；路径含空格时加双引号。输出目录已存在时换新名字，不覆盖已有结果。

## 当前能力边界

检查器只校验记录结构，不直接观察浏览器。实际页面操作需要宿主提供可用浏览器能力；验证必须由本人按平台要求完成。

## 验证范围

本指南示例已在Windows独立副本中运行复核，见[命令复核结果](https://github.com/miaorrr8888-cloud/agent-skills-worklog/blob/main/USER_GUIDES_VERIFICATION.md)。已有回归测试只覆盖被测试行为，不证明真实业务结果。WorkBuddy实际运行、手机端使用和所有系统版本均不在本次已验证范围内。

许可证和素材来源分别见 [LICENSE](LICENSE)、[PROVENANCE.md](PROVENANCE.md)。
