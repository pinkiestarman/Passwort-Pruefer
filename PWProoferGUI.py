#! python3
import tkinter as tk
from tkinter import ttk 
import pypassproof



outstring = ""

window = tk.Tk(screenName="Passwort-Pruefer")
window.title("Passwort-Pruefer")
window.geometry( '800x600+50+50' )

notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)

# create frames
Testen = ttk.Frame(notebook, width=780, height=580)
Einstell = ttk.Frame(notebook, width=780, height=580)

# Testen
password = tk.StringVar()
testLabel = ttk.Label(Testen,text="Bitte Passwort eingeben:").pack()
testEntry = ttk.Entry(master=Testen,width=300).pack()

def testen():

    
    if int(passwordlen.get()) < pypassproof.passlen(password):
        outstring += password.get() + " ist nicht lang genug!"
    else:
        pass
    if int(passwordlower.get()) < pypassproof.howmanylower(password):
        outstring += password.get() + " hat zu wenige kleinbuchstaben."
    else:
        pass
    
testButton = ttk.Button(master=Testen,text="Test!",command=testen).pack()
outLabel = ttk.Label(master=Testen,text=outstring).pack()

# Einstellungen
lenLabel = ttk.Label(Einstell,text="Länge des Passworts:")
passwordlen = tk.StringVar(value=8)
#lenSlider = ttk.Scale(Einstell,from_=5,to=50).pack()
lenBox = ttk.Spinbox(Einstell,from_=5,to=50,textvariable=passwordlen,wrap=False)
lenLabel.pack()
lenBox.pack()

numLabel = ttk.Label(Einstell,text="Zahlen:")
passwordnum = tk.StringVar(value=1)
#numSlider = ttk.Scale(Einstell,from_=5,to=50).pack()
numBox = ttk.Spinbox(Einstell,from_=0,to=10,textvariable=passwordnum,wrap=False)
numLabel.pack()
numBox.pack()

lowerLabel = ttk.Label(Einstell,text="kleinbuchstaben:")
passwordlower = tk.StringVar(value=1)
#lowerSlider = ttk.Scale(Einstell,from_=5,to=50).pack()
lowerBox = ttk.Spinbox(Einstell,from_=0,to=10,textvariable=passwordlower,wrap=False)
lowerLabel.pack()
lowerBox.pack()

upperLabel = ttk.Label(Einstell,text="GROSSBUCHSTABEN:")
passwordupper = tk.StringVar(value=1)
#upperSlider = ttk.Scale(Einstell,from_=5,to=50).pack()
upperBox = ttk.Spinbox(Einstell,from_=0,to=10,textvariable=passwordupper,wrap=False)
upperLabel.pack()
upperBox.pack()

specialLabel = ttk.Label(Einstell,text="Sonderzeichen:")
passwordspecial = tk.StringVar(value=1)
#specialSlider = ttk.Scale(Einstell,from_=5,to=50).pack()
specialBox = ttk.Spinbox(Einstell,from_=0,to=10,textvariable=passwordspecial,wrap=False)
specialLabel.pack()
specialBox.pack()


Einstell.pack(fill='both', expand=True)
Testen.pack(fill='both', expand=True)

#fill frames



# add frames to notebook

notebook.add(Testen, text='Testen')
notebook.add(Einstell, text='Einstellungen')


window.mainloop()

    