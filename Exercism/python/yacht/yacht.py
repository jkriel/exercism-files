"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

import random

# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None

class Die:
    def __init__(self, face = None):
        self.face = random.randint(1,6)



hand = []
for x in range(5):
    hand.append(Die())

for x in range(5):
    print(hand[x].face)

# class HandRoll:
    

#     def __init__(self, hand):
#         self.hand = []

#     def Roll(self):
#         for x in range(5):
#             self.hand.append[Die.face]
#         print(self.hand[::1])        

def score(dice, category):
    pass

