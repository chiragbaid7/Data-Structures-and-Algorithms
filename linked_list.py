from typing import NamedTuple


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head
        self.size=0

    def insert_tail(self,data): #O(n)
        node=self.head
        while(node.next):
            node=node.next
        node.next=Node(data)
        self.size+=1

    def print(self):
        temp=self.head
        while(temp):
            print(f'{temp.data}->',end=' ')
            temp=temp.next
        print()
    def insert_head(self,data): #O(1)
        node=Node(data)
        node.next=self.head
        self.head=node  
        self.size+=1

    def delete_head(self):
        self.head=self.head.next
        self.size-=1    
    
    def remove_at(self,index):
        if(index<0 or index>=self.size):
            raise IndexError('Index out of bounds')

        if(index==0):
            self.delete_head()
        else:
            prev=self.head
            node=prev.next
            pos=1
            while(pos<index):
                prev=node
                node=node.next
                pos+=1
            prev.next=node.next
            self.size-=1

    def insert_at(self,index,data):
        ''' 
        insertion at head takes O(1) whereas 
        for inserting at _ takes O(n) because 
        it has to tarverse each node
        '''
        if(index<0 or index>self.size):
            raise IndexError('Index out of bounds')

        if(index==0):
            self.insert_head(data)

        elif(index==self.size):
            self.insert_tail(data)
            
        else:
            prev=self.head
            pos=1
            while(pos<index):
                prev=prev.next
                pos+=1
            node=Node(data)
            node.next=prev.next
            prev.next =node
            self.size+=1

    def reverse(self):
        prev=None
        next=None 
        curr=self.head
        while(curr):
            next=curr.next  #hard work
            curr.next=prev 
            prev=curr
            curr=next 
        self.head=prev 

    def recursive_reverse(self,head):
        if(head.next==None or head==None ):
            #self.head=head
            return head 
        node=self.recursive_reverse(head.next)
        head.next.next=head 
        head.next=None
        return node
        
List1=LinkedList()
List1.insert_head(3)
List1.insert_head(3)
List1.insert_head(4)
List1.insert_head(13)
List1.insert_tail(14)
List1.insert_tail(16)
List1.insert_tail(17)
List1.delete_head()
List1.insert_at(3,10)
List1.insert_at(1,9)
#List1.insert_at(8,10)
List1.print()
List1.remove_at(1)
List1.print()
List1.remove_at(0)
List1.print()
new_node=List1.recursive_reverse(List1.head);
reverse_List=LinkedList(new_node)
reverse_List.print()