grupo_um = []
grupo_dois = []
grupo_tres = []
verificadores = []
cpfs = []
def main():
    # Pega o cpf em formato de str e converte nas listas separadas como valores int
    cpf = input("Digite um cpf para verificar se ele é válido: ")
    
    # Aloca os dígitos do cpf em seus respectivos grupos
    for i in range(len(cpf)):
        if i < 3:
            grupo_um.append(int(cpf[i]))
            
        elif i < 6:
            grupo_dois.append(int(cpf[i]))
        elif i < 9:
            grupo_tres.append(int(cpf[i]))
        else: 
            verificadores.append(int(cpf[i]))
        cpfs.append(cpf[i])
    
    
    print(f"O seu cpf é: {cpfs[0]}{cpfs[1]}{cpfs[2]}.{cpfs[3]}{cpfs[4]}{cpfs[5]}.{cpfs[6]}{cpfs[7]}{cpfs[8]}-{cpfs[9]}{cpfs[10]}")
    #print(type(grupo_um[0]))
    #print(type(grupo_dois[1]))
    #print(type(grupo_tres[2]))
    #print(type(verificadores[0]))

    if check() == False:
        print("CPF inválido!")
    else:
        print("CPF Válido!")
    return

def check():
    valor = 0
    for i in range(3):
        valor += grupo_um[i] * (10 - i)
        valor += grupo_dois[i] * (7 - i)
        valor += grupo_tres[i] * (4 - i)
    
    # Verificar o verificador[0]. Se der falso, retorne erro para a main() imediatamente!
    if (valor % 11) < 2:
        if verificadores[0] != 0:
            #print("verificador J deu erro.")
            return False
    elif (11 - (valor % 11)) != verificadores[0]:
        #print("verificador J deu erro.")
        return False
    
    # Verificar o verificador[1]
    valor = 0
    for i in range(3):
        valor += grupo_um[i] * (11 - i)
        valor += grupo_dois[i] * (8 - i)
        valor += grupo_tres[i] * (5 - i)
        if i == 0:
            valor += verificadores[0] * 2
    
    if (valor % 11) < 2:
        if verificadores[1] != 0:
            #print("verificador K deu erro")
            return False
        else:
            return True
    elif 11 - (valor % 11) != verificadores[1]:
        #print("verificador K deu erro")
        return False
    
    return True


main()