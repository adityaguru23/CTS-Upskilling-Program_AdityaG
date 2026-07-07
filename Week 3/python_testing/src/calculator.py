class SimpleCalculator:
    def __init__(self):
        self.memory = 0

    def sum(self, x, y):
        return x + y

    def quotient(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

    def store(self, value):
        self.memory += value

    def show_memory(self):
        return self.memory

    def reset_memory(self):
        self.memory = 0

calc = SimpleCalculator()

print(calc.sum(15, 5))
print(calc.quotient(20, 4))

calc.store(50)
print("Memory:", calc.show_memory())

calc.reset_memory()
print("Memory after reset:", calc.show_memory())