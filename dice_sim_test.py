import unittest
from dice_sim import DiceSimulator
import operator

class DiceSimTestCase(unittest.TestCase):
    def setUp(self):
        self.d6_roller = DiceSimulator()
        self.d10_roller = DiceSimulator(dice_size=10)

    def test_default_probability_roll_exactly_1_on_1d6(self):
        roller = self.d6_roller

        calculated_prob = roller.get_probability()
        exact_prob = 1.0/6.0

        self.assertAlmostEqual(calculated_prob, exact_prob, places=2)

    def test_probability_with_1d10(self):
        roller = self.d10_roller

        calculated_prob = roller.get_probability()
        exact_prob = 1.0/10.0

        self.assertAlmostEqual(calculated_prob, exact_prob, places=2)

    def test_probability_with_2d10(self):
        roller = self.d10_roller
        roller.set_num_dice(2)

        calculated_prob = roller.get_probability(success_value=2)
        exact_prob = 1.0/100.0

        self.assertAlmostEqual(calculated_prob, exact_prob, places=2)

    def test_greater_than_or_equal_1_on_1d6(self):
        roller = self.d6_roller

        calculated_prob = roller.get_probability(success_value=1, success_operator=operator.ge)
        exact_prob = 1

        self.assertAlmostEqual(calculated_prob, exact_prob, places=2)

    def test_greater_than_5_on_1d6(self):
        roller = self.d6_roller

        calculated_prob = roller.get_probability(success_value=5, success_operator=operator.gt)
        exact_prob = 1.0/6.0

        self.assertAlmostEqual(calculated_prob, exact_prob, places=2)

    def test_less_than_or_equal_2_on_2d6(self):
        roller = self.d6_roller
        roller.set_num_dice(2)

        calculated_prob = roller.get_probability(success_value=2, success_operator=operator.le)
        exact_prob = 1.0/36.0

        self.assertAlmostEqual(calculated_prob, exact_prob, places=2)
    
    def test_less_than_13_on_2d6(self):
        roller = self.d6_roller
        roller.set_num_dice(2)

        calculated_prob = roller.get_probability(success_value=13, success_operator=operator.lt)
        exact_prob = 1

        self.assertAlmostEqual(calculated_prob, exact_prob, places=2)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
