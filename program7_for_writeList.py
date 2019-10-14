#Beispiel aus Buch: Werte in eine Liste mit FOR-Schleife schreiben

liste = [55, 66, 77, 88, 99]
print ("\n", "Liste:", liste, "\n")

# Listenihalt mit for-Schleife ausgeben
print("Elemente der Liste mit for-Schleife ausgeben:")
for inhalt in liste:
  print(" ", inhalt)

# Ändern Werte in Liste mit for-Schleife nicht direkt möglich, sondern nur mit Umweg mit der enumerate-Funktion
print()
print("Elemente in der Liste mit for-Schleife mit Hilfe der enumerate-Funktion mit 100 multiplizieren.")
for inhalt in enumerate(liste):
  liste[inhalt[0]] =  inhalt[1] * 100
 # print(liste[inhalt[0]])
  #print(liste)

# print()
print(" Geänderte Liste:", liste, "\n")

# Ausgeben der mit der enumerate-Funktion angelegten indizierten Hilfsliste.
# Ausgegeben wird Index und Werte jedes Listen-Eintrags
print("Ausgabe jedes Eintrags (Index und Wert) in der mit der enumerate-Funktion angelegten indizierten Hilfsliste:")
for index, inhalt in enumerate(liste):
  print(" ", "Index:", index, "    Wert:", inhalt)

print ("\n", "--> CODE ENDE", "\n")
