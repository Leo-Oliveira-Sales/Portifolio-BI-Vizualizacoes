import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calcula_iv_categoricas(
    df,
    target,
    *colunas,
    show_plot=True,      # 👈 gráfico aparece por padrão
    return_df=False,     # 👈 DataFrame NÃO aparece por padrão
    figsize=(10, 12),
    eps=1e-6
):
    """
    Calcula o Information Value (IV) para variáveis categóricas.

    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame com os dados

    target : str
        Nome da variável alvo (binária: 0 e 1)

    colunas : str ou list
        Nomes das colunas categóricas

    show_plot : bool, default=True
        Se True, exibe o gráfico

    return_df : bool, default=False
        Se True, retorna o DataFrame com os IVs

    figsize : tuple
        Tamanho da figura

    eps : float
        Valor pequeno para evitar divisão por zero
    """

    # 🔹 Normaliza entrada (lista + argumentos)
    colunas_cat = []
    for col in colunas:
        if isinstance(col, (list, tuple, set)):
            colunas_cat.extend(col)
        else:
            colunas_cat.append(col)

    colunas_cat = list(dict.fromkeys(colunas_cat))  # remove duplicados

    iv_list = []

    for col in colunas_cat:
        tabela = pd.crosstab(
            df[col],
            df[target],
            normalize='columns'
        )

        tabela['woe'] = np.log((tabela[1] + eps) / (tabela[0] + eps))
        iv = np.sum(tabela['woe'] * (tabela[1] - tabela[0]))

        iv_list.append(iv)

    df_iv = (
        pd.DataFrame({
            'Feature': colunas_cat,
            'IV': iv_list
        })
        .set_index('Feature')
        .sort_values(by='IV')
    )

    # 🔹 Gráfico (opcional, default ON)
    if show_plot:
        plt.figure(figsize=figsize)
        df_iv.plot(
            kind='barh',
            title='Information Value das Variáveis Categóricas',
            colormap='Accent',
            legend=False
        )

        for idx, val in enumerate(round(df_iv['IV'], 3)):
            plt.text(val, idx, str(val))

        plt.show()

    # 🔹 DataFrame (opcional, default OFF)
    if return_df:
        return df_iv