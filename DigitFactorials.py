## Benjamin Chappell ##

def main():
    factorials = [1]

    for i in range(1,10):
        factorials.append(factorials[i - 1] * i)

    print (factorials)

if __name__ == "__main__":
    main()