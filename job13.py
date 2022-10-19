import re

nombre = int(input("Entrez un nombre : "))
#Ouverture du fichier en lecture
f = open("data.txt", 'r')
#Tri du fichier
regex = re.findall(r"\b[a-zA-Z]{%d}\b" %(nombre), f.read())
#Nombres de mots triés
print(f"Il y a {len(regex)} mots de {nombre} caractères dans ce fichier")