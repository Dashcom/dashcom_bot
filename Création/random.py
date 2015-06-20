# -*- coding: UTF-8 -*-
import numpy
from numpy import random
dico=open('../Résolution/Dico_final.txt', 'r')
list=(dico.readline()).split()
#print(list)
wd=list[random.randint(0,len(list))]
letter=0
tr=1
#nécessité de modifier les print en envoi de tweet
print('Mot de {} lettres, commencant par {}'.format(len(wd), wd[0]))
verif=[]
#print(wd)
usr=raw_input('entrer un mot : ')
pos=[]
if wd in list:
    for i in range(0, len(wd)):
        if usr[i] in wd:
            if wd[i]==usr[i]:
                verif.append(2)
            else:
                verif.append(1)
        else:
            verif.append(0)
    print(verif)
else:
    print('\'\'')
if usr=='SOLUCE0401':
    print(wd)
while usr!=wd:
    verif=[]
    usr=raw_input('entrer un mot : ')
    if wd in list:
        pos=wd
        for i in range(0, len(wd)):
            if usr[i] in wd:
                if wd[i]==usr[i]:
                    verif.append(2)
                    #pos.remove(i)
                else:
                    verif.append(1)
            else:
                verif.append(0)
        print(verif)
    else:
        print('\'\'')
    if usr=='SOLUCE0401':
        print(wd)
    tr=(tr+1)
print('C\'est bien {}, trouve en {} essais.'.format(usr, tr))
