from aviao import Aviao
import time

aviao = Aviao()

print("\n")
valor = int(input("Deseja iniciar o programa para controle da pista de decolagem? (1- Sim | 2- Não): "))
if valor == 1:
    print("Iniciando o programa..." "\n")
    time.sleep(2)
else:
    print("O programa não será inicializado")
    exit()

x = 1
while x == 1:
    print("-------------------------- MENU PRINCIPAL ---------------------------")
    opcao = int(input("O que você deseja fazer?" "\n"
    "1- Permitir a decolagem do primeiro avião na fila" "\n"
    "2- Adicionar um avião na fila de decolagem" "\n"
    "3- Mostrar o total de aviões aguardando na fila de decolagem" "\n"
    "4- Listar todos os aviões na fila de decolagem" "\n"
    "5- Listar as características do próximo avião a decolar" "\n"
    "6- Mostrar a posição de um avião conforme o número do voo" "\n"
    "7- Sair" "\n"
    "---------------------------------------------------------------------"
    "\n"
    "Escolha uma opção: "))

    if opcao == 1:
        aviao.decolar()

    if opcao == 2:
        aviao.dados()
        time.sleep(2)

    if opcao == 3:
        aviao.size()

    if opcao == 4:
        aviao.todos()

    if opcao == 5:
        aviao.caracteristicas()

    if opcao == 6:
        aviao.posicao()

    if opcao == 7:
        print("\n""Fechando o programa...")
        time.sleep(2)
        exit()

    if opcao >= 8:
        print("\n""Opção inválida, por favor escolha uma opção válida""\n")
        time.sleep(5)