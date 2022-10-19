#J'indique les paramètres de ma variable entre parenthèses après le nom de ma fonction.
#Dans ma variable "resultat", j'indique vouloir additionner mes deux paramètres.
#return me permet de stocker le résultat de l'addition.
#Je définit ma variable "variable" en y intégrant ma fonction "myAddition" ainsi que les chiffres choisis pour le calcul.
#J'imprime cette dernière variable.

def myAddition (a,b):
    resultat = a + b
    return resultat

variable = myAddition(7,3)
print(variable)