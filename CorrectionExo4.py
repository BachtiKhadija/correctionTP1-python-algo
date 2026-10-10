"""
const TVA=0.2
const PA=5.00
const PB=2.5
const PC=3.00
const PD=10.00
const PE=7.00
var ptht,pttc : Réel
var X,Y,Z,T,U : Entier
début
  lire X,Y,Z,T,U 
  ptht=X*PA+Y*PB+Z*PC+T*PD+U*PE
  pttc=ptht + ptht*TVA
  
  Ecrire "le montant à payer est : ",pttc
Fin

"""
TVA,PA,PB,PC,PD,PE=0.2,5.00,2.5,3.00,10.00,7.00
X,Y,Z,T,U =int(input("saisir X: ")),int(input("saisir Y: ")),int(input("saisir Z: ")),int(input("saisir T: ")),int(input("saisir U: "))
ptht=X*PA+Y*PB+Z*PC+T*PD+U*PE
pttc=ptht + ptht*TVA
  
print("le montant hors est  : ",ptht,"\nle montant à payer est : ",pttc,sep="=>")

