#Übungsaufgabe aus Buch: Mit Break For-Schleife beenden

aktion = "ja"
print("")

while aktion == "ja":
  zahl = eval(input("Gebe eine GANZE Zahl ein, die wir für Dich verdoppeln sollen: "))
  print(isinstance(zahl, int))
  print(zahl)
  
  if not isinstance(zahl, int):
    print("So geht's nicht: Du hast", zahl, "eingenben --> Das ist keine GANZE Zahl!")
    break
    
  print("Doppelter Wert von", zahl, "ist:", zahl *2)
  aktion=input("Wenn Du das wiederholen möchtestm gebe 'ja' ein: ")
  print("")

print ("\n", "--> ENDE Programm", "\n")
