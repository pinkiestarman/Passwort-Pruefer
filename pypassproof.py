#! python3
import re

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
    return len(re.findall("[0-9]", password))
        

def howmanyspecial(password = ""):
    """
    Wie viele Sonderzeichen sind im string
    @return int
    """
    return len(re.findall("[_@$!]", password))


def howmanylower(password = ""):
    """
    Wie viele Sonderzeichen sind im string
    @return int
    """
    return len(re.findall("[a-z]", password))


def howmanyupper(password = ""):
    """
    Wie viele Sonderzeichen sind im string
    @return int
    """
    return len(re.findall("[A-Z]", password))
