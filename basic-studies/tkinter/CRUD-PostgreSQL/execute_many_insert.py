import psycopg2 as conector

conexao = conector.connect("dbname=python_projects user=postgres password=123456")

registros = (
    (2, 'Fulano', '11100033000'),
    (3, 'Ciclano', '22200033000'),
    (4, 'Beltrano', '11122233000')
)

cursor = conexao.cursor()

query = '''INSERT INTO "AGENDA" (id, nome, telefone) VALUES (%s, %s, %s)'''
cursor.executemany(query, registros)
conexao.commit()

cursor.close()
conexao.close()
