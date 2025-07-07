import csv

def ler_clientes(caminho_arquivo: str) -> list[dict]:
    clientes = []
    with open(caminho_arquivo, encoding='utf-8') as f:
        leitor = csv.DictReader(f, delimiter='\t')
        for linha in leitor:
            clientes.append(linha)
    return clientes