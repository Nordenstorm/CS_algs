#Olof Nordenstorm, Find best prize with hashing

def optimize_price(v):
	"""Code is made to find optimal prize for a certain length of fabric"""
	# The code take in a input of prize on garment in diffrent length. The index indicate the length of the garment
	# The output is the optimal prize
	# It first bug checks
	# Then it starts the recussion algortim
	# The total time is T(n^2). Since Recussion will run T(n) and alternativ will run T(m). 
	# m is a function of the amount of times the code has been run. It will start at one and inceres with one for everytime it is run.
	# Therefore we will get a sum of 1 to n. This can simply to (n^2+n)/2=>>O(n^2)

	for i in range(0,len(v)):# Test if list is only int

		if type(v[i])!=int:

			print("Invalid input")

			return None

	p,lista=recussion(v)

	result=max(p)

	return result , lista


def recussion(h,p=[0],k=0):
	"""Recussion is applied to use the old result to find the new values"""
	# Time complexity of T(n)
	# It runs the alternativ code where we find what could be added as a list
	# It takes the biggest of those elements and append it to p
	# It return the list p. Recussuin size is T(n) and O(n) where n is len(h)

	Lista=[]

	if len(p)<len(h):

		v, l =alternativ(h,p) # Find the possiblites 


		p.append(max(v))

		recussion(h,p,k=3) 

		Lista.append(p[l])

	return p, Lista


def alternativ(h,p):
	""" Create a vector of all alternativ in whitch we can choice p and h """
	# It create all possbile alternatives of h and p. 
	# After having added all the possbile combinations it returns a vector v
	# It has time complexity O(m) where m=len(p)

	v=[]

	m=len(p)

	l=0

	for i in range (1,m+1):

		v.append(h[i]+p[m-i])

		l=m-i

	return v , l


def healthy():
	"""Test if the function is broken or not with known cases"""
	#Runs a series of command to test some cases where the answer is known
	#Also try some incorrect statement.

	h=[0,2,5,6,9]

	p,lista=optimize_price(h)
	print(p)
	print(lista)



if __name__ == "__main__":
	
   healthy()




