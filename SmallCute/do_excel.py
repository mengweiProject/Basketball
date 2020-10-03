
import pandas as pd


df = pd.DataFrame(pd.read_excel("folders/afterWork.xlsx"))
print(df[(df['encrypt'].notnull())])
# df_unfinished = df[df["state"]=="未完成"]
# print(df_unfinished.loc[:, ["target", "name", "encrypt", "data"]])