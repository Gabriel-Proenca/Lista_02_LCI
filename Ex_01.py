import math 

entrada = input("Digite uma lista de 15 números, separados por vírgula: ")

numeros = [float(x) for x in entrada.split(',')]

for i in range(len(numeros)):
    if numeros[i] < 0 :
        numeros[i] = -1
    else:
        numeros[i] = math.sqrt(numeros[i])

formatados = ','.join(map(str,numeros))

print("\nValores armazenados:", formatados)