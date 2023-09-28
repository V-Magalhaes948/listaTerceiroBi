try:
    nomeArquivo = input("Digite o nome do arquivo HTML: \n")
    tituloDocumento = input("Digite o nome do documento: \n")
    tagUsuario = input("Informe a tag à ser utilizada: \n")
    tagUsuario = tagUsuario.split()
    usuarioTexto = input("Digite o texto para o arquivo: \n")
    arquivo = open(f'c:/Users/Vinicius/Desktop/Minha pasta/Técnico/POOI/lista/{nomeArquivo}.html', 'w')
    arquivo.write(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{tituloDocumento}</title>
        </head>
        <body>
            <h1>{tagUsuario[0]}{usuarioTexto}{tagUsuario[1]}</h1>
        </body>
        </html>"""
    )
    
except:
    print("erro")
else:
    print('Arquivo aberto com sucesso')
finally:
    print('fim do programa')