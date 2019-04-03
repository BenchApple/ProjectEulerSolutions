## Benjamin Chappell

def main():
    s = 1

    for j in range(10, 100):
        for i in range(10, j):
            digitArray = []

            chari = str(i)
            charj = str(j)

            digitArray.append(float(chari[0]))
            digitArray.append(float(chari[1]))
            digitArray.append(float(charj[0]))
            digitArray.append(float(charj[1]))

            if (digitArray[0] == digitArray[3]) ^ (digitArray[1] == digitArray[2]) and (digitArray[1] != 0 and digitArray[3] != 0):
                if ((digitArray[0] / digitArray[3]) == float(i) / float(j)) or ((digitArray[1] / digitArray[2]) == float(i) / float(j)):
                    #print (str(i) + " " + str(j))
                    s *= (float(i) / float(j))
                    print (s)



if __name__ == "__main__":
    main()