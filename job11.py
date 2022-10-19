#Pour ouvrir le fichier
fichier = open('domains.xml')
#Pour lire le fichier domains.xml
lire_fichier = fichier.read()
#La variable "fichier_filtré" me permettra de filtrer uniquement le nombre de nom de domaine.
fichier_filtré = lire_fichier.count('"domain">')
#Pour afficher le resultat filtré
print(fichier_filtré)
