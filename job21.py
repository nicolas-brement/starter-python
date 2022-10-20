def myFunction(*args):                      #Je créer "myFunction" suivi de mon paramètre.
    args = list(args)                       #Je créer une première liste nommé "args".     
    r=[]                                    #Je créer une deuxième liste nommé "r".

    while args:                             #Je créer une boucle while afin de pouvoir déplacer des valeurs d'un fichier à un autre par ordre croissant.
        mini=args[0]
        for x in args:                      
            if x < mini:
                mini=x
        args.remove(mini)                   #.remove permet de supprimer la première valeur.
        r.append(mini)                      #.append permet d'ajouter un élément à la fin de la liste.
    return r


def myDisplay(te):                          #Je créer une deuxième fonction "myDisplay(te)""
    print(te)                               #Je demande à imprimer ma fonction
myDisplay(myFunction(17,7,91,12,1,13,4,12,18)) #J'exécute mes deux fonctions.

