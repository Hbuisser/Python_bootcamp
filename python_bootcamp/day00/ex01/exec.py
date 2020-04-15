import sys

def reverseAlpha(str):
    return str[::-1].swapcase()

i = len(sys.argv) - 1

while i > 1:
    print(reverseAlpha(sys.argv[i]), end=' ')
    i -= 1

print(reverseAlpha(sys.argv[i]))