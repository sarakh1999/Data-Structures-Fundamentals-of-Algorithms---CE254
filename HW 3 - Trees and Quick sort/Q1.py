class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


def in_order(arr,i,bt):
    if i<len(arr):
        in_order(arr,2*i+1,bt)
        bt.append(arr[i])
        in_order(arr,2*i+2,bt)
    return bt


def quicksort(arr, start, end,arrpos):
    if start < end:
        split = partition(arr, start, end,arrpos)
        quicksort(arr, start, split - 1,arrpos)
        quicksort(arr, split + 1, end,arrpos)


def partition(arr, pivot_index, end,arrpos):
    stored_index = pivot_index + 1
    for i in range(pivot_index + 1, end + 1):
        if arr[i] < arr[pivot_index]:
            arr[stored_index], arr[i] = arr[i], arr[stored_index]
            arrpos[stored_index], arrpos[i] = arrpos[i], arrpos[stored_index]
            stored_index += 1
    arr[pivot_index], arr[stored_index - 1] = arr[stored_index - 1], arr[pivot_index]
    arrpos[pivot_index], arrpos[stored_index - 1] = arrpos[stored_index - 1], arrpos[pivot_index]
    return stored_index - 1


def min_swaps(arr):
    n = len(arr)
    arrpos = []
    vis=[]
    for i in range(n):
        arrpos.append(i)
        vis.append(False)
    quicksort(arr,0,n-1,arrpos)
    result = 0
    for i in range(n):
        if vis[i] or arrpos[i] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j]
            cycle_size += 1
        if cycle_size > 0:
            result += (cycle_size - 1)
    return result


n=int(input())
arr = list(map(int, input().split()))
binary_tree=[]
in_order(arr,0,binary_tree)
print(min_swaps(binary_tree))
