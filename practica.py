import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df_data = pd.read_excel("_ml_jug.xlsx")


df_data = df_data.drop(["spcsm",  "bloc", "nfr"], axis="columns")

cc = pd.DataFrame()
cc = cc.assign(name = df_data["nombre"])
cc = cc.assign(pxg = df_data["pts_ganados"]/df_data['games_jug'])
cc = cc.assign(nfxg = df_data["NF_total"]/df_data['games_jug'])
cc = cc.assign(rem = (df_data["sm_total"] + df_data["nsmtotal"])/df_data['games_jug'])

cc = cc.groupby("name")[["pxg","nfxg","rem"]].mean().sort_values(by="pxg", ascending=False)

cc = cc.apply(round,2)

