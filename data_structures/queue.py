from typing import Any

class CircularQueue():
    DEFAULT_CAPACITY:int = 10
    def __init__(self):
        self._size:int = 0
        self._front:int = 0
        self._data:list[Any] = [None] * CircularQueue.DEFAULT_CAPACITY
        
    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def first(self)-> Any:
        if self._size == 0:
            raise ValueError("list is empty")
        return  self._data[self._front]
    
    def dequeue(self):
        if self._size == 0:
            raise ValueError("list is empty")
        answer: Any = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self.size -= 1
        return answer
        
    def enqueue(self, element:Any)-> None:
        if self._size > len(self._data):
            self._resize(2* len(self._data))
        index: int = (self._front +self._size) % len(self._data)
        self._data[index] =element
        self.size += 1
        
    def _resize(self, size):
        old:list[Any] = self._data
        self._data:list[Any] = [None]*size
        walk = self._front
        
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1)% old
        self._front = 0
            
        
        