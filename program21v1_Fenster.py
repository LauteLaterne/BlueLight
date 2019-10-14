#Übung: TKinter - ein erstes Fenster anzeigen

from tkinter import  *

fenster = Tk()
fenster.title("BUSINESS BULLSHIT GENERATOR")
fenster.geometry("640x480")
rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)
label = Label(rahmen, text="Mein Name ist HAL3000 :-)")
label.pack(expand=1)
label.pack()
fenster.mainloop()



