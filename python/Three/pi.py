frequency = int(input("迭代的次数是："))
sum = 0
for i in range(frequency):
    sum += float(1/(2*i+1) * (-1)**i)

print("pi的近似值为：%f"%(4*sum))