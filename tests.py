from ast import Attribute
from unittest.mock import patch
import unittest

from entities import *


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Entity("Dummy", 1)

    def test_stat_increase(self):
        self.hero.increase_stat(StatType.STRENGTH, 5)
        self.assertEqual(self.hero.stats.strength, 5)

    def test_stat_increase_error(self):
        with self.assertRaises(AttributeError):
            self.hero.increase_stat("strongth", 5)

    def test_life(self):
        self.assertEqual(self.hero.max_life, 0)
        self.hero.increase_stat(StatType.VITALITY, 5)
        self.assertEqual(self.hero.max_life, 25)

    def test_take_damage(self):
        self.hero.take_damage(10)
        self.assertEqual(self.hero.current_life, self.hero.max_life - 10)

    def test_attack(self):
        enemy = Enemy("Evil Person", 1)
        with patch("entities.random", return_value=0):
            enemy.attack(self.hero)
        self.assertEqual(self.hero.current_life, self.hero.max_life - 10)

    def test_attack_miss(self):
        enemy = Enemy("Evil Person", 1)
        with patch("entities.random", return_value=1):
            enemy.attack(self.hero)
        self.assertEqual(self.hero.current_life, self.hero.current_life)

    def test_apply_effect(self):
        self.hero.apply_effect(Effect(10, 0, 0, 0))
        self.assertEqual(self.hero.stats.strength, 10)
        self.assertEqual(self.hero.stats.dexterity, 0)


if __name__ == "__main__":
    unittest.main()
