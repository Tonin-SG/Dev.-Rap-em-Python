def contar_linhas_nao_vazias(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            contador_linhas = 0
            for linha in f:
                if linha.strip():
                    contador_linhas += 1
            print(f"O arquivo '{nome_arquivo}' tem {contador_linhas} linhas não vazias.")
    except FileNotFoundError:
        print("Sinto muito! Arquivo não foi encontrado.")
    except PermissionError:
        print("Acesso negado! Por favor verifique se você tem pemissão para usar essa pasta.")
        print("Tente executar o programa no modo administrador")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
arquivo_de_frases = "frases.txt"
contar_linhas_nao_vazias(arquivo_de_frases)