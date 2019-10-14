#Übung: TKinter - mehrere Elemente in einem Fenster anzeigen

from tkinter import  *

fenster = Tk()
fenster.title("BUSINESS BULLSHIT GENERATOR")
fenster.geometry("1024x768")
rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)
label = Label(rahmen, text="Mein Name ist HAL3000 :-)")
label.pack(expand=1)
label.pack()
text2 = Text(height=2, width=28)
text2.insert(END, "so! und so weiter... nöhhh")
text2.pack()
text3 = Text(height=4, width=35)
text3.tag_configure('format', font=('Verdana', 20, 'bold'))
text3.insert(END, "NOW you see ME!", 'format')
text3.pack()
bild = PhotoImage (file="ESB-Special-Edition-small.gif")
label2 = Label(fenster, image=bild)
label2.pack()
fenster.mainloop()


