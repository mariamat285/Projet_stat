import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import os
os.makedirs("../outputs/figures", exist_ok=True)

plt.savefig("../outputs/figures/distribution_quantites.png")

#--------------------DATA FRAME-----------------------------
df = pd.read_csv("../data/ventes_supermarche.csv", sep=';')
print(df.head())
#--------------------CHIFFRE D'AFFAIRE TOTAL-----------------------------
ca = df['prix_unitaire'] * df['quantite']
print(f"CHIFFRE D'AFFAIRE : {ca}")
#-------------------DISTRIBUTION QUANTITE VENDUS-------------------------
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df['quantite'], bins=10, color='mediumpurple', edgecolor='white')

plt.title("Distribution des quantités vendues")
plt.xlabel("Quantité")
plt.ylabel("Fréquence")

plt.tight_layout()
plt.savefig("../outputs/figures/distribution_quantites.png")
plt.show()
print("=== Interprétation : Distribution des quantités vendues ===")
print("Les quantités vendues varient entre 1 et 6 articles par transaction.")
print("Les achats de 1 et 3 articles dominent avec 26 occurrences chacun,")
print("ce qui montre que les clients effectuent majoritairement des achats")
print("en petites quantités.")
print("Les grandes quantités (5 et 6) restent minoritaires,")
print("suggérant que les achats en gros sont rares dans ce supermarché.")
#---------------------PRODUIT LE PLUS VENDU------------------------------------
produit_plus_vendu = df.groupby('produit')['quantite'].sum().idxmax()
quantite_max = df.groupby('produit')['quantite'].sum().max()

print(f"Produit le plus vendu : {produit_plus_vendu}")
print(f"Quantité totale : {quantite_max}")
#--------------------CATEGORIE PLUS FREQUENTE----------------------------------
categorie_plus_frequente = df['categorie'].value_counts().idxmax()
frequence_max = df['categorie'].value_counts().max()

print(f"Catégorie la plus fréquente : {categorie_plus_frequente}")
print(f"Nombre d'apparitions : {frequence_max}")





