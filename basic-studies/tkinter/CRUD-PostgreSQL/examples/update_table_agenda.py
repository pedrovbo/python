import psycopg2

conexao = psycopg2.connect(database="python_projects", user="postgres", password="123456", host="127.0.0.1",
                           port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cursor = conexao.cursor()
print("Consulta antes da atualização")
cursor.execute("""select * from AGENDA where "id" = 1""")
registro = cursor.fetchone()
print(registro)

# Atualização de um único registro
cursor.execute("""Update AGENDA set "telefone" = '02188888888' where "id" = 1""")
conexao.commit()
print("Registro Atualizado com sucesso! ")
cursor = conexao.cursor()
print("Consulta depois da atualização")
cursor.execute("""select * from AGENDA where "id" = 1""")
registro = cursor.fetchone()
print(registro)
conexao.commit()
print("Seleção realizada com sucesso!")
conexao.close()
