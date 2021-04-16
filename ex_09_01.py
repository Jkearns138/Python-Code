Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fname = input ('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open (fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])

print(di)

largest = -1
theword= None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k

Print(theword, largest)
