def mySort(*args):
    n = len(args)
    argsList = list(args)
    for i in range(n-1):
        for j in range (0, n-1):
            if (argsList[j] > argsList[j+1]):                               #J'indique que lorsque la première valeur est supérieur à la deuxième
                argsList[j], argsList[j+1] = argsList[j+1], argsList[j]     #Alors la deuxième valeur sera prioritaire sur la première lors de l'affichage.
    return argsList

def myDisplay(argsSort):                    #Sort me permet de modifier la liste.
    print(argsSort)
myDisplay(mySort(5,8,34,2,20,90,3,7))