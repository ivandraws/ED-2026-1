sal = float(input("Digite seu salário: "))
# Em porcentagem
taxas = [27.5, 22.5, 15, 7.5, 0]

print("Impostos a pagar: ", end="")

if sal > 4664.69:
    print(f"R$ {(sal * (taxas[0] / 100)) - 896:.2f}")
elif sal > 3751.06:
    print(f"(R$ {(sal * (taxas[1] / 100)) - 662.77:.2f}")
elif sal > 2826.66:
    print(f"(R$ {(sal * (taxas[2] / 100)) - 381.44:.2f}")
elif sal > 2259.21:
    print(f"R$ {(sal * (taxas[3] / 100)) - 158.40:.2f}")
else:
    print("Isento")