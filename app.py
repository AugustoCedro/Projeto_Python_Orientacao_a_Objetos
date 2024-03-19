from livros_payload import Payload
import os
biblioteca = Payload()
def main():
    """
    Função principal para iniciar o programa Biblioteca
    """
    def menu():
        """
        Exibe o menu principal e permite o usuário escolher uma opção
        """
        while True:
            print('Bem vindo(a) à biblioteca')
            print('0 - Listar Catálago de livros')
            print('1 - Solicitar um Livro')
            print('2 - Devolver um Livro')
            print('3 - Sair do programa')
            try:
                escolha = int(input('Oque você deseja fazer?: '))
                if escolha == 0:
                    listar_livros()
                    voltar_ao_menu()
                elif escolha == 1:
                    solicitar_livro()
                    voltar_ao_menu()
                elif escolha == 2:
                    devolver_livro()
                    voltar_ao_menu()
                elif escolha == 3:
                    limpar_terminal()
                    break
                else:
                    print('Escolha inválida, tente novamente')
            except ValueError:
                 print('Escolha inválida, tente novamente')
                 input()
                 limpar_terminal()
    
    def listar_livros():
        """
        Mostra os detalhes de todos os livros na biblioteca
        """
        biblioteca.listar_livros()

    def solicitar_livro():
        """
        Função que busca o livro pelo nome que o usuário escolheu
        Marca como indisponivel se estiver disponivel na biblioteca
        """
        try:
            escolha_livro = input('Digite o nome do filme que você deseja pegar: ')
            livro = biblioteca.buscar_livro_por_nome(escolha_livro)
            if livro._disponivel == True:
                livro.alterar_disponibilidade()
                print('Livro entregue com sucesso')
            else:
                print('Livro já em uso, escolha outro livro ou tente mais tarde')
        except:
            print('Livro não encontrado, tente novamente')

    def devolver_livro():
        """
        Função que busca o livro pelo nome que o usuário escolheu
        Marca como disponivel se estiver indisponivel na biblioteca
        """
        try:
            escolha_livro = input('Digite o nome do filme que você deseja devolver: ')
            livro = biblioteca.buscar_livro_por_nome(escolha_livro)
            if livro._disponivel == False:
                livro.alterar_disponibilidade
                print('Livro devolvido com sucesso')
            else:
                print('Livro já está na biblioteca, escolha outro livro')
        except:
            print('Livro não encontrado, tente novamente')
            
    def voltar_ao_menu():
        """
        pede ao usuário para clicar em uma tecla para voltar ao menu principal
        """
        print()
        input('Aperte qualquer tecla para voltar ao menu principal: ')
        limpar_terminal()

    def limpar_terminal():
        """
        Limpa o terminal
        """
        os.system('cls')

    
    menu()
if __name__ == '__main__':
    main()









