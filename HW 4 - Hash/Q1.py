def find_index(key:int):
    global a,m
    return (a*key)%m


def hash_str(s:str):
    return int.from_bytes(s.encode(),'big')


def find_common_str(size:int):
    global m,str1,str2
    hash_table=[[]for i in range(m)]
    for i in range(len(str1)-size+1):
        h=hash_str(str1[i:i+size])
        hash_table[find_index(h)].append(h)
    for i in range(len(str2)-size+1):
        h=hash_str(str2[i:i+size])
        for string in hash_table[find_index(h)]:
            if string==h:
                return str2[i:i+size]
    return ""


def binary_search_string_procesing():
    start=0
    end = min(len(str1),len(str2))+1
    x=""
    while end-start>1:
        substring_length = (start+end) // 2  # hamoon mid ast
        s=find_common_str(substring_length)
        if (s==None or s==""):
            end = substring_length
        else:
            start = substring_length
            x=s
    return x


str1=input()
str2=input()
m=5003
a=23
print(binary_search_string_procesing())