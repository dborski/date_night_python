import unittest
from lib.binary_search_tree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_it_exists(self):
        self.assertIsInstance(self.tree, BinarySearchTree)

    def test_head_is_none_by_default(self):
        self.assertEqual(self.tree.head, None)

    def test_insert(self):
        self.assertEqual(self.tree.insert(61, "Bill & Ted's Excellent Adventure"), 0)
        self.assertEqual(self.tree.insert(16, "Johnny English"), 1)
        self.assertEqual(self.tree.insert(92, "Sharknado 3"), 1)
        self.assertEqual(self.tree.insert(50, "Hannibal Buress: Animal Furnace"), 2)
        self.assertEqual(self.tree.insert(60, "Die Hard"), 3)
        self.assertEqual(self.tree.insert(14, "Hot Tub Time Machine"), 2)
        self.assertEqual(self.tree.insert(19, "Catwoman"), 3)

    def test_has_score(self):
        self.assertEqual(self.tree.has_score(3), False)

        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(92, "Sharknado 3"), 1
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(60, "Die Hard")
        self.tree.insert(14, "Hot Tub Time Machine")
        self.tree.insert(19, "Catwoman")

        self.assertEqual(self.tree.has_score(61), True)
        self.assertEqual(self.tree.has_score(16), True)
        self.assertEqual(self.tree.has_score(19), True)
        self.assertEqual(self.tree.has_score(72), False)
        self.assertEqual(self.tree.has_score(15), False)

    def test_depth_of(self):
        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(92, "Sharknado 3")
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(60, "Die Hard")
        self.tree.insert(14, "Hot Tub Time Machine")
        self.tree.insert(19, "Catwoman")

        self.assertEqual(self.tree.depth_of(92), 1)
        self.assertEqual(self.tree.depth_of(50), 2)
        self.assertEqual(self.tree.depth_of(60), 3)
        self.assertEqual(self.tree.depth_of(14), 2)
        self.assertEqual(self.tree.depth_of(13), None)
        self.assertEqual(self.tree.depth_of(87), None)

    def test_max_score(self):
        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(92, "Sharknado 3")
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(60, "Die Hard")
        self.tree.insert(14, "Hot Tub Time Machine")
        self.tree.insert(19, "Catwoman")

        expected = {
            "Sharknado 3": 92
        }

        self.assertEqual(self.tree.max(), expected)

    def test_min_score(self):
        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(92, "Sharknado 3")
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(60, "Die Hard")
        self.tree.insert(14, "Hot Tub Time Machine")
        self.tree.insert(19, "Catwoman")

        expected = {
            "Hot Tub Time Machine": 14
        }

        self.assertEqual(self.tree.min(), expected)

    def test_sort(self):
        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(97, "Shrek")
        self.tree.insert(92, "Sharknado 3")
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(15, "Die Hard")

        expected = [
            {"Die Hard": 15},
            {"Johnny English": 16},
            {"Hannibal Buress: Animal Furnace": 50},
            {"Bill & Ted's Excellent Adventure": 61},
            {"Sharknado 3": 92},
            {"Shrek": 97}
        ]

        self.assertEqual(self.tree.sort(), expected)

    def test_load(self):
        expected = [
            {'Meet My Valentine': 17},
            {'A Place on Earth 20, All That Glitters': 39},
            {'Experimenter': 55},
            {'French Dirty': 75},
            {'Airforce One': 99}
        ]

        self.assertEqual(self.tree.load("./source/movies_truncated.txt"), 5)
        self.assertEqual(self.tree.sort(), expected)

    def test_health(self):
        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(92, "Sharknado 3"), 1
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(98, "Animals United")
        self.tree.insert(58, "Armageddon")
        self.tree.insert(36, "Bill & Ted's Bogus Journey")
        self.tree.insert(93, "Bill & Ted's Excellent Adventure")
        self.tree.insert(86, "Charlie's Angels")
        self.tree.insert(38, "Charlie's Country")
        self.tree.insert(69, "Collateral Damage")

        self.assertEqual(self.tree.health(0), [[61, 11, 100]])
        self.assertEqual(self.tree.health(1), [[16, 5, 45], [92, 5, 45]])
        self.assertEqual(self.tree.health(2), [[50, 4, 36], [86, 2, 18], [98, 2, 18]])
        self.assertEqual(self.tree.health(3), [[36, 2, 18], [58, 1, 9], [69, 1, 9], [93, 1, 9]])

    def test_leaves(self):
        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(92, "Sharknado 3")
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(98, "Animals United")
        self.tree.insert(58, "Armageddon")
        self.tree.insert(36, "Bill & Ted's Bogus Journey")
        self.tree.insert(93, "Bill & Ted's Excellent Adventure")
        self.tree.insert(86, "Charlie's Angels")
        self.tree.insert(38, "Charlie's Country")
        self.tree.insert(69, "Collateral Damage")
        self.tree.insert(35, "Snowpiercer")

        self.assertEqual(self.tree.leaves()[0], 5)

    def test_height(self):
        self.tree.insert(61, "Bill & Ted's Excellent Adventure")
        self.tree.insert(16, "Johnny English")
        self.tree.insert(92, "Sharknado 3")
        self.tree.insert(50, "Hannibal Buress: Animal Furnace")
        self.tree.insert(98, "Animals United")
        self.tree.insert(58, "Armageddon")
        self.tree.insert(36, "Bill & Ted's Bogus Journey")
        self.tree.insert(93, "Bill & Ted's Excellent Adventure")
        self.tree.insert(86, "Charlie's Angels")
        self.tree.insert(38, "Charlie's Country")
        self.tree.insert(69, "Collateral Damage")
        self.tree.insert(35, "Snowpiercer")

        self.assertEqual(self.tree.height(), 4)

