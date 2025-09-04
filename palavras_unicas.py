def contar_palavras_distintas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return
    conteudo = conteudo.lower()
    pontuacao = '.,!?;:()[]{}'
    for caractere in pontuacao:
        conteudo = conteudo.replace(caractere, '')
    palavras = conteudo.split()
    palavras_distintas = set(palavras)
    print(f"O arquivo contém {len(palavras_distintas)} palavras distintas.")
arquivo = "texto.txt"
contar_palavras_distintas(arquivo)