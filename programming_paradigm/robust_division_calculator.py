import sys
def safe_divide(numerator, denominator):
     try:
          numerator=float(numerator)
          denominator=float(denominator)
          return numerator/denominator
     except ZeroDivisionError:
       return ["Error: Cannot divide by zero."]
     except ValueError:
       return ["Error: Please enter numeric values only."] 
if __name__ == "__main__":
     main()
def main():
     numerator = input("Enter the numerator: ")
     denominator = input("Enter the denominator: ")
     result = safe_divide(numerator, denominator)
     if result is not None:
          print(f"The result of divison is {result}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
