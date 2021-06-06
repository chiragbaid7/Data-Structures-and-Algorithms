class Dynamic_Array:
    
    def __init__(self):
        self.capacity=4
        self.static_array=[None]*self.capacity
        self.size=0

    def _increase_capacity(self):
        self.capacity*=2
        temp=self.static_array
        self.static_array=[None]*self.capacity

        for i in range(len(temp)):
            self.static_array[i]=temp[i]

    def add(self,element):

        if(self.size==self.capacity):
            self._increase_capacity();
        self.static_array[self.size]=element
        self.size+=1

    def size(self):
        return self.size

    def get(self,index):
        if(index<0 or index>self.size):
            raise IndexError("Index out of bounds")
        return self.static_array[index]

    def remove(self):
        self.static_array[self.size-1]=None
        self.size-=1

    def clear(self):
        self.capacity=4
        self.static_array=[None]*self.capacity
        self.size=0
        
    def insert_at(self,index,element):
        if(self.size==self.capacity):
            self._increase_capacity()
            #increase the capacity of the capacity
        if(index>self.size or index<0):
            raise IndexError('No Index exists');
        
        for i in range(self.size,index,-1):        
            self.static_array[i]=self.static_array[i-1]
        self.static_array[index]=element
        self.size+=1

myarray=Dynamic_Array()

myarray.add(3)
myarray.add(4)
myarray.add(5)
myarray.add(6)
myarray.add(8)

myarray.add(10)
myarray.add(11)
myarray.remove()
myarray.add(99)
myarray.remove()
myarray.remove()
print(myarray.size)

#print(myarray.static_array)
#myarray.remove()
#myarray.clear()

myarray.insert_at(100,80)
print(myarray.static_array)
