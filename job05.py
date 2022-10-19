valeur1 = int(input("Valeur 1: "))
valeur2 = int(input("Valeur 2: "))

if (valeur1 == valeur2):
    print("Valeurs égales")
elif (valeur1 < valeur2):
    for i in range(valeur1+1, valeur2): #+1 car nous voulons afficher le chiffre qui vient juste après la valeur1.
        print(i)
elif (valeur1 > valeur2):
    for i in range (valeur1-1,valeur2, -1): #_1 car nous voulons afficher le chiffre qui vient juste avant la valeur1.
        print(i)

# <<<- Le "for i in range" va nous permettre d'afficher les valeurs comprises entre valeur1 et valeur2.
