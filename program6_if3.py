#Zweite Übungsaufgabe Kapitel 7.5 --> 5 Rechneaufgaben mit Punktevergabe und finaler Auswertung der erreichten Punkte

# Aufgabe vorstellen
print("\n", "***** RECHENTEST ****", "\n")
print(" --> Du bekommst 5 Rechenaufgaben gestellt.")
print( " --> Für jede richtig gelöste Aufgabe bekommst Du einen Punkt.")
print(" --> Danach teilen wir Dir dann Dein Ergebnis mit.", "\n")

punkte=0

#Aufgaben und Punktevergabe
eingabe = eval(input("Aufgabe 1:   1 + 1 = "))
if eingabe == 2:
  punkte=punkte+1

eingabe = eval(input("Aufgabe 2:   1 * 1 = "))
if eingabe == 1:
  punkte=punkte+1

eingabe = eval(input("Aufgabe 3:   23 - 7 = "))
if eingabe == 16:
  punkte=punkte+1
  
eingabe = eval(input("Aufgabe 4:   42 /  7 = "))
if eingabe == 6:
  punkte=punkte+1

eingabe = eval(input("Aufgabe 5:   1 * 0 = "))
if eingabe == 0:
  punkte=punkte+1

# Punkte auswerten und Ergebnis ausgeben
print ("\n", "++++ DEIN ERGEBNIS ++++")

if punkte == 0:
  print("\n", "Du hast", punkte, "Punkte erreicht.")
  print ("\n", "----- VERSAGER!!! -----")

elif punkte == 1:
  print("\n", "Du hast", punkte, "Punkt erreicht")
  print ("\n", "Immerhin! Du hast noch VIEL Luft nach oben!")

elif punkte == 2:
  print("\n", "Du hast", punkte, "Punkte erreicht")
  print ("\n", "Na ja! Da hast Du ja noch Luft nach oben!")

elif punkte == 3:
  print("\n", "Du hast", punkte, "Punkte erreicht")
  print ("\n", "Gar nicht SO schlecht! Aber das geht noch besser, oder?") 

elif punkte == 4:
  print("\n", "Du hast", punkte, "Punkte erreicht")
  print ("\n", "FAST perfekt!") 

elif punkte == 5:
  print("\n", "Du hast", punkte, "Punkte erreicht")
  print ("\n", "°°°°°° PERFETTO!!! °°°°°°") 

print ("\n", "--> CODE ENDE", "\n")
