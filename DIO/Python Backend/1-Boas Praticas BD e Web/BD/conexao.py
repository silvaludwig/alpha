import sqlite3
from pathlib import Path

#criando uma variável ROOT_PATH pra que o BD esteja na pasta atual do projeto
ROOT_PATH = Path(__file__).parent

#Estabelecendo conexão com o BD. Caso ele não exista, está criando um novo
conexao = sqlite3.connect(ROOT_PATH / "teste_db.db")

#cria uma instancia de cursor(), que é a base pra comandos sql dentro do python
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    #utilizando a instancia criada anteriormente, cria uma tabela clientes, caso não exista no BD
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (clientes_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
        "clientes_NOME VARCHAR(100), clientes_EMAIL VARCHAR(150));"
        )
    conexao.commit()

def inserir_registros(conexao, cursor, clientes_NOME, clientes_EMAIL):
    #inserindo valores na tabela criada anteriormente
    #criando uma variavel data que armazena os dados que eu quero inserir na tabela
    data = (clientes_NOME, clientes_EMAIL)

    #chama a função execute na instancia cursor com os comandos SQL pra inserir os dados
    cursor.execute("INSERT INTO clientes(clientes_NOME, clientes_EMAIL) VALUES (?,?);", data)

    #chama a função commit da instancia conexao, o que faz com que os dados sejam persistidos na tabela
    conexao.commit()

def atualizar_registros(conexao, cursor, clientes_NOME, clientes_EMAIL, clientes_ID):
    data = (clientes_NOME, clientes_EMAIL, clientes_ID)
    cursor.execute("UPDATE clientes SET clientes_NOME=?, clientes_EMAIL=? WHERE clientes_ID=?;", data)
    conexao.commit()


# inserir_registros(conexao, cursor, "Geraldo", "geraldo@email.com")

atualizar_registros(conexao, cursor, "Jeronimo", "jeronimo@email.com", 1)