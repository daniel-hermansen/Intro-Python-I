# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def isEven(num):
    return num % 2 == 0
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

print("It is even." if isEven (num) else "It is odd")
    