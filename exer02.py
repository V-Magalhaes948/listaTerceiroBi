import mysql.connector
from mysql.connector import Error

try:

    conexao = mysql.connector.connect(host='localhost', database='professorePy', user = 'root', password = '')

    if conexao.is_connected():
        cursor = conexao.cursor()
        codProfessor = input("Digite o código do professor?\n")
        cursor.execute(f'SELECT nomeprof FROM professores WHERE registro = {codProfessor};')
        linhas = cursor.fetchall()
        nomeProf = linhas
        print ("Resultado:")
        i = 0
        #for linha in linhas:
         #   for i in range(5):
          #      print (linha[i])


except Error as e:
    print("Erro ao acessar tabela MySQL", e)

finally:
    if (conexao.is_connected()):
        cursor.close
        conexao.close()
        print ("Conexão ao MySQL foi encerrada")