import sqlite3


#conectando ao BD
conn = sqlite3.connect('escola.db')
        

# Definir um cursor
cursor = conn.cursor()
#criar tabelas
cursor.execute ("""CREATE TABLE IF NOT EXISTS funcionario (
            id_func INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(40) NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            data_nasci INTEGER CHAR(8) NOT NULL,
            telefone VARCHAR(9),
            funcao VARCHAR(1) NOT NULL
            
            );
            """)

cursor.execute ("""CREATE TABLE IF NOT EXISTS aluno (
            id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(40) NOT NULL,
            cpf VARCHAR(11) NOT NULL,
           nasc INTEGER CHAR(8) NOT NULL,
            telefone VARCHAR(9) NOT NULL,
            serie VARCHAR(1) NOT NULL
         
        );
        """)




conn.commit()
print('Tabela criada com sucesso')
