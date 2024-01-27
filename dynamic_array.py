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
        if(index<0 or index>=self.size):
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
    
    def delete_at(self,index):
        if(index<0 or index>=self.size):
            raise IndexError("Index out of bounds")
        for i in range(index,self.size):
            self.static_array[i]=self.static_array[i+1]
        self.size-=1


class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.array = [0]*2
    def resize(self):
        self.capacity*=2
        tempArray = [0]*self.capacity
        #Copy elements to temp array
        for i in range(self.length):
            tempArray[i] = self.array
        self.array = tempArray
        
    def append(self, n):
        if self.length == self.capacity:
            self.resize()
        # resized array now
        self.array[self.length] = n
        self.length +=1

    def popback(self):
        if(self.length > 0):
            self.length-=1
    def insert(self, index, element):
        # validate index
        if(index > self.capacity or index < 0):
            raise IndexError('No such error')
            self.array[index] = element
        # if the array is full, then create 2*x array
        if(self.length == self.capacity):
            self.resize()
        '''
            input - [1,2,3,4,5,.,.,.]
            insert(100,1)
            the array will start filling elements from n till index + 1 leaving index empty
            Now just cake
        '''
        for i in range(self.length, index ,-1):
            self.array[i] = self.array[i-1]
        self.array[index] = element
        self.length+=1
            
    def remove(self,index):
        if(index >= self.length or index < 0):
            raise IndexError('Error')
        # popback op
        if(index == self.length -1):
            self.popback()
            return
        '''
            input - [1,2,4,5,6]
            remove(2)
            Same array start flling from index to the length-1
        '''
        for i in range(index, length-1):
            self.array[i] = self.array[i+1]
        self.length -= 1
    
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

#print(myarray.static_array)
#myarray.remove()
print(myarray.static_array)
#myarray.clear()
myarray.delete_at(10)
print(myarray.size)
#print(myarray.get(5))
print(myarray.static_array)
