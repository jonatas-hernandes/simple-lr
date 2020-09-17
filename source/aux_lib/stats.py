def minimo(lista):
    """Encontra o menor valor presente na lista

    Args:
        lista (list): lista com números

    Returns:
        float/int: número cujo valor é o menor na lista
    """
    menor = lista[0]
    for elemento in lista[1:]:
        if elemento < menor:
            menor = elemento

    return menor


def maximo(lista):
    """Encontra o maior valor presente na lista

    Args:
        lista (list): lista com números

    Returns:
        float/int: número cujo valor é o maior na lista
    """
    maior = lista[0]
    for elemento in lista[1:]:
        if elemento > maior:
            maior = elemento

    return maior


def raiz(numero, n):
    """Calcula a raiz enésima do número

    Args:
        numero (float): número que se deseja calcular a raiz
        n (float): ordem da raiz

    Returns:
        float: resultado do cálculo da raiz
    """
    return numero ** (1 / n)


def soma_lista(lista):
    """Calcula a soma dos elementos presentes na lista

    Args:
        lista (list): lista com números

    Returns:
        float: valor da soma da lista
    """
    soma = lista[0]
    for elemento in lista[1:]:
        soma += elemento

    return soma


def media_lista(lista):
    """Calcula a média dos elementos presentes na lista

    Args:
        lista (list): lista com números

    Returns:
        float: valor da média da lista
    """
    soma = soma_lista(lista)
    media = soma / len(lista)

    return media


def variancia(lista):
    """Calcula a variância amostral da lista

    Args:
        lista (list): lista com números

    Returns:
        float: valor da variância da lista
    """

    media = media_lista(lista)

    lista_desvios = [(numero - media) ** 2 for numero in lista]

    variance = soma_lista(lista_desvios) / (len(lista_desvios) - 1)

    return variance


def desvio_padrao(lista):
    """Calcula a desvio padrão da amostra presente na lista

    Args:
        lista (list): lista com números

    Returns:
        float: valor do desvio padrão dos elementos da lista
    """
    std = variancia(lista) ** (0.5)
    return std


def cova(lista1, lista2):
    """Calcula a covariância entre as duas listas

    Args:
        lista1 (list): lista com números
        lista2 (list): lista com números

    Returns:
        float: valor da covariância entre as as duas listas
    """
    media_lista1 = media_lista(lista1)
    media_lista2 = media_lista(lista2)

    # assumindo que as duas tem o mesmo tamanho
    cova_list = []
    for i in range(len(lista1)):
        cova_i = (lista1[i] - media_lista1) * (lista2[i] - media_lista2)
        cova_list.append(cova_i)

    covariance = soma_lista(cova_list)(len(cova_list) - 1)

    return covariance


def rmse(valores_preditos, valores_reais):
    """Raiz quadrada dos erros médios entre as duas listas

    Args:
        valores_preditos (list): lista com os valores preditos
        valores_reais (list): lista com os valores reais

    Returns:
        float: rmse
    """

    lista_squares = []
    for i in range(len(valores_preditos)):
        square = (valores_preditos[i] - valores_reais[i]) ** 2
        lista_squares.append(square)

    root_mean_se = raiz((media_lista(lista_squares)), 2)

    return root_mean_se


def beta(lista_x, lista_y):
    """Coeficiente angular da regressão linear

    Args:
        lista_x (list): lista de valores do eixo x
        lista_y (list): lista de valores do eixo y
    Returns:
        float: valor do coeficiente angular da reta de regressão
    """

    return cova(lista_x, lista_y) / variancia(lista_x)


def alpha(lista_x, lista_y):
    """Intercecção do eixo x da regressão linear

    Args:
        lista_x (list): lista de valores do eixo x
        lista_y (list): lista de valores do eixo y
    Returns:
        float: valor de intercecção da reta de regressão
    """
    angular_coef = beta(lista_x, lista_y)
    intercepcao = media_lista(lista_y) - angular_coef * (media_lista(lista_x))

    return intercepcao


def predict(lista_x, angular_coef, intercepcao):
    """Função de predição dos valores de y a partir da 
    lista de elementos em x

    Args:
        lista_x (list): lista dos elementos de x
        angular_coef (float): coeficiente angular da reta de regressão
        intercepcao (float): intercepção da reta de regressão

    Returns:
        list: lista com os elementos preditos a partir de x
    """

    predito = [(angular_coef * x + intercepcao) for x in lista_x]

    return predito
