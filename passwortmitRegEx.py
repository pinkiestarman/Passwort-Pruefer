#ich probiere mal meinen Mist :D

import re #re für Regular Expressions

password = input("Dein Passwort: ")
if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print ("Valid password") #ausgabe wenn alles ok
else:
    print ("Password not valid") #ausgabe wenn nicht ok