import psycopg2 as conector
conexao = conector.connect("dbname=python_projects user=postgres password=123456")

comando = '''CREATE TABLE public."AGENDA"
             (
                id integer NOT NULL,
                nome text COLLATE pg_catalog."default" NOT NULL,
                telefone char(12) COLLATE pg_catalog."default" NOT NULL
             )
             TABLESPACE pg_default;'''

cursor = conexao.cursor()

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
