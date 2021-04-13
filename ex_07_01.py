Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fh = open('mbox-short.txt')

for lx in fh:
    ly=lx.rstrip()
    print (ly.upper())
