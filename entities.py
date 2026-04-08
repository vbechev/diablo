from enum import StrEnum
from random import random


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


class Entity:
    _BASE_STATS = (0, 0, 0, 0)

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.stats = Stats(*self._BASE_STATS)
        self.current_life = self.max_life

    def increase_stat(self, stat, value):
        self.stats.increase_stat(stat, value)

    @property
    def max_life(self):
        return self.stats.vitality * 5

    @property
    def max_mana(self):
        return self.stats.energy * 5

    def attack(self, entity):
        damage = self.stats.strength // 2
        hit_chance = self.stats.dexterity / 50
        if random() < hit_chance:
            entity.take_damage(damage)

    def take_damage(self, damage):
        self.current_life -= damage


class Enemy(Entity):
    _BASE_STATS = (20, 20, 20, 20)


class Barbarian(Entity):
    _BASE_STATS = (15, 10, 15, 5)


class Sorceress(Entity):
    _BASE_STATS = (5, 10, 10, 15)


ivan = Barbarian("Ivan", 1)
