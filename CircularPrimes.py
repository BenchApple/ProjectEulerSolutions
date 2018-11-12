#Benjamin Chappell

def main():
	limit = 1000000
	
	primes = [] #index 0 is equal to 2 in the real world, make sure to account for that transition.
	for i in range(0, limit - 2):
		primes[i] = True
	
	primes = seive(primes, limit)
	
def seive(a, l):
	for i in range(2, l ** (1/2)):
		
	
if __name__ == "__main__":
	main()
