#Übungsaufgabe aus Buch: Inhalt einer Liste mit While- und For-Schleife ausgeben

liste = ["Heidelberg", "Gilching", "München", "Wessling", "Meran", "Vicopisano", "Porto", "Lisboa", "Vancouver", "Herrsching"]
print("\n", "Liste:", liste, "\n")

print("Listenelemente mit FOR-Schleife auslesen:")
for element in liste:
  print(" ", element)

print("")
print("Listenelemente mit WHILE-Schleife auslesen:")
i = 0
while i < len(liste):
  print(" ", liste[i])
  i = i +1
  
print ("\n", "--> CODE ENDE", "\n")
