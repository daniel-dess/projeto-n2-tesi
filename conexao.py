import sqlite3
from sqlite3 import Error


def conecta():
    try:
        con = sqlite3.connect('banco.db')
        return con
    except Error as er:
        print('Erro durante a conexão.')

tabelas = ['''CREATE TABLE IF NOT EXISTS "usuario"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" VARCHAR(100) NOT NULL,
    "senha" VARCHAR(20) NOT NULL
);''',
'''CREATE TABLE IF NOT EXISTS "disciplina"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" VARCHAR(100) NOT NULL
);''',
'''CREATE TABLE IF NOT EXISTS "questao"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "conteudo" TEXT,
    "tentativas" INTEGER,
    "acertos" INTEGER,
    "dificuldade" INTEGER,
    "id_autor" INTEGER NOT NULL,
    "data_criacao" TIMESTAMP,
    FOREIGN KEY ("id_autor") REFERENCES "usuario" ("id")
);''',
'''CREATE TABLE IF NOT EXISTS "alternativa"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "conteudo" TEXT NOT NULL,
    "valor" INTEGER NOT NULL,
    "id_questao" INTEGER NOT NULL,
    FOREIGN KEY ("id_questao") REFERENCES "questao" ("id")
);''',
'''CREATE TABLE IF NOT EXISTS "comentario"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "conteudo" TEXT NOT NULL,
    "id_questao" INTEGER NOT NULL,
    "id_autor" INTEGER NOT NULL,
    FOREIGN KEY ("id_questao") REFERENCES "questao" ("id"),
    FOREIGN KEY ("id_autor") REFERENCES "autor" ("id")
);''',
'''CREATE TABLE IF NOT EXISTS "simulado"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "questoes" TEXT,
    "id_usuario" INTEGER NOT NULL,
    FOREIGN KEY ("id_usuario") REFERENCES "usuario" ("id")
);'''
]

def criar_tabela(sql):
    con = conecta()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
    except:
        print('Tabela não criada!')
    con.close()

for tabela in tabelas:
    criar_tabela(tabela)

def listar(sql):
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    con.close()
    return resultado

def inserir(sql):
    con = conecta()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
    except Error as e:
        print(f'Erro durante a inserção: {e}')
    con.close()


def atualizar(sql):
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

def remover(sql):
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()