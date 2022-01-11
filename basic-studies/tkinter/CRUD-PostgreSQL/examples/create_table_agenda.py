import psycopg2 as conector
conexao = conector.connect(database="python_projects", user="postgres", password="123456", host="127.0.0.1",
                           port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")

comando = '''CREATE TABLE Agenda
             (
                ID INT PRIMARY KEY NOT NULL,
                Nome TEXT NOT NULL,
                Telefone CHAR(12)
             );'''

cursor = conexao.cursor()

cursor.execute(comando)
print("Tabela criada com sucesso")

conexao.commit()

cursor.close()
conexao.close()
