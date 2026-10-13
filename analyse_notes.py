notes_etudiants = [14, 16, 12, 15, 13, 17]
moyenne = sum(notes_etudiants)/len(notes_etudiants)
note_max = max(notes_etudiants)
note_min = min(notes_etudiants)
print("***Rapport d'analyse de données***")
print(f"Série de notes : {notes_etudiants}")
print(f"Moyenne générale : {moyenne:.2f}")
print(f"Note maximale : {note_max}")
print(f"Note minimale : {note_min}")