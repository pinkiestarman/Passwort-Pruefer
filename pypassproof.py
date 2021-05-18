#! python3

def passlen(minlen = 8, password=""):
    """
    Ist das Passwort lang genug?
    @return bool
    """
    return password.length >= minlen

def howmanynumbers(password=""):
    """
    Wie viele Zahlen sind im string
    @return int
    """
    r = 0
    for c in password:
        r += c.isdecimal()
    return r

def howmanyspecial(string = ""):
    """
    Wie viele Sonderzeichen sind im string
    @return int
    """
    r = 0
    for c in string:
        r += c.isalnum()
    return r - string.length

def readcfg(file = "passwdparams.txt"):
    f = open(file)
    paramlist = f.read().splitlines()
    print(paramlist)

def hallo():