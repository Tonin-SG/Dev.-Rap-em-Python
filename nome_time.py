def processar_jogadores(arquivo_entrada, arquivo_log):
    jogadores_times = {}
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f_entrada, \
             open(arquivo_log, 'w', encoding='utf-8') as f_log:
            for numero_linha, linha in enumerate(f_entrada, 1):
                linha = linha.strip()
                try:
                    nome, time = linha.split(',', 1)
                    jogadores_times[nome.strip()] = time.strip()
                except ValueError:
                    f_log.write(f"Linha {numero_linha} inválida: '{linha}'\n")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
        return {}
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {}
    return jogadores_times
arquivo_de_dados = "jogadores_times.txt"
arquivo_de_log = "linhas_invalidas.log"
dicionario_jogadores = processar_jogadores(arquivo_de_dados, arquivo_de_log)
print("Dicionário de jogadores e times:")
print(dicionario_jogadores)