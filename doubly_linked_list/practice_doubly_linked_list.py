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
        # printing method to print value in the nodes   
            
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
        # if there is no head
        if self.head is None:
            # then create new node
            new_node = ListNode(value)
            # now new has .prev to None
            new_node.prev = None
            # setting new_node as head
            self.head = new_node
        #if there is a list 
        else:
            #create new_node
            new_node = ListNode(value)
            # now previous head should .prev to new_node 
            self.head.prev = new_node
            # .next of new_node now should point to original head
            new_node.next = self.head
            # now setting new_node as head
            self.head = new_node
            # and pointing .prev of new_node to None because new_node is Head now
            new_node.prev = None
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    
    # append
    def add_to_tail(self, value):
        # if there is no head
        if self.head is None:
            #creating a new node
            new_node = ListNode(value)
            # setting .prev of new_node to None
            new_node.prev = None
            # making new_node head
            self.head = new_node
        else: # if there is already node in the list
            # need to create new node
            new_node = ListNode(value)
            # now retreating from head until we reach the tail
            # and to achieve that we need to set current place to head
            current = self.head
            # while current.next is not None  keep going until the tail node whose next is None
            while current.next:
                # keep going to the next node until reaches the Null
                current = current.next
            # setting new-node to the current tail pointing .next from old .next  from current node
            current.next = new_node
            # once reaches the null seting .prev of new_nod to the current/old tail
            new_node.prev = current
            # now it is tail and  need to set new_node.next to None
            new_node.next = None
            
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
        
    def add_after_node(self, key, value):
        # setting current as surrent state
        cur = self.head
        # setting while loop
        while cur:
            # if .next of current which is head is none and current data is provided key
            if cur.next is None and cur.value == key:
                # then adding new_node after the original node using add_to_tail(prepend) method
                self.add_to_tail(value)
                return # return to loop out 
            # if we reach ti the current data and data matches the key
            elif cur.value == key:
                # create new node
                new_node = ListNode(value)
                #this is naming pointer to the current next which we are manipulating and later it will point o new_node
                nxt = cur.next
                # now current,next is pointing to new_node
                cur.next = new_node
                # now setting .next of new_node to cur.next which is same as original .next current
                new_node.next = nxt
                # setting .prev of new_node to point cur 
                new_node.prev = cur
                # also previous nxt.prev is now pointing to new_node
                nxt.prev = new_node
            #updating pointer from head to null
            cur = cur.next    

    
    def add_before_node(self, key, value):

        # setting current as surrent state
        cur = self.head
        # setting while loop,  if there is only one node and that is head
        while cur:
            # if .next of current which is head is none and current data is provided key
            if cur.next is None and cur.value == key:
                # then adding new_node after the original node using add_to_tail(prepend) method
                self.add_to_head(value)
                return # return to loop out 
            # if we reach ti the current data and data matches the key
            elif cur.value == key:
                # create new node
                new_node = ListNode(value)
                #this is naming pointer to the current prev which we are manipulating and later it will point to new_node
                prev = cur.prev
                # now previous.next is pointing to new_node
                prev.next = new_node
                # now setting current.previous pointer to  new_node
                cur.prev = new_node
                # setting .next of new_node to point cur 
                new_node.next = cur
                # also previous nxt.prev is now pointing to new_node
                new_node.prev = prev
            #updating pointer from head to null
            cur = cur.next 
            
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.value == key and cur == self.head:
                #case 1: removing head node and has no other node
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                #case 2: removing head that is connected with another node
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.value == key:
                # case 3: removing node in between nodes
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # case 4: removing tail
                else:
                    prev = cur.prev
                    prev.nest = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
            
# learned from :- https://www.youtube.com/watch?v=Am5u1vaT0x0&list=PL5tcWHG-UPH3nDinW5u_oRcNv6hwhY7ET&index=3
                
            
    
dllist = DoublyLinkedList()
dllist.add_to_head(0)
dllist.add_to_tail(1)
dllist.add_to_tail(2)
dllist.add_to_tail(3)
dllist.add_to_tail(4)
dllist.add_to_tail(5)
dllist.add_to_head(15)

dllist.add_after_node(2, 22)
dllist.add_after_node(4, 555)
dllist.add_after_node(5, 777)

dllist.add_before_node(5, 888)
dllist.add_after_node(555, 111)

dllist.delete(0)

dllist.print_list()