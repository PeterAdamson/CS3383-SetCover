#!/usr/bin/python
import random
import copy

def chang(X,C,currMin,totMin):
	if not X:
		return min(currMin, totMin)
	if currMin >= totMin:
		return totMin
	if not C:
		return totMin

	T = random.choice(C)

	C1 = copy.copy(C)

	C1.remove(T)

	X1 = copy.copy(X)

	for elementX in X:
		for elementT in T:
			if elementT == elementX:
				X1.remove(elementX)

	totMin = chang(X1,C1,currMin + 1, totMin)
	totMin = chang(X,C1,currMin,totMin)
	return totMin

X = [1,2,3,4,5,6,7,8]
C = [[1,4,5,8],[2,7,8],[3,5,6],[1,4,7]]
print chang(X,C,0,len(C))
