import singly_linked_list 

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
        
#     def __len__(self):
#         self.size = len(self.storage)
#         return self.size
    
#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)
#         return self.storage
    
#     def pop(self):
#         data = None
#         if(len(self.storage) >= 1):
#             data = self.storage.pop()
#         self.size = len(self.storage)
#         return data


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = singly_linked_list.LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.size + 1
        return self.storage.tail.value

    def pop(self):
        data = self.storage.remove_tail()
        if self.size != 0:
            self.size = self.size - 1
        return data
