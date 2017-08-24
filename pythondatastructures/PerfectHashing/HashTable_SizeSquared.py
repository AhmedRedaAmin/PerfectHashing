from .UniversalHashFunction import UniversalHashGenerator
import sys
from .AbstractHashTableImp import AbstractHashTable
import math


class HashTableN2(AbstractHashTable):
    def __init__(self):
        super().__init__()
        self.__errorFlag = 1;

    # Hashes the array of values into the hashArray which is of size^2 of the original
    # Rehashing the original array whenever a collision occurs , No return

    ## @Overriden ##
    def hashify(self, elem):
        self.__elements = elem;
        if math.pow(len(elem) , 2) <= sys.maxsize:
            self.__hashArray = [' '] * int(math.pow(len(elem) , 2));
            self.__hashSeed = UniversalHashGenerator(int(math.pow(len(elem) , 2)), max(elem));
            collision = 1;
            while collision != 0:
                self.__hashArray = [' '] * int(math.pow(len(elem), 2));
                self.__hashSeed.generateHashCode();
                collision = 0;
                for i in range(0, len(elem)):
                    loc = self.__hashSeed.generateHashKey(key=self.__elements[i]);
                    if self.__hashArray[loc] == ' ':
                        self.__hashArray[loc] = self.__elements[i];
                    elif self.__hashArray[loc] == self.__elements[i]:
                        continue
                    else:
                        collision = 1;
                        break;
            self.__errorFlag = 0;
        else:
            self.__errorFlag = 1;
            raise MemoryError('Array Exceeds The Acceptable size on this Machine');

    # looks up a value in the hashArray which was constructed earlier , Aborts if an error
    # occured and the table wasn`t constructed correctly , returns boolean found or not and if found
    # the index of the value

    ## @Overriden ##
    def lookUp(self, key):
        if self.__errorFlag == 0:
            loc = self.__hashSeed.generateHashKey(key);
            if (self.__hashArray[loc] == key):
                output = [True, loc];
                print(output);
                return output;
            else:
                output = [False, 'Not Found'];
                print(output);
                return output;
        else:
            raise AttributeError('The hash Table wasn`t built properly , so you can`t perform lookups');
