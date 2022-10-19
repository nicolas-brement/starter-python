#le mode regex
import re
#fonction pour retourner une liste
def longueur(liste):
	c = 0
	for j in liste:
		c += 1
	return c

#pour ouvrir le fichier et le lire
with open("data.txt") as file:
	contenu = file.read()

#J'utilise regex pour isoler tous les mots d'une liste
mots = re.findall(r"\b[a-zA-Z]{1,}\b", contenu)
print ("Nombre de mots = ", longueur(mots))