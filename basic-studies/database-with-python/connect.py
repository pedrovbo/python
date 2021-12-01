import psycopg2 as conector

v1 = "5"
v2 = "Geoffrey"
v3 = "37"
try:
    # Abertura de conexão
    conexao = conector.connect(user="postgres", password="123456", database="test", host="localhost", port="5432")

    # Aquisição de um cursor
    cursor = conexao.cursor()

    # Execução comandos: SELECT..CREATE...
    cursor.execute(
        "INSERT INTO pessoa VALUES (%s, %s, %s);",
        (v1, v2, v3)
    )
    # cursor.fetchall()

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões
    if conexao:

        cursor.close()
        conexao.close()
