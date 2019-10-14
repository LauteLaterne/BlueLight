#Spielen mit Datentypen

text=input("Gebe einen Text ein: ")
print("Du hast diesen Text eingegeben:", text)
text=text.upper()
print("Dein Text umgewandelt: ", text)
print("Datentyp Deiner Eingabe ist:", type(text))
#ab hier läuft es nur weiter, wenn eine Zahl eingegeben wurde
text=eval(text)+1000
print("Dein Text wurde geändert in:", text)
print("Datentyp Deiner Eingabe ist:", type(text))
