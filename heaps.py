import math
class Heap:
  def __init__(self, type = 'maxHeap', maxSize = 10):
    self.heapArray = [None]* size
    self.heapSize = 0
    self.maxSize = maxSize
    self.type = type

  def getParentIndex(childIndex):
    return math.floor(childIndex/2)

  def getMax(self):
    return self.heapArray[0] if heapSize > 0 else raise Exception("Heap is empty")

  def compare(self, childIndex, parentIndex):
    if(self.type == 'maxHeap'):
      return self.heapArray[parentIndex] > self.heapArray[childIndex]
    else:
      return self.heapArray[childIndex]<self.heapArray[parentIndex]

  def insert(item):
    '''
      1. Insert item at the end of the array.
      2. Locate its correct position as per heap by comparing with parent: arr[index] , arr[floor(index/2)] till we reach the top
      Time Complexity - O(logN), height of the tree
    '''
    if(self.heapSize> self.maxSize):
      raise Exception("Heap overflow")
    self.heapArray[self.heapSize] = item
    currentElementindex = self.heapSize
    self.heapSize+=1
    parentIndex = self.getParentIndex(currentElementIndex)
    while(currentElementindex!=0 and self.heapArray[currentElementindex]>=self.heapArray[parentIndex]):
      #Swap
      self.heapArray[currentElementindex], self.heapArray[parentIndex] = self.heapArray[parentIndex], self.heapArray[currentElementindex]
      currentElementIndex = parentIndex
      parentIndex = self.getParentIndex(currentElementIndex)
  def swap(self, index1, index2):
    self.heapArray[index1], self.heapArray[index2] = self.heapArray[index2], self.heapArray[index1]
  def heapify(self, parentIndex=0):
    '''
      24
    /   \
    12   33
      Recursively balance the heap property by comparing parent value with its children
      Max Heap 
        - Swap parent with max(left,right)
      Min Heap
        - Swap parent with min(left, right)
    '''
    #we need to keep track which subtree we need to balance
    currentActualIndex = parentIndex
    left = 2*parentIndex+1
    right = 2*parentIndex+2
    if(left<=self.maxSize -1 and not self.compare(left, currentActualIndex)):
        currentActualIndex = left
    if(right<=self.maxSize-1 and not self.compare(right, currentActualIndex)):
        currentActualIndex = right
    if(currentActualIndex!=parentIndex):
      self.swap(currentActualIndex, parentIndex)
      self.heapify(currentActualIndex)
    return
    
  def remove(self):
    '''
      Remove the max/min Element - root node
      1. Swap the root node value with last element and pop the element.
      2. Balance the tree - Heapify()
    '''
    lastIndex = self.heapSize - 1
    self.heapArray[0], self.heapArray[lastIndex] = self.heapArray[lastIndex], self.heapArray[0]
    self.heapArray[lastIndex] = None
    self.heapify()

h = Heap()
