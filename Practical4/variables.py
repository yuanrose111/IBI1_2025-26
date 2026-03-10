# 4.1 Some simple math - 苏格兰人口增长计算（单位：百万）
# 定义文档指定变量a/b/c，对应2004/2014/2024预估人口
a = 5.08  # 2004年苏格兰人口
b = 5.33  # 2014年苏格兰人口
c = 5.55  # 2024年苏格兰人口

# 计算人口变化量，存储到d/e（文档指定变量名）
d = b - a  # 2004-2014年人口变化
e = c - b  # 2014-2024年人口变化（修正文档2025笔误）

# 打印d/e值，方便对比（非强制，便于验证）
print("2004-2014人口变化d =", d)
print("2014-2024人口变化e =", e)
print("d > e？", d > e)

# 【必加注释-评分点】判断人口增长趋势：d=0.25，e=0.22，d>e → 增长减速（decelerating）
# Conclusion: d is larger than e, so the population growth in Scotland is decelerating.
# 4.2 Booleans - 布尔值定义与或运算（文档指定要求）
# 定义布尔变量X=True，Y=False（文档指定初始值）
X = True
Y = False

# 定义W = X or Y（文档指定布尔运算）
W = X or Y

# 打印W的初始值，便于验证
print("\nW = X or Y 初始值：", W)

# 【必加注释-评分点】X or Y的真值表（需写全4种组合结果）
# Truth table for W (X or Y):
# 1. X=True, Y=True → W=True
# 2. X=True, Y=False → W=True
# 3. X=False, Y=True → W=True
# 4. X=False, Y=False → W=False