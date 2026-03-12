import time

TEST_VALUES = [10, 100, 500, 900]


class FactorialCalculator:

    def factorial(self, number):
        if number == 0 or number == 1:
            return 1

        return number * self.factorial(number - 1)


def measure_execution_time(number):

    calculator = FactorialCalculator()

    start_time = time.time()
    calculator.factorial(number)
    end_time = time.time()

    return end_time - start_time


def main():

    user_number = 5

    calculator = FactorialCalculator()
    result = calculator.factorial(user_number)

    print(f"\nFatorial de {user_number} = {result}\n")
    print("Tempo de execução para diferentes valores de n:\n")

    for value in TEST_VALUES:
        execution_time = measure_execution_time(value)
        print(f"n = {value} -> tempo = {execution_time:.6f} segundos")


if __name__ == "__main__":
    main()