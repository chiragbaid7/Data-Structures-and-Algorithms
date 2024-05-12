#insert 
#deletion
#search
#Time Complexity - O(H) - In case of balanced B Tree
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
         #The current node pointer must be now linked to new node
        elif (key<node.data):
            node.left=self.__insert__util(key,node.left)
        elif(key>node.data):
            node.right=self.__insert__util(key,node.right)
        return node

    def insert(self,data):
        if(root==None):
            self.root=Node(data)
        else:
            #since we are creating a copy
            self.root=self.__insert__util(data,self.root)
    def __delete_node(self,data,node):
        #1.first find the node that you want to delete 
        if(node==None):
            #print when no such 
            print("No key exists")
            return None 
        elif(data<node.data):
            node.left=self.__delete_node(data,node.left)
        elif(data>node.data):
            node.right=self.__delete_node(data,node.right)
        else:
            #when key is found 
            if(not node.right):
                return node.left 
            elif(not node.left):
                return node.right 
            #when 2 childrens exists
            else:
                # find the in order successor and replace it with current node 
                temp=node.right 
                while(temp.left):
                    temp=temp.left 
                node.data=temp.data
                node.right=self.__delete_node(temp.data,node.right)
        return node 
    
    def delete(self,data):
        self.root=self.__delete_node(data,self.root)

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
root.delete(4)
root.print_tree()
