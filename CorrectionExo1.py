A,B=int(input("saisir A :")),int(input("saisir B :"))
print("*"*20,"BEFORE","*"*20,sep='')
print(f"A={A} - B = {B}")
"""C=A
A=B
B=C"""
A,B=B,A
print("*"*20,"After","*"*20,sep='')
print(f"A={A} - B = {B}")
