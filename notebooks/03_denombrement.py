import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import os
os.makedirs("../outputs/figures", exist_ok=True)



#--------------------DATA FRAME-----------------------------
df = pd.read_csv("../data/ventes_supermarche.csv", sep=';')

from math import comb

# ---- Q3.1 : Paniers de 3 produits différents ----
nb_produits = df['produit'].nunique()
paniers = comb(nb_produits, 3)

print(f"Nombre de produits distincts : {nb_produits}")
print(f"Nombre de paniers de 3 produits possibles : C({nb_produits}, 3) = {paniers}")

# ---- Q3.2 : Combinaisons de produits par catégorie ----
print("\n=== Combinaisons de 2 produits par catégorie ===")
for categorie, groupe in df.groupby('categorie'):
    nb = groupe['produit'].nunique()
    combinaisons = comb(nb, 2) if nb >= 2 else 0
    print(f"{categorie} : {nb} produits → C({nb}, 2) = {combinaisons} combinaisons")