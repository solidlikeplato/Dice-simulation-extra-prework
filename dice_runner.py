import operator
from dice_sim import DiceSimulator


num_dice = 2
dice_size = 6
success_value = 9
success_operator = operator.ge
operators = {
    'ge': '>=',
    'gt': '>',
    'le': '<=',
    'lt': '<',
    'eq': '='
}

roller = DiceSimulator(num_dice=num_dice, dice_size=dice_size)

probability = roller.get_probability(success_value=success_value, success_operator=success_operator)

print("Thanks for using our dice simulator")
print(f"The probability of rolling a value {operators[operator.ge.__qualname__]} {success_value} when rolling {num_dice} {dice_size} sided dice is approximately {probability:.3f}")