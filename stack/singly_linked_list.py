class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding 
        self.value = value 
        # reference to the next node in the linked list
        self.next_node = next_node

    # method to get the value of the node 
    def get_value(self):
        return self.value

    # method to get the node's `next_node`
    def get_next(self):
        return self.next_node

    # method to update the node's `next_node` to the input node 
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # printing method to print value in the nodes   
    def print_list(self):
        # lets say current node is the head of the list
        current_node = self.head
        # while current node is not null
        while current_node:
            # print the value/data in the head of current node
            print(current_node.value)
            # and if next is not null point to next node
            current_node = current_node.next_node


    def add_to_tail(self, value):
        # wrap the value in a Node
        new_node = Node(value)
        # check if the Linked List is empty 
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.tail.set_next(new_node)
            # update `self.tail` to point the new node we just added 
            self.tail = new_node

    def remove_tail(self):
        # check if the linked list is empty 
        if self.head is None and self.tail is None:
            return None
 
        # check if the linked list has only one node 
        if self.head == self.tail:
            # store the node we're going to remove's value 
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, the linked list has more than one Node 
        else:
            # store the last Node's value in a nother variable so we can return it 
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last Node
            # the only way we can do this, is by traversing the whole linked list
            # from the beginning 
            
            # starting from the head, we'll traverse down to the second-to-last Node 
            # init another reference to keep track of where we are in the linked 
            # list as we're iterating 
            current = self.head 

            # keep iterating until the node after `current` is the tail
            while current.get_next() != self.tail:
                # keep iterating 
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None) 
            return val

    def remove_head(self):
        # check if the linked list empty 
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node 
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value that we need to return 
            val = self.head.get_value()
            # set `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            # return the old_head's value 
            return val
    
    def add_head(self, value):
        # creating a new node
        new_node = Node(value)
        
        # now .next of new_node should point the original head
        new_node.next_node = self.head
        # now setting new_node as new head
        self.head = new_node
        
    # insert_node method will insert new_node in-between already existing nodes
    def insert_after_node(self, prev_node, value):
        # first check if there is prev_node
        if not prev_node:
            print("Previous node is not in the list")
            return
        # if there is prev_node, create new_node
        new_node = Node(value)
        # now .next of new_node should point to the same 
        # node that .next of prev_node is pointing to
        new_node.next_node = prev_node.next_node
        # now .next of prev_node should point to new_node
        # and original .next of prev-node should be deleted
        prev_node.next_node = new_node
        
llist = LinkedList()
llist.add_to_tail("A")
llist.add_to_tail("B") 
llist.add_to_tail("C") 
llist.add_to_tail("D")
llist.add_head("E")
llist.insert_after_node(llist.head.next_node, "ZZ")

llist.print_list() 