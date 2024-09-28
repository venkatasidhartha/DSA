

def bubble_sort(customLIst):
    for i in range(len(customLIst)-1):
        for j in range(len(customLIst)-i-1):
            if customLIst[j] > customLIst[j+1]:
                customLIst[j],customLIst[j+1] = customLIst[j+1],customLIst[j]
    print(customLIst)


def selectionSort(customLIst):
    for i in range(len(customLIst)):
        min_index = i
        for j in range(i+1,len(customLIst)):
            if customLIst[min_index] > customLIst[j]:
                min_index = j
        customLIst[i],customLIst[min_index] = customLIst[min_index],customLIst[i]
    print(customLIst)


clist = [2,1,7,6,5,3,4,9,8]
selectionSort(customLIst=clist)
# bubble_sort(customLIst=clist)