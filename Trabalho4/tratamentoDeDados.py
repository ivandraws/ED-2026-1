try:
    with open("nomes100k.txt", "r") as f:
        contend = f.read()
        lista = contend.split("\n")
        for i in range(len(lista)):
            lista[i] = lista[i].lower()
        print(lista[-3:-1])
        
except FileNotFoundError:
    print("Arquivo não encontrado")

try:
    with open("nomes100kmin.txt", "w") as f:
        for i in range(len(lista)):
            f.write((lista[i] + "\n"))
except Exception as e:
    print(f"Erro inesperado: {e}")