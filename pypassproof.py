#! python3

# Passwort-Prüfer von Jan Steenken und Jenny Treichel
import re

def passlen(password="", passlen=8):
    """
    Ist das Passwort lang genug?
    @return bool
    """
    return passlen <= len( password ) 

def proofnumbers(password="", numeric = 1 ):
    """
    Überprüfung ob mehr Zahlen 
    im password sind als threshold
    @return bool
    """
    return numeric <= len(re.findall("[0-9]", password))
        

def proofspecial(password = "", threshold=1):
    """
    Überprüfung ob mehr Sonderzeichen 
    im password sind als threshold
    @return bool
    """
    return threshold <= len(re.findall("[_@$!.,-+*~#'\"§$%&ẞ@<>/\\{([])=?;:}]", password))


def prooflower(password = "", threshold=1):
    """
    Überprüfung ob mehr kleinbuchstaben 
    im password sind als threshold
    @return bool
    """
    return threshold <= len(re.findall("[a-z]", password))

def proofupper(password = "", threshold=1):
    """
    Überprüfung ob mehr GROSSBUCHSTABEN 
    im password sind als threshold
    @return bool
    """
    return threshold <= len(re.findall("[A-Z]", password))

def passworteingabe():
    password = input("Dein Passwort: ")

    return  password

def ausgabe(istgut = False):
    if istgut:
        print ("Valid password")
    else:
        print ("Invalid password")

def proofpasswd(password="", passcrit={"Length":8,"Upper":1,"Lower":1,"Numbers":1,"Special":1}):
    """
    Das password wird nach Kriterien in passcrit überprüft.
    @return bool
    """
    istgut = True
    if not passlen(password, passcrit["Length"]):
        istgut = False
    elif not proofnumbers(password, passcrit["Numbers"]):
        istgut = False
    elif not prooflower(password, passcrit["Lower"]):
        istgut =False
    elif not proofupper(password, passcrit["Upper"]):
        istgut=False
    elif not proofspecial(password, passcrit["Special"]):
        istgut=False
    else:
        pass
    return istgut

if __name__ == "__main__":
    password = passworteingabe() # Eingabe des Passworts
    istgut = proofpasswd(password) # Überprüfung des Passworts
    ausgabe(istgut) # Ausgabe