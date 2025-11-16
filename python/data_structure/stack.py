from hmac import new
from queue import Empty
from typing import Any


class ArrayStack():
    def __init__(self) -> None:
        self._data:list[Any] = []
        
    def __len__(self) -> int:
        return len(self._data)
        
    def is_empty(self) -> bool:
        if len(self._data) == 0:
            return True
        else:
            return False
        
    def push(self,element:Any) -> None:
        self._data.append(element)
    
    def pop(self) -> Any:
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data.pop()
    
    def top(self) -> Any:
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data[-1]
    
    def __repr__(self) -> str:
        return str(self._data)
        
    