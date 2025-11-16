import ctypes
from tkinter import NO
from typing import Any

class DynamicArray():
    def __init__(self) -> None:
        self._size:int = 0
        self._capacity:int = 1
        self._array: ctypes.Array[ctypes.py_object] = self._make_array(self._capacity)
        
    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, index: int) -> Any:
        if not 0 <= index < self._size:
            raise IndexError('invalid_index')
        return self._array[index]
    
    def append(self,obj) -> None:
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        self._array[self._size] = obj
        self._size += 1
        
    def _resize(self,capacity:int)->None :
        new_array: ctypes.Array[ctypes.py_object[Any]] = self._make_array(capacity)
        for k in range(self._size):
            new_array[k] = self._array[k]
        self._array = new_array
        self._capacity = capacity
        
    def _make_array(self,c:int) -> ctypes.Array[ctypes.py_object]:
        return(c*ctypes.py_object)()
    
        
    
    
dinamic_array = DynamicArray()

dinamic_array.append(3)
dinamic_array.append(4)
dinamic_array.append(5)
dinamic_array.append(6)
dinamic_array.append(7)
dinamic_array.append(3)
dinamic_array.append(3)
dinamic_array.append(3)
print(len(dinamic_array))
print(dinamic_array[0])