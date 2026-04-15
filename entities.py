from enum import StrEnum
from random import random
from typing import Self


class StatType(StrEnum):
    STRENGTH = "strength"
    DEXTERITY = "dexterity"
    VITALITY = "vitality"
    ENERGY = "ENERGY"


class Stats:
    def __init__(self, strength: int, dexterity: int, vitality: int, energy: int):
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy

    def increase_stat(self, stat: StatType, value: int):
        current_value = getattr(self, stat)
        setattr(self, stat, current_value + value)

    def __getitem__(self, index):
        return [self.strength, self.dexterity, self.vitality, self.energy][index]

    def __add__(self, other):
        return Stats(*(left + right for left, right in zip(self, other)))


class Effect:
    def __init__(self, *stats):
        self.stats = stats


class Entity:
    _BASE_STATS = (0, 0, 0, 0)

    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level
        self.stats = Stats(*self._BASE_STATS)
        self.current_life = self.max_life

    def increase_stat(self, stat: StatType, value: int):
        self.stats.increase_stat(stat, value)

    @property
    def max_life(self) -> int:
        return self.stats.vitality * 5

    @property
    def max_mana(self):
        return self.stats.energy * 5

    def attack(self, entity):
        damage = self.stats.strength // 2
        hit_chance = self.stats.dexterity / 50
        if random() < hit_chance:
            entity.take_damage(damage)

    def take_damage(self, damage: float):
        self.current_life -= damage

    def apply_effect(self, effect):
        self.stats += effect.stats


class Enemy(Entity):
    _BASE_STATS = (20, 20, 20, 20)


class Barbarian(Entity):
    _BASE_STATS = (15, 10, 15, 5)


class Sorceress(Entity):
    _BASE_STATS = (5, 10, 10, 15)
