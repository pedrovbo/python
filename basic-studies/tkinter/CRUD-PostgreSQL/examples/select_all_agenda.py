import psycopg2 as conector

conexao = conector.connect(database="python_projects", user="postgres", password="123456", host="127.0.0.1",
                           port="5432")
print("Conexão com o Banco de Dados aberta com sucesso")

cursor = conexao.cursor()

cursor.execute("""SELECT * FROM AGENDA WHERE "id" = 1""")
registro = cursor.fetchone()
print(registro)

conexao.commit()
print("Seleção realizada com sucesso!")
conexao.close()
