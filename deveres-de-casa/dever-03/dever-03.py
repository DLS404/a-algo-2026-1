"""
Verificação recursiva se um array é palíndromo.
"""

ARRAY_EXAMPLES = [
    [0, 1, 2, 3, 2, 1, 0],
    ["a", "b", "b", "a"],
    ["a", "b", "c", "b", "a"],
    ["a", "b", "c", "f", "b", "a"]
]


class PalindromeChecker:
    """
    Classe responsável por verificar se um array é palíndromo.
    """

    def is_palindrome(self, array, left, right):
        """
        Verifica recursivamente se o array é palíndromo.
        """

        if left >= right:
            return True

        if array[left] != array[right]:
            return False

        return self.is_palindrome(array, left + 1, right - 1)


def main():
    """
    Executa os testes com os arrays de exemplo.
    """

    checker = PalindromeChecker()

    for array in ARRAY_EXAMPLES:
        result = checker.is_palindrome(array, 0, len(array) - 1)

        if result:
            print(f"{array} -> É palíndromo")
        else:
            print(f"{array} -> Não é palíndromo")


if __name__ == "__main__":
    main()