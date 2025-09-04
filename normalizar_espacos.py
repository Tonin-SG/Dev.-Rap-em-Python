def limpar_comentarios(entrada, saida):
    conteudo = ""
    try:
        with open(entrada, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except UnicodeDecodeError:
        try:
            with open(entrada, 'r', encoding='latin-1') as f:
                conteudo = f.read()
        except FileNotFoundError:
            print(f"Erro: O arquivo '{entrada}' não foi encontrado.")
            return
    except FileNotFoundError:
        print(f"Erro: O arquivo '{entrada}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return
    conteudo_limpo = conteudo.replace("...", ".")
    conteudo_limpo = " ".join(conteudo_limpo.split())
    try:
        with open(saida, 'w', encoding='utf-8') as f:
            f.write(conteudo_limpo)
        print(f"Arquivo '{saida}' criado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")
arquivo_entrada = "comentarios.txt"
arquivo_saida = "comentarios_limpos.txt"
limpar_comentarios(arquivo_entrada, arquivo_saida)