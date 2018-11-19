from service.controle import *


def main():
    opcao = -1
    contole_trello = Controle()
    menu_usuario = "login/Cadastro\n" \
                   "1 - criar conta\n" \
                   "2 - logar\n" \
                   "-> "
    menu_painel = "1 - Criar quadro: \n" \
                  "2 - Selecionar quadro:\n" \
                  "3 - listar quadros:\n" \
                  "4 - apagar quadro:\n" \
                  "0 - sair:\n" \
                  "-> "
    while opcao != 0:
        opcao = int(input(menu_painel))

        if opcao == 1:
            titulo_quadro = input("Digite o titulo do quadro: ")
            contole_trello.criar_quadro(titulo_quadro)
        if opcao == 2:
            seleciona_quadro = input("Digite o nome do quadro para entrar: ")
            escolhe = contole_trello.seleciona_quadro(seleciona_quadro)
            if escolhe:
                escolha = -1
                print("entrou")
                while escolha != 0:
                    menu_quadro = "1 - Add lista \n" \
                                  "2 - Adicionar cartão a uma lista\n" \
                                  "3 - arquivar lista\n" \
                                  "4 - Arquivar cartão de uma lista\n" \
                                  "5 - Adicionar etiqueta a um cartão\n" \
                                  "6 - Listar listas com seus cartões\n" \
                                  "0 - voltar\n" \
                                  "-> "
                    escolha = int(input(menu_quadro))

                    if escolha == 1:
                        titulo_lista = input("Digite o titulo da lista")
                        contole_trello.criar_lista(titulo_lista)
                    if escolha == 2:
                        select_lista = input("Digite a lista que queira adicionar um cartao: ")
                        nome_cartao = input("Digite o titulo do cartao: ")
                        descricao = input("Digite a descriçao:")
                        contole_trello.adicionar_cartao(select_lista, nome_cartao, descricao)
                    if escolha == 6:
                        contole_trello.exibir_listas()

            else:
                print("falha")

        if opcao == 3:
            contole_trello.exibir_quadros()


if __name__ == '__main__':
    main()
