import os
os.listdir("files")
import pandas

# df_csv = pandas.read_csv("files/supermarkets.csv")
# print(df_csv)

# df_json = pandas.read_json("files/supermarkets.json")
# print(df_json)

df_xls = pandas.read_excel("files/supermarkets.xlsx")
# print(df_xls)
# print(df_xls.loc[0:2, "Address":"Country"])
# print(df_xls.iloc[0:3, 1:5])
# df_xls["Continent"] = df_xls.shape[0] * ["North America"]
# print(df_xls)
# df_xls["Continent"] = df_xls["Country"] + ", " + ["North America"]
print(df_xls)
df_xls_t = df_xls.T
print(df_xls_t)
df_xls_t[6]=[7, "14601 Staked Plains Loop", "Austin", "Texas 78717", "USA", "HEB", 500]


# df_txt = pandas.read_csv("files/data.txt", header=None)
# df_txt.columns = ["ID", "Math", "Social Study"]
# print(df_txt)





