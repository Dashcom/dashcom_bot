# -*- coding: UTF-8 -*-
import time
liste=[]
nope=[]
l12={}
I=[]
open('log2.txt', 'w').write('')
while len(I)!=2:
	I=open('../Création/log.txt','r').readline().replace('\n','').split(', ')
# -*- coding: ASCII -*-
L=I[1]
N=int(I[0])
dico=open('Dico_final.txt', 'r')
dico=(dico.readline()).split()
dico2=dico[:]
for x in range(0, len(dico)):
	if dico[x].startswith(L) and len(dico[x])==N:
		liste.append(dico[x].lower())
a='azertyuiopqsdfghjklmwxcvbn'
for b in range(0,26):
	l12[a[b]]=0
while len(liste)>1:
	sl1={}
	l0=[]
	sl=[]
	S=[]
	a='azertyuiopqsdfghjklmwxcvbn'
	for b in range(0,26):
		sl1[a[b]]=0
	l12p=l12.copy()
	l12=sl1.copy()
	for y in range(0,N):
		sl2=sl1.copy()
		for x in range(0,len(liste)):
			sl2[liste[x][y]]=sl2[liste[x][y]]+1
		sl.append(sl2)
	for x in range(0,len(liste)):
		S.append(0)
		for y in range(0,N):
			S[x]=S[x]+sl[y][liste[x][y]]
	M=0
	for x in range(0,len(liste)):
		if S[x]>S[M]:
			M=x
	open('log2.txt', 'w').write(liste[M])
	# -*- coding: UTF-8 -*-
	R=[]
	while len(R)!=N:
		R=open('../Création/log.txt','r').readline()
	# -*- coding: ASCII -*-
	liste2=[]
	for x in range(0,len(liste)):
		E=0
		for y in range(0,N):
			if liste[x][y]==liste[M][y] and R[y]=='2':
				E=E+1
			if liste[x][y]!=liste[M][y] and R[y]!='2':
				E=E+1
		if E==N:
			liste2.append(liste[x])
	for y in range(0,N):
		if R[y]=='0':
			l0.append(liste[M][y])
		else:
			l12[liste[M][y]]=l12[liste[M][y]]+1
	for b in l12:
		if l12p[b]>l12[b]:
			l12[b]=l12p[b]
	liste3=[]
	for x in range(0,len(liste2)):
		E=0
		for y in range(0,N):
			if (liste2[x][y] in l0) and (liste2[x].count(liste2[x][y])==l12[liste2[x][y]]):
				E=E+1
			if ((liste2[x][y] in l0)==False) and (liste2[x].count(liste2[x][y])>=l12[liste2[x][y]]):
				E=E+1
		if E==N:
			liste3.append(liste2[x])
	liste4=[]
	for x in range(0,len(liste3)):
		E=0
		for b in l12:
			if liste3[x].count(b)>=l12[b]:
				E=E+1
		if E==26:
			liste4.append(liste3[x])
	liste=liste4[:]
open('log2.txt', 'w').write(liste[0])
