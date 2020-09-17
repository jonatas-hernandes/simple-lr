import aux_lib as ax

if __name__ == "__main__":
    
    file_path = "./data/housing.csv"
    # leitura do arquivo
    dataset = ax.leitura(file_path)
    
    print(dataset['RM'])
    # tamanho das listas
    #n_data_rows = len(dataset['RM'])

    # Predizer valores de MEDV a partir do RM
    # 70% do dataset para pegar os coeficientes
    #limite_rows = round(n_data_rows*0.7)
    #angular_coef = beta(dataset['RM'][:limite_rows],dataset['MEDV'][:limite_rows])
    #intercepcao = alpha(dataset['RM'][:limite_rows],dataset['MEDV'][:limite_rows])

    # Predizer os valores para os outros 30%
    #predito = pred(dataset['RM'][limite_rows:],angular_coef,intercepcao)

    #print(angular_coef, intercepcao, dataset['RM'][limite_rows-1],dataset['MEDV'][limite_rows-1],predito[0])
    # verifica o erro dos valores preditos
    #erro_medio_quad = rmse(predito,dataset['MEDV'][limite_rows:])

    #return erro_medio_quad
    #pass