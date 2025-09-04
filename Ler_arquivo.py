try:
    with open('notas.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    print("O arquivo 'notas.txt' não foi encontrado. Criando...")
    with open('notas.txt', 'w') as arquivo:
        arquivo.write("Arquivo criado.")
    print("Arquivo 'notas.txt' criado com sucesso. Lendo o novo conteúdo:")

    with open('notas.txt', 'r') as arquivo:
        novo_conteudo = arquivo.read()
        print(novo_conteudo)