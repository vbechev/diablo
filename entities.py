from enum import StrEnum


class StatType(StrEnum):
    STRENGTH = "strength"
    DEXTERITY = "dexterity"
    VITALITY = "vitality"
    ENERGY = "ENERGY"


class Stats:
    def __init__(self, strength, dexterity, vitality, energy):
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy

    def increase_stat(self, stat, value):
        current_value = getattr(self, stat)
        setattr(self, stat, current_value + value)


class Hero:
    _BASE_STATS = (0, 0, 0, 0)

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.stats = Stats(*self._BASE_STATS)

    def increase_stat(self, stat, value):
        self.stats.increase_stat(stat, value)


class Barbarian(Hero):
    _BASE_STATS = (15, 10, 15, 5)


class Sorceress(Hero):
    _BASE_STATS = (5, 10, 10, 15)


ivan = Barbarian("Ivan", 1)
