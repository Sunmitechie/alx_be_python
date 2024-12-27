user = int(input("ener the size of the pattern:"))
rows = user
columns = user
for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, columns + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks
