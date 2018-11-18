#Benjamin Chappell

from itertools import permutations

def main():
	limit = 100
	counter = 0
	
	testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	print binarySearch(testList, 109)

	primes = findPrimes(limit)

	toPermute = []
	#print primes
	for i in primes:
		isCircular = True

		print set(permutations(str(i)))

		for j in set(permutations(str(i))):
			#print j
			if not binarySearch(primes, int("".join(j))):
				#print binarySearch(primes, int("".join(j)))
				isCircular = False
				break

		#print ""

		if isCircular == True:
			counter += 1
	
	print counter

	
def findPrimes(n): #Returns a list of primes below n
	sieve = [True] * n

	for i in range(3, int(n**0.5) + 1, 2):
		if sieve[i]:
			sieve[i*i :: 2*i] = [False]*((n-i*i-1)/(2*i)+1)

	return [2] + [i for i in range(3, n, 2) if sieve[i]]
	
def binarySearch(a, n): #Implementation of Binary search, shell method for easy calls
	#print (len(a))
	search(a, n, 0, len(a) - 1)
	
	
def search(a, n, start, end): #Underlying method for search.
	if start >= end:
		return False
	else:
		m = int((start + end) / 2)

		if a[m] == n:
			return True
		elif a[m] > n:
			result = search(a, n, start, m-1)
			return result
		elif a[m] < n:
			result = search(a, n, m+1, end)
			return result
	
	
if __name__ == "__main__":
	main()
