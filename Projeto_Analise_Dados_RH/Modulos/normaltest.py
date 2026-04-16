from scipy.stats import normaltest

def teste_normalidade(df, *colunas, alpha=0.05):
    """
    Testa a normalidade das colunas numéricas de um DataFrame.
    
    Parâmetros:
    df : DataFrame
    colunas : passar o nome da lista de colunas: colunas=[...] 
        ou passar direto o nome das colunas entre aspas: "coluna1, coluna2"
    alpha : float
        Nível de significância (padrão = 0.05)
    """
    
    for i in colunas_numericas:
        stats, pval = normaltest(df[i])
        
        if pval > alpha:
            print(f"{i}: Distribuição Normal")
        else:
            print(f"{i}: Distribuição Não Normal")
            