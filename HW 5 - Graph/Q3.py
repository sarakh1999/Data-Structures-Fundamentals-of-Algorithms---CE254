n, m = map(int, input().split())
my_set = set([])
for i in range (n):
    my_set.add(i)
for i in range(m):
    u, v = map(int, input().split())
    if(my_set.__contains__(u)):
        my_set.remove(u)
print(len(my_set))