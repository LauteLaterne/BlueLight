#Übung: TKinter - mehrere Elemente in einem Fenster anzeigen

from tkinter import  *

class BetterButton(Button):
    def aktion(self):
            print("\n", "VERDAMMT! Du hast den Button gedrückt!")
            text = Text(height = 4, width = 40)
            text.tag_configure('format', font= ('Verdana', 20, 'bold'))
            text.insert(END, "VERDAMMT! Du hast den Kopf gedrückt!!!", 'format')
            text.pack()
         
fenster = Tk()
fenster.title("BUSINESS BULLSHIT GENERATOR")
fenster.geometry("600x800")
rahmen = Frame(fenster, relief="ridge", borderwidth = 5)
rahmen.pack()
#rahmen.pack(fill="both", expand = 1)
label = Label(rahmen, text="Mein Name ist HAL3000 :-)")
label.grid(row = 1, column = 1, columnspan = 2, padx = 200, pady = 10)
knopf1 = Button(rahmen, text = "Ok", command=fenster.destroy)
knopf1.grid(row = 2, column = 1)
knopf2 = BetterButton(rahmen, text="NICHT drücken!")
knopf2["command"] = knopf2.aktion
knopf2.grid(row = 2, column = 2)

text2 = Text(height = 2, width = 28)
text2.insert(END, "so! und so weiter... nöhhh")
text2.pack()

text3 = Text(height = 2, width = 35)
text3.tag_configure('format', font=('Verdana', 20, 'bold'))
text3.insert(END, "NOW you see ME!", 'format')
text3.pack()

bild = PhotoImage (file="ESB-Special-Edition-small.gif")
label2 = Label(fenster, image=bild)
label2.pack()

fenster.mainloop()

