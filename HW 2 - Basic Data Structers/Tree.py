def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def insert(arr, v):
    arr.append(v)
    min_heapify_up(arr, len(arr) - 1)

def min_heapify_up(arr, i):
    if i > 0 and arr[i] < arr[parent(i)]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        min_heapify_up(arr, parent(i))

def min_heapify_down(arr, i):
    largest = i
    if (left(i) < len(arr) and arr[i] > arr[left(i)]):
        largest = left(i)
    if (right(i) < len(arr) and arr[largest] > arr[right(i)]):
        largest = right(i)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        min_heapify_down(arr, largest)

def build_min_heap(arr):
    for i in range(len(arr) // 2, -1, -1):
        min_heapify_down(arr, i)
    return arr

def remove_min(arr):
    arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
    result = arr.pop()
    min_heapify_down(arr, 0)
    return arr

a = input().split()
n = int(a[0])  # b[0]=n=tedad nomarte akbar
m = int(a[1])  # b[1]=m=tedad marahele poz dadan
k = int(a[2])  # b[2]=k=tedad roozhaye mande
arr = list(map(float, input().strip().split()))[:n]

for i in range(len(arr)):
    if (arr[i] % 1 == 0):
        arr[i] = int(arr[i])

# building the k member heap from the n member array
heap = build_min_heap(arr[:k])

# checking members k to n
# if they are greater than min(heap[0])
# they must beadded to the heap instead of the root
# and then use the min_heapify_down for the root
for i in range(k, n):
    if len(heap) >= k and arr[i] > heap[0]:
        heap[0] = arr[i]
        min_heapify_down(heap, 0)

for i in range(m):
    a = input()
    b = a.split()
    if (b[0] == "1"):                           # insert
        value = float(b[1])
        if value % 1 == 0:
            value = int(value)
        if (value > heap[0]):
            heap[0] = value
            min_heapify_down(heap, 0)
    if (b[0] == "2"):                            # find_k_max
        print(heap[0])
    if (b[0] == "3"):                            #remove heap root
        heap = remove_min(heap)


