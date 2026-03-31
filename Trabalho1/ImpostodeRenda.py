import os

class impostoRenda():
    def __init__(self, salario):
        self.salario = salario

        lista_valoresMinimos = [2259.20, 2826.65, 3751.05, 4664.68]
        lista_aliquota = [0, 0.075, 0.15, 0.225, 0.275]
        lista_parcela = [0, 158.40, 381.44, 662.77, 896]


        if self.salario <= 0:
            print("Não é possível calcular o Imposto de Renda de um salário nulo ou negativo.")
            return

      
        if self.salario > lista_valoresMinimos[-1]:
            imposto = self.salario * lista_aliquota[4] - lista_parcela[4]
            print(
                f"Imposto de R$ {self.salario:.2f} com taxa {lista_aliquota[4]*100:.1f}% "
                f"e dedução de R$ {lista_parcela[4]:.2f} = R$ {imposto:.2f}"
            )
            print(f"Total de IR: R$ {imposto:.2f}")
            return

       
        for i in range(4):  
            if self.salario <= lista_valoresMinimos[i]:
                imposto = self.salario * lista_aliquota[i] - lista_parcela[i]
                print(
                    f"Imposto de Renda de R$ {self.salario:.2f} com taxa {lista_aliquota[i]*100:.1f}% "
                    f"e dedução de R$ {lista_parcela[i]:.2f} = R$ {imposto:.2f}"
                )
                print(f"Total de IR: R$ {imposto:.2f}")
                return
            

def limpa_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ---------------- MENU INTERATIVO ----------------

while True:
    limpa_tela()
    print("\n===== CALCULADORA DE IMPOSTO DE RENDA =====")
    print("1 - Calcular Imposto de Renda")
    print("2 - Sair do Programa")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            salario = float(input("Digite o valor do salário: R$ "))
            impostoRenda(salario)
            input("Pressione enter para voltar para o menu...")

        elif opcao == 2:
            print("Encerrando o programa... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione enter para voltar para o menu...")

    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        input("Pressione enter para voltar para o menu...")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        input("Pressione enter para voltar para o menu...")