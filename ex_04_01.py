Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def computepay(hours, rate) :
    #print('In computepay', hours, rate)
    if fh > 40 :
        reg = rate* hours
        otp = (hours - 40.0)*(rate *0.5)
        pay = reg + otp
    else:
        pay = hours *rate
        #print("Returing", pay)
        return pay

sh = input ("Enter Hours: ")
sr = input ("Enter Rate: ")
fh = float (sh)
fr = float(sr)
#print(fh,fr)
cumputepay(fh, fr)

print("Pay:", xp)
