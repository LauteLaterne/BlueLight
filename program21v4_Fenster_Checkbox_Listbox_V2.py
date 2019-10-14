#Übung: TKinter - mehrere Elemente in einem Fenster anzeigen

from tkinter import  *

class BetterButton(Button):

    def __init__(self):
        self.__auswahl = auswahlliste2.curselection()    

    def aktion1(self):
        print("\n", "VERDAMMT! Du hast den Button gedrückt!")
        text1 = Text(height = 4, width = 40)
        text1.tag_configure('format', font= ('Verdana', 15, 'bold'))
        text1.insert(END, "VERDAMMT!   Du hast den Kopf gedrückt!!!", 'format')
        text1.pack()
    def aktion2(self):
        print("\n", "Dein eingebener BULLSHIT: ", eingabe.get())
        text2 = Text(height = 2, width = 40)
        text2.tag_configure('format', font= ('Verdana', 12, 'bold'))
        text2.insert(END, eingabe.get(), 'format')
        text2.pack()
        eingabe.delete(0, 'end')

    def aktion3(self):
        print("\n", "Wert der Checkbox: ", haken.get())
        text3 = Text(height = 2, width = 40)
        text3.tag_configure('format', font= ('Verdana', 12, 'bold'))
        text3.insert(END, haken.get(), 'format')
        text3.pack()
        
    def aktion4(self):
        print("\n", "Einträge in der Listbox: ", auswahlliste2.size())
        print("\n", "Auswahl der Listbox: ", auswahlliste2.curselection())
        text4 = Text(height = 2, width = 40)
        text4.tag_configure('format', font= ('Verdana', 10, 'bold'))
        text4.insert(END, auswahlliste2.size(), 'format')
        text4.insert(END, "\n", 'format')
        text4.insert(END, auswahlliste2.curselection(), 'format')
        text4.pack()

    def getAuswahl():
        return auswahl

                     
fenster = Tk()
fenster.title("BUSINESS BULLSHIT GENERATOR")
fenster.geometry("320x640")

rahmen = Frame(fenster, relief="ridge", borderwidth = 2)
rahmen.pack(fill="both", expand = 1)

label = Label(rahmen, text="Gebe Dein BULLSHIT ein")
label.pack(side = "top")
eingabe = Entry(rahmen, bd=1, width = 30)
eingabe.pack()

haken = IntVar()
prüfknopf = Checkbutton(rahmen, text = "Setze ein Häkchen!", variable = haken)
prüfknopf.pack()

knopf1 = Button(rahmen, text = "SCHLIESSEN", command=fenster.destroy)
knopf1.pack(side = "bottom")

knopf2 = BetterButton(rahmen, text="NICHT drücken!")
knopf2["command"] = knopf2.aktion1
knopf2.pack(side = "bottom")

knopf3 = BetterButton(rahmen, text="Dein BULLSHIT bestätigen")
knopf3["command"] = knopf3.aktion2
knopf3.pack(side = "bottom")

knopf4 = BetterButton(rahmen, text="Check die Checkbox")
knopf4["command"] = knopf4.aktion3
knopf4.pack(side = "bottom")

knopf5 = BetterButton(rahmen, text="Ergebnis Auswahlliste")
knopf5["command"] = knopf5.aktion4
knopf5.pack(side = "bottom")

auswahlliste2 = Listbox(rahmen, selectmode = MULTIPLE, fg = "blue", highlightcolor = "cyan", selectbackground = "blue")
auswahlliste2.insert(END, "Wähle Dein BULLSHIT aus")
for eintrag in ["nnöh!", "so!", "wie auch immer", "ja!", "am Ende des Tages"]:
    auswahlliste2.insert(END, eintrag)
auswahlliste2.activate(2)
auswahlliste2.pack()

fenster.mainloop()



