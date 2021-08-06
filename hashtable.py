

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
    def __rehash(self):
        #1.create a table of size 2n
        #2.copy all the contents into new table rehash
        old_table_size=self.table_size
        self.table_size=2*self.table_size
        #temp is to rehash all elements to new table
        temp=self.table
        self.table=[None]*self.table_size
        self.cs=0
        for i in range(old_table_size):
            bucket=temp[i]
            if(bucket):
                while(bucket):
                    self.__setitem__(bucket.key,bucket.val)
                    bucket=bucket.next

        #3.delete the old table
        
    def __setitem__(self,key,val):
        """
        seprate chaining is used to handle collisions
        Linked list is the data struture and nodes are 
        inserted at the head
        """
        index=self.__hash(key)
        node=Node(key,val)
        node.next=self.table[index]
        self.table[index]=node 
        self.cs+=1
        load_factor=self.cs/self.table_size
        if(load_factor>0.75):
            self.__rehash()

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
d["rani"]=14
d["mahesh"]=12
d["hh"]=54
d["rahul"]=8.3
print(d["chirag"])
print(d["rahul"])
#print(d["cirag"])
