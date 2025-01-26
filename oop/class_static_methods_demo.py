class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to calculate the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to calculate the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
