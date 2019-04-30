from tabula import read_pdf
import pandas as pd
import numpy as np
import os
import warnings

warnings.filterwarnings("ignore")



def mix_all_data(files):
    data_frames = []
    for file in files:
        print("Processing file %s" % file)
        try:
            df = read_pdf(file, silent=True)
            # remove the first two irrelevant rows.
            df = df[2:]

            all_names = np.concatenate((df.ix[:, 0].values, df.ix[:, 3].values))
            all_units = np.concatenate((df.ix[:, 1].values, df.ix[:, 4].values))
            all_prices = np.concatenate((df.ix[:, 2].values, df.ix[:, 5].values))

            df = pd.DataFrame({"Nombre": all_names, "Unidades": all_units, "Precios": all_prices})

            df = df.dropna(axis=0, how='all')

            df["Fecha"] = file.split('.')[0].split('_')[-1]

            data_frames.append(df)
        except:
            print('Error in file: %s' % file)

    return data_frames


def get_files_of_type(file_type, directory):
    files = []
    for file in os.listdir("%s" % directory):
        if file.endswith(".%s" % file_type):
            files.append(os.path.join("%s" % directory, file))

    return files


data_files = get_files_of_type('pdf', 'files')
print("Total files: %d" % len(data_files))

dfs = mix_all_data(data_files)
global_df = pd.concat(dfs)
global_df.to_csv("data_combine.csv", index=False, encoding='utf-8-sig')

print('done')
