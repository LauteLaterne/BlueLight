# Übung: Programm zum Verwenden der Python-Standardbibiliothek: Ausgabe der aktuellen Uhrzeit mit Datum mit Funktion aus der Standardbibliothek
# Übung ist im ersten Teil falsch über Objekte gelöst, weil ich die Funktionen nicht in der Doku fand.
# Im Nachhinein gar nicht schlecht, weil ich so erste Berührung mit objektorientierter Programmierung hatte.

import datetime
import time

# Hauptprogramm mit Wiederholungsschleife
aktion = "ja"
start= ""
print("\n", "*** Wir zeigen Dir die aktuelle Zeit mit Datum an! ***")
start = input("Zum Starten gebe 'ja' ein: ")
print("")

if start == "ja":
    while aktion == "ja":

       # falscher Lösungsweg mit dem falschen Modul "datetime" über Objekte/Methoden
       from datetime import date
       print("\n", "+++OBJECT DATE: Rainer & Aktuell+++")
       d = date(1968, 1, 16)
       print(d)
       print(d.day)
       print(d.month)
       print(d.year)
       d = d.today()
       print(d)
       print(d.strftime("%A"))
       print("\n", "+++OBJECT DATETIME+++")
       # Beachte: Die Ausgabe des Wochentagnames in Deutsch wäre mit dem Modul "locale" möglich. Aber auf diesem System ist das notwenige deutsche locale nicht installiert. Bei der Visual Studio Sprache habe ich nur Englisch eingestellt.

       from datetime import datetime
       dt = datetime.now()
       print(dt)
       print("\n", "+++OBJECT TIME+++")
       h = datetime.now().hour
       print(h)
       m = datetime.now()
       print(m.minute)

       print("\n", "*** Ausgabe Lösung Übungsaufgabe via daytime-Modul & dessen Objekte, Methoden***")
       print("Heute ist %s der %s.%s.%s"%(d.strftime("%A"), d.strftime("%d"), d.strftime("%m"), d.strftime("%Y")))
       print("Die aktuelle Uhrzeit ist: %s:%s"%(datetime.now().hour, datetime.now().minute))
       print("")

       # Richtiger Lösungsweg mit dem richtigen Modul "time" und dessen Funktion
       print("\n", "*** Ausgabe Lösung Übungsaufgabe via time-Modul & dessen Funktion time.local**")
       tu = time.localtime()
       print(tu[0])
       print("Das heutige Datum ist %d.%d.%d"%(tu[2], tu[1], tu[0]))
       print("Die aktuelle Uhrzeit ist: %d:%d"%(tu[3], tu[4]))
      
       print("")

       aktion = input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
       print("")
else:
  print("\n", "SCHADE! -->  Ein anderes Mal! ")

print ("\n", "--> ENDE Programm", "\n")
