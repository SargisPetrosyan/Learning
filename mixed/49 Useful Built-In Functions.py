import json
from typing import Iterator, Any

"""
abs(), any(), all(), ascci(), bin(), bool(), callable(), complex(),  dict()

dir(), divmod(), enumerate(), eval(), exec(), filet(), float(), help(), isinstance()

issubclass(), iter(), len(), list(), map(), min(), max(), open(), ord(), pow(), print()

range(), zip(), type(), tuple(), sum(), str(), sorted(), slice(), set(), round(), reverse(),

repr(), 


"""


# abs
def abs_func() -> None:
    x: float = 3.45
    y: int = -3
    z: float = -2.45

    print(abs(x)) # output: 3
    print(abs(y)) # output: 3
    print(abs(z)) # output: 2


# all() return True if all of voles in list are True.
def all_func() -> None:
    voult1: list[int] = [1, 1, 1, 1, 1]
    voult2: list[int] = [1, 1, 1, 1, 0]
    voult3: list[int] = [0, 0, 0, 0, 0]

    print(all(voult1)) # output True
    print(all(voult2)) # output False
    print(all(voult3)) # output True


# any() return True if any of voles in list are True
def any_func() -> None:
    voult1: list[int] = [1, 1, 1, 1, 1] # output True
    voult2: list[int] = [1, 1, 1, 1, 0] # output True
    voult3: list[int] = [0, 0, 0, 0, 0] # output False

    print(any(voult1))
    print(any(voult2))
    print(any(voult3))


# ascii() When you want to include characters that are outside the ASCII range
def ascii_func():
    print(ascii("®")) # output \xae


# represent character with binary code
def bin_func() -> None:
    print(bin(1))
    print(bin(10))
    print(bin(2))
    print(bin(3_000_000))


# convert volue to boolian type 1,"bob" is true adn 0, "", {} are none
def bool_func():
    print(bool({}))
    print(bool("ok"))


# check if callable or not print() is callable, x= 10 is not callable
def callable_func() -> None:
    x: int = 10
    print(
        (
            f"""
    function classes are callble I call 
    
    callable: print() {callable(print)}
    
    Not callable: x=10 {callable(x)}
    
    """
        )
    )


# complex function creating complex of numbers
def complex_func() -> None:
    print(complex(5))
    print(complex("3+0j"))


# dict() is converting data of pair to dict
def dict_func():
    contenier: list[tuple[str, int]] = [("a", 2), ("b", 3)]
    contenier_1: list[tuple[str]] = [("a3"), ("b4")]
    print(dict(contenier))
    print(dict(contenier_1))


# dir() is giving methods and names of that file
def dir_func() -> None:
    print(dir(json))


# divmod()
def divmod_func() -> None:
    print(divmod(3, 3))
    print(divmod(2, 3))
    print(divmod(6, 3))


# enumerate
def enumerate_func():
    friends: list[str] = ["Gev", "Edo", "Armush", "Arthur"]
    enumeration: enumerate = enumerate(friends)
    print(list(enumeration))
    print(list(enumeration))


# eval() evaluating code
def eval_func() -> None:
    text: str = input("")
    print(eval(text))


# exec() executing code
def exec_func():
    source: str = """
a:int = 10
b:int = 20
c:int = 30

print(a+b+c)
"""

    exec(source)


# filter()
def filter_func() -> None:
    names: list[str] = ["Saqo", "Saro", "Simba", "bob"]

    s_names: filter = filter(lambda s: s[0].lower() == "s", names)
    print(list(s_names))


# float() converting everything to float:
def float_func():
    print(float())
    print(float(5))
    print(float(0))
    print(float(True))


# frozenset()
def frozenset_func() -> None:
    fs: frozenset = frozenset({1, 2, 3, 5})
    print(hash(fs))


"""
A regular set cannot be inside another set, 
but a frozenset can because it is hashable.
Enable Fast Lookups (O(1) Time Complexity
"""


# help() provide information about function
def help_func():
    help(print)


def id_func() -> None:
    """
    func() is returning object ID number
    each obect hase uniqe id number even they have same volue:
    ID for each obecj is different
    """
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [1, 2, 3, 4]

    print(list_1 == list_2, list_1 is list_2)
    print(id(list_1))
    print(id(list_2))


# int() converting voule to integer
def int_func() -> None:
    print(int(2.4))
    print(int(4.5))
    print(int(4.9))


# isinstance checking volue class type
def isinstance_func() -> None:
    mylist: list = 2

    if isinstance(mylist, int):
        print("mylist type is int")
    elif isinstance(mylist, str | tuple):
        print("mylist type is string or tuple")
    else:
        print("I dont know this toype")


def issubclass_func() -> None:
    class Parent:
        pass

    class Child(Parent):
        pass

    print(issubclass(Child, Parent))


# iter() creating iterator
def iter_func() -> None:
    mylist: list[int] = [1, 2, 3]
    iterator_1: Iterator[int] = iter(mylist)

    print(next(iterator_1))
    print(next(iterator_1))
    print(next(iterator_1))
    print(list(iterator_1))


# len()
def len_func() -> None:
    print(len("qwert"))
    print(len([1, 2, 3, 4]))
    print(len((1, 2, 3, 4)))
    print(len({"a": 1, "b": 3}))


# list() converting to list
def list_func() -> None:
    print(list((1, 2)))
    print(list({2, 4, 5, 6}))
    print(list("qwertyuiop"))


# map() mapping iterable volues to function
def map_func() -> None:
    all_upper: Iterator[str] = map(lambda s: s.upper(), ["bob", "Jecob"])

    print(list(all_upper))


# max() Returning max vloue for string you can set how to determniate max
def max_func() -> None:
    names: list[str] = ["bob", "Jecob"]
    print(max([1, 2, 3, 4]))
    print(max(names, key=len))


# min() Returning min vloue for string you can set how to determniate min
def min_func() -> None:
    names: list[str] = ["bob", "Jecob"]
    print(min([1, 2, 3, 4]))
    print(min(names, key=len))


# open() working with files
def open_func():
    file: str = "hello.txt"
    with open(file, "r") as f:
        print(f.read())


# ord() return unicode code for character
def ord_func() -> None:
    print(ord("a"))
    print(ord("b"))


# pow is power of number
def pow_func() -> None:
    print(pow(2, 3))
    print(pow(2, 3, 3))


# print() with some aditional options.
def print_func() -> None:
    mylist: list[str] = ["bob", "jack", "jhon"]
    print(*mylist, sep=", ", end=".\n")
    print(1, 2, 3, 4, sep="_")


# range() gives range of numbers
def range_func() -> None:
    normal: range = range(5, 10, 2)
    normal_2: range = range(10, 5, -2)
    print(list(normal))
    print(list(normal_2))


# repr() return representation of object or volue developers need it
def repr_func() -> None:
    print(repr(10))
    print(repr("Representation"))
    print(repr([1, 2, 3, 4]))


# reverse() givs reversed objects
def reverse_func() -> None:
    mylist: list[int] = [1, 3, 2, 5]
    r: Iterator[int] = reversed(mylist)
    print(list(r))


# round() rounding numbers
def round_func() -> None:
    n: float = 1243.54565
    print(round(n, 3))
    print(round(n, 0))
    print(round(n, -2))


# set() converting list or other data storages to unique voules
def set_func() -> None:
    mylist: list[int] = [
        1,
        2,
        2,
        4,
        5,
        6,
    ]
    print(set(mylist))


# slice() can slice list to parts
def slice_func() -> None:
    numbers: list[int] = [1, 3, 4, 5, 9, 7, 8, 9, 2]
    my_slice_1: slice = slice(2, None, 2)
    print(numbers[my_slice_1])


# sorted() sorting numbers
def sorted_func():
    numbers: list = [2, 4, 3, 7, 5, 6]
    print(sorted(numbers))


# str() converting str
def str_func() -> None:
    print(str((2, 3, 4)))


# sum() retuning sum of numbers:
def sum_func() -> None:
    list_1: list[int] = [2, 4, 5, 7, 8]
    print(sum(list_1))


# tuple() converting to touple
def tuple_func() -> None:
    mylist: list[int] = [2, 4]
    print(tuple(mylist))


# Any can set any type
def type_func() -> None:
    elements: list[Any] = [
        "Saqo",
        20,
        False,
        [
            2,
            4,
            5,
        ],
        {7, 8, 5},
    ]
    for _ in elements:
        print(type(_))


# zip() zipping the data
def zip_func() -> None:
    a: list[str] = ["a", "b", "c"]
    b: list[int] = [1, 2, 3]
    c: list[bool] = [False, True, True]

    zipped: Iterator[tuple[str, int, bool]] = zip(a, b, c)
    for a, b, c in zipped:
        print(a, b, c, sep="-")


if __name__ == "__main__":
    # abs_func()
    # all_func()
    # any_func()
    ascii_func()
    # bin_func()
    # bool_func()
    # callable_func()
    # complex_func()
    # dict_func()
    # dir_func()
    # divmod_func()
    # enumerate_func()
    # eval_func()
    # exec_func()
    # filter_func()
    # float_func()
    # frozenset_func()
    # help_func()
    # id_func()
    # int_func()
    # isinstance_func()
    # issubclass_func()
    # iter_func()
    # len_func()
    # list_func()
    # map_func()
    # max_func()
    # min_func()
    # open_func()
    # ord_func()
    # pow_func()
    # print_func()
    # range_func()
    # repr_func()
    # reverse_func()
    # print_func()
    # round_func()
    # set_func()
    # sorted_func()
    # str_func()
    # sum_func()
    # tuple_func()
    # type_func()
    # zip_func()
