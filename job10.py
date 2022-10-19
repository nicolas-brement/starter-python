answer = input("Entrez 'wr' pour écrire dans le fichier ou 're' pour le lire: ")

if answer == "wr" :
    n = input("Entrez votre texte: ") #"n" correspond à la variable du contenu de mon fichier.
    f = open("output.txt" , mode = 'a') #"f" correspond à la variable de mon fichier.
    f.write(n) #Cette méthode me permettra d'écrire dans le fichier.
    f.close() #Cette méthode me permettra de fermer le fichier.
elif answer == "re" : 
    f = open("output.txt" , mode = 'r') #Ma variable "f" me permettra d'ouvrir le fichier uniquement en lecture.
    print(f.read())



