

# creation de la base de donnees pour enregistrer les administrateurs de la banque
def creation_bd_administration () :
    import sqlite3

    fichier_administrations = "les_ouvriers.db"
    try:
        administrations = sqlite3.connect(fichier_administrations)
        administrations_curseur = administrations.cursor()
        administrations_curseur.execute(""" create table les_ouvriers
            cin text primary key ,
            nom text ,
            prenom text ,
            age integer ,
            adresse text ,
            code_postal text ,
            adresse_mail text ,
            poste text ;)""")
        administrations.commit()
    except sqlite3.OperationalError :
        print("ERREUR LA TABLE DES OUVRIERS EXISTE DEJA")
    finally:
        administrations.close()




# ajouter un administrateur a la base de donnees
def ajouter_administrateur () :
    import administrateur
    import sqlite3
    fichier_administrations = "les_ouvriers.db"

    try:

        nom = administrateur.nom_administrateur()
        prenom = administrateur.prenom_administrateur()
        age = administrateur.age_administrateur()
        adresse = administrateur.adresse()
        code_p = administrateur.code_postal()
        cin = administrateur.cin_administrateur()
        adresse_mail = administrateur.adresse_mail()
        poste = administrateur.poste_administrateur()


        conn = sqlite3.connect(fichier_administrations)
        cur = conn.cursor()
        print("CONNEXION REUSSIE A VOTRE BASE DE DONNEES ")
        sql = "insert into les_ouvriers (cin , nom ,prenom , age ,adresse ,code_postal ,adresse_mail ,poste"
        value = (cin,nom,prenom,age,adresse,code_p,adresse_mail,poste)
        cur.execute(sql,value)
        conn.commit()
        print("ENREGISTREMENT TERMINER ")
        cur.close()
        conn.close()

    except sqlite3.Error :
        print("ERREUR !!! LORS DE L'INSERTION DE L'ADMINISTRATEUR ")





# supprimer un administrateur a la base de donnees
def supprimer_administrateur () :
    import administrateur
    import sqlite3
    fichier_administrations = "les_ouvriers.db"
    try:
        cin = administrateur.cin_administrateur()
        conn = sqlite3.connect(fichier_administrations)
        cur = conn.cursor()
        print("CONNEXION REUSSIE A VOTRE BASE DE DONNEES ")

        sql = "delete from les_ouvriers where cin = ?"
        cur.execute(sql,(cin,))
        conn.commit()
        print("ENREGISTREMENTS SUPPRIMES AVEC SUCCES")

        cur.close()
        conn.close()
    except sqlite3.Error :
        print("ERREUR !!! LORS DU SUPPRISSION DE L'ADMINISTRATEUR ")





# modifier le nom de l'ouvrier
def modifier_nom_ouvrier () :
    import administrateur
    import sqlite3
    fichier_administrations = "les_ouvriers.db"


    try:
        print("LA MODIFICATION : ")
        cin = administrateur.cin_administrateur()
        nom = administrateur.nom_administrateur()

        conn = sqlite3.connect(fichier_administrations)
        cur = conn.cursor()
        print("CONNEXION REUSSIE A VOTRE BASE DE DONNEES")
        sql = "update les_ouvriers set nom = ? where cin = ?"
        value = (nom,cin)

        cur.execute(sql,value)
        conn.commit()
        print("ENREGISTREMENT MIS A JOUR AVEC SUCCES")
        cur.close()
        conn.close()
    except sqlite3.Error :
        print("ERREUR !!! LORS DU MIS A JOUR DANS LA BASE DE DONNEES ")





# modifier le prenom de l'ouvrier
def modifier_prenom_administrateur () :
    import administrateur
    import sqlite3
    fichier_administrations = "les_ouvriers.db"

    try :
        print("LA MODIFICATION : ")
        cin = administrateur.cin_administrateur()
        prenom = administrateur.prenom_administrateur()

        conn = sqlite3.connect(fichier_administrations)
        cur = conn.cursor()
        print("CONNEXION REUSSIE A VOTRE BASE DE DONNEES ")
        sql = "update les_ouvriers set prenom = ? where cin = ?"
        value = (prenom,cin)

        cur.execute(sql,value)
        conn.commit()
        print("ENREGISTREMENT AVEC SUCCES")
        cur.close()
        conn.close()
    except sqlite3.Error :
        print("ERREUR !!! LORS DU MIS A JOUR DANS LA BASE DE DONNEES")



# modifier l'age de l'ouvrier
def modifier_age_administrateur () :
    import administrateur
    import sqlite3
    fichier_administrations = "les_ouvriers.db"

    try :
        print("LA MODIFICATION : ")
        cin = administrateur.cin_administrateur()
        age = administrateur.age_administrateur()

        conn = sqlite3.connect(fichier_administrations)
        cur = conn.cursor()
        print("CONNEXION REUSSIE AVEC SUCCES")
        cur.close()
        conn.close()
    except sqlite3.Error :
        print("ERREUR !!! LORS DU MIS A JOUR DANS LA BASE DE DONNEES ")





