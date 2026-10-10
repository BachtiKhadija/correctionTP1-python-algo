"""
const TVA=0.2
var pht,qte,ptht,pttc :Reel 
debut 
  /*ph => prix hors taxe
  ptht =>prix total hors taxe 
  pttc => prix tout taxe comprise*/
  //ceci et un commentaire monoligne
  #ceci est un commentaire monoligne
  
  
  Ecrire "saisir le prix unitaire"
  lire pht 
   Ecrire "saisir la quantité"
   lire qte 
   ptht=pht*qte 
   pttc=ptht + ptht*TVA
  
  Ecrire "Le pric à payer est : ",pttc

Fin
"""
TVA=0.2
"""ph => prix hors taxe
  ptht =>prix total hors taxe 
  pttc => prix tout taxe comprise"""
#ceci et un commentaire monoligne
pht=float(input("saisir le prix unitaire : "))
qte=int(input("saisir la quantité : "))
ptht=pht*qte 
pttc=ptht + ptht*TVA
  
print(f"ptht =>{ptht}")
print("pttc =>{}".format(pttc))

