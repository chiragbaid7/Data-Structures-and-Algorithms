#insert 
#deletion
#search 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 

class BST:
    def __init__(self):
        self.root=None 
    def __insert__util(self,key,node):  
        if(node==None):
            return Node(key)
        elif (key<node.data):
            node.left=self.__insert__util(key,node.left)
        elif(key>node.data):
            node.right=self.__insert__util(key,node.right)
        return node

    def insert(self,data):
        if(root==None):
            self.root=Node(data)
        else:
            self.root=self.__insert__util(data,self.root)

        #print DFS
    def __print_util(self,node):
        if(node==None):
            return
        print(node.data)
        self.__print_util(node.left)
        self.__print_util(node.right)

    def print_tree(self):
        self.__print_util(self.root)
 
root=BST()
root.insert(6)
root.insert(4)
root.insert(9)
root.insert(40)
root.insert(3)
root.insert(5)
root.insert(1)
root.print_tree()