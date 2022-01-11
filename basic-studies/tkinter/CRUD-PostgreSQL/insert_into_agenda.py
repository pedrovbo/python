import psycopg2 as conector
conexao = conector.connect("dbname=python_projects user=postgres password=123456")

comando = '''INSERT INTO public."AGENDA"( id, nome, telefone)
                VALUES (1, 'teste 1', '02199999999');'''

cursor = conexao.cursor()

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
