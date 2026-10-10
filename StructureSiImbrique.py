"""  
var temp:réel

Debut
  lire temp
  si temp<0 alors
     ecrire"c est de la glace"
  sinon si temp<100 alors
     ecrire "liquide"
  sinon    
      ecrire "vapeur"
  fin si 
Fin

"""
temp=float(input("saisir temp : "))
if temp<0 :
    print("c est de la glace")
elif temp<100 :
    print( "liquide")
else:    
    print("vapeur")
 

