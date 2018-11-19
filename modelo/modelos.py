class Usuario:
    def __init__(self):
        self.contas = []

    def criar_conta(self):
        pass


class Trello:
    def __init__(self):
        self.nome = "nome"

    def criar_quadro(self, quadros, titulo):
        quadros.append([titulo])
        print(quadros)

    def criar_lista(self, quadro_atual,titulo):
        quadro_atual.append([titulo])

    def adicionar_cartao(self,lista_selecionada, quadro_atual,titulo,descricao):
        for i in range(1, len(quadro_atual)):
            lista_atual = quadro_atual[i][0]
            if lista_atual == lista_selecionada:
                quadro_atual[i].append([titulo, descricao])
    def adicionar_etiqueta(self):
        pass

    def exibir_listas(self):
        pass

    def exibir_quadros(self):
        pass
