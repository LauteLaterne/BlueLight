#Übung: TKinter - Übungsaufgabe Fenster Tkinter - einfacher Taschenrechner

from tkinter import  *

class BetterButton(Button):
    
    def addition(self):
        ergebnis.delete(0, 'end')
        zahl1 = int(eingabe1.get())
        zahl2 = int(eingabe2.get())
        addiert = zahl1 + zahl2
        print("\n", "Ergebnis Addition: ", addiert)
        text = Text(height = 2, width = 40)
        #text.tag_configure('format', font= ('Verdana', 12, 'bold'))
        #text.insert(END, addiert, 'format')
        #text.pack()
        ausgabe = str(zahl1) + " + " + str(zahl2) + " = " + str(addiert)
        #ergebnis.insert(END, zahl1+zahl2)
        ergebnis.insert(END, ausgabe)
        eingabe1.delete(0, 'end')
        eingabe2.delete(0, 'end')
                    
fenster = Tk()
fenster.title("RECHNER")
fenster.geometry("240x180")

rahmen = Frame(fenster, relief="ridge", borderwidth = 2)
rahmen.pack(fill="both", expand = 1)

label = Label(rahmen, text="Gebe zwei Zahlen ein")
label.pack(side = "top")
eingabe1 = Entry(rahmen, bd=1, width = 15)
eingabe1.pack()
eingabe2 = Entry(rahmen, bd=1, width = 15)
eingabe2.pack()

plusknopf = BetterButton(rahmen, text="Zahlen addieren")
plusknopf["command"] = plusknopf.addition
plusknopf.pack(side = "top")

label = Label(rahmen, text="Ergebnis")
label.pack(side = "top")
ergebnis= Entry(rahmen, bd=1, width = 15)
ergebnis.pack()

exitknopf = Button(rahmen, text = "SCHLIESSEN", command=fenster.destroy)
exitknopf.pack(side = "bottom")

fenster.mainloop()





