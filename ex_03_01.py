Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sh = input ("Enter Hours: ")
sr = input ("Enter Rate: ")
fh = float (sh)
fr = float(sr)
#print(fh,fr)
if fh > 40 :
    #print("Overtime")
    reg = fr* fh
    otp = (fh - 40.0)*(fr *0.5)
    #print(reg,otp)
    xp = reg + otp
else:
    #print("Regular")
    xp = fh *fr
print("Pay:", xp)
