# Step 1
average = 0

# Step 2
total = 0

# Step 3
howManyEntered = 0

# Step 4
print("How many test scores would you like to average?")

# Step 5
howMany = int(input())

# Step 6
print("Enter test score: ")

# Step 7
testScore = int(input())

# Step 8
total = total + testScore

# Step 9
howManyEntered = howManyEntered + 1

# Step 10
while howManyEntered < howMany:
    # Steps 6 to 9 repeated inside the loop
    print("Enter test score: ")
    testScore = int(input())
    total = total + testScore
    howManyEntered = howManyEntered + 1

# Step 11
average = total / howMany

# Step 12
print("The average for the test scores you entered is: ")

# Step 13
print(average)
