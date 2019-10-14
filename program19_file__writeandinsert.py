# Übung: Eine Datei für eine Einladungsliste erstellen und Gästename reinschreiben oder in vorhandene Datei weitere Gäste hinzufügen
           
import sys

# Start Hauptprogramm mit Wiederholungsschleife

auswahl = ""
print("\n")
while auswahl == "":
    auswahl = input("Gebe bitte an, ob Du eine NEUE Einladungsliste anlegen möchtest oder WEITERE Gäste in die vorhandene Gästeliste hinzuzufügen: ") 
    if auswahl == "NEUE":
        f = open('gaesteliste.txt', 'w')
        f.write("vorname"+";")
        f.write("nachname"+"\n")
    elif auswahl == "WEITERE":
        f = open('gaesteliste.txt', 'a')
    else:
        print("*** Du hast weder NEUE noch WEITERE angegeben --> wiederhole die Auswahl noch mal! ***", "\n")
        auswahl = ""
        
    # wäre noch besser, oben eine EXCEPTION einzufügen, wenn Zugriff auf Datei fehlschlägt bzw. verweigert wird

aktion = "ja"
start= ""
print("\n", "*** Möchtest Du jetzt Gäste in die Einladungsliste aufnehmen?  ***")
start = input("Zum Starten gebe 'ja' ein: ")
# print("")

if start == "ja":

    while aktion == "ja":
        print("\n")
        print("*** Jetzt kannst Du einen neuen Gast für die Einladungsliste angeben ***")
        vorname = input("Gebe den Vorname des neuen Gast ein: ")
        nachname = input("Gebe den Nachname des neuen Gast ein: ")
        vorname = vorname.upper()
        nachname = nachname.upper()
        aufnehmen = input("Wenn Du den Gast %s %s in die Gästeliste aufnehmen möchtest gebe 'ja' ein: " %(vorname, nachname))

        if aufnehmen == "ja":
            f.write(vorname+";")
            f.write(nachname+"\n")
        else:
            print("\n", "---> Der Gast %s %s wird NICHT in die Gästeliste aufgenommem!!" %(vorname, nachname))

        aktion = input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
        print("")

    else:
        print("\n", "ENDE AUFNAHME NEUER GÄSTE IN DIE EINLADUNGSLISTE")

else:
    print("\n", "KEINE AUFNAHME NEUER GÄSTE IN DIE EINLADUNGSLISTE")

print ("\n", "--> ENDE Programm", "\n")





