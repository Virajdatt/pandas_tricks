'''
Here are the code snippets for the article written on medium named "Pandas, tips to deal with huge dataset!!"
The link to the article: https://kvirajdatt.medium.com/pandas-tips-to-deal-with-huge-datasets-f6a012d4e953 
'''
## Tip 1 Pandas read only first few rows

import pandas as pd
data_file = '/path/to/my/datafile'
df = pd.read_csv(data_file, n_rows = 100)

## Tip 2 a. Pandas Explicitly pass the data-types


data_file = '/path/to/my/datafile'
df = pd.read_csv(data_file, n_rows = 100, dtype=({'col1': 'object', 'col2': 'float32', ........} )
                 
## Tip 2 b. Pandas explicitily pass data-types by some inference
                 

data_file = '/path/to/my/datafile'
df = pd.read_csv(data_file, n_rows = 100)
dtype_dic = {}
for key, value in df.dtypes.items():
   dtype_dic[key] = value
bigger_df = pd.read_csv(data_file, n_rows = 10000, dtype=dtype_dic)
                 
## Tip 3 Read data in chunks

                 
data_file = '/path/to/my/datafile'
                 
CHUNK = 10000
                 
def calculate_some_stats_on_chunk():
 pass

def plot_grapgs_on_chunk():
 pass
                 
df = pd.read_csv(data_file, n_rows = 100)
dtype_dic = {}
for key, value in df.dtypes.items():
   dtype_dic[key] = value
                 
chunk_stats_list = []
for chunk in pd.read_csv(data_file, chunksize = CHUNK, dtype=dtype_dic):
   plot_grapgs_on_chunk(chunk)
   stats = calculate_some_stats_on_chunk(chunk)
   chunk_stats_list.append(stats)
                 
## Tip 4 Maybe select a subset of columns and conduct EDA


data_file = '/path/to/my/datafile'
cols_i_wanna_use = ['col1', 'col2',]
df = pd.read_csv(data_file, usecols=cols_i_wanna_use)
