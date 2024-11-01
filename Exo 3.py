def somme(l):
	
	if l == []:
		return 0

	s = 0

	for ele in l:
		s += ele
		
	return s


def ranger(l, p):

	if p < 0 or l == []:
		print("Erreur, capacité insuffisante")
		return

	boite = [[]] * len(l)

	print(boite)

	for ele in l:
		for i in range(len(boite)):
			
			if somme(boite[i]) + ele <= p:
				boite[i].append(ele)
				break

	return boite


print(ranger([3, 6, 6, 8, 6, 3, 10, 9, 10, 8], 20))
		
