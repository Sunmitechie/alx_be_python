def safe_divide(numerator, denominator):
     try:
          numerator=float(numerator)
          denominator=float(denominator)
          return numerator/denominator
     except ZeroDivisionError:
       return ["Error: Cannot divide by zero."]
     except ValueError:
       return ["Error: Please enter numeric values only."] 

def main():
     numerator = input("Enter the numerator: ")
     denominator = input("Enter the denominator: ")
     result = safe_divide(numerator, denominator)
     if result is not None:
          print(f"Result: {result}")
