def F(n):
    if n == 1:
        return 2
    else:
        return 2 * F(n - 1) + n**2


def main():
    n = int(input("Digite um valor para n: "))
    
    if n < 1:
        print("Por favor, digite um valor inteiro maior ou igual a 1.")
    else:
        resultado = F(n)
        print(f"F({n}) = {resultado}")


if __name__ == "__main__":
    main()