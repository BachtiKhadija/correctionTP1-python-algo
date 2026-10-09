"""
Var a ,b,S,P: entier
Debut 
   Ecrire ‘’saisir a ‘’
   Lire a
   Ecrire ‘’saisir b‘’
   Lire b 
   S=a+b
   P=a*b 
   Ecrire ‘’La somme de’’,a,’’ et’’,b,’’ est :’’,S
   Ecrire ‘’Le prduit de’’,a,’’ et’’,b,’’ est :’’,P
Fin
ceci est un commentaire sur plusieurs lignes
"""
#ceci est un commentaire => un code invisible pour le processeur
a=int(input("saisir a "))#   Lire a
print(type(a))
b=int(input("saisir b : "))#   Lire b
print(type(b))
S=a+b
P=a*b 
print("La somme de",a,"et",b,"est :",S,sep="**",end="#####")
#print("Le produit de",a,"et",b,"est :",P)
print(f"Le produit de {a} et {b} est :{P}")
print("Le produit de {} et {} est :{}".format(a,b,P))