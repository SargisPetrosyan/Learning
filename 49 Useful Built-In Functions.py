"""
abs(), any(), all(), ascci(), bin(), bool(), callable(),
"""
#abs
def abs_func():
    x: float = 3.45
    y: int = -3
    z: float = -2.45
    
    print(abs(x))
    print(abs(y))
    print(abs(z))

#all() return True if all of volues in list are True.
def all_func():
    voult1: list[int] = [1,1,1,1,1]
    voult2: list[int] = [1,1,1,1,0]
    voult3: list[int] = [0,0,0,0,0]
    
    print(all(voult1))
    print(all(voult2))
    print(all(voult3))

#any() return True if any of volues in list are True
def any_func():
    voult1: list[int] = [1,1,1,1,1]
    voult2: list[int] = [1,1,1,1,0]
    voult3: list[int] = [0,0,0,0,0]
    
    print(any(voult1))
    print(any(voult2))
    print(any(voult3))

#ascii() When you want to include characters that are outside the ASCII range
def ascii_funct():
    print(ascii("®"))

#represent character with binery code
def bin_func():
    print(bin(1))
    print(bin(10))
    print(bin(2))
    print(bin(3_000_000))

#convert volue to boolian type 1,"bob" is true adn 0, "", {} are none
def bool_func():
    print(bool({}))
    print(bool("ok"))

#check if callable or not print() is callable, x= 10 is not callable
def callable_func():
    x = 10
    print((f"""
    function classes are callble I call 
    
    callable: print() {callable(print)}
    
    Not callable: x=10 {callable(x)}
    
    """))









if __name__ == "__main__":
    # abs_func()
    # all_func()
    # any_func()
    # ascii_funct()
    # bin_func()
    # bool_func()
    callable_func()


