import sqlite3 as conector


comando = """
COMANDO SQL DESEJADO;
"""
# Abertura de conexão
conexao = conector.connect("meu_banco.db")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
cursor.execute(comando)
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
