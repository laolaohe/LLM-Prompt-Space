from llm_api import call_llm
from attacks.direct_injection import direct_injection_attack
from attacks.Jailbreak import jailbreak_attack
from attacks.indirect import indirect_injection_attack
from attacks.code_injection import code_injection_attack
from attacks.recursive import recursive_injection_attack
from defense import (
    sanitize_messages,
    add_post_prompt,
    sandwich_defense,
    random_wrapper,
    xml_wrap_messages,
    llm_evaluate_response
)

# -------------------- 攻击成功率函数 --------------------
def attack_with_success_rate(messages, target, trials=5):
    success_count = 0
    last_response = ""
    for i in range(trials):
        resp = call_llm(messages)
        last_response = resp  
        if resp and target in resp:
            success_count += 1
    success_rate = success_count / trials
    print(f"\n攻击成功率: {success_count}/{trials} = {success_rate:.0%}")
    return last_response

# -------------------- 主程序 --------------------
print("=== LLM Prompt Injection 实验平台 ===")

print("选择攻击类型:")
print("1 Direct Injection")
print("2 Jailbreak Attack")
print("3 Indirect Injection")
print("4 code injection")
print("5 Recursive Injection")

choice = input("请输入攻击编号: ")
target = ""

# -------------------- 防御开关 --------------------
defense_enabled = input("是否开启防御？(y/n): ").lower() == 'y'
use_post_prompt = use_sandwich = use_random_shell = use_xml_wrap = use_llm_eval = False

if defense_enabled:
    use_post_prompt = input("是否开启后提示(Post-Prompt)？(y/n): ").lower() == 'y'
    use_sandwich = input("是否开启三明治防御(Sandwich Defense)？(y/n): ").lower() == 'y'
    use_random_shell = input("是否开启随机序列外壳(Random Shell)？(y/n): ").lower() == 'y'
    use_xml_wrap = input("是否开启XML/标记封装(XML Wrap)？(y/n): ").lower() == 'y'
    use_llm_eval = input("是否开启单独LLM评估(LLM Evaluation)？(y/n): ").lower() == 'y'

# -------------------- 攻击模块 --------------------
if choice == "1":
    target = input("请输入攻击目标: ")
    messages = direct_injection_attack(target)
elif choice == "2":
    target = input("请输入攻击目标: ")
    messages = jailbreak_attack(target)
elif choice == "3":
    target = input("请输入攻击目标: ")
    content = input("请输入文章内容（可多行，结束用Enter+Ctrl+Z）：\n")
    messages = indirect_injection_attack(target, content)
elif choice == "4":
    a = int(input("请输入 a: "))
    b = int(input("请输入 b: "))
    messages = code_injection_attack(a, b)
    target = str(a + b)
elif choice == "5":
    target = input("请输入攻击目标: ")
    messages = recursive_injection_attack(target)
else:
    print("输入错误")
    exit()

# -------------------- 防御模块应用 --------------------
if defense_enabled:
    # 1. 过滤关键词
    messages = sanitize_messages(messages)
    # 2. 后提示
    if use_post_prompt:
        messages = add_post_prompt(messages)
    # 3. 三明治防御
    if use_sandwich:
        messages = sandwich_defense(messages)
    # 4. 随机序列外壳
    if use_random_shell:
        messages = random_wrapper(messages)
    # 5. XML/标记封装
    if use_xml_wrap:
        messages = xml_wrap_messages(messages)

# -------------------- 打印攻击Prompt --------------------
print("\n=== 攻击Prompt（用户消息） ===")
for msg in messages:
    if msg["role"] == "user":
        print(msg["content"])

# -------------------- 调用 LLM 并统计攻击成功率 --------------------
response = attack_with_success_rate(messages, target, trials=5)

# -------------------- 单独LLM评估 --------------------
if use_llm_eval:
    safe = llm_evaluate_response(response, target)
    if safe:
        print("\nLLM评估结果: 回答安全 ✅")
    else:
        print("\nLLM评估结果: 回答不安全 ❌")

# -------------------- 最终AI回复 --------------------
print("\n=== 最终AI回复 ===")
print(response)