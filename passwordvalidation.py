#ich probiere mal meinen Mist :D

import re #re für Regular Expressions

password = input("Ihr Passwort: ") #eingabefeld
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        print("Das Passwort muss mindestens 8 Zeichen lang sein")
        break
    elif not re.search("[a-z]", password):
        flag = -1
        print("Das Passwort muss Kleinbuchstaben haben")
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        print("Das Passwort muss Großbuchstaben haben")
        break
    elif not re.search("[0-9]", password):
        flag = -1
        print("Das Passwort muss mindetsens eine Zahl enthalten")
        break
    elif not re.search("[_@$!]", password):
        flag = -1
        print("Das Passwort muss mindestens ein Sonderzeichen enthalten")
        break
    elif re.search("\s", password):
        flag = -1
        print("Das Passwort darf kein Leerzeichen enthalten")
        break
    else:
        flag = 0
        print("Valid Password")
        break
  
if flag ==-1:
    print("Not a Valid Password")