def safe_divide(numerator, denominator):
     try:
          numerator=float(numerator)
          denominator=float(denominator)
          return numerator/denominator
     except ZeroDivisionError as e :
       return ["Error: Cannot divide by zero."]{e}
     except ValueError as e:
         print(f"Non-numeric input {e}")

def main():
     numerator = input("Enter the numerator: ")
     denominator = input("Enter the denominator: ")
     result = safe_divide(numerator, denominator)
     if result is not None:
          print(f"Result: {result}")
