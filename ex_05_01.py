Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval =float(sval)
    except:
        print('Invalid input')
        continue    
    #print (fval)
    num =nam + 1
    tot = tot + fval

#print('ALL DONE')
print(tot,num,tot/num)
