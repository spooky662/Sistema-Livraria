from database import buscar_livros_por_autor, backup, adicionar_livro,listar_livros, atualizar_livro, excluir_livro
from manipulador_csv import exportar_csv, importar_csv

def main():
    while True:
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Excluir Livro")
        print("5. Buscar Livros por Autor")
        print("6. Exportar para CSV")
        print("7. Importar de CSV")
        print("8. Fazer Backup")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            preco = float(input("Preço: "))
            adicionar_livro(titulo, autor, ano, preco)
        elif escolha == '2':
            livros = listar_livros()
            for livro in livros:
                print(livro)
        elif escolha == '3':
            id = int(input("ID do livro a atualizar: "))
            titulo = input("Novo Título: ")
            autor = input("Novo Autor: ")
            ano = int(input("Novo Ano: "))
            preco = float(input("Novo Preço: "))
            atualizar_livro(id, titulo, autor, ano, preco)
        elif escolha == '4':
            id = int(input("ID do livro a excluir: "))
            excluir_livro(id)
        elif escolha == '5':
            autor = input("Nome do Autor: ")
            livros = buscar_livros_por_autor(autor)
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro encontrado para esse autor.")
        elif escolha == '6':
            exportar_csv('livros.csv')
        elif escolha == '7':
            importar_csv('livros.csv')
        elif escolha == '8':
            backup()
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
