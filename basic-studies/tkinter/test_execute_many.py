import psycopg2 as conector

conexao = conector.connect("dbname=python_test user=postgres password=123456")

carros = (
    (2, 'Fulano', 11100033),
    (3, 'Ciclano', 22200033),
    (4, 'Beltrano', 11122233)
)

cursor = conexao.cursor()

query = "INSERT INTO cars (id, nome, preco) VALUES (%s, %s, %s)"
cursor.executemany(query, carros)
# cursor.fetchall()
conexao.commit()

cursor.close()
conexao.close()
