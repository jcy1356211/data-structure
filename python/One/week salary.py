a = float(input("每小时的薪水为："))
h1 = float(input("一周的总常规工作时间："))
h2 = float(input("一周的总加班时间："))
f = a * (h1 + 1.5 * h2)

print("一个雇员的总周薪为；%.2f" % f)