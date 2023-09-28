import mysql.connector
from mysql.connector import Error

try:

    conexao = mysql.connector.connect(host='localhost', database='professorePy', user = 'root', password = '')
    # if conexao.is_connected():
    cursor = conexao.cursor()
    codProfessor = input("Digite o código do professor?\n")
    cursor.execute(f'SELECT professores.nomeprof, disciplinasprof.coddisciplina, disciplinasprof.curso, disciplinas.nomedisc FROM disciplinasprof INNER JOIN disciplinas ON disciplinasprof.coddisciplina = disciplinas.codigodisc INNER JOIN professores ON disciplinasprof.codprofessor = professores.registro WHERE disciplinasprof.codprofessor = {codProfessor};')
    linhas = cursor.fetchall()
    valores = []
    for linha in linhas:
        valores.append(linha)
    print(valores)

    cursoProfessor = valores[0][1]
    print(cursoProfessor)

except Error as e:
    print("Erro ao acessar tabela MySQL", e)
    
finally:
    cursor.close()
    conexao.close()
    print ("Conexão ao MySQL foi encerrada")

try:
    arquivo = open(f'c:/Users/Vinicius/Desktop/Minha pasta/Técnico/POOI/lista/{codProfessor}.html', 'w')
    curso = valores
    arquivo.write(f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Título da página</title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">      
        </head>
        <body>
            <h1>Disciplinas do professor:{curso[0][0]}</h1>
            <h1>Curso:{curso[0][2]}</h1>
            <h2>CÓDIGO DA DISCIPLINA | NOME DISCIPLINA</h2>
            <h3>{curso[0][1]} | {curso[0][3]}</h3>
            <h3>{curso[1][1]} | {curso[1][3]}</h3>
            <br>
            <h1>Curso:{curso[2][2]}</h1>
            <h3>{curso[2][1]} | {curso[2][3]}
        </body>
    </html>""")

    arquivo.close()

except Exception as erro:
    print(f'erro {erro}')

finally:
    print('succeso')