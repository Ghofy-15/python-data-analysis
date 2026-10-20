import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# 1. Création d'un jeu de données réaliste (Expérience, Equipe, Salaire)
data = {
    'Experience_Ans' : [1, 2, 3, 5, 6, 8, 10, 12],
    'Taille_Equipe' : [0, 0, 2, 3, 5, 6, 8, 10],
    'Salaire_Annuel' : [28000, 31000, 36000, 48000, 53000, 64000, 75000, 88000]
    }
df = pd.DataFrame(data)
print("--- Aperçu du jeu de données ---")
print(df)
print("\n" + "="*45 + "\n")
# 2. Analyse de corrélation (Détecter l'impact de l'expérience sur le salaire)
correlation = df['Experience_Ans'].corr(df['Salaire_Annuel'])
print(f"Coefficient de corrélation (Expérience vs Salaire) : {correlation:.2f}")
# 3. Modélisation Prédictive (Régression Linéaire)
x = df[['Experience_Ans']]
y = df['Salaire_Annuel']
model = LinearRegression()
model.fit(x,y)
# 4. Faire une prédiction pour un profil ayant n7 ans d'expérience
exp_test = np.array([[7]])
salaire_predict = model.predict(exp_test)[0]
print(f"\n--- PREDICTON ---")
print(f"Salaire estimé pour 7 ans d'expérience : {salaire_predict:.2f}$")
# 5. Visualisation de la droite de régression
plt.figure(figsize=(8,5))
plt.scatter(df['Experience_Ans'], df['Salaire_Annuel'], color = 'blue', label = 'Données réelles')
plt.plot(df['Experience_Ans'], model.predict(x), color="red", linewidth=2, label="Modèle prédictif")
plt.title("Modèle de Prédiction des Salaires par l'Expérience",fontsize=13, fontweight='bold')
plt.xlabel("Années d'Expérience", fontsize=11)
plt.ylabel("Salaire Annuel ($)", fontsize=11)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()