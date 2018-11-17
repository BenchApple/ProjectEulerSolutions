#Benjamin Chappell

from itertools import permutations

def main():
	limit, counter = 1000000

    primes = [] #index 0 is equal to 2 in the real world, make sure to account for that transition.
    
    for i in range(0, limit - 2):
		primes[i] = True
	
	primes = seive(primes, limit)

    toPermute = []
	for i in primes:
        toPermute = list(str(i))
        isCircular = True

        for i in permutations(toPermute):
            if not search(primes, int("".join(i)):
                isCircular = False
                break
        
        if isCircular:
        counter += 1

	
def seive(a, n): #Implementation of the Seive of Eratosthenes
	for i in range(2, n ** (1/2)):
		if a[i]:
			for j in range(i ** 2, n):
				a[j] = False
	
	toReturn = []
	
	for i in range(0, len(primes)):
		if a[i]:
			toReturn.append(i)

    return toReturn
	
def search(a, n): #Implementation of Binary search, shell method for easy calls
	search(a, n, 0, len(a) - 1)
	
	
def search(a, n, start, end): #Underlying method for search.
	if (start > end):
		return False
	else:
		m = a[(start + end) / 2]
		
		if m = n:
			return True
		elif m > n:
            return search(a, n, m+1, end)
        elif m < n:
            return search(a, n, start, m-1)
	
	
if __name__ == "__main__":
	main()
