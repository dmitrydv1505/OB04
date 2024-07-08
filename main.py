# Шаг 1: Создание абстрактного класса Weapon
from abc import ABC, abstractmethod


class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):

    def attack(self):
        return "удар мечом"


class Bow(Weapon):

    def attack(self):
        return "удар из лука"

# Шаг 3: Модификация класса Fighter

class Fighter:

    def __init__(self, weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon

    def fight(self, monster):
        print("Боец выбирает", type(self.weapon).__name__ + ".")
        print("Боец наносит", self.weapon.attack() + ".")
        print("Монстр побежден!")

# Шаг 4: Реализация боя
class Monster:
    pass

# Создаем бойца и монстра
fighter = Fighter(Sword())
monster = Monster()

# Бой
fighter.fight(monster)

# Смена оружия и новый бой
fighter.changeWeapon(Bow())
fighter.fight(monster)

