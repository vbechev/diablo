import unittest

from entities import *


class TestHero(unittest.TestCase):
    def test_stat_increase(self):
        hero = Hero("Dummy", 1)
        hero.increase_stat(StatType.STRENGTH, 5)
        self.assertEqual(hero.stats.strength, 5)

    def test_stat_increase_error(self):
        hero = Hero("Dummy", 1)
        with self.assertRaises(AttributeError):
            hero.increase_stat("strongth", 5)


if __name__ == "__main__":
    unittest.main()
