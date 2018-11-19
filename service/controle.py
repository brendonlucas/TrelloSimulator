from modelo.modelos import *

class Controle:

    def __init__(self):
        self.nada = ""
        self.quadros = []
        self.trello = Trello()
        self.quadro_atual = ""

    def criar_quadro(self, titulo):
        self.trello.criar_quadro(self.quadros, titulo)

    def seleciona_quadro(self, quadro_solicitado):
        for i in range(len(self.quadros)):
            quadro_atual = self.quadros[i][0]
            if quadro_atual == quadro_solicitado:
                self.quadro_atual = self.quadros[i]
                return True
        return False

    def criar_lista(self, titulo):
        self.trello.criar_lista(self.quadro_atual,titulo)

    def adicionar_cartao(self, lista_selecionada, titulo, descricao):
        self.trello.adicionar_cartao(lista_selecionada, self.quadro_atual,titulo,descricao)

    def adicionar_etiqueta(self):
        pass

    def exibir_listas(self):
        for i in range(1, len(self.quadro_atual)):
            lista_atual = self.quadro_atual[i][0]
            print(lista_atual)
          #  print(">> "+ lista_atual)
            for k in range(len(self.quadro_atual[i])):
                cartao = self.quadro_atual[k]
               # print("   >" + cartao)
                print(cartao)

    def exibir_quadros(self):
        for i in range(len(self.quadros)):
            quadro_atual = self.quadros[i][0]
            print(quadro_atual)
        print(self.quadro_atual)


