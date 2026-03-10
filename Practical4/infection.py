# 【伪代码规划-文档强制要求，保留】
# 1. 定义基础变量：初始感染人数initial_infected、日增长率growth_rate（小数）、总学生数total_students=91
# 2. 定义计数器：days=0（记录感染天数），current_infected=initial_infected（当前感染人数，初始为初始值）
# 3. 创建while循环：当current_infected < total_students时，持续执行循环
# 4. 循环内操作：打印当日感染人数 → 计算次日感染人数 → 天数加1
# 5. 循环结束后：打印最终感染人数（≥91）和总感染天数
# 6. 示例：initial_infected=5，growth_rate=0.4 → 第2天感染人数=7（验证公式正确性）
# 实际代码 - 感染率模拟计算
# 定义基础变量（文档示例：初始5人，增长率40%，总人数91）
initial_infected = 5
growth_rate = 0.4  # 40%日增长率，用小数表示
total_students = 91

# 定义计数器变量
current_infected = initial_infected  # 当前感染人数，初始为初始值
days = 0  # 初始天数为0

# 打印标题，便于查看结果
print("IBI1班级感染人数每日变化：")
print("-" * 40)

# while循环：未全部感染时持续计算
while current_infected < total_students:
    print(f"第{days}天：{current_infected:.1f} 人感染")  # 保留1位小数，更清晰
    current_infected = current_infected * (1 + growth_rate)  # 计算次日感染人数
    days += 1  # 天数加1

# 循环结束：打印全感染结果（核心要求）
print(f"第{days}天：{current_infected:.1f} 人感染（全班级91人全部感染）")
print("-" * 40)
print(f"感染整个班级共花费：{days} 天")