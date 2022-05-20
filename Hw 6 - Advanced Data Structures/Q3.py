def fill_trie(trie):
    for i in range(30):
        j = i + 1
        trie[i][0] = j


n = int(input())
xor_value = 0
k = 31
trie_length = k - 1
trie_range = k - 2
trie = [[0, 0] for i in range(600000)]
fill_trie(trie)

for query in range(n):
    order = input().split()

    if order[0] == '1':
        i = 0
        a = (int(order[1]) ^ xor_value)
        for j in range(trie_length):
            val = (a >> (trie_range - j)) & 1
            if trie[i][val] == 0:
                trie[i][val] = k
                k += 1
            i = trie[i][val]

    elif order[0] == '2':
        xor_value ^= int(order[1])

    elif order[0] == '3':
        i, max = 0, 0
        for j in range(trie_length):
            val = (xor_value >> (trie_range - j)) & 1
            if val == 0:
                if trie[i][1] == 0:
                    i = trie[i][0]
                else:
                    max += 1 << (trie_range - j)
                    i = trie[i][1]
            elif val == 1:
                if trie[i][0] == 0:
                    i = trie[i][1]
                else:
                    max += 1 << (trie_range - j)
                    i = trie[i][0]
        print(max)
