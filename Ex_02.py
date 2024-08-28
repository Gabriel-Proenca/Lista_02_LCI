import math 

soma = 0

x_graus = float(input("Digite o valor de x em graus: "))

x_rad = math.radians(x_graus)

for n in range(15):
    termo = ((-1) **n) * (x_rad ** (2 * n + 1)) / math.factorial(2* n + 1)
    soma += termo

print(f"O seno de {x_graus} é : {soma}")