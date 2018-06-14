import math
tall = float(input("初始高度:"))
frequency = int(input("弹跳次数:"))
c = 0.6
high = tall
for i in range(frequency):
    high = tall * c
    tall += high

print("总运动距离为: %0.2f"%tall)