class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None 

class Hashtable:
    def __init__(self,size=10):
        self.table_size=size 
        self.table=[None]*self.table_size
        self.cs=0

    def __hash(self,key):
        """
        prime number is considered to 
        have keys distributed uniformly
        """
        index=0
        prime=1
        for i in range(len(key)):
            index+=(ord(key[i])*prime)%self.table_size
            prime=(prime*27)%self.table_size
        return (index)%self.table_size

    def __setitem__(self,key,val):
        """
        seprate chaining is used to handle collisions
        Linked list is the data struture and nodes are 
        inserted to the head
        """
        index=self.__hash(key)
        node=Node(key,val)
        node.next=self.table[index]
        self.table[index]=node 

    def __getitem__(self,key):
        index=self.__hash(key)
        try:
            temp=self.table[index]
            if(temp==None):
                raise KeyError("Key is not present")
            while(temp):
                if(temp.key==key):
                    return temp.val
                temp=temp.next
            raise KeyError("key is not present")
        except Exception as e:
            raise(e)

d=Hashtable(5)
d["chirag"]=12
d["chirag"]=14
d["mahesh"]=12
d["rahul"]=8.3
print(d["chirag"])
print(d["rahul"])
#print(d["cirag"])
