import pandas as pd
import matplotlib.pyplot as plt
# Création d'un mini jeu de données de ventes
data = {
    'Produit': ['Clavier', 'Souris', 'Ecran', 'Casque', 'Webcam'],
    'Categorie': ['Accessoire', 'Accessoire', 'Informatique', 'Accessoire', 'Informatique'],
    'Prix_unitaire': [45.0, 25.0, 180.0, 60.0, 75.0],
    'Quantite_vendue': [12, 25, 8, 15, 10]
}
# Transformation en tableau
df = pd.DataFrame(data)
# Sauvegarde au format CSV sur votre ordinateur
df.to_csv('ventes.csv', index=False)
print("Fichier 'vente.csv' créé avec succès !")
df = pd.read_csv('ventes.csv')
print("***Aperçu des données de ventes***")
#display(df)
df['Chiffre_affaires'] = df['Prix_unitaire'] * df['Quantite_vendue']
ca_total = df['Chiffre_affaires'].sum()
produit_top = df.loc[df['Chiffre_affaires'].idxmax(), 'Produit']
print("\n***Rapport d'Analyse Automatique***")
print(f"Chiffre d'affaires global : {ca_total} $")
print(f"Produit le plus rentable : {produit_top}")
# créer un graphique de barre
plt.figure(figsize = (8, 5))
plt.bar(df['Produit'], df['Chiffre_affaires'], color='skyblue', edgecolor='black')
# Personalisation
plt.title("Chiffre d'affaire par produit", fontsize=14,fontweight='bold')
plt.xlabel("Produit", fontsize=12)
plt.ylabel("Chiffre d'affaires ($)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()