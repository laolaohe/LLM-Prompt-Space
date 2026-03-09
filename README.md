# LLM-Prompt-Injection-
本项目是一个面向大语言模型（LLM）的 Prompt Injection 攻击与防御实验平台，旨在帮助研究者和安全爱好者理解和模拟 LLM 在现实应用中的安全风险。
通过本平台，你可以：

探索不同类型的 Prompt Injection 攻击手法

测试模型的防御能力

分析攻击成功率和防御效果

功能模块
攻击模块

Direct Injection（直接注入攻击）
模拟直接修改用户输入或系统提示进行攻击。

Jailbreak（越狱攻击）
利用模型规则漏洞，绕过安全限制执行非预期操作。

Indirect / Recursive（间接/递归攻击）
通过引导模型执行多步任务或间接提示达到攻击目的。

Code Injection（代码注入攻击）
向模型注入可执行代码，测试模型处理能力和风险。

防御模块

输入过滤：检测敏感关键词和异常输入

提示模板增强：通过约束系统提示减少攻击面

日志与统计分析：记录攻击尝试和防御效果，用于优化策略

项目结构
LLM-Prompt-Injection/
│
├─ attacks/              # 攻击模块源码
│  ├─ direct_injection.py
│  ├─ jailbreak.py
│  ├─ indirect.py
│  └─ code_injection.py
│
├─ defense/              # 防御模块源码
│  ├─ filter_check.py
│  └─ defense_core.py
│
├─ requirements.txt      # Python依赖
└─ README.md             # 项目说明

请确保你已正确配置你的 API Key
