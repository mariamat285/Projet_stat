import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#  Séparateur ";"
df = pd.read_csv("../data/ventes_supermarche.csv", sep=';')

# Conversion de la date
df['date'] = pd.to_datetime(df['date'])

# Colonne chiffre d'affaires 
df['chiffre_affaires'] = df['prix_unitaire'] * df['quantite']

df.head()

# Q1 — Corrélation prix_unitaire / quantité

corr = df['prix_unitaire'].corr(df['quantite'])
print(f"Corrélation : {corr:.3f}")

sns.barplot(data=df, x='prix_unitaire', y='quantite', hue='categorie', alpha=0.7, errorbar=None)
plt.title("Prix unitaire vs Quantité vendue")
plt.xlabel("Prix unitaire")
plt.ylabel("Quantité")
plt.tight_layout()
plt.show()


# Q2 — Catégorie qui génère le plus de CA

ca_cat = df.groupby('categorie')['chiffre_affaires'].sum().sort_values(ascending=True)

ca_cat.plot(kind='barh', color='coral', edgecolor='white', figsize=(8, 5))
plt.title("Chiffre d'affaires total par catégorie")
plt.xlabel("CA")
plt.tight_layout()
plt.show()

# Afficher le top
print(ca_cat.sort_values(ascending=False))

# Q3 — Le prix influence-t-il les ventes ?

# Quantité moyenne vendue par catégorie + prix moyen
analyse = df.groupby('categorie').agg(
    prix_moyen=('prix_unitaire', 'mean'),
    quantite_moyenne=('quantite', 'mean')
).sort_values('prix_moyen', ascending=False)

print(analyse)

# Visualisation double
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

analyse['prix_moyen'].plot(kind='barh', ax=axes[0], color='steelblue')
axes[0].set_title("Prix moyen par catégorie")

analyse['quantite_moyenne'].plot(kind='barh', ax=axes[1], color='salmon')
axes[1].set_title("Quantité moyenne par catégorie")

plt.tight_layout()
plt.show()