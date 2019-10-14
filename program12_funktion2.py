#Übung: Programm zum Prüfen, ob eingeben Userdaten (Login-Name, Passwort) in der User-Liste vorhanden sind

def login_prüfen(username_eingabe, password_eingabe):
# Funktion prüft, ob in der Liste ein passendes Paar zum übergebenen Paar vorhanden ist
    # Teil 1: Aufbau der unveränderlichen User-Liste --> diese noch mit einer Funktion in eine eigene Datei auslagern

    user1 = dict(username = "erika", password= "1944")
    user2 = dict(username = "georg", password= "1940")
    user3 = dict(username = "birgit", password= "1971")
    user4 = dict(username = "rainer", password= "1968")
    userliste = [user1, user2, user3]
    print(userliste)

    # Teil 2: Prüft, ob ein passendes Paar in der Liste vorhanden ist
    login_korrekt = False
    for inhalt in userliste:
        print(inhalt["username"])
        print(inhalt["password"])

    for inhalt in userliste:
        if username_eingabe == inhalt["username"]:
            print("--> VORNAME DRIN!")
            if password_eingabe ==  inhalt["password"]:
                print("*** DU BIST DRIN! ***")
                login_korrekt = True
              
    return(login_korrekt)  

    
# Hauptprogramm
 # Start Wiederholungsschleife für Hauptprogramm

aktion = "ja"
print("")
while aktion == "ja":
    username_eingabe = input("Gebe Deinen Nutzernamen an: ")
    password_eingabe= input("Gebe Deinen Passwort an: ")
    print("Nutzername: ", username_eingabe)
    print("Passwort: ", password_eingabe)

    login_valide = login_prüfen(username_eingabe, password_eingabe)
    print("Userdaten sind korrekt:", login_valide)
    print("")
    aktion=input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
    print("")

print ("\n", "--> ENDE Programm", "\n")
