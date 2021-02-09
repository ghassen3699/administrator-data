
# lire le nom de l'administrateur
def nom_administrateur () :
    print("LE NOM : ")
    nom = input("---> ")
    return nom




# lire le prenom de l'administrateur
def prenom_administrateur () :
    print('LE PRENOM : ')
    prenom = input("---> ")
    return prenom





# lire l'age de l'administrateur
def age_administrateur () :
    print("L'AGE : ")
    test = False
    while test == False :
        while True :
            try:
                age = int(input("---> "))
                break
            except ValueError :
                print("ERREUR ENTRER UN ENTIER ")
        if age < 18 :
            test = False
            print("ERREUR IF FAUT QUE L'AGE SUPPERIEUR A 18 ")
    return age





# lire l'adresse de l'administrateur
def adresse () :
    print("ADRESSE : ")
    adresse = input("---> ")
    return adresse





# lire le code postal de l'administrateur
def code_postal () :
    test = True
    print("LE CODE POSTAL : ")
    while test == False :
        code_p = input("---> ")
        if len(code_p) == 4 :
            test = True
        else:
            print("ERREUR ENTRER VOTRE CODE POSTAL CORRECTEMENT ")
    return code_p





# lire l'adresse mail de ladministrateur
def adresse_mail () :
    compteur = 0
    compteur_2 = 0
    test_1 = '.'
    test_2 = '@'
    print("ADRESSE MAIL : ")
    test = False
    while test == False :
        adrese_m = input("---> ")
        for i in range(len(adrese_m)) :
            if adrese_m[i] == test_1 :
                compteur += 1
            else:
                pass

        for i in range(len(adrese_m)) :
            if adrese_m[i] == test_2 :
                compteur_2 += 1
            else:
                pass

        if compteur == 1 and compteur_2 == 1 :
            test = True
        else :
            print("ERREUR ENTRER VOTRE ADRESSE MAIL CORRECTEMENT !!!")
    return adrese_m




# lire le numero de la carte national de l'administrateur
def cin_administrateur () :
    print("CIN : ")
    test = False
    while test == False :
        cin = input("---> ")
        if len(cin) == 8 :
            test = True
        else:
            print("ERREUR ENTRER LE NUMERO DE CIN CORRECTEMENT !!!")
    return cin




# lire le poste de l'administrateur
def poste_administrateur () :
    print("VOTRE POSTE : ")
    print("1) AGENT DE CAISSE")
    print("2) AGENT DE COMPTABILITE")
    print("3) AGENT DE RESSOURSE HUMAINE")
    print("4) PDG")

    test = False
    while test == False :
        while True :
            try:
                poste = int(input("---> "))
                break
            except ValueError :
                print("ERREUR ENTRER UN ENTIER DE 1 A 4 SUIVANT VOTRE POSTE ")
        if poste == 1 or poste == 2 or poste == 3 or poste == 4 :
            test = True
        else:
            print("ERREUR ENTRER VOTRE POSTE CORRECTEMENT ")

    if poste == 1 :
        poste_ad = "AGENT DE CAISSE"
        return poste_ad
    elif poste == 2 :
        poste_ad = "AGENT DE COMPTABILITE"
        return poste_ad
    elif poste == 3 :
        poste_ad = "AGENT DE RESSOURSE HUMAINE"
        return poste_ad
    else:
        poste_ad = "PDG"
        return poste_ad




