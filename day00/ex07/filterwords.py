import sys

def filter(str, integer):
    i = int(integer)
    list = str.split()
    list2 = []
    for word in list:
        if len(word) > i:
            list2.append(word)
    print(list2)

filter(sys.argv[1], sys.argv[2])