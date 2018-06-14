import math
r = float(input("请输入球体半径r："))
d = 2 * r
c = 4 * math.pi * r**2
v = 4 / 3 * math.pi * r**3

print("球体直径为%f\n球体表面积为%f\n球体体积为%f"%(d,c,v))