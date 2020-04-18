import sys

MORSE = { 'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-', ' ':'/'}

liste = []
for i in sys.argv[1:]:
    liste += i.split()
i = 0
for word in liste:
    for letter in word:
        if letter.isalnum() is False:
            print("ERROR")
            i = 1
            break
if i == 0:      
    for word in liste:
        for letter in word:
            print(MORSE[letter.upper()], end=' ')

# lst=[x.upper() for x in sys.argv[1:]]
# if any([not (i.isalnum() or ' ' in i) for i in lst]):
#     print("ERROR")
# else:
#     new_str = ' '.join(lst)
#     print(' '.join([MORSE_CODE_DICT[letter] for letter in new_str]))











# list = []
# i = 0
# for x in sys.argv[1:]:
#     list += x.split()
# for word in list:
#     if word.isalnum() is False:
#         print("ERROR")
#         i = 1
# if i == 0:
#     for word in list:
#         for letter in word:
#             print(MORSE[letter], end=' ')
