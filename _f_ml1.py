import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


#dataset con los datos por equipo con resultado - df_gop (gano o perdio)
df_gop = pd.read_excel("_ml1_eqxset.xlsx")

#quitar outlier de sd en bruselas 3er set
df_gop.drop(49, axis=0, inplace=True)
df_gop

#cambiar index 
df_gop.set_index('nombre',inplace=True)

#agregar puntos netos
df_gop["pts_netos"] = df_gop["pto_tot"] - df_gop["nf"]


#df con games ganados
df_gano = df_gop[df_gop["gano_set"]=="g"]

all_cols = ['nf', 'w', 'sm', 'ns', 'csm', 'fondo', 'm3', 'm5',
       'm7', 'pto_tot', 'tot_snf', "pts_netos", 'ed','games jug', "set"]

#res_col = ["nf", "pto_tot", "tot_snf","sm","ns", "games jug"]
res_col = ["pto_tot", "tot_snf", "pts_netos", "nf","games jug"]


df_gano = df_gano[res_col]

df_ganoxgame = round(df_gano.div(df_gano["games jug"], axis=0),3)
df_ganoxgame["result"] ="g"


#df con games perdidos
df_perdio = df_gop[df_gop["gano_set"]=="p"]
df_perdio = df_perdio[res_col]

df_perdioxgame = round(df_perdio.div(df_perdio["games jug"], axis=0),3)
df_perdioxgame["result"] ="p"

#concatenar los df gano y perdio 

all = pd.concat([df_ganoxgame, df_perdioxgame])
all.drop("games jug", axis=1, inplace=True)
all["result"] = np.where(all["result"] == "g",1,0)


df_corr = all.corr()
df_corr.drop(["nf","pto_tot","tot_snf","pts_netos"], axis=1,inplace=True)

fig,axs = plt.subplots(2,2, figsize= (6,4))

#primer grafico
ax = axs[0,0]
ax.scatter(all["pto_tot"], all["result"], color="black")
ax.set_title("Puntos totales")
ax.set_yticks([0,1],["Perdedor","Ganador"])
ax.set_xlabel("Cantidad por game")
ax.set_
plt.margins(y=2)  # Ajusta el margen vertical


ax = axs[0,1]
ax.scatter(all["nf"], all["result"], color="black")
ax.set_title("No forzados")
ax.set_yticks([0,1],["Perdedor","Ganador"])
ax.set_xlabel("Cantidad por game")


#segunda fila
ax = axs[1,0]
ax.scatter(all["tot_snf"], all["result"], color="black")
ax.set_title("Puntos sin no forzados rivales")
ax.set_yticks([0,1],["Perdedor","Ganador"])
ax.set_xlabel("Cantidad por game")
plt.margins(y=0.1)  # Ajusta el margen vertical


ax = axs[1,1]

ax.scatter(all["pts_netos"], all["result"], color="black")
ax.set_title("Puntos netos")
ax.set_yticks([0,1],["Perdedor","Ganador"])
ax.set_xlabel("Cantidad por game")
plt.tight_layout()
plt.show()
