def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right ) // 2
        if target ==sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
        print("左边的值为：%d,右边的值为：%d,中间的值为：%d"%(sortedLyst[left],sortedLyst[right],sortedLyst[midpoint]))
    return -1

number = [20,44,48,55,62,66,74,88,93,99]
binarySearch(44,number)
