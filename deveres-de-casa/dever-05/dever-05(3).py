#Parte 3 da atividade
import math

# T(n) = 2T(n/4) + sqrt(n)
def T1(n):
    if n <= 1:
        return 1
    return 2*T1(n//4) + math.sqrt(n)

# T(n) = 2T(n/4) + n
def T2(n):
    if n <= 1:
        return 1
    return 2*T2(n//4) + n

# T(n) = 16T(n/4) + n^2
def T3(n):
    if n <= 1:
        return 1
    return 16*T3(n//4) + n**2


valores = [4, 16, 64, 256]

print("T1:")
for v in valores:
    print(v, T1(v))

print("\nT2:")
for v in valores:
    print(v, T2(v))

print("\nT3:")
for v in valores:
    print(v, T3(v))