def MergeSort(arr):
    global proximity
    global prize
    i=len(arr)//2
    if(i>=1):
        left = arr[:i]
        right = arr[i:]
        right = MergeSort(right)
        left = MergeSort(left)
        out = []
        leftPointer = 0
        rightPointer = 0
        leftLen = len(left)
        rightLen = len(right)
        while(rightPointer != rightLen and leftPointer != leftLen):
            if(proximity[left[leftPointer]]*prize[left[leftPointer]] + proximity[left[leftPointer]]*proximity[right[rightPointer]]*prize[right[rightPointer]] >= proximity[right[rightPointer]]*prize[right[rightPointer]] + proximity[left[leftPointer]]*prize[left[leftPointer]]*proximity[right[rightPointer]]):
                out.append(left[leftPointer])
                leftPointer += 1
            else:
                out.append(right[rightPointer])
                rightPointer += 1
        if(rightPointer == rightLen):
            for i in range(leftPointer,leftLen):
                out.append(left[i])
        elif(leftPointer == leftLen):
            for i in range(rightPointer,rightLen):
                out.append(right[i])
        return out
    return arr
if __name__ == '__main__':
    n = int(input())
    proximity = []
    prize = []
    arr1 = []
    i=0
    for i in range(n):
        p, c = input().split()
        proximity.append(float(p) / 100)
        prize.append(float(c))
        arr1.append(i)
    arr1 = MergeSort(arr1)
    output=float(0)
    omid=1
    for i in range(0, n):
        omid *= proximity[arr1[i]]
        output += prize[arr1[i]] * omid
    print('%.3f'%output)
