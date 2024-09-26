import pandas as pd
from database import listar_livros, adicionar_livro

def exportar_csv(arquivo):
    #copia a lista de livros
    livros = listar_livros()
    #cria um dataframe e exporta para o csv
    dataframe = pd.DataFrame(livros, columns=['ID', 'Título', 'Autor', 'Ano', 'Preço'])
    dataframe.to_csv(arquivo, index=False)

def importar_csv(arquivo):
    #le o arquivo csv e cria um df com os dados
    dataframe = pd.read_csv(arquivo)
    for _, row in dataframe.iterrows():
        adicionar_livro(row['Título'], row['Autor'], row['Ano'], row['Preço'])
