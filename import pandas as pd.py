import pandas as pd

def gera_df_filtrado():
    caminho = r'.\Users\renat\Downloads\MICRODADOS.csv'  

    # Gera o DataFrame com base no .csv
    df = pd.DataFrame(pd.read_csv(caminho, sep=";", encoding="ISO-8859-1", low_memory=False))

    # Remove todas as linhas em que o municipio seja diferente de CARIACICA
    df.drop(df[df.Municipio != 'CARIACICA'].index, inplace=True)

    # Substitui os valores NaN por uma string vazia
    df.fillna(value='', inplace=True)

    # Remove as linhas que nao possuem data de obito
    df.drop(df[df.DataObito == ''].index, inplace=True)

    # Remove as linhas em que nao possui tabagismo como comorbidade
    df.drop(df[df.ComorbidadeTabagismo != 'Sim'].index, inplace=True)
    
    # Remove as linh em que o óbito não foi causado pelo COVID-19
    df.drop(df[df.Evolucao != 'Óbito pelo COVID-19'].index, inplace=True)

    #reseta o index do dataframe
    df.reset_index(drop=True, inplace=True)

    df.to_excel(r'.\Users\renat\Downloads\teste.xlsx')
    return df

gera_df_filtrado()