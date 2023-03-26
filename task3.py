#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
import math
data = input("Please enter some data and then press the Enter Key")
print("You entered:" + data)
print("\n\n\n")
question = "a= b= c=   "
response = input(question)
a = 5
b = 1
c = 11
x = 2
print(f"{response}")
print((c - b)/a)
