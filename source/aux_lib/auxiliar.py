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


def core(arquivo):

    # leitura do arquivo
    dataset = leitura(arquivo)

    # tamanho das listas
    n_data_rows = len(dataset["RM"])

    # Predizer valores de MEDV a partir do RM
    # 70% do dataset para pegar os coeficientes
    limite_rows = round(n_data_rows * 0.7)
    angular_coef, intercepcao = fit(dataset["RM"][:limite_rows], dataset["MEDV"][:limite_rows])

    # Predizer os valores para os outros 30%
    predito = predict(dataset["RM"][limite_rows:], angular_coef, intercepcao)

    print(
        angular_coef,
        intercepcao,
        dataset["RM"][limite_rows - 1],
        dataset["MEDV"][limite_rows - 1],
        predito[0],
    )
    # verifica o erro dos valores preditos
    erro_medio_quad = rmse(predito, dataset["MEDV"][limite_rows:])

    return erro_medio_quad
