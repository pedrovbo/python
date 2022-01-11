import psycopg2 as conector
conexao = conector.connect("dbname=python_projects user=postgres password=123456")

comando = '''ALTER TABLE public."AGENDA"
                OWNER to postgres;'''

cursor = conexao.cursor()

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
