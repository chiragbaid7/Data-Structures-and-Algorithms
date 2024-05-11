from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 

# Linked list implementation
class Tree:
    def __init__(self):
        self.root=None 
        self.size=0
    #BFS 
    def insert(self,data):
        if(self.root==None):
            self.root=Node(data)
        else:
            q=deque()
            q.append(self.root)
            while(len(q)):
                parent =q.popleft()
                if(parent.left==None):
                    parent.left=Node(data)
                    break 
                elif(parent.right==None):
                    parent.right=Node(data)
                    break 
                q.append(parent.left)
                q.append(parent.right)
    #print DFS
    def __print_util(self,node):
        if(node==None):
            return
        print(node.data)
        self.__print_util(node.left)
        self.__print_util(node.right)

    def print_tree(self):
        self.__print_util(self.root)
    
    def __height(self,node):
        if(node==None ):
            return 0
        return max(self.__height(node.left),self.__height(node.right))+1
    def printHeight(self):
       return  self.__height(self.root)
        
root=Tree()
root.insert(10)
root.insert(11)
root.insert(9)
root.insert(7)
root.insert(12)
root.insert(15)
root.insert(8)
root.insert(14)
root.print_tree()

print(root.printHeight())



# 2.0
from collections import deque
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
class Tree:
    def __init__(self):
        self.root = None
    # BFS - level order traversal
    '''
        If a pointer(L or R) is null we insert a node and return
        till then we recursively travel Left and the Right
    '''
    def height(self, node):
        if(self.node == None):
            return 0
        return max(self.height(self.node.left), self.height(self.node.right)) + 1

    def printLevelNodes(nLevel, root, level):
        if(root == None):
            return
        if(nLevel == level):
            print(root.data)
            return
        printLevelNodes(nLevel,root.left, level + 1)
        printLevelNodes(nLevel,root.right, level + 1)
    def recursiveLevelOrder(self,node):
        height = self.height(node)
        for i in range (1, height + 1):
            printLevelNodes(i, root, 1)
    def iterativeBFS(self, data):
        if(self.root == None):
            self.root = Node(data)
        else:
            q= dequeue()
            q.append(self.root)
            while(len(q)):
                root = q.popleft()
                if(root.left):
                    root.left = Node(data)
                    break
                elif(root.right):
                    root.right = Node(data)
                    break
                q.append(root.left)
                q.append(root.right)
