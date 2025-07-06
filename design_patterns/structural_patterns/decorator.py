from abc import ABC

"""
The Decorator Design Pattern allows dynamic behavior addition to objects without changing their code. 

In this implementation:
- The `Character` class defines basic character behavior.
- `CharacterDecorator` is an abstract base class that wraps a `Character` object, enabling behavior modification.
- Concrete decorators like `FireWarrior`, `ColdWarrior`, and `ShieldWarrior` extend the functionality by adding new features (e.g., fire damage, ice damage, shields).

This pattern promotes flexibility by allowing functionality to be combined at runtime, reducing the need for many subclasses.
"""


class Character(ABC):
    def get_description(self):
        return "warrior"

    def get_damage(self):
        return 50


class CharacterDecorator(Character, ABC):
    def __init__(self, character):
        self._character = character

    def get_description(self):
        pass

    def get_damage(self):
        pass


class FireWarrior(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + "with fire"

    def get_damage(self):
        return self._character.get_damage() + 10


class ColdWarrior(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + "with ice"

    def get_damage(self):
        return self._character.get_damage() + 30


class ShieldWarrior(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + "Shield"

    def get_damage(self):
        return self._character.get_damage() - 10


warrior_1 = Character()
fire_warrior = FireWarrior(warrior_1)
cold_warrior = ColdWarrior(warrior_1)
fire_warrior_shield = ShieldWarrior(fire_warrior)
cold_warrior_shield = ShieldWarrior(cold_warrior)

print(warrior_1.get_damage())
print(fire_warrior.get_damage())
print(cold_warrior.get_damage())
