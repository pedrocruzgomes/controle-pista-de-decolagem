import time
from itertools import zip_longest

class Aviao:
    def __init__(self):
        self.fila = []
        self.fila2 = []

    def decolar(self):
        if self.fila == []:
            print("\n""A fila de decolagem está vazia, por favor insira um avião na fila de decolagem""\n")
            time.sleep(5)
        else:
            print("\n""O avião no começo da fila irá decolar!")
            print("Ele possui as seguintes características: " "\n"+str(self.fila.pop()))
            print("\n")
            self.fila2.pop()
            time.sleep(7)

    def dados(self):
        modelo_aviao = str(input("\n""Informe o modelo do avião: "))
        self.modelo_aviao = modelo_aviao
        empresa_aviao = str(input("Informe a empresa aérea responsável pelo avião: "))
        self.empresa_aviao = empresa_aviao
        origem_aviao = str(input("Informe a origem do voo para o avião: "))
        self.origem_aviao = origem_aviao
        destino_aviao = str(input("Informe o destino do voo para o avião: "))
        self.destino_aviao = destino_aviao
        passageiros_aviao = int(input("Informe a quantidade de passageiros presentes no avião: "))
        self.passageiros_aviao = passageiros_aviao
        voo_aviao = int(input("Informe o número do voo: "))
        print(f"O voo de número {voo_aviao} foi adicionado na fila de decolagem!" "\n")
        self.voo_aviao = voo_aviao
        tudo = "Modelo: " +modelo_aviao, "Empresa: " +empresa_aviao, "Origem: " +origem_aviao, \
               "Destino: " +destino_aviao, "Número de Passageiros: " +str(passageiros_aviao), \
               "Número do voo: " +str(voo_aviao)
        self.fila.insert(0, tudo)
        self.fila2.insert(0, voo_aviao)

    def size(self):
        if len(self.fila) >= 1:
            print("\n""Número de aviões aguardando na fila de decolagem: " +str(len(self.fila))+ "\n")
            time.sleep(5)
        else:
            print("\n""Não há nenhum avião aguardando na fila de decolagem")
            print("\n")
            time.sleep(5)

    def todos(self):
        def elementos(i, iteracao, valor="x"):
            return zip_longest(*[iter(iteracao)] * i, fillvalue=valor)
        if self.fila == []:
            print("\n""Não há nenhum avião na fila de decolagem")
            print("\n")
            time.sleep(2)
        else:
            print("\n")
            print("Os aviões na fila de decolagem são: ")
            for saida in elementos(1, self.fila):
                print(saida)
            print("\n")
            time.sleep(10)

    def caracteristicas(self):
        if self.fila == []:
            print("\n""Não há nenhum avião na fila de decolagem para mostrar suas características")
            print("\n")
            time.sleep(5)
        else:
            print("\n""O próximo avião a decolar possui as seguintes características: " 
                  "\n"+str(self.fila[len(self.fila)-1])+ "\n")
            time.sleep(7)

    def posicao(self):
        if self.fila2 == []:
            print("\n""Não há nenhum avião na fila de decolagem para mostrar sua posição")
            print("\n")
            time.sleep(5)
        else:
            print("\n""Esses são os aviões conforme número de voo estão na fila de decolagem: " +str(self.fila2))
            escolha = str(input("Escolha um número de voo para saber onde ele está na fila de decolagem: "))
            fila2 = self.fila2
            posicao = fila2.index(int(escolha))
            print(f"O avião com o número de voo {escolha} está na posição {posicao} na fila de decolagem""\n")
            time.sleep(7)