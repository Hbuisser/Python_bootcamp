import sys

def ft_progress(lst):
    for i in lst:
        a = i + 1
    barLength = a
    status = ""
    block = int(round(barLength*10))
    text = "\rETA: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), *100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01) 
print()
print(ret)