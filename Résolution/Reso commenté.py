liste=[]							#liste des mots possibles
nope=[]								#liste des mots à enlever du dictionnaire
L=input("Premiere lettre : ")
N=input("Nombre de lettres : ")
dico=open('Dico8.txt', 'r')
dico=(dico.readline()).split()
for x in range(0, len(dico)):					#pour chaque mot du dictionnaire
	if dico[x].startswith(L) and len(dico[x])==N:		#si le mot de la liste commence par la bonne lettre et a la bonne longueur
		liste.append(dico[x].lower())			#ajouter le mot à la liste des mots possibles, et en minuscule
while len(liste)>1:						#tant qu'il y a plus d'un mot possible
	sl1={}
	l0=[]
	sl=[]
	S=[]
	a='azertyuiopqsdfghjklmwxcvbn'				#l'ensemble de l'alphabet
	for b in range(0,26):
		sl1[a[b]]=0					#dictionnaire contenant une lettre de l'alphabet par key, toute ayant 0 comme valeur
	l12=sl1.copy()
	for y in range(0,N):					#pour chaque lettre des mots
		sl2=sl1.copy()
		for x in range(0,len(liste)):			#pour chaque mot possible
			sl2[liste[x][y]]=sl2[liste[x][y]]+1	#ajouter 1 à la valeur de la key correspondant à la lettre du mot
		sl.append(sl2)					#ajoute ce dictionnaire à une liste
	for x in range(0,len(liste)):				#pour chaque mot possible
		S.append(0)
		for y in range(0,N):				#pour chaque lettre du mot
			S[x]=S[x]+sl[y][liste[x][y]]		#ajoute à une liste la fréquence de la lettre pour ce mot
	M=0
	for x in range(0,len(liste)):				#pour chaque mot possible
		if S[x]>S[M]:					#si la somme des fréquence du mot est supérieur au précédent record
			M=x					#set un nouveau record
	print(liste[M])						#print le mot magique
	R=input()						#input la réponse de BotBotBotus
	if R=='':						#si la réponse est ''
		nope.append(liste[M])				#set comme mot à enlever du dictionnaire
		del liste[M]					#enleve le mot des mots possibles
	else:							#sinon
		liste2=[]
		for x in range(0,len(liste)):					#pour chaque mot possible
			E=0							#compteur de lettres convenables
			for y in range(0,N):					#pour chaque lettre du mot
				if liste[x][y]==liste[M][y] and R[y]=='2':	#si lettre du mot = lettre du mot magique et que le bot a répondu 2
					E=E+1					#ajoute 1 au compteur
				if liste[x][y]!=liste[M][y] and R[y]!='2':	#si lettre du mot != lettre du mot magique et que le bot a répondu 0/1
					E=E+1					#ajoute 1 au compteur
			if E==N:						#si le compteur est au max
				liste2.append(liste[x])				#set le mot comme possible
		for y in range(0,N):						#pour chaque lettre des mots
			if R[y]=='0':						#si le bot a répondu 0
				l0.append(liste[M][y])				#mettre la lettre dans la liste des 0
			else:							#sinon
				l12[liste[M][y]]=l12[liste[M][y]]+1		#ajouter 1 à la valeur de key correspondant à la lettre du mot magique
		liste3=[]
		for x in range(0,len(liste2)):					#pour chaque mot possible
			E=0							#compteur de lettres convenables
			for y in range(0,N):					#pour chaque lettre du mot
				if (liste2[x][y] in l0) and (liste2[x].count(liste2[x][y])==l12[liste2[x][y]]):		#si la lettre est dans la liste des 0 et qu'elle est autant présente dans le mot que dans le mot magique
					E=E+1										#ajoute 1 au compteur
				if ((liste2[x][y] in l0)==False) and (liste2[x].count(liste2[x][y])>=l12[liste2[x][y]]):#si la lettre n'est pas dans la liste des 0 et qu'elle est au moins autant présente dans le mot que dans le mot magique
					E=E+1										#ajoute 1 au compteur
			if E==N:											#si le compteur est au max
				liste3.append(liste2[x])								#set le mot comme possible
		liste=liste3[:]
print(liste[0])							#output le mot magique dans le cas où la réponse suffit à avoir le mot à coup sûr
print(nope)							#output la liste des mots à enlever du dictionnaire
