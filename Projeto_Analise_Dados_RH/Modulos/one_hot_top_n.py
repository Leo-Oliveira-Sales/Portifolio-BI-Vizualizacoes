def one_hot_top(df, top_n=10):
    # Função para aplicar top_n=10 em todo dataset
    # Útil quando não vai usar todo o data set; vai usar somente as categorias mais relevantes
    df = df.copy()
    
    for coluna in df.columns:
        
        # pega os top N valores da coluna
        top_valores = df[coluna].value_counts().head(top_n).index
        
        # cria as colunas one-hot-encoding
        for val in top_valores:
            df[f"{coluna}_{val}"] = (df[coluna] == val).astype(int)
            # df[f"{coluna}_{val}"] Cria uma nova coluna no dataframe com nome dinâmico
            # Ex:
            # coluna = 'X1'
            # val = 'aa'
            # Resultado: X1_aa
    return df