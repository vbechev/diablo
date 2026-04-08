class Stats:
    def __init__(self, strength, dexterity, vitality, energy):
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy


class Hero:
    _BASE_STATS = (0, 0, 0, 0)

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.stats = Stats(*self._BASE_STATS)

    def increase_stat(self, stat, value):
        pass


class Barbarian(Hero):
    _BASE_STATS = (15, 10, 15, 5)


class Sorceress(Hero):
    _BASE_STATS = (5, 10, 10, 15)


ivan = Barbarian("Ivan", 1)
