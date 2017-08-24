import random



class UniversalHashGenerator:
    __prime = 0;
    __arrSize = 0;
    __randA = 0;
    __randB = 0;
    __keyMax = 0;

    def __init__(self, arrSize, kMax):
        self.__arrSize = arrSize;
        self.__keyMax = kMax;
        self.__prime = self.__genPrimes__(self.__keyMax);

    def generateHashCode(self):
        self.__randA = random.randint(1,self.__prime-1);
        self.__randB = random.randint(0, self.__prime - 1);

    def generateHashKey(self, key: object) -> object:
        hashKey = ((self.__randA*key + self.__randB)% self.__prime)% self.__arrSize;
        return hashKey;

    def __genPrimes__(self, initial):
        """ Generate an infinite sequence of prime numbers.
        """
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        D = {}

        # The running integer that's checked for primeness
        q = int(initial);

        while True:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                #
                if q > self.__keyMax:
                    self.__prime = q;
                    return q;
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next
                # multiples of its witnesses to prepare for larger
                # numbers
                #
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]

            q += 1
