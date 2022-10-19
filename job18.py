#Je créer ma fonction "myFunction" et ma variable "myList" 
# "(*param)" correspond à mes paramètres
#L'étoile devant me permet d'indiquer qu'il s'agit de plusieurs paramètres.
def myFunction(*param):
    myList = [*param]
#La méthode .sort() permet d'afficher les nombres d'une liste par ordre croissant.
    myList.sort()
    print(myList)

myFunction(10,9,8,7,6,5,4,3,2,1)




