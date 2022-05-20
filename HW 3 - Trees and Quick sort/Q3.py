import sys


def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        a=(quicksort(less)+equal+quicksort(greater))
        for i in range(len(a)):
            print(a[i],end=" ")
        print()
        return a
    else:
        return array


n=int(input())
sys.setrecursionlimit(n + 10)
arr= list(map(int, input().split()))
quicksort(arr)