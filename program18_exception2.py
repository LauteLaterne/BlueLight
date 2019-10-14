# Übung: Eingabe einer Zeichenkette mit geraden Anzahl an Zeichen. Diese dann in zwei Strings trennen und ausgeben.
# Eingabe ungerade Anzahl von Zeichen mit einer selbst definierter Exception abfangen.
           
import sys

class UnevenStringNumberError(Exception):
    def __init__(self, word):
        self.Eingabe = word


# Start Hauptprogramm mit Wiederholungsschleife

aktion = "ja"
start= ""
print("\n", "*** Soll die Schleife starten?  ***")
start = input("Zum Starten gebe 'ja' ein: ")
print("")

if start == "ja":
    while aktion == "ja":    
        print("WIEDERHOLUNGSSCHLEIFE")
        try:
            wort = input("Gebe ein Wort mit einer GERADEN Anzahl an Buchstaben ein: ")
            wort = wort.upper()
            print("Du hast das Wort < %s > eingegeben." %(wort))
            anzahl = len(wort)
            print("Dein Wort hat %d Zeichen." %(anzahl))
            rest = anzahl % 2
            print("Ungerade Anzahl an Buchstaben erfüllt:", rest)

            if rest != 0:
                raise UnevenStringNumberError(wort)
            if rest == 0:
                mitte = int(anzahl/2)
                teil1 = wort[:mitte]
                teil2 = wort[mitte:]
                print("Wort geteilt: ", teil1, "<--->", teil2)
                      
        except UnevenStringNumberError as zeichenkette:
            print("*** EXCEPTION *** Das Wort <", zeichenkette.Eingabe, "> kann nicht geteilt werden, weil es eine UNGERADE  Anzahl an Buchstaben hat !!!")
        except ZeroDivisionError:
            print("ZeroDivisionError --> Er ist nicht möglich, eine Zahl durch 0 zu teilen!!!")
        except TypeError:
            print("TypeError --> KEINE Zeichen zulässig!!!")
        except ValueError:
            print("ValueError --> Als Divisor darfst Du nur GANZE Zahlen eingeben!!!")
        except:
            print("Folgender Fehler ist aufgetreten: ", sys.exc_info()[0])
        finally:
            print("Jetzt wird noch aufgeräumt.")
            
        
        aktion = input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
        print("")
    else:
        print("\n", "ENDE WIEDERHOLUNGSSCHLEIFE")

print ("\n", "--> ENDE Programm", "\n")





