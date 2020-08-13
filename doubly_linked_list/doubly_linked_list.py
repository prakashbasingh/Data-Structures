"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value # creates a node object based on the data/value we passed in
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    #prepend
    def add_to_head(self, value):
         # creating a new node
        new_node = ListNode(value)
        # if there is no head and tail then
        if self.head is None and self.tail is None:
            #assigning new_node to the head and tail
            self.head = new_node
            self.tail = new_node
            self.length += 1
            #now linking nodes together
            self.head.next = new_node
            self.head.prev = None
            self.tail.next = None
            self.tail.prev = new_node
        # if there is a head and pointing to a certain value
        else:
            # assign the current head's prev value to the new_node
            self.head.prev = new_node
            # assign the new node's next value to the current head
            new_node.next = self.head
            # assign the current head to the new node
            self.head = new_node
            # incrementing the length
            self.length += 1
            # returning the added head
            return self.head
        # # or or or
        # # if there is no head
        # if self.head is None:
        #     # then create new node
        #     new_node = ListNode(value)
        #     # now new has .prev to None
        #     new_node.prev = None
        #     # setting new_node as head
        #     self.head = new_node
        # #if there is a list 
        # else:
        #     #create new_node
        #     new_node = ListNode(value)
        #     # now previous head should .prev to new_node 
        #     self.head.prev = new_node
        #     # .next of new_node now should point to original head
        #     new_node.next = self.head
        #     # now setting new_node as head
        #     self.head = new_node
        #     # and pointing .prev of new_node to None because new_node is Head now
        #     new_node.prev = None

            
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # # if there is no head
        # if self.head is None:
        #     return None
        # # if there is head
        # else:
        #     # storing value of head that is going to be removed
        #     value = self.head.value
        #     # setting new head which is next to the removed_head
        #     self.head = self.head.next
        #     # setting the .prev of new head to None
        #     self.head.prev = None
        #     # decrementing the length
        #     self.length -= 1
        #     #returning the removed head value
        #     return value 
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    
    # append
    def add_to_tail(self, value):
         # creating a new node
        new_node = ListNode(value)
        # if there is no head and tail then
        if self.head is None and self.tail is None:
            #assigning new_node to the head and tail
            self.head = new_node
            self.tail = new_node
            self.length += 1
            #now linking nodes together
            self.head.next = new_node
            self.head.prev = None
            self.tail.next = None
            self.tail.prev = new_node
        # if there is a tail
        else:
            # setting tail.next to new_node
            self.tail.next = new_node
            #setting new node.prev to the tail
            new_node.prev = self.tail
            # setting teh tail to new_node
            self.tail = new_node
            # now setting tail.next to None
            self.tail.next = None
            # and incrementing the length
            self.length+= 1
        # # or or or
        # # if there is no head
        # if self.head is None:
        #     #creating a new node
        #     new_node = ListNode(value)
        #     # setting .prev of new_node to None
        #     new_node.prev = None
        #     # making new_node head
        #     self.head = new_node
        # else: # if there is already node in the list
        #     # need to create new node
        #     new_node = ListNode(value)
        #     # now retreating from head until we reach the tail
        #     # and to achieve that we need to set current place to head
        #     current = self.head
        #     # while current.next is not None  keep going until the tail node whose next is None
        #     while current.next:
        #         # keep going to the next node until reaches the Null
        #         current = current.next
        #     # setting new-node to the current tail pointing .next from old .next  from current node
        #     current.next = new_node
        #     # once reaches the null seting .prev of new_nod to the current/old tail
        #     new_node.prev = current
        #     # now it is tail and  need to set new_node.next to None
        #     new_node.next = None
            
            
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # # if there is no tail
        # if self.tail is None:
        #     return None
        # # if there is tail
        # else:
        #     # storing value of tail that is going to be removed
        #     value = self.tail.value
        #     # setting new tail as old tail.prev
        #     self.tail = value.prev
        #     # setting the tail.next to None
        #     self.tail.next = None
        #     # decrementing the length
        #     self.length -= 1
        #     #returning the removed tail value
        #     return value 
        value = self.tail.value
        self.delete(self.tail)
        return value
        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # # checking if node is head
        # if self.head == node:
        #     return
        # # now checking if node is tail
        # if self.tail == node:
        #     self.tail = self.tail.prev
        #     # now setting tail.next to None
        #     self.tail.next = None
        # # else:
        # #     # setting node.prev.next = node.next
        # #     node.prev.next = node.next
            
        # #setting node.next to head
        # self.head.prev = node
        # #setting node.prev to None
        # node.next = self.head
        # # set head.prev to node
        # node.prev = None
        # # setting head to node
        # self.head = node
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # #checking if node passed is tail
        # if self.tail == node:
        #     return
        # # checking if node passed is head
        # if self.head == node:
        #     self.head = self.head.next
        #     self.head.prev = None
        # # else:
        # #     # setting node.prev.next = node.next
        # #     node.prev.next = node.next
        
        # #setting node.next to tail
        # self.tail.prev = node
        # #setting node.prev to None
        # node.prev = self.tail
        # # set tail.prev to node
        # node.next = None
        # # setting tail to node
        # self.tail = node
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # is there anything to delete?
        if self.head is None and self.tail is None:
            return
        # check if there's only one node 
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # check if the node is the head 
        elif node is self.head:
            self.head = node.next
            node.delete()
        # check if the node is the tail 
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # otherwise, the node is some node in the middle 
        else:
            node.delete()
        # don't forget to decrement the length 
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if the list is empty, return None 
        if self.head is None and self.tail is None:
            return
        # keep track of the largest value we've seen so far 
        max_value = self.head.value
        # traverse the entirety of the linked list 
        current = self.head.next
        
        while current is not None:
            # if we see a value > the largest value we've seen so far 
            if current.value > max_value:
                # update the largest value 
                max_value = current.value
            # update current to point to the next node 
            current = current.next
        # return the largest value 
        return max_value
    
    
    # printing method to print value in the nodes   
    def print_list(self):
        # lets say current node is the head of the list
        current_node = self.head
        # while current node is not null
        while current_node:
            # print the value/data in the head of current node
            print(current_node.value)
            # and if next is not null point to next node
            current_node = current_node.next
    
    
dllist = DoublyLinkedList()
dllist.add_to_head(0)
dllist.add_to_tail(1)
dllist.add_to_tail(2)
dllist.add_to_tail(3)
dllist.add_to_tail(4)
dllist.add_to_tail(5)
dllist.add_to_head(15)

dllist.print_list()