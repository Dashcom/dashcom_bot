# -*- coding: UTF-8 -*-
import numpy
from numpy import random
dico=open('../Résolution/Dico_final.txt', 'r')
list=(dico.readline()).split()
wd=list[random.randint(0,len(list))]
letter=0
tr=1
#nécessité de modifier les print en envoi de tweet
print('Mot de {} lettres, commencant par {}'.format(len(wd), wd[0]))
verif=[]
usr=raw_input('entrer un mot : ')
pos=[]
usr1=[]
if usr=='DEFINE':
    wd=raw_input('wd ?')
    usr=raw_input('entrer un mot : ')
if wd in list:
    for i in range(0, len(wd)):
        pos.append(wd[i])
        usr1.append(usr[i])
    for i in range(0, len(wd)):
        if usr[i]==wd[i]:
            verif.append(2)
            pos[i]=0
            usr1[i]=2
        else:
            verif.append(0)
    for i in range(0, len(pos)):
        if usr1[i] in pos:
            verif[i]=1
            rm=pos.index(usr1[i])
            pos[rm]=0
    print(verif)
else:
    print('\'\'')
if usr=='SOLUCE0401':
    print(wd)
if usr=='DEFINE':
    wd=raw_input('wd ?')
while usr!=wd:
    verif=[]
    pos=[]
    usr1=[]
    usr=raw_input('entrer un mot : ')
    if wd in list:
        for i in range(0, len(wd)):
            pos.append(wd[i])
            usr1.append(usr[i])
        for i in range(0, len(wd)):
            if wd[i]==usr[i]:
                verif.append(2)
                pos[i]=0
                usr1[i]=2
            else:
                verif.append(0)
        for i in range(0, len(pos)):
            if usr1[i] in pos:
                verif[i]=1
                rm=pos.index(usr1[i])
                pos[rm]=1
        print(verif)
    else:
        print('\'\'')
    if usr=='SOLUCE0401':
        print(wd)
    tr=(tr+1)
print('C\'est bien {}, trouve en {} essais.'.format(usr, tr))
