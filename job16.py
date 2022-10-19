#Je défini ma fonction, l'étoile juste avant la variable me permet d'imprimer l'ensemble de mes arguments.
#Utiliser la boucle me permettra d'afficher les arguments sous forme de liste dans le terminal.
def nb_arguments_indefini(*args):
	for x in args:
		print (x)

nb_arguments_indefini("Naruto","Uzumaki","7 ème Hokage","rasengan","Itachi", "Uchiwa")