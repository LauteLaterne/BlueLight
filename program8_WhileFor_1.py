#Übungsaufgabe aus Buch: Quadratzahlen von 1 bis 10 ausgeben mit wile und for

i = 1
print("\n", "Quadrat einer Zahl mit FOR-Schleife berechnen:")

for i in range(1,11):
  n = i*i
  print("   Das Quadrat von", i, "ist:", n)

i = 1
print("\n", "Quadrat einer Zahl mit WHILE-Schleife berechnen:")
while i<=10:
  n = i * i
  print("   Das Quadrat von", i, "ist:", n)
  i =  i + 1
  
print ("\n", "--> CODE ENDE", "\n")
