def longest_palindrome(string):
    stringLen = len(string)
    list = []
    i = 0
    pal_len = 0
    while i < stringLen:
        if i > pal_len and string[i - pal_len - 1] == string[i]:
            pal_len += 2
            i += 1
            continue
        list.append(pal_len)
        s = len(list) - 2
        e = s - pal_len
        for j in range(s, e, -1):
            d = j - e - 1
            if list[j] == d :
                pal_len = d
                break
            list.append(min(d, list[j]))
        else:
            pal_len = 1
            i += 1
    list.append(pal_len)
    list_len = len(list)
    s = list_len - 2
    e = s - (2 * stringLen + 1 - list_len)
    for i in range(s, e, -1):
        d = i - e - 1
        list.append(min(d, list[i]))
    print(max(list))


string=input()
longest_palindrome(string)

''''
tanha baraye check kardane 2 character az ==
estefade karde am
na baraye check kardane 2 string
'''
