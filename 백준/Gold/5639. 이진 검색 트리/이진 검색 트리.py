import sys
sys.setrecursionlimit(10 **4 )

class Node(object):
    def __init__(self, item):
        self.item=item
        self.left=self.right=None

    
class BinaryTree(object):
    def __init__(self):
        self.root=None


    def preorder(self):
        def _preorder(node):
            print(node.item)
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)


    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.item)
        _postorder(self.root)




BT=BinaryTree()
nodes={}
stack=[]
i=0
while True:
    x= sys.stdin.readline().strip()

    if not x:
        break

    x=int(x)

    if x not in nodes:
        nodes[x]=Node(x)


    if stack and stack[-1] < x:
        while stack and stack[-1] < x:
            here = stack.pop()
        nodes[here].right=nodes[x]
    elif stack and stack[-1]>x: #x가 이전값보다 작으면 왼쪽에
        nodes[stack[-1]].left=nodes[x]
    
    if i ==0:
        BT.root=nodes[x]

    stack.append(x)
    i+=1

# BT.preorder()
BT.postorder()