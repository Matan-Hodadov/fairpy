#!python3

"""
Demonstration of the cut-and-choose protocol.

Programmer: Shalev Goldshtein
Since: 2019-11
"""

from agents import *


import ContiguousCakeCutting, logging, sys

ContiguousCakeCutting.logger.addHandler(logging.StreamHandler(sys.stdout))
ContiguousCakeCutting.logger.setLevel(logging.INFO)


print("\n### Example 1: \n")
Erel = ContiguousCakeCutting.PiecewiseConstantAgent([2, 8, 2], name="Erel")
Shalev = ContiguousCakeCutting.PiecewiseConstantAgent([4, 2, 6], name="Shalev")
lstES = [Erel,Shalev]
print(Erel)
print(Shalev)
print()

ContiguousCakeCutting.algor1(lstES)
print()


#################################################################################################


print("\n### Example 2: \n")
ALICE = ContiguousCakeCutting.PiecewiseConstantAgent([11, 22, 33, 44], "ALICE")
BOB = ContiguousCakeCutting.PiecewiseConstantAgent([7, 13, 51, 12], "BOB")
CHARLIE = ContiguousCakeCutting.PiecewiseConstantAgent([60, 31, 18, 3], "CHARLIE")
DANY = ContiguousCakeCutting.PiecewiseConstantAgent([4, 10, 43, 63], "DANY")
lstABCD = [ALICE, BOB, CHARLIE, DANY]
print(ALICE)
print(BOB)
print(CHARLIE)
print(DANY)
print()

ContiguousCakeCutting.algor1(lstABCD)


# the cake for example 2

# 0.0           0.15                            0.55                 0.77               1.0
#  ---------------------------------------------------------------------------------------
#  |             |                               |                     |                 |
#  |             |                               |                     |                 |
#  |             |                               |                     |                 |
#  |   CHARLIE   |              BOB              |         DANY        |      ALICE      |
#  |             |                               |                     |                 |
#  |             |                               |                     |                 |
#  |             |                               |                     |                 |
#  |             |                               |                     |                 |
#  ---------------------------------------------------------------------------------------


####################################################################################################

print()
print("\n### Example 3: \n")

BEN = ContiguousCakeCutting.PiecewiseConstantAgent([4, 10, 20], name="BEN")
GUR = ContiguousCakeCutting.PiecewiseConstantAgent([14, 42, 9, 17], name="GUR")
ION = ContiguousCakeCutting.PiecewiseConstantAgent([30, 1, 12], name="ION")
lstaaa = [BEN,GUR,ION]

print(BEN)
print(GUR)
print(ION)
print()

ContiguousCakeCutting.algor1(lstaaa)
