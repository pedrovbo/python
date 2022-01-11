import psycopg2 as conector
conexao = conector.connect(database="python_projects", user="postgres", password="123456", host="127.0.0.1",
                           port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")

comando = '''INSERT INTO AGENDA ( "id", "nome", "telefone")
                VALUES (2, 'Pessoa 2', '02439999999')'''

cursor = conexao.cursor()

cursor.execute(comando)

conexao.commit()
print("Inserção realizada com sucesso")

cursor.close()
conexao.close()
