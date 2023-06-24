from abc import ABC
import random


class Fighter(ABC):
    _name: str = None
    _maxhp: float = 0
    _hp: float = 0
    _ltdmg: float = 0  # light attack damage
    _dmg: float = 0  # medium attack damage
    _hdmg: float = 0  # heavy attack damage
    _critchance: float = 0  # critical damage chance
    _critboost: float = 0  # damage boost
    _maxstamina: int = 0
    _stamina: int = 0
    _lastamina: int = 0  # light attack stamina usage
    _mastamina: int = 0  # medium attack stamina usage
    _hastamina: int = 0  # heavy attack stamina usage
    _recoverystamina: int = 0
    _isalive: bool = True
    _potions: int = 3

    def __init__(self, hp, ltdmg, dmg, hdmg, critchance, critboost, stamina,
                 ltstamina, mastamina, hastamina, recoverystamina):
        self._maxhp = self._hp = hp
        self._ltdmg = ltdmg
        self._dmg = dmg
        self._hdmg = hdmg
        self._critchance = critchance
        self._critboost = critboost
        self._recoverystamina = recoverystamina
        self._maxstamina = self._stamina = stamina
        self._ltstamina = ltstamina
        self._mastamina = mastamina
        self._hastamina = hastamina

    def receive_damage(self, damage):
        if (self._hp - damage) <= 0:
            self._hp = 0
            self._isalive = False
        else:
            self._hp -= damage

    def attack(self, target, damage, stamina):
        critical = random.randint(0, 100)

        if self._stamina >= stamina:
            self._stamina -= stamina

            if critical < self._critchance:  # if it's a critical hit
                target.receive_damage(self._critboost * damage)  # critical hit
            else:
                target.receive_damage(damage)

        else:
            target.receive_damage(0)  # no stamina, so enemy doesn't receive damage

    def rest(self, target):  # in case I have low to no stamina, rest might be a good choice
        if (self._stamina + self._recoverystamina) > self._maxstamina:
            self._stamina = self._maxstamina
        else:
            self._stamina += self._recoverystamina
        target.receive_damage(0)

    def heal(self, target):
        if self._potions > 0:
            self._potions -= 1   # consume a potion
            if(self._maxhp - self._hp) < 40:
                self._hp = self._maxhp
            else:
                self._hp += 40
            target.receive_damage(0)
        else:
            self.rest(target)   # no potions left, at lest we should do something and rest a bit

    def getname(self):
        return self._name

    def getalive(self):
        return self._isalive

    def gethp(self):
        return self._hp

    def getldmg(self):
        return self._ltdmg

    def getdmg(self):
        return self._dmg

    def gethdmg(self):
        return self._hdmg

    def getstamina(self):
        return self._stamina

    def getlstm(self):
        return self._ltstamina

    def getstm(self):
        return self._mastamina

    def gethstm(self):
        return self._hastamina

    def getpotions(self):
        return self._potions

    def printdetails(self):
        print(self._name + ": " + str(self._hp) + " hp remaining, " + str(self._stamina) + " stamina remaining")
