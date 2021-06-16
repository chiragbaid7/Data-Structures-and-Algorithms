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
        if(node.left ==None and node.right==None):
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