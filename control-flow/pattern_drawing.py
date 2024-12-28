size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Outer loop for rows
while row < size:
    # Inner loop for columns (using for loop)
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to the next line
    print()  # Move to the next row (new line)
    row += 1
