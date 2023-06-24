from FighterClass import *


class Human(Fighter):
    def __init__(self, name):
        super().__init__(200, 40, 50, 65, 15, 1.5, 100, 20, 30, 40, 20)
        self._name = name


class Goblin(Fighter):
    def __init__(self, name):
        super().__init__(150, 20, 25, 30, 25, 1.6, 150, 10, 15, 25, 15)
        self._name = name


class Orc(Fighter):
    def __init__(self, name):
        super().__init__(400, 40, 60, 75, 10, 1.3, 90, 30, 40, 55, 25)
        self._name = name


class Mage(Fighter):
    def __init__(self, name):
        super().__init__(225, 50, 75, 80, 20, 1.5, 80, 50, 60, 80, 30)
        self._name = name

    # the mage has a special ability: if he rests he has a 15% chance of dealing 30 damage to the enemy
    def rest(self, target):
        if (self._stamina + self._recoverystamina) > self._maxstamina:
            self._stamina = self._maxstamina
        else:
            self._stamina += self._recoverystamina
        special = random.randint(0, 100)
        if special >= 15:
            target.receive_damage(0)
        else:
            target.receive_damage(30)


# the healer has 5 better potions
class Healer(Fighter):
    def __init__(self, name):
        super().__init__(200, 15, 25, 30, 20, 1.5, 150, 35, 45, 60, 25)
        self._name = name
        self._potions = 5

    def heal(self, target):
        if self._potions > 0:
            self._potions -= 1   # consume a potion
            if(self._maxhp - self._hp) < 65:
                self._hp = self._maxhp
            else:
                self._hp += 65
            target.receive_damage(0)
        else:
            self.rest(target)


# the trickster has a 10% chance of dodging the attack, receiving no damage
class Trickster(Fighter):
    def __init__(self, name):
        super().__init__(175, 35, 40, 55, 25, 1.2, 150, 30, 40, 50, 25)
        self._name = name

    def recieve_damage(self, damage):
        dodge = random.randint(0, 100)
        if dodge > 10:  # in case the trickster didn't manage to dodge the attack
            super().receive_damage(damage)
