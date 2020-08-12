import time 
from singly_linked_list import LinkedList

n = 100000

l = []
ll = LinkedList()

start_time = time.time()
for i in range(n):
    l.append(i) # O(1)
end_time = time.time()
print(f"Adding {n} elements to list took {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    ll.add_to_tail(i) # O(1)
end_time = time.time()
print(f"Adding {n} elements to linked list took {end_time - start_time} seconds")

start_time = time.time()
# O(n^2)
for i in range(n): # O(n)
    l.pop(0) # O(n)
end_time = time.time()
print(f"List pop from front took {end_time - start_time} seconds")

start_time = time.time()
# O(n)
for i in range(n): # O(n)
    ll.remove_head() # O(1)
end_time = time.time()
print(f"Linked list remove from front took {end_time - start_time} seconds")