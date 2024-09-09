# Computers absolutely excel at performing calculations. The “compute” in their name comes from their historical association with providing answers to mathematical questions. Python performs the arithmetic operations of addition, subtraction, multiplication, and division with +, -, *, and /.


# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)

# Prints "2.0"
print(10 / 5)


# Notice that when we perform division, the result has a decimal place. This is because Python converts all ints to floats before performing division. In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division would always round down to the nearest integer..

# Division can throw its own special error: ZeroDivisionError. Python will raise this error when attempting to divide by 0.

# Mathematical operations in Python follow the standard mathematical order of operations.

# Question: 
# Print out the result of this equation: 25 * 68 + 13 / 28

print(25 * 68 + 13 / 28)

# Output:
# 1700.4642857142858


# ---------------------------
# Changing Numbers
# ---------------------------

# Variables that are assigned numeric values can be treated the same as the numbers themselves. Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and literals (like the number 2 in this example). Performing arithmetic on variables does not change the variable — you can only update a variable using the = sign..

coffee_price = 1.50
number_of_coffees = 4

# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price 
coffee_price = 2.00

# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# We create two variables and assign numeric values to them. Then we perform a calculation on them. This doesn’t update the variables! When we update the coffee_price variable and perform the calculations again, they use the updated values for the variable!.

# quilt_width = 8
# quilt_length = 8

# print(quilt_width * quilt_length)

# Output: 64 