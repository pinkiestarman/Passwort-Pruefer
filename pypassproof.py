#! python3
import re
import einaus

def passlen(password="", passlen=8):
    """
    Ist das Passwort lang genug?
    @return bool
    """
    return passlen <= len( password ) 

def howmanynumbers(password="", numeric = 1 ):
    """
    Wie viele Zahlen sind im string
    @return int
    """
    return numeric <= len(re.findall("[0-9]", password))
        

def howmanyspecial(password = "", threshold=1):
    """
    Wie viele Sonderzeichen sind im string
    @return int
    """
    return threshold <= len(re.findall("[_@$!]", password))


def howmanylower(password = "", threshold=1):
    """
    Wie viele Sonderzeichen sind im string
    @return int
    """
    return threshold <= len(re.findall("[a-z]", password))


def howmanyupper(password = "", threshold=1):
    """
    Wie viele Sonderzeichen sind im string
    @return int
    """
    return threshold <= len(re.findall("[A-Z]", password))

if __name__ == "__main__":
    istgut = True
    passcrit = einaus.passcriteriain()
    password = einaus.eingabe()
    if not passlen(password, passcrit["Length"]):
        istgut = False
    elif not howmanynumbers(password, passcrit["Numbers"])
