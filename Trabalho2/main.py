def menu():
    '''
    ### Função do Menu de Terminal
    '''
    print("------Loren Ipsum Sit Dolor Amen------")
    print("1. Chamar pessoa para atendimento")
    print("2. Carregar arquivo TXT para armazenamento de fila (ou eu tento usar minhas habilidade em pandas ?)")
    print("0. Sair\n")
    choice = int(input())

    match (choice):
        case 1:
            print("Digite o nome da pessoa: ")
            print("É prioridade ? ")
        case 2:
            lerArquivos()
        case 0:
            return

def lerArquivos():
    '''
        ### Função para ler arquivos TXT
    '''
    arquivo = str(input("Digite o nome do arquivo, junto com a extensão presente na pasta ""Trabalho2"" para leitura: "))
    try:
        with open(arquivo, 'r') as f:
            content = f.read()
            
    except FileNotFoundError:
        print("Arquivo não existe. Tente novamente...")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    
        
    
if __name__ == "__main__":
    menu()
