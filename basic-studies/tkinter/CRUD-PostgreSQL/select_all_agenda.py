import psycopg2 as conector
from agenda_modelo import Agenda
conexao = conector.connect("dbname=python_projects user=postgres password=123456")

comando = '''SELECT * FROM public."AGENDA";'''

cursor = conexao.cursor()

cursor.execute(comando)

registros = cursor.fetchall()
for registro in registros:
    contato = Agenda(*registro)
    print(f'Id: {contato.id} \nNome: {contato.nome} \nTelefone: {contato.telefone}')

conexao.commit()

cursor.close()
conexao.close()
