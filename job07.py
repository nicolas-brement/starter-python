for fizzbuzz in range(100):                         #Je crée ma boucle for ainsi qu'une liste d'une valeur numérique de 100.
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:     #J'indique que lorsqu'un chiffre est un multiple de 3 et de 5 à
        print("fizzbuzz")                           #alors "fizzbuzz" s'affichera à la place de ce chiffre.
        continue
    elif fizzbuzz % 3 == 0:                         #J'indique que lorsqu'un chiffre est un multiple de  3
        print("fizz")                               #alors "fizz" s'affichera à la place de ce chiffre.
        continue
    elif fizzbuzz % 5 == 0:                         ##J'indique que lorsqu'un chiffre est un multiple de 5
        print("buzz")                               #alors "buzz" s'affichera à la place de ce chiffre.
        continue
    print(fizzbuzz)