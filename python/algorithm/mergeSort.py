from arrays import Array

def mergeSort(lyst):
    #lyst   被存储的列表
    #copyBuffer  合并过程中需要的临时空间
    copyBuffer = Array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst   被存储的列表
    # copyBuffer  合并过程中需要的临时空间
    # low, high  子列表的界限
    # middle  子列表的中间位置

    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):
    # lyst        被存储的列表
    # copyBuffer  合并过程中需要的临时空间
    # low         第一个排序子列表的开始
    # middle      第一个排序子列表的结束
    # middle + 1  第二个排序子列表的开始
    #high         第二个排序子列表的结束

    #将i1和i2初始化为每个子列表中的第一项
    i1 = low
    i2 = middle + 1

    #将子列表中的项目交换到 copyBuffer 中来保持顺序
    for i in range(low, middle + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]  #第一个子列表已经耗尽
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]  #第二个子列表已经耗尽
            i1 += 1
        elif lyst[i1] < lyst[i2] :
            copyBuffer[i] = lyst[i1] #项目在第一个子列表中
            i1 += 1
        else :
            copyBuffer[i] = lyst[i2] #项目在第二个子列表中
            i2 += 1

    for i in range(low, high + 1):
        lyst[i] = copyBuffer[i]

    #将已分类的项目复制到合适的位置

