#Übung: zwei Zahlen abfragen und Bereich dazwischen in einer Funktion schrittweise abzählen

def eingabe_prüfen(input1, input2):
#Funktion zum Validieren der Eingaben. Erlaubt sind nur Integer-Werte.

  liste = [input1, input2]
  print(liste)

  for inhalt in liste:
    print(inhalt)
    if not isinstance(inhalt, int):
      print("So geht's nicht: Du hast", inhalt, "eingegeben --> Das ist keine GANZE Zahl!")


def eingabe_ausgeben(input1, input2):
#Ausgabe jeder zweiten Zahl, die zwischen den beiden eingegebenen Werten liegen.
#Ausgabe erfolgt als Liste, damit es übersichtlicher ist.   
  print("Jetzt gebe ich Dir die Zahlen zwischen", input1, "und", input2, "in Zweierschritten aus:")
  if input2 > input1:
    input1=input1+2
    liste=[input1]
    for n in range(input1+2, input2, 2):
      liste = liste + [n]
    print(liste)

  if input1 > input2:
    input1=input1-2
    liste=[input1]
    for n in range(input1-4, input2, -2):
      liste = liste + [n]
    print(liste)

    
# Hauptprogramm
aktion = "ja"
print("")
while aktion == "ja":
  zahl1 = eval(input("Gebe erste GANZE Zahl ein: "))
  zahl2 = eval(input("Gebe zweite GANZE Zahl ein: "))
  eingabe_prüfen(zahl1, zahl2)
  eingabe_ausgeben(zahl1, zahl2)
  print("")
  aktion=input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
  print("")

print ("\n", "--> ENDE Programm", "\n")
