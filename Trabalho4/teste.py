import random

# Configurações
quantidade = 50000
limite_superior = 1000000

# Gerando a lista
numeros = [random.randint(0, limite_superior) for _ in range(quantidade)]

# Salvando em um arquivo
with open("numeros.txt", "w") as f:
    for i in range(len(numeros)):
        f.write(str(numeros[i])+"\n")

print(f"Lista com {quantidade} números gerada com sucesso!")