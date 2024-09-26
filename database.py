import sqlite3
import pandas as pd

def create_db():
    conexao = sqlite3.connect('livraria.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            preco REAL
        )
    ''')
    conexao.commit()
    conexao.close()

create_db()

def adicionar_livro(titulo, autor, ano, preco):
    conexao = sqlite3.connect('livraria.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)
    ''', (titulo, autor, ano, preco))
    conexao.commit()
    conexao.close()

    backup()

def listar_livros():
    conexao = sqlite3.connect('livraria.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conexao.close()
    return livros

def atualizar_livro(id, titulo, autor, ano, preco):
    conexao = sqlite3.connect('livraria.db')
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE livros SET titulo = ?, autor = ?, ano = ?, preco = ? WHERE id = ?
    ''', (titulo, autor, ano, preco, id))
    conexao.commit()
    conexao.close()

    backup()

def excluir_livro(id):
    conexao = sqlite3.connect('livraria.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()

    backup()

def buscar_livros_por_autor(autor):
    conexao = sqlite3.connect('livraria.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livros WHERE autor = ?', (autor,))
    livros = cursor.fetchall()
    conexao.close()
    return livros

def backup(arquivo='backup_livros.csv'):
    # Obtém a lista de livros
    livros = listar_livros()
    # Cria um DataFrame a partir da lista de livros
    dataframe = pd.DataFrame(livros, columns=['ID', 'Título', 'Autor', 'Ano', 'Preço'])
    # Salva o DataFrame em um arquivo CSV
    dataframe.to_csv(arquivo, index=False)

