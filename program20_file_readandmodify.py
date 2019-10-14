# Übung: Aus einer Datei für eine Einladungsliste einen angegebenen Namen suchen und diesen aus der Datei entfernen bzw. die gekürzte Einladungsliste in eine andere Datei schreiben
           
import sys

# Start Hauptprogramm mit Wiederholungsschleife

aktion = "ja"
start= ""
print("\n", "*** Möchtest Du jetzt Gäste von der Einladungsliste entfernen?  ***")
start = input("Zum Starten gebe 'ja' ein: ")
f = open('gaesteliste.txt', 'r')

if start == "ja":
    liste = f.readlines()
    print("")
    print(liste)
    eintraege = int(len(liste)-1)
    print("")
    print("Anzahl Einträge in Liste: ", eintraege)

    for i in range(eintraege):
        #print("#", i, liste[i+1])
        print("   #%d %s" %(i, liste[i+1]))
        
    while aktion == "ja":
        eintraege = int(len(liste)-1)
        print(eintraege)
        print("\n")
        print("*** Jetzt kannst Du einen neuen Gast aus der Einladungsliste entfernen ***")
        print("")
        vorname = input("Gebe den Vorname des unwillkommenen Gast ein: ")
        nachname = input("Gebe den Nachname des unwillkommenen Gast ein: ")
        vorname = vorname.upper()
        nachname = nachname.upper()
        print("")
        entfernen = input("Wenn Du diesen JETZT aus der Gästeliste entfernen möchtest gebe 'ja' ein: ")

        if entfernen == "ja":
            target = vorname + ";" + nachname + "\n"
            try:
                liste.remove(target)
                eintraege = int(len(liste)-1)
                print("\n", "ENTFERNT -->  Anzahl der Einträge in der Einladungsliste nach dem Entfernen: ", eintraege)
                print("")
                for i in range(eintraege):
                    print("#", i, liste[i+1])  
            except ValueError:
                print("\n", "ValueError --> Der Name ist nicht in der Liste vorhanden")
            
        else:
            print("\n", "---> Der Gast %s %s wird NICHT aus der Gästeliste entfernt!!" %(vorname, nachname))

        aktion = input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
        print("")

    else:
        print("\n", "ENDE ENTFERNEN VON GÄSTEN AUS DER EINLADUNGSLISTE")
        print("")
        abspeichern = input("Wenn Du die geänderte Liste jetzt in die Datei abspeichern möchtest, gebe 'ja' ein: ")

        if abspeichern == "ja":
            f.close
            f = open('gaesteliste_mod.txt', 'w')
            f.write("vorname"+";")
            f.write("nachname"+"\n")
            for i in range(eintraege):
                f.write(liste[i+1])
            print("")
            print("\n", "--> GESPEICHERT !!!")
            f.close
            f = open('gaesteliste_mod.txt', 'r')
            inhalt = f.read()
            print("\n", "+++ Inhalt der modifizierten EInladungsliste in der neuen Datei +++")
            print(inhalt)
            
else:
    print("\n", "KEINE GÄSTE AUS DER EINLADUNGSLISTE ENTFERNEN")

print ("\n", "--> ENDE Programm", "\n")





