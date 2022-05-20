def find_set(parent, x):
    if x != parent[x]:
        parent[x] = find_set(parent, parent[x])
    return parent[x]


n = int(input())
data = list(map(int, input().strip().split()))[:n]
parent = []
max_count = []
min_count = []
maximum = []
minimum = []
for i in range(n):
    max_count.append(1)
    min_count.append(1)
    parent.append(i)
for i in range(len(data)):
    maximum.append(data[i])
    minimum.append(data[i])
q = int(input())
for query in range(0, q):
    order = input().split()
    if order[0] == '1':
        a = int(order[1]) - 1
        b = int(order[2]) - 1
        group1 = find_set(parent, a)
        group2 = find_set(parent, b)
        if group1 != group2:
            if maximum[group1] == maximum[group2]:
                max_count[group1] += max_count[group2]
            elif maximum[group1] < maximum[group2]:
                max_count[group1] = max_count[group2]
                maximum[group1] = maximum[group2]
            if minimum[group1] == minimum[group2]:
                min_count[group1] += min_count[group2]
            elif minimum[group1] > minimum[group2]:
                min_count[group1] = min_count[group2]
                minimum[group1] = minimum[group2]
            parent[group2] = group1
    elif order[0] == '2':
        a = int(order[1]) - 1
        group1 = find_set(parent, a)
        variaty = (maximum[group1] - minimum[group1]) * max_count[group1] * min_count[group1]
        print(variaty)
