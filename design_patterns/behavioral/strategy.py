from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def update(self, start: str, end: str) -> None:
        ...
        

class Algorithm1(Strategy):
    def compute_route(start:str, end:str) -> str:
        return f"StrategyA_result: {start} + B + H + {end}"
    
class Algorithm2(Strategy):
    def compute_route(start:str, end:str) -> str:
        return f"StrategyB_result: {start} + B + H + {end}"

class Context():
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self,strategy:Strategy):
        self._strategy= strategy
    
    def do_some_business_logic(self) -> None:
        result = self._strategy.compute_route("A", "L")
        print(result)
        
if __name__== "__main__":
    context = Context(Algorithm1)
    context.strategy = Algorithm2
    context.do_some_business_logic()
    context.strategy = Algorithm1
    context.do_some_business_logic()
    
    



    
