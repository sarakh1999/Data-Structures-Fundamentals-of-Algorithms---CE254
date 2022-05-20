def get_tree_value(position):
    value = 0
    while position > 0:
        value = (value + fenwick_tree[position])
        position -= position & -position
    value %= 7
    return value


def update(position, value, n, data, fenwick_tree):
    x = value - data[position]
    data[position] = value
    value = x
    k = (n - position) % 3
    if k == 0:
        value = value * 1 % 7
    elif k == 1:
        value = value * 2 % 7
    elif k == 2:
        value = value * 4 % 7
    while position < n + 1:
        fenwick_tree[position] += value
        position += position & -position


n = int(input())
for rounds in range(n):
    str = input()
    data = []
    fenwick_tree = []
    for i in range(len(str) + 1):
        data.append(0)
        fenwick_tree.append(0)
    for i in range(len(str)):
        if str[i] == '1':
            update(i + 1, 1, len(str), data, fenwick_tree)
    number_of_queries = int(input())
    for i in range(number_of_queries):
        query = input().split()
        if query[0] == '0':
            l = int(query[1])
            r = int(query[2]) + 1
            mod = 0
            k = (len(str) - r) * 2 % 3
            if k == 0:
                mod = (get_tree_value(r) - get_tree_value(l)) * 1 % 7
            elif k == 1:
                mod = (get_tree_value(r) - get_tree_value(l)) * 2 % 7
            elif k == 2:
                mod = (get_tree_value(r) - get_tree_value(l)) * 4 % 7
            print(mod)
        elif query[0] == '1':
            p = int(query[1]) + 1
            v = int(query[2])
            if data[p] != v:
                update(p, v, len(str), data, fenwick_tree)
