#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254
import math
data = input("Please enter some data and then press the Enter Key")
print("You entered:" + data)
print("\n\n\n")
question = "How much is the radius"
response = input(question)
answer = 4 * math.pi * 3**3 / 3
print(answer)
