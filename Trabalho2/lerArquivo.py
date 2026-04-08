from pathlib import Path
from listaEncadeadaSimples import Fila

def lerArquivos(comPrio: Fila, semPrio: Fila):
    '''
        ### Função para ler arquivos TXT

        Pega o arquivo txt (preferencialmente em formato "p1, p2, p3, p4, *p5, p6,*p7, *p8, p9, p10, [...]") e separa as pessoas 
        pela ordem de prioridade

        #### IMPORTANTE!
            O arquivo que deve ser lido deve estar na mesma pasta do programa
    '''
    arquivo = str(input("Digite o nome do arquivo, junto com a extensão presente na pasta ""Trabalho2"" para leitura: "))
    dirAtual = Path(__file__).parent
    dir = dirAtual / arquivo
    
    try:
        with open(dir, 'r') as f:
            
            content = f.read()
            pessoas = content.strip().split(",")
            print(str(content))
            
            for i in range(len(pessoas)):
                pessoas[i] = pessoas[i].replace(" ", "")
            print(pessoas)


            for i in pessoas:
                if i.find("*") != -1:
                    comPrio.enqueue(i)
                else:
                    semPrio.enqueue(i)
            
    except FileNotFoundError:
        print("Arquivo não existe. Tente novamente...")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")