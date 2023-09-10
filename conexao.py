import sqlite3
from sqlite3 import Error

def conecta():
    try:
        con = sqlite3.connect('banco.db')
        return con
    except Error:
        print('Erro durante a conexão.')

tabelas = ['''
CREATE TABLE usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(60) NOT NULL,
    senha VARCHAR(20) NOT NULL
);
''',
'''
CREATE TABLE disciplina(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL
);
''',
'''
CREATE TABLE conteudo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_disciplina INTEGER NOT NULL,
    FOREIGN KEY (id_disciplina) REFERENCES disciplina (id)
);
''',
'''
CREATE TABLE questao(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    tentativas INTEGER,
    acertos INTEGER,
    id_autor INTEGER NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES usuario (id)
);
''',
'''
CREATE TABLE alternativa(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    valor INTEGER NOT NULL,
    id_questao INTEGER NOT NULL,
    FOREIGN KEY (id_questao) REFERENCES questao (id)
);
''',
'''
CREATE TABLE comentario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    id_questao INTEGER NOT NULL,
    id_autor INTEGER NOT NULL,
    FOREIGN KEY (id_questao) REFERENCES questao (id),
    FOREIGN KEY (id_autor) REFERENCES autor (id)
);
'''
]

def criar_tabela(sql):
    con = conecta()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
        print('Tabela criada com sucesso!')
    except:
        print('Tabela não criada!')
    con.close()

for tabela in tabelas:
    criar_tabela(tabela)

#inserir(sql_inserir_cliente)
#atualizar(sql_atualizar)
#remover(sql_remover)
#mostrar_tabela(sql_mostra_cliente)
#listar(sql_mostra_cliente)