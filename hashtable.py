#Implementation  of open hashing
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
            # look through each bucket
            bucket=temp[i]
            if(bucket): # if none then there is no key,value pair there
                while(bucket): # if present then scan the linked list
                    self.__setitem__(bucket.key,bucket.val)
                    bucket=bucket.next

        
    def __setitem__(self,key,val):
        """
        seperate chaining is used to handle collisions
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

# d=Hashtable(5)
# d["chirag"]=12
# d["rani"]=14
# d["mahesh"]=12
# d["hh"]=54
# d["rahul"]=8.3
# print(d["chirag"])
# print(d["rahul"])
#print(d["cirag"])





'''
(k1:v1)
(k2:v2)
(k3:v3)
TODO:
    Create a Hash table where each slot is a Pair(key:value) object.
    Maintain a LF and check that it doesn't crosses threshold during insertion, rehash it then.
    Create a hash function that returns an index for a key, main logic.
Operations:-
    get(key)
    set(key,value)
    delete(key)
'''

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
class hashTable:
    def __init__(self):
        self.size = 0
        self.slots = 10
        self.map = [None] * self.slots

    def __hash(self,key):
        '''
            A good hash function is which reduces the chance of collisions for better performance.
            A prime number is used as a multiplier because of its unique factors. The hash value will not share 
            common patterns with the hash table size.
        '''
        hashValue = 0
        primeNumber = 1
        for i in range(len(key)):
            hashValue+= ((ord(key[i]) * primeNumber) % self.slots)
            primeNumber = (primeNumber * 27) % self.slots
        return hashValue % self.slots
    def __reHash(self):
        '''
            Create a new hashMap with 2* capacity
            Iterate through old map and do insertion ops for each pair in your new map.
        '''
        self.slots*=2
        newMap = [None]*self.slots
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if(pair):
                self.setItem(pair.key, pair.value)

    def setItem(self, key, value):
        '''
            HashTable - [pair1, pair2, pair3]
            1. Get the hashValue.
            2. Create a pair object
            3. If collision then go for quadratic probing
            if key already exists then insert new value for that key
        '''
        try:
            hashValue = self.__hash(key)
            while True:
                # If key if not present, insert it in the slot, check loadfactor as well
                if self.map[hashValue] == None:
                    self.map[hashValue] =  Pair(key, value)
                    self.size+=1
                    loadFactor = self.size / self.slots
                    if(loadFactor >= 0.75):
                        print("reHashing happenindg", key)
                        self.__reHash()
                    return
                # If key is already present, update the value and return
                elif self.map[hashValue].key == key:
                    self.map[hashValue].value = value
                    return
                # If the slot returned by hash function is occupied --> collision --> quadratic probing
                hashValue = (hashValue * hashValue) % self.slots
        except Exception as e:
            print(e)

    def getItem(self, key):
        '''
            If no key present then return None
            If the key is not present in the given slot that means it was inserted during collision
            so we must do update the hash value and check if the key is present in new slot
        '''
        hashValue = self.__hash(key)
        while self.map[hashValue] != None:
            if(self.map[hashValue].key == key):
                return self.map[hashValue].value
            hashValue = (hashValue * hashValue) % self.slots
        return None
        
    def __setitem__(self, key, value):
        self.setItem(key, value)
    
    def __getitem__(self, key):
       return self.getItem(key)
    
d = hashTable()
d["chirag"] = 23
d["ganesh"] = 22
d["mitestgh"] = 21
d["rajesh"] = 22
d["hsdfkh"] = 22
d["mNanegs"] =22
d["faman"] =21
d["rabad"] =21

print(d.map)

