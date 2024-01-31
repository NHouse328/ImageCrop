import pandas as pd
import os

# Caminho para o diretório que contém os arquivos CSV
input_folder = 'entrada/'

# Cria uma lista com o caminho completo de todos os arquivos CSV no diretório
csv_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.csv')]

if len(csv_files) == 0:
    print('Não foram encontrados arquivos CSV no diretório especificado.')
else:
    # Lê cada arquivo CSV em um DataFrame pandas e adiciona à lista
    data_frames = []
    for file in csv_files:
        df = pd.read_csv(file)
        data_frames.append(df)

    # Concatena todos os DataFrames em um único DataFrame
    concatenated_df = pd.concat(data_frames, ignore_index=True)

    # Escreve o DataFrame concatenado em um arquivo CSV
    output_file = 'entrada/saida.csv'
    concatenated_df.to_csv(output_file, index=False)
