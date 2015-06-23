# -*- coding: utf-8 -*-
from twitter import *
t = Twitter(auth=OAuth('3317742490-VCmb9dUCXxtiKjOVBigRfDWQEko34TOJmRqZB9W', 'OIunphd5UoKe8kMFAAGoHnOuJ5GXF2ROceE39feBlZ8eS','IicoNuhSOlY6ciZ9bdzzbva8s', 'Cmr35qwqd1n06tdDtYmRzbqmYvZFXQmrLmsWDenKf3GYZTFBXO'))
import numpy
from numpy import random
dico=open('../Résolution/Dico_final.txt', 'r')
list=(dico.readline()).split()
wd=list[random.randint(0,len(list))]
letter=0
tr=1
#nécessité de modifier les print en envoi de tweet
print('Mot de {} lettres, commencant par {}'.format(len(wd), wd[0]))
t.statuses.update(status='Mot de {} lettres, commencant par {}'.format(len(wd), wd[0]))
verif=[]
usr=str(input('entrer un mot : '))
pos=[]
usr1=[]
if usr=='DEFINE':
    wd=str(input('wd ?'))
    usr=str(input('entrer un mot : '))
if usr in list:
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
    t.statuses.update(status=usr+':'+str(verif))
else:
    print('\'\'')
    #t.statuses.update(status='\'\'')
if usr=='SOLUCE0401':
    print(wd)
if usr=='DEFINE':
    wd=str(input('wd ?'))
while usr!=wd:
    verif=[]
    pos=[]
    usr1=[]
    usr=str(input('entrer un mot : '))
    if usr in list:
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
        t.statuses.update(status=usr+' : '+str(verif))
    else:
        print('\'\'')
        #t.statuses.update(status='\'\'')
    if usr=='SOLUCE0401':
        print(wd)
    tr=(tr+1)
print('C\'est bien {}, trouve en {} essais.'.format(usr, tr))
t.statuses.update(status='C\'est bien {}, trouve en {} essais.'.format(usr, tr))
