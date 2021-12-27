def napa(N):
    rishoni = [True for i in range(0, N)]
    rishoni[0] = False
    # make rishoni to be an array of True values for prime numbers
    rishoni = getOutNonePrimes(2, N, rishoni)

    return [i for i in range(0, len(rishoni)) if rishoni[i]]


#  method to became false to none prime numbers 
def getOutNonePrimes(i, N, rishoni):
    if i == N:
        return rishoni
    if rishoni[i]:
        rishoni = step2(i, N, i * 2, rishoni)
    return getOutNonePrimes(i + 1, N, rishoni)


# method to became False to evry multiply number
def step2(i, N, mlt, rishoni):
    if mlt == N or mlt > N:
        return rishoni
    rishoni[mlt] = False
    return step2(i, N, mlt + i, rishoni)


# version 1 : none generator
def primefactors(N):
    if isinstance(N, int):
        return [i for i in range(1, len(napa(N))) if N % i == 0 and i in napa(N)]
    else:
        print("ERROR,nust be an integer ")
        return


# version 2: generator

def primefactorsGen(N):
    if isinstance(N, int):
        return list(i for i in range(1, len(napa(N))) if N % i == 0 and i in napa(N))
    else:
        print("ERROR,nust be an integer ")
        return


# version 3: generator yield

def primefactorsGenYield(N):
    if isinstance(N, int):
        for i in range(1, N):
            if N % i == 0 and i in napa(N):
                yield i
    else:
        print("ERROR,nust be an integer ")
        return


def main():
    N = eval(input("enter an integer number:\n"))
    print("the primes' divs of  this number none generator:", primefactors(N))
    print("the primes' divs of  this number  generator:", primefactorsGen(N))
    print("the primes' divs of  this number  yield generator:", list(primefactorsGenYield(N)))


main()
