import psycopg2
conexao = psycopg2.connect(database="python_projects", user="postgres", password="123456", host="127.0.0.1",
                           port="5432")
print ("Conexão com o Banco de Dados aberta com sucesso!")
cursor = conexao.cursor()
cursor.execute("""Delete from AGENDA where "id" = 1""")
conexao.commit()
cont = cursor.rowcount
print(cont, "Registro excluído com sucesso! ")
print("Exclusão realizada com sucesso!")
conexao.close()