'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        
    def length(self):
        if not self.head:
            return 0
        res = 0
        tmp = self.head
        while tmp:
            res += 1
            tmp = tmp.next
        return res
            
            

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.length() - 1:
            return -1
        tmp = self.head
        counter = 0
        while counter < index:
            tmp = tmp.next
            counter += 1
        return tmp.data
            
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        
        if not self.head:
            self.head  = new_node
            return
            
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length():
            return
        
        
        elif index == self.length():
            self.addAtTail(val)
            return
            
        elif index == 0:
            self.addAtHead(val)
            return
            
        new_node = Node(val)
        tmp = self.head
        counter = 0
        while counter < index - 1:
            counter += 1
            tmp = tmp.next
        new_node.next = tmp.next
        tmp.next = new_node
            
            
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index < 0 or index > self.length() - 1:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        counter = 0
        tmp = self.head
        while counter < index - 1:
            counter += 1
            tmp = tmp.next
        
        tmp.next = tmp.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
