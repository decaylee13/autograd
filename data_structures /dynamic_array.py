from typing import Generic, TypeVar 
#track size and capacity, and resize by doubling


T = TypeVar("T")
class DynamicArray(Generic[T]):
    def __init__(self, initial_capacity): 
        self.capacity = 4 if initial_capacity < 4 else initial_capacity
        self.size = 0 
        self.arr = [None] * self.capacity

    def _resize(self, new_capacity): 
        new_arr = [None] * new_capacity
        for i in range(self.size): 
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity 

    def append(self, x):
        if self.size == self.capacity: 
            self._resize(self.capacity * 2) 
        self.arr[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0: 
            return None
        ele = self.arr[self.size - 1] 
        self.arr[self.size - 1] = None 
        self.size -= 1 
        if self.size > 0 and self.size == self.capacity // 4: 
            self._resize(self.capacity // 2) 
        return ele
        


    def get(self, i):
        return self.arr[i]

    def insert(self, i, x): #(shift right)

    def remove(self, i): #(shift left)

    def __len__(self):

    def __iter__(self):

