from robots_class import Roboter

r1 = Roboter()
r2 = Roboter()

r3 = r2

print("__name__ hat den Wert:", __name__)

print(r1 == r2)
print(r3 == r2)
