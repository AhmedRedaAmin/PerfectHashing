from PerfectHashing.HashTable_SizeSquared import HashTableN2
from PerfectHashing.HashTable_TwoLevelHashing import HashTableN



# Main function

reader = open("testCases_lab4/keys10000001000000.txt",'r');
Elements = reader.read();
Elements = Elements.split(",");
Elements = [x for x in Elements if x != '']
for i in range (0,len(Elements)):
    Elements[i] = int(Elements[i])
try:
    trial1 = HashTableN();
    trial1.hashify(Elements);
except Exception:
    pass
try:
    trial2 = HashTableN2();
    trial2.hashify(Elements);
except Exception:
    pass
while True:
    method = input('Insert the method you want to use : ');
    if method == '1' :
        key = input('Insert the key you are looking for : ');
        trial1.lookUp(int(key));
    else :
        key = input('Insert the key you are looking for : ');
        try:
            trial2.lookUp(int(key));
        except:
            print ("Size is far too large to handle , please revert to method 1"
                   " for very large dictionaries");
