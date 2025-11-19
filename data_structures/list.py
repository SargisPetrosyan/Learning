import ctypes
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
    
    def pop(self):
        if self._size == 0:
            raise IndexError("cant pop from empty list")
        pop_value = self._array[-1]
        self._array[-1] = None
        return pop_value
    
    def remove(self,element:Any) -> None:
        for i in range(self._size):
            if self._array[i] == element:
                for k in range(i, self._size-1):
                    self._array[k]= self._array[k+1]
                self._array[self._size -1] = None
                self._size -= 1
                return
        raise ValueError("value was not found")
    
    def _resize(self,capacity:int)->None :
        new_array: ctypes.Array[ctypes.py_object[Any]] = self._make_array(capacity)
        for k in range(self._size):
            new_array[k] = self._array[k]
        self._array = new_array
        self._capacity = capacity
        
    def _make_array(self,c:int) -> ctypes.Array[ctypes.py_object]:
        return(c*ctypes.py_object)()


new_array = DynamicArray()

new_array.append(2)
new_array.append(3)
new_array.append(5)
new_array.append(8)
new_array.append(9)
new_array.remove(3)

print(len(new_array))
