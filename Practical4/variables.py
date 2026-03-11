# 4.1 Some simple math - 苏格兰人口增长计算 scotland population growth calculation（unit:millions）
# Define variables a/b/c，for estimated population in 2004/2014/2024 预估人口
a = 5.08  # 2004 population of scotland
b = 5.33  # 2014 population of scotland
c = 5.55  # 2024 population of scotland

# calculate the change of population， store in d/e（文档指定变量名）
d = b - a  # 2004-2014 population change
e = c - b  # 2014-2024 population change


print("2004-2014 population change d =", d)
print("2014-2024 population change e =", e)
if d > e :
    x = "decelerating"
elif d < e :
    x = "accelerating"
else :
    x = "unchange" 
print("the change rate of the populatin x =", x)
 
# 4.2 Booleans - Boolean definition and OR operation
# define boolean variables X=True，Y=False
X = True
Y = False

# define W = X or Y
W = X or Y

print("\nW = X or Y origin：", W)

# Truth table for W (X or Y):
# 1. X=True, Y=True → W=True
# 2. X=True, Y=False → W=True
# 3. X=False, Y=True → W=True
# 4. X=False, Y=False → W=False