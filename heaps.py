'''
For a node at index i in the array:

Parent index → (i - 1) // 2

Left child index → 2*i + 1

Right child index → 2*i + 2
https://chatgpt.com/c/68cd8008-a64c-8333-84a4-a00d96a1f4ae
'''
import math

class Heap:
  def __init(self, isMin = True):
    self.heap = []
    self.isMin = isMin

  def push(self, value):
    # append the value to last position
    #perform heapify up to put the element to right position - by comparing its parent O(logN)
    self.heap.append(value)
    self._heapify_up(len(self.heap)-1)

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
  
  def __getParent(self, childIndex):
    return (childIndex-1)//2

  def _leftChild(self, index):
    return (2*index)+1

  def _rightChild(self, index):
    return (2*index)+2

  def __compare(self, childValue, parentValue):
    # not follwowing the invariant property then return true
    return childValue < parentValue if self.isMin else childValue > parentValue
    
  
  def __heapify_up(self, currentIndex):
    #compare with parent
    parentIndex = self.__getParent(currentIndex)
    while( currentIndex > 0 and self.__compare(self.heap[currentIndex], parentIndex):
      #if true then swap
      self._swap(currentIndex, parentIndex)
      currentIndex = parentIndex

  def pop(self): #pop, heapify down on max or min heap
    if not self.heap:
      return IndexError("Pop from empty heap")

    root = self.heap[0]
    self.heap[0] = self.heap.pop() #move the last element to top, jaan puch kar to mess up
    self._heapify_down(0) #now maintain the heap property
    return root
        
  def _heapify_down(currentIndex):
    best = currentIndex
    leftChild, rightChild = self._leftChild(currentIndex), self._rightChild(currentIndex)
    # on each subtree we compare and satisfy the heap variant property
    if leftChild < len(self.heap) and self._compare(self.leftChild, best):
      best = leftChild
    if rightChild < len(self.heap) and self._compare(self.rightChild, best):
      best = rightChild
    if best!=currentIndex:
      self._swap(best, currentIndex)
      self._heapify_down(best)


h = Heap()
