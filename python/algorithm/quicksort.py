def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation +1,right)

def partition(lyst, left, right):
    # 找到基准点并与最后一位交换
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    #将边界点设置到第一个位置
    #boundary 代表边界后的一个位置
    boundary = left
    #将项目移动到基准点的左侧
    for index in range(left,right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    #交换边界点和基准点
    swap (lyst, right, boundary)
    return boundary

#快速排序的检测
# import random
#
# def main(size = 20, sort = quicksort):
#     lyst = []
#     for count in range(size):
#         lyst.append(random.randint(1, size + 1))
#     print(lyst)
#     sort(lyst)
#     print(lyst)
#
# if __name__ == "__main__":
#     main()