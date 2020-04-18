import sys

def filter(string, integer):
    size = len(sys.argv)
    if size == 3:
        if integer.isdigit() is True and string.isdigit() is False:
            i = int(integer)
            list = string.split()
            list2 = []
            for word in list:
                word = word.replace(",", "")
                if len(word) > i:
                    list2.append(word)
            print(list2)
        else:
            print("ERROR")
    else:
        print("ERROR")
    

filter(sys.argv[1], sys.argv[2])