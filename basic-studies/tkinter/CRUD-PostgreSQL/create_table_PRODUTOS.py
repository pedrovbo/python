import psycopg2

conn = psycopg2.connect(database="python_test",
                        user="postgres",
                        password="123456",
                        host="127.0.0.1",
                        port="5432")
print("Conexão com o Banco de Dados feita com sucesso!")
cur = conn.cursor()
cur.execute('''CREATE TABLE PRODUTO(
                CODIGO INT PRIMARY KEY NOT NULL,
                NOME TEXT NOT NULL,
                PRECO REAL NOT NULL);''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()