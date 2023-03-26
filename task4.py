#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
data = input("Please enter some data and then press the Enter Key")
print("You entered:" + data)
print("\n\n\n")
question = "How much is height and radius "
response = input(question)
L = math.sqrt(3**2 + 5**2)
answer = math.pi * 3 * L
print(answer)