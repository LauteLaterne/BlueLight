# Übung: Abfragen zweier Zahlen, um diese zu dividieren. Ausnahme für Eingabe 0 und eine wenn statt Zahl Zeichen eingegeben werden.
           
import sys

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
            dividend = eval(input("Gebe eine Zahl an, die geteilt werden soll (eval): "))
            divisor = int(input("Gebe eine GANZE Zahl an, durch die geteilt werden soll (int): "))
            print("*** Der Quotient ist :", dividend/divisor)
        except ZeroDivisionError:
            print("ZeroDivisionError --> Er ist nicht möglich, eine Zahl durch 0 zu teilen!!!")
        except TypeError:
            print("TypeError --> KEINE Zeichen zulässig!!!")
        except ValueError:
            print("ValueError --> Als Divisior darfst Du nur GANZE Zahlen eingeben!!!")
        except:
            print("Folgender Fehler ist aufgetreten: ", sys.exc_info()[0])
        finally:
            print("Jetzt wird noch aufgeräumt")
            
        
        aktion = input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
        print("")
    else:
        print("\n", "ENDE WIEDERHOLUNGSSCHLEIFE")

print ("\n", "--> ENDE Programm", "\n")





