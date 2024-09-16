import tkinter as tk
from tkinter import PhotoImage
import winsound
import threading
import random


ekirjasto = {
    "eX":1720,
    "eY":random.randint(300,500),
    "eScore":0
}

kkirjasto = {
    "kX":0,
    "kY":random.randint(300,500),
    "kScore":0
}

def lisaaEleima():
    ekirjasto["eY"]=random.randint(300,500)
    eleima.place(x=ekirjasto["eX"], y=ekirjasto["eY"])

def kheitto():
    tomaattix=kkirjasto["kX"]
    tomaattiy=kkirjasto["kY"]
    tomaattileimaK = tk.Label(root, image=tomaatti)
    
    splatleima.place_forget()
    def ktomaatti():
        nonlocal tomaattix, tomaattiy
        if tomaattix < 800:
            tomaattix += 10
            tomaattileimaK.place(x=tomaattix, y=tomaattiy)
            root.after(10,ktomaatti)
        else:
            tomaattileimaK.place_forget()
            lantti = random.randint(1,3)
            
            if lantti > 1:

                print("Wow Kernesti osu!")
                splatleima.place(x=tomaattix, y=tomaattiy)
                winsound.Beep(1177,300)
                kkirjasto["kScore"] += 1
                paivitapisteet()
            else:
                print("Yikes Kernesti ei osunu!")   
                winsound.Beep(300,300)
    def kVoittoheitto():
        nonlocal tomaattix, tomaattiy
        if tomaattix < 1720:
            tomaattix += 10
            tomaattileimaK.place(x=tomaattix, y=tomaattiy)
            root.after(10,kVoittoheitto)
        else:
            tomaattileimaK.place_forget()
            lantti = random.randint(1,3)
            
            if lantti > 1:

                print("Wow Kernesti osu Ernestiin ja voitti!")
                splatleima.place(x=tomaattix, y=tomaattiy)
                voittoK()
                winsound.Beep(1377,300)

            else:
                print("Yikes Kernesti ei osunu!")   
                winsound.Beep(300,300)

    def tarkistus():
        if kkirjasto["kScore"] - ekirjasto["eScore"] <= 1:                   
            ktomaatti()
        else:
            print("voittoa saa yrittää")
            kVoittoheitto()
    tarkistus()            

def eheitto():
    tomaattix=ekirjasto["eX"]
    tomaattiy=ekirjasto["eY"]
    tomaattileimaE = tk.Label(root, image=tomaatti)

    splatleima.place_forget()
    def etomaatti():
        nonlocal tomaattix, tomaattiy
        if tomaattix > 800:
            tomaattix -= 10
            tomaattileimaE.place(x=tomaattix, y=tomaattiy)
            root.after(10,etomaatti)
        else:
            tomaattileimaE.place_forget()
            lantti = random.randint(1,3)
            
            if lantti > 1:

                print("Wow Ernesti osu!")
                splatleima.place(x=tomaattix, y=tomaattiy)
                winsound.Beep(1177,300)
                ekirjasto["eScore"] += 1
                paivitapisteet()
            else:
                print("Yikes Ernesti ei osunu!")   
                winsound.Beep(300,300)

    def eVoittoheitto():
        nonlocal tomaattix, tomaattiy
        if tomaattix > 0:
            tomaattix -= 10
            tomaattileimaE.place(x=tomaattix, y=tomaattiy)
            root.after(10,eVoittoheitto)
        else:
            tomaattileimaE.place_forget()
            lantti = random.randint(1,3)
            
            if lantti > 1:

                print("Wow Ernesti osu Kernestiin ja voitti!")
                splatleima.place(x=tomaattix, y=tomaattiy)
                voittoE()
                winsound.Beep(1377,300)

            else:
                print("Yikes Ernesti ei osunu!")   
                winsound.Beep(300,300)

    def tarkistus():
        if ekirjasto["eScore"] - kkirjasto["kScore"] <= 1:                   
            etomaatti()
        else:
            print("voittoa saa yrittää")
            eVoittoheitto()
    tarkistus()                

def saikeKHeitto():
    kahvaHeittoK=threading.Thread(target=kheitto)
    kahvaHeittoK.start()

def saikeEHeitto():
    kahvaHeittoE=threading.Thread(target=eheitto)
    kahvaHeittoE.start()

def paivitapisteet():
    markkeriPisteet.config(text=f'PISTEET Kernesti:{kkirjasto["kScore"]} ja Ernesti:{ekirjasto["eScore"]}') 
def reset():
    ekirjasto["eScore"] = 0
    kkirjasto["kScore"] = 0
    markkeriPisteet.config(text=f'PISTEET Kernesti:{kkirjasto["kScore"]} ja Ernesti:{ekirjasto["eScore"]}')
    splatleima.place_forget() 
def voittoK():
    markkeriPisteet.config(text='Kernesti VOITTI!!!')  
def voittoE():
    markkeriPisteet.config(text='Ernesti VOITTI!!!')              

root=tk.Tk()
root.title("Tomaattikisa")
root.geometry("1920x1200")

tomaatti = PhotoImage(file="images/tomaatti.png")
kernesti = PhotoImage(file="images/kerne.png")
ernesti = PhotoImage(file="images/erne.png")
splat = PhotoImage(file="images/splat.png")
maalitaulu = PhotoImage(file="images/maalitaulu.png")


maalileima = tk.Label(root ,image=maalitaulu)
eleima = tk.Label(root ,image=ernesti)
kleima = tk.Label(root, image=kernesti)
splatleima = tk.Label(root, image=splat)


maalileima.place(x=700, y=300)
kleima.place(x=kkirjasto["kX"],y=kkirjasto["kY"] )

enappi = tk.Button(root, text="Herärä Ernesti", command=lisaaEleima)
enappi.place(x=100, y=0)

kHeittoNappi = tk.Button(root, text="Kernesti heittää tomaatin", command=saikeKHeitto)
kHeittoNappi.place(x=200, y=0)

eHeittoNappi = tk.Button(root, text="Ernesti heittää tomaatin", command=saikeEHeitto)
eHeittoNappi.place(x=350, y=0)

markkeriPisteet = tk.Label(root, text=f'PISTEET Kernesti:{kkirjasto["kScore"]} ja Ernesti:{ekirjasto["eScore"]}', bg="light grey")
markkeriPisteet.place(x=875,y=250)

resetnappi = tk.Button(root, text = "Nollaa pisteet", command=reset)
resetnappi.place(x=915, y=275)



root.mainloop()