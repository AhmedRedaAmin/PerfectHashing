# Abstract HashTable implementation

class AbstractHashTable:
    __elements = [];
    __hashArray = [];
    __errorFlag = 1;
    __hashSeed = None;
    # Hashes the array of values into the hashArray which is of same size as the original
    # Rehashing the original array whenever a collision occurs , No return
    def hashify(self,elem):
       return None;

    # looks up a value in the hashArray which was constructed earlier , Aborts if an error
    # occured and the table wasn`t constructed correctly , returns boolean found or not and if found
    # the index of the value
    def lookUp(self,key):
       return None;
