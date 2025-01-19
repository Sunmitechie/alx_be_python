def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator / denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    except ValueError:
        print(f"Error: Please enter numeric values only.")
def main():
    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")
    result = safe_divide(numerator, denominator)
    print(f"The result of division is {result:.1f}")

if __name__ == "__main__":
    main()
