import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/ventes_supermarche.csv", sep=';')

# Préparation des données
df['date'] = pd.to_datetime(df['date'])
df['chiffre_affaires'] = df['prix_unitaire'] * df['quantite']

# Q1 — P(client achète un produit alimentaire)
categories_alim = ['Fruits & Légumes', 'Boulangerie', 'Épicerie Sèche', 
                   'Produits Laitiers', 'Boucherie']

p_alim = df['categorie'].isin(categories_alim).mean()
print(f"P(produit alimentaire) = {p_alim:.3f} soit {p_alim*100:.1f}%")

# Q2 — P(produit vendu est une boisson)
p_boisson = (df['categorie'] == 'Boissons').mean()
print(f"P(Boisson) = {p_boisson:.3f} soit {p_boisson*100:.1f}%")

# Q3 — P(vente > moyenne journalière)
ca_par_jour = df.groupby(df['date'].dt.date)['chiffre_affaires'].sum()
moyenne_jour = ca_par_jour.mean()
print(f"CA moyen journalier : {moyenne_jour:.2f}")

p_sup = (df['chiffre_affaires'] > moyenne_jour).mean()
print(f"P(vente > moyenne journalière) = {p_sup:.3f} soit {p_sup*100:.1f}%")