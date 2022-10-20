valeur = input(">")               #J'indique que le chevron correspond à ma valeur.

while valeur != "Aurevoir":       #Je créer une boucle while
    if valeur == "Bonjour":       #J'indique sur si le résultat rentré est "Bonjour"
     print("Bonjour à toi")       #alors le terminal devra répondre "Bonjour à toi".
     valeur = input(">")          #Après chaque réponse, le terminal devra continuer d'afficher un chevron.

    elif valeur == "Aurevoir":    #J'indique que si l'utilisateur saisit "Aurevoir"
        exit()                    #Alors le programme devra s'arrêter.
    valeur = input(">")           #J'indique que si la réponse saisi est différente de "Aurevoir" ou "Bonjour", alors un chevron devra réapparaitre pour une nouvelle saisi.

