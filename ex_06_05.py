Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str = 'X-DSPAM-Confidence: 0.8475'

ipos =str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
value = float(piece)
print(value)
