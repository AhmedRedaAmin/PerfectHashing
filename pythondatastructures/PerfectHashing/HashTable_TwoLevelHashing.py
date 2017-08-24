from gi.overrides import override
from .AbstractHashTableImp import AbstractHashTable
from .UniversalHashFunction import UniversalHashGenerator
from .HashTable_SizeSquared import HashTableN2

class HashTableN(AbstractHashTable):
    def __init__(self):
        super().__init__()

    # Hashes the array of values into the hashArray which is of same size as the original
    # Uses two level hashing for collision resolution , No return

    ## @Overriden ##
    def hashify(self, elem):
        self.__elements = elem;
        self.__hashArray = [[] for i in range(len(elem))];
        self.__hashSeed = UniversalHashGenerator(len(elem),kMax=max(elem));
        self.__hashSeed.generateHashCode();
        for i in range (0,len(elem)) :
            loc = self.__hashSeed.generateHashKey(elem[i]);
            if len(self.__hashArray[loc]) != 0 :
                self.__hashArray[loc].append(elem[i]);
            else :
                self.__hashArray[loc].append(elem[i]);
        for i in range(0,len(elem)):
            if len(self.__hashArray[i]) != 1 and len(self.__hashArray[i]) != 0:
                levelTwo = HashTableN2();
                levelTwo.hashify(self.__hashArray[i])
                self.__hashArray[i] = levelTwo;
        self.__errorFlag = 0;


    # looks up a value in the hashArray which was constructed earlier , Aborts if an error
    # occured and the table wasn`t constructed correctly , returns boolean found or not and if found
    # the index of the value

    ## @Overriden ##
    def lookUp(self, key):
        if self.__errorFlag == 0:
            loc = self.__hashSeed.generateHashKey(key)
            if isinstance(self.__hashArray[loc],list) and len(self.__hashArray[loc]) == 1:
                if self.__hashArray[loc][0] == key :
                    output = [True,loc] ;
                    print(output);
                    return output;
                else:
                    output = [False,'Not Found']
                    print(output);
                    return output;
            elif isinstance(self.__hashArray[loc],list) and len(self.__hashArray[loc]) == 0:
                output = [False, 'Not Found']
                print(output);
                return output;
            else:
                if self.__hashArray[loc].lookUp(key)[0]:
                    output = [True, loc];
                    print(output);
                    return output;
                else:
                    output = [False,'Not Found'];
                    return output;
        else:
            raise AttributeError('The hash Table wasn`t built properly , so you can`t perform lookups');