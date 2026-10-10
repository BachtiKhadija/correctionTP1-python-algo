"""
demander l age et afficher adulte ou mineur 

var age : Entier
Debut
    Ecrire "saisir votre age"
    lire age 
    si age>=18 alors
        ecrire "vous êtes adulte"
    sinon
        ecrire "tu es mineur"
    FinSi
Fin
"""

age=int(input("saisir votre age : ")) 
if age>=18 :
    print("vous êtes adulte")
else:
    print("tu es mineur")

