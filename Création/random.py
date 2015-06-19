# -*- coding: latin-1 -*-
import numpy
from numpy import random
dico=open('../Résolution/dico8.txt', 'r')
list=(dico.readline()).split()
#print(list)
wd=list[random.randint(0,len(list))]
letter=0
#nécessité de modifier les print en envoi de tweet
print('mot de ', len(wd), 'lettres', 'commencant par', wd[0])
verif=[]
print(wd)
usr=input('entrer un mot ')
if wd in list == True:
    for i in range(0, len(wd)):
        if wd[i]==usr[i]:
            verif.append(2)
        else:
            verif.append(0)
    print(verif)
else:
    print('\'\'')
while usr!=wd:
    verif=[]
    usr=input('entrer un mot ')
    if wd in list == True:
        for i in range(0, len(wd)):
            if wd[i]==usr[i]:
                verif.append(2)
            else:
                verif.append(0)
        print(verif)
    else:
        print('\'\'')
print('c\'est bien', usr, 'bravo')
