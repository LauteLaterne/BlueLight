#Übung: Programm zum Verwenden der Python-Standardbibiliothek: Zahlen würfeln mit Zufallsgenerator

import random

# Hauptprogramm mit Wiederholungsschleife
aktion = "ja"
start= ""
print("\n", "*** Wir würfeln für Dich! ***")
start=input("Zum Starten gebe 'ja' ein: ")
print("")

if start == "ja":
    while aktion == "ja":
        zahl = random.randint(1, 6)  
        print("Du hast eine %d gewürfel."%(zahl))
        print("")
        aktion=input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
        print("")
else:
  print("\n", "SCHADE! -->  Ein anderes Mal! ")

print ("\n", "--> ENDE Programm", "\n")
