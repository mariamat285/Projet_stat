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
print(f"Corrélation entre le prix_unitaire et quantité est: {corr:.3f}")

sns.barplot(data=df, x='prix_unitaire', y='quantite', hue='categorie', alpha=0.7, errorbar=None)
plt.title("Prix unitaire vs Quantité vendue")
plt.xlabel("Prix unitaire")
plt.ylabel("Quantité")
plt.tight_layout()
plt.show()

print("""
Interprétation :
Le graphique révèle que la relation entre prix et quantité n'est pas 
strictement linéaire. Si les produits très chers (5.5, 8.9) sont 
effectivement achetés en faibles quantités, ce n'est pas vrai pour les 
prix les plus bas : ce sont plutôt les produits à prix intermédiaire 
(Produits Laitiers, Fruits & Légumes, entre 1 et 2.5) qui affichent 
les quantités moyennes les plus élevées. Cela explique pourquoi le 
coefficient de corrélation linéaire calculé reste faible : la relation 
prix-quantité semble davantage en forme de cloche inversée qu'une 
simple tendance décroissante.
""")


# Q2 — Catégorie qui génère le plus de CA

ca_cat = df.groupby('categorie')['chiffre_affaires'].sum().sort_values(ascending=True)

ca_cat.plot(kind='barh', color='coral', edgecolor='white', figsize=(8, 5))
plt.title("Chiffre d'affaires total par catégorie")
plt.xlabel("CA")
plt.tight_layout()
plt.show()

# Afficher le top
print(ca_cat.sort_values(ascending=False))

print("""
Interprétation :
Fruits & Légumes arrive en tête du chiffre d'affaires (environ 157), 
suivi de très près par Entretien & Maison (environ 151). Ce résultat 
est notable : Fruits & Légumes doit son succès à un volume de vente 
élevé (produits peu chers mais achetés en grande quantité), alors 
qu'Entretien & Maison atteint un CA presque équivalent grâce à un prix 
unitaire élevé (8.9) malgré des quantités plus faibles.

Les catégories Boissons et Épicerie Sèche se situent ensuite à un 
niveau intermédiaire (environ 85€ chacune), suivies de Produits 
Laitiers et Boucherie (75-77).

Hygiène & Beauté ferme nettement le classement avec un CA d'environ 
17, largement en dessous des autres catégories — ce qui s'explique 
probablement par un nombre restreint de produits et de transactions 
dans cette catégorie.
""")

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

print("""
Interprétation :
En comparant les deux graphiques, on observe une tendance globale 
cohérente : les catégories les plus chères (Entretien & Maison à 
8.9, Boucherie à environ 5) affichent les quantités moyennes les 
plus faibles (autour de 2 et 1.7 respectivement).

À l'inverse, les catégories à prix modéré comme Produits Laitiers 
(1.3) et Fruits & Légumes (2.2) affichent les quantités moyennes 
les plus élevées (environ 4.3 et 4).

Cependant, la relation n'est pas parfaitement linéaire : Boulangerie, 
malgré son prix très bas (environ 1), n'a pas la quantité la plus 
élevée (3.5), restant inférieure à Produits Laitiers et Fruits & 
Légumes. De même, Hygiène & Beauté et Boissons, à prix similaires 
(environ 2.3-2.5), ont des quantités moyennes comparables (environ 
2.3-2.5).

Globalement, le prix semble donc influencer les ventes, mais cette 
influence n'est nette que sur les extrêmes (très cher → faible 
quantité) ; entre les catégories à prix bas et modéré, d'autres 
facteurs (nature du produit, fréquence d'achat) entrent probablement 
en jeu.
""")