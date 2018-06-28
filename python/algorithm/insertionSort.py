def insertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToSert = lyst[i]
        j = i - 1
        while j >= 0:
            if lyst[itemToSert] < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
            lyst[j + 1] = itemToSert
            i += 1