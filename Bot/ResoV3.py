#NE PAS UTILISER : TROP EFFICACE
import time
from tweepy import OAuthHandler
import tweepy
consumer_key='xxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxx'
access_token='xxxxxxxxx-xxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxx'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
liste=[]
nope=[]
l12={}
I=[]
L=input("Premiere lettre : ")
N=int(input("Nombre de lettres : "))
# -*- coding: UTF-8 -*-
dico=open('../Résolution/Dico_final.txt', 'r')
# -*- coding: ASCII -*-
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
	print(liste[M])
	api.update_status(status='@BotBotBotus '+liste[M])
	P=liste[M]
	time.sleep(2)
	R=[]
	while len(R)<N:
		R=open('log.txt','r').readline()
	print(R)
	open('log.txt','w').write('')
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
if liste[0]!=P:
	print(liste[0])
	api.update_status(status='@BotBotBotus '+liste[0])
