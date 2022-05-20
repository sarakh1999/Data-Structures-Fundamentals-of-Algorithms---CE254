n=int(input())
arr=input()
stack=[]
stack.append(-1)
max_length=0
count_of_max_length=0
for i in range(n):
    if arr[i] == '(':
        stack.append(i)
    else:
        stack.pop()
    if len(stack) != 0:
        if(max_length < i - stack[len(stack) - 1]):
            max_length = i - stack[len(stack) - 1]
            count_of_max_length=0
        if( max_length == i - stack[len(stack) - 1]):
            count_of_max_length+=1
    else:
        stack.append(i)
print(max_length,count_of_max_length)