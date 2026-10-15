# AI网页任务的人工验证交接

AI停在登录或验证处，回来后忘了原任务；把页面可见误当成业务已完成。

这个开源技能可以帮助你：用交接模板记录目标、原任务和本人动作；检查完成记录是否具备页面观察和结果证据。

**适合谁：**让AI协助处理网页任务，但需要自己登录、扫码或验证的使用者。

**怎么开始：**下载并解压独立仓库，按USER_GUIDE先跑自带示例，再换成自己的资料。需要电脑和相应运行环境。

**能看到的结果：**示例返回 HUMAN_ACTION_REQUIRED。页面可见但原任务未核实时返回 RESUME_ORIGINAL_TASK；记录完成只表示 TASK_REPORTED_COMPLETE，独立验证仍为false。

**使用前知道：**检查器只校验记录结构，不直接观察浏览器。实际页面操作需要宿主提供可用浏览器能力；验证必须由本人按平台要求完成。

[项目与下载入口](https://github.com/miaorrr8888-cloud/local-browser-human-handoff) · [逐步使用指南](https://github.com/miaorrr8888-cloud/local-browser-human-handoff/blob/main/USER_GUIDE.md)

说明：示例、演示与实际业务结果分开记录；介绍文案已准备，尚未发布到自媒体平台。
