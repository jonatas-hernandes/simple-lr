def leitura(arquivo):
    """Lê arquivo csv no formato de colunas e
    retorna um dicionário com cada coluna como chave

    Args:
        arquivo (str): caminho do arquivo

    Returns:
        dictionary: dicionário com listas de floats
    """
    with open(arquivo) as f:
        file = f.readlines()

    dic_columns = {}
    # getting headers
    headers = file[0].strip().split(",")

    for header in headers:
        dic_columns[header] = []

    for linha in file[1:]:
        columns = linha.strip().split(",")
        if len(columns) == len(headers):
            for i in range(len(columns)):
                dic_columns[headers[i]].append(float(columns[i]))

    return dic_columns
