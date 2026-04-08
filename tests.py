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
        self.assertEqual(self.hero.life, 0)
        self.hero.increase_stat(StatType.VITALITY, 5)
        self.assertEqual(self.hero.life, 25)


if __name__ == "__main__":
    unittest.main()
