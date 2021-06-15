def eingabe():
    password = input("Dein Passwort: ")

    return  password

def ausgabe(istgut = False):
    if istgut:
        print ("Valid password")
    else:
        print ("Invalid password")

def passcriteriain():
    passcriteria = {"Length":8,"Upper":1,"Lower":1,"Numbers":1,"Special":1}
    return passcriteria