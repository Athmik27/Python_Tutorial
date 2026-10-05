import pandas as pd

df=pd.read_csv("sample.csv")
print(df.head())

import pandas as pd

df=pd.read_csv("sample.csv")
print(df.head(5))

import pandas as pd

df=pd.read_csv("sample.csv")
print(df.tail(5))

import pandas as pd

df=pd.read_csv("sample.csv")
print(df.describe())


import pandas as pd

df=pd.read_csv("sample.csv")
print(df.info())



import pandas as pd

df=pd.read_csv("sample.csv")
print(df.isnull())


import pandas as pd

df=pd.read_csv("sample.csv")
print(df.isnull().sum())

import pandas as pd


df=pd.read_csv("sample.csv")
print(pd.DataFrame(df))

import pandas as pd

df=pd.read_csv("sample.csv")
df["Height"].fillna(df["Height"].mean(),inplace=True)
print('Height')

import pandas as pd
df=pd.read_csv("sample.csv")
result=df.duplicated()
print(result)

import pandas as pd
df=pd.read_csv("sample.csv")
result=df.duplicated().sum()
print(result)


import pandas as pd
df=pd.read_csv("sample.csv")
result=df.duplicated().sum()
print(result)

