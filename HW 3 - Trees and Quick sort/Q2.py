class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count=1


def find(root, key):
    while root != None:
        if key > root.data:
            root = root.right
        elif key < root.data:
            root = root.left
        else:
            return root
    return None


def insert(Node, data):
    if Node == None:
        return newNode(data)
    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)
    return Node


def nuum_of_strings_with_equal_abc(string):
    root = None
    root=insert(root,(0,0))
    a, b, result = 0, 0, 0
    for i in range(len(string)):
        if string[i] == 'a':
            a += 1
        elif string[i] == 'b':
            b += 1
        elif string[i] == 'c':
            a -= 1
            b -= 1
        temp=(a,b)
        k=find(root,temp)
        if k!=None:
            result+=k.count
            k.count+=1
        else:
            insert(root,temp)
    return result


string = input()
print(nuum_of_strings_with_equal_abc(string))

