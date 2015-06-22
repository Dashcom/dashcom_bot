# -*- coding: UTF-8 -*-
import numpy
import time
from numpy import random
debug='False'
testAll='False'
fileOutput='True'
sync='True'
syncfile=open('../Résolution/log2.txt', 'r')
log=open('log.txt', 'w')
essais=open('essais.txt','a')
try:
    config=open('config.txt', 'r').readlines()
    if 'debug:ON\n' in config:
        debug='True'
    if 'testAll:ON\n' in config:
        testAll='True'
    if 'fileOutput:ON\n' in config:
        fileOutput='True'
        log=open('log.txt', 'w')
        essais=open('essais.txt','a')
    if 'sync:On\n' in config:
        sync='True'
        try:
            syncfile=open('../Résolution/log2.txt', 'r')
        except NameError:
            sync='False'
            pass
        except IOError:
            sync='False'
            pass
except NameError:
    config=[]
    pass
except IOError:
    pass
    config=[]
dico=open('../Résolution/Dico_final.txt', 'r')
liste=(dico.readline()).split()
if testAll=='False':
    wd=liste[random.randint(0,len(liste))]
else :
    wd=liste[0]
letter=0
tr=1
print('Mot de {} lettres, commencant par {}'.format(len(wd), wd[0]))
if fileOutput=='True':
    log.write('{}, {}'.format(len(wd),wd[0]))
    log.close()
verif=[]
if fileOutput=='False':
    usr=raw_input('entrer un mot : ')
if fileOutput=='True' and sync=='True':
    time.sleep(0,5)
    usr=syncfile.readline()
pos=[]
usr1=[]
if debug=='True':
    if usr=='DEFINE':
        wd=raw_input('wd ?')
        usr=raw_input('entrer un mot : ')
if usr in liste:
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
    if fileOutput=='True':
        for i in range(0,len(verif)):
            verif[i]=str(verif[i])
        verif="".join(verif)
        log=open('log.txt', 'w')
        log.write(verif)
        log.close()
else:
    print('\'\'')
    if fileOutput=='True':
        log=open('log.txt', 'w')
        log.write('\'\'')
        log.close()
if debug=='True':
    if usr=='SOLUCE':
        print(wd)
    if usr=='DEFINE':
        wd=raw_input('wd ?')
if fileOutput=='True':
    essais.write('{}:{}'.format(usr,tr))
if testAll=='True':
    for i in (1, len(liste)):
        wd=liste[i]
        letter=0
        tr=1
        print('Mot de {} lettres, commencant par {}'.format(len(wd), wd[0]))
        if fileOutput=='True':
            log=open('log.txt', 'w')
            log.write('{}, {}'.format(len(wd),wd[0]))
            log.close()
        verif=[]
        if fileOutput=='False':
            usr=raw_input('entrer un mot : ')
        if fileOutput=='True' and sync=='True':
            usr=syncfile.readline()
        pos=[]
        usr1=[]
        if debug=='True':
            if usr=='DEFINE':
                wd=raw_input('wd ?')
                usr=raw_input('entrer un mot : ')
        if usr in liste:
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
        if debug=='True':
            if usr=='SOLUCE':
                print(wd)
            if usr=='DEFINE':
                wd=raw_input('wd ?')
        while usr!=wd:
            verif=[]
            pos=[]
            usr1=[]
            if fileOutput=='False':
                usr=raw_input('entrer un mot : ')
            if fileOutput=='True' and sync=='True':
                time.sleep(0,5)
                usr=syncfile.readline()
            if usr in liste:
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
                if fileOutput=='True':
                    log.write(''.join(verif))
                    log.close()
            else:
                print('\'\'')
                if fileOutput=='True':
                    log.write('\'\'')
                    log.close()
            if debug=='True':
                if usr=='SOLUCE':
                    print(wd)
            tr=(tr+1)
        print('C\'est bien {}, trouve en {} essais.'.format(usr, tr))
        if fileOutput=='True':
            essais.write('{}:{}'.format(usr,tr))
else:
    while usr!=wd:
        log=open('log.txt', 'w')
        verif=[]
        pos=[]
        usr1=[]
        if fileOutput=='False':
            usr=raw_input('entrer un mot : ')
        if fileOutput=='True' and sync=='True':
            time.sleep(0,5)
            usr=syncfile.readline()
        if usr in liste:
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
            if fileOutput=='True':
                log=open('log.txt', 'w')
                log.write(''.join(verif))
                log.close()
        else:
            print('\'\'')
            if fileOutput=='True':
                log=open('log.txt', 'w')
                log.write('\'\'')
                log.close()
        if debug=='True':
            if usr=='SOLUCE':
                print(wd)
        tr=(tr+1)
print('C\'est bien {}, trouve en {} essais.'.format(usr, tr))
if fileOutput=='True':
    essais.write('{}:{}'.format(usr,tr))
