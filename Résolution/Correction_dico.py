aj=input("Ajout : ")
re=input("Retrait : ")
dico=open('Dico_final.txt', 'r')
dico=(dico.readline()).split()
dico2=dico[:]
for x in range(0, len(dico)):
	for y in range(0,len(re)):
		if dico[x]==re[y]:
			dico2.remove(dico[x])
for z in range(0, len(aj)):
	dico2.append(aj[z])
dico2.sort()
dico3=open("Dico_final.txt",'w')
dico3.write(" ".join(dico2))
