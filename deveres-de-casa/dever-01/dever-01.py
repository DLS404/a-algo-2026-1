"""
Comparação entre Insertion Sort (O(n²)) e sorted() (Timsort - O(n log n)).
"""

import random
import time

LIST_SIZES = [1000, 5000, 10000, 20000, 50000]


class SortAlgorithms:
    """
    Implementação de algoritmos de ordenação.
    """

    def insertion_sort(self, data):
        """
        Ordena uma lista utilizando o algoritmo Insertion Sort.
        """

        for index in range(1, len(data)):
            key = data[index]
            previous = index - 1

            while previous >= 0 and data[previous] > key:
                data[previous + 1] = data[previous]
                previous -= 1

            data[previous + 1] = key

        return data


def generate_random_list(size):
    """
    Gera uma lista de números aleatórios.
    """

    return [random.randint(0, 100000) for _ in range(size)]


def measure_execution_time(sort_function, data):
    """
    Mede o tempo de execução de um algoritmo de ordenação.
    """

    start_time = time.time()
    sort_function(data)
    end_time = time.time()

    return end_time - start_time


def main():
    """
    Executa os testes de desempenho dos algoritmos.
    """

    sorter = SortAlgorithms()

    for size in LIST_SIZES:

        random_list = generate_random_list(size)

        list_for_insertion = random_list.copy()
        list_for_sorted = random_list.copy()

        insertion_time = measure_execution_time(
            sorter.insertion_sort, list_for_insertion
        )

        sorted_time = measure_execution_time(
            sorted, list_for_sorted
        )

        print(f"\nTamanho da lista: {size}")
        print(f"Insertion Sort: {insertion_time:.6f} segundos")
        print(f"sorted() (Timsort): {sorted_time:.6f} segundos")


if __name__ == "__main__":
    main()