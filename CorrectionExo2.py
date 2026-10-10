"""
var x,y,som,div,mul,sous: Reel

Debut
  Ecrire 'Saisir une valeur'
  lire x
  Ecrire 'Saisir une autre valeur'
  lire y
  som=x+y
  div=x/y
  mul=x*y
  sous=x-y
  
  Ecrire "somme : ",som
  Ecrire "division :',div
  Ecrire "mul : ",mul
  Ecrire "sous :",sous
Fin

"""
x=float(input('Saisir une valeur : ')) 
y=float(input('Saisir une autre valeur : '))
som=x+y
div=x/y #division réel
divEnt=x//y
mod=x%y
mul=x*y
sous=x-y
exp=x**y
print("somme : ",som,sep="=>",end="***")

