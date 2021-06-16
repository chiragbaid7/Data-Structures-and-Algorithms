class Node:
    def __init__(self,data):
        self.data=data 
        self.children=[]

class N_Array: 
    def __init__(self):
        self.root=None 
        self.size=0

    def __find_node(self,key,node):
        if(node.data==key):
            return node 
        for child in node.children:
            parent=self.__find_node(key,child) 
            if(parent!=None):
                return node 
        return None 

    def insert(self,data,key=None):
        #1st insert root element 
        if(self.root==None):
            self.root=Node(data)    
        else:
            #return node of that key and then append 
            node=self.__find_node(key,self.root);
            if(node==None):
                raise ValueError("No key exists")
            else:
                node.children.append(Node(data))
        self.size+=1

    def print_util(self,parent):
        if(parent==None):
            print("No element")
            return 
        print(parent.data)
        for node in parent.children:
            self.print_util(node)
        return 
   
    def print(self):
        self.print_util(self.root)
   
    def length(self):
        print(f'total elements is:{self.size} ')

root=N_Array()
root.insert(10)
root.insert(20,10)
root.insert(70,20)
root.insert(60,20)
root.insert(50,60)
root.insert(40,60)
root.insert(10,60)
root.insert(30,10)
root.insert(80,30)

root.insert(40,10)
root.print()

root.length()

"""
           10
          /\  \ 
         20 30  40
         /\    \ 
        70 60   80 
           /\ \ 
         50 40 10
""" 
