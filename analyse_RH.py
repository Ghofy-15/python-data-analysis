import pandas as pd
# 1. Création d'un jeu de données simulant des données RH
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Departement': ['IT', 'Marketing', 'IT', 'RH', 'Marketing', 'IT'],
    'Salaire': [3500, 2900, 4200, 2500, 3100, None],
    'Année_experience': [3, 2, 5, 1, 4, 6]
}
df = pd.DataFrame(data)
print("--- Données brutes initiale ---")
print(df)
print("\n" + "="*40 + "\n")

#2. Nettoyage des données : Remplacer les salaires manquants par la moyenne du salaire
salaire_moyen = df['Salaire'].mean()
df['Salaire'] = df['Salaire'].fillna(salaire_moyen)
print("--- Données après nettoyage (Valeurs manquantes corrigées) ---")
print(df)
print("\n" + "="*40 + "\n")

#3. Analyse statistiques avancée : Regroupement par département
salaire_par_dep = df.groupby('Departement')['Salaire'].mean()
print("--- Salaire moyen par département ---")
print(salaire_par_dep)

#4. Sauvegarde propre du résultat nettoyé
df.to_csv("employes_nettoyes.csv", index = False)
print("\nFichier 'employes_nettoyes.csv' généré et sauvegarder avec succès !")