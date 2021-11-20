import pandas as pd
import random

df = pd.DataFrame({"col1":["A0", "A1", "A0", "A2", "A0", "A1"]})


# 1. Retriving row info

# Retrieve first column value

print(df.iloc[0].col1)

# Retrieve last column value

print(df.iloc[-1].col1)

# Retrive data using index

print(df.loc[0, 'col1'])


#----------------------------------------------------------------------------

# 2. Good way to add new column
new_col = list(range(len(df)))

#a
df.loc[:, 'new_col'] = new_col

# b, bonus add multiple columns here
df = df.assign(new_colum2 = new_col, new_colum3 = new_col)

print(df.head())

#----------------------------------------------------------------------------


#3. Filtering in pandas 

df2 = pd.DataFrame({'num': [2, 3.4, 2.2, 1.9, 7.8]})

print(df2[df2['num'].between(2,3)])

#### 4 Split Data into train and test

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

