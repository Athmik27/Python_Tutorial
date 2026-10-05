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