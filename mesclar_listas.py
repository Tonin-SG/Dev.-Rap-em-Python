def unificar_e_ordenar_arquivos(arquivo_a, arquivo_b, arquivo_saida):
    itens_unicos = set()
    try:
        with open(arquivo_a, 'r', encoding='utf-8') as f:
            for linha in f:
                itens_unicos.add(linha.strip())
    except FileNotFoundError:
        print(f"Aviso: O arquivo '{arquivo_a}' não foi encontrado. Prosseguindo com o outro arquivo.")
    try:
        with open(arquivo_b, 'r', encoding='utf-8') as f:
            for linha in f:
                itens_unicos.add(linha.strip())
    except FileNotFoundError:
        print(f"Aviso: O arquivo '{arquivo_b}' não foi encontrado. Prosseguindo com o que temos.")
    itens_ordenados = sorted(list(itens_unicos))
    if not itens_ordenados:
        print("Nenhum item foi encontrado nos arquivos. O arquivo de saída não será criado.")
        return
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for item in itens_ordenados:
                if item:
                    f.write(item + '\n')
        print(f"Arquivo '{arquivo_saida}' criado com sucesso com {len(itens_ordenados)} itens únicos e ordenados.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo '{arquivo_saida}': {e}")
lista_a = "lista_a.txt"
lista_b = "lista_b.txt"
lista_unica = "lista_unica.txt"
unificar_e_ordenar_arquivos(lista_a, lista_b, lista_unica)