class House:
    """Main class"""

    def __init__(self, builder) -> None:
        self.window: str = builder.window
        self.door: str = builder.door
        self.roof: str = builder.roof
        self.noise_protect: bool = builder.noise_protect

    def __repr__(self):
        return f"HouseBuilder(window={self.window}, door={self.door}, \
                roof={self.roof}, noise_protect={self.noise_protect})"

    def __str__(self):
        return f"House class use HouseBUilder to build it "


class HouseBuilder:
    """builder class that building House class part by part"""

    def __init__(self):
        self.window: str = None
        self.door: str = None
        self.roof: str = None
        self.noise_protect: str = None

    def set_window(self, window: str):
        self.window = window
        return self

    def set_door(self, door: str):
        self.door = door
        return self

    def set_roof(self, roof: str):
        self.roof = roof
        return self

    def set_roof(self, roof: str):
        self.roof = roof
        return self

    def set_noise_protect(self, noise_protect: bool):
        self.noise_protect = noise_protect
        return self

    def built(self):
        return House(self)

    def __repr__(self):
        return f"HouseBuilder(window={self.window}, door={self.door}, \
                roof={self.roof}, noise_protect={self.noise_protect})"

    def __str__(self):
        return f"HouseBuilder class to create House clase"


# Building process step by step you can seperate object creation process
house_1 = HouseBuilder()
house_1.set_door("mettal").set_window("duble")
house_1.set_roof("flat").set_noise_protect(True)

# this will return HouseBuild method becouse built() function wasnt called
print(house_1)

house = house_1.built()

# this will return House object becouse built() is calling House() class
print(house)


# Director class controlling building process you can set some sample of Houses
class Director:
    def __init__(self, builder):
        self.biuilder = builder

    # sample of one story house
    def one_story_house(self):
        self.biuilder.set_window("duble").set_door("dubble").set_roof(
            "flat"
        ).set_noise_protect(True).built()


house_2 = HouseBuilder()
director = Director(house_2)

one_story_house = director.one_story_house()

print(house_2.window)
