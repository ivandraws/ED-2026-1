import unicodedata
import re

letrasSpe = list()

def otimizador(texto:str):
    texto = texto.strip()
    texto = texto.replace(' ', '')
    textoLower = texto.lower()
    texto_tratato = unicodedata.normalize('NFKD', textoLower)
    textoSemAcento = texto_tratato.encode('ASCII', 'ignore').decode('utf-8')
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', textoSemAcento)
    return texto_limpo

def trataArquivo(nome: str):
    try:
        with open(nome, "r") as f:
            contend = f.read()
            lista = contend.split("\n")
            for i in range(len(lista)):
                lista[i] = otimizador(lista[i])
                if not lista[i].isalnum():
                    for j in range(len(lista[i])):
                        if not lista[i][j].isalnum() and lista[i][j] not in letrasSpe:
                            letrasSpe.append(lista[i][j])
            if len(letrasSpe) > 0:        
                print(letrasSpe)

    except FileNotFoundError:
        print("Arquivo não encontrado")

    try:
        with open(f"min{nome}", "w") as f:
            for i in range(len(lista)):
                if i == len(lista) - 1:
                    f.write(lista[i])
                else:
                    f.write((lista[i] + "\n"))
    except Exception as e:
        print(f"Erro inesperado: {e}")