class InventoryItem:
    def __init__(self, name, quentity) -> None:
        self.name = name
        self.quentity = quentity

    def __str__(self) -> str:
        return f"name:{self.name} and quentity:{self.quentity}"

    def __repr__(self) -> str:
        return f"InventoryItem(name = {self.name}, quentity = {self.quentity})"

    def __add__(self, other: object):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quentity + other.quentity)
        raise ValueError("cannot add items of tifferent types")

    def __sub__(self, other: object):
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.quentity >= other.quentity:
                return InventoryItem(self.name, self.quentity - other.quentity)
            raise ValueError("cannot subtract more than available quentity")
        raise ValueError("cannot add items of tifferent types")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, int(self.quentity * factor))
        raise ValueError("Multiplication factor must be number")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quentity == other.quentity
        return False

    def __gt__(self, other: object):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quentity > other.quentity
        raise ValueError("cannot add items of tifferent types")


item_1 = InventoryItem("apple", 40)
item_2 = InventoryItem("apple", 70)
item_3 = InventoryItem("pinch", 10)
item_4 = InventoryItem("pinch", 30)

result = item_1 < item_2
print(result)
