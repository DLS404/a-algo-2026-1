def F(n):
    if n == 1:
        return 2
    else:
        return 2 * F(n - 1) + n**2


def main():
    n = 25  # coloque algum valor até 30 aqui
    resultado = F(n)
    print(f"F({n}) = {resultado}")


if __name__ == "__main__":
    main()
