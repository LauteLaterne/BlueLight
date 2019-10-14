class Roboter:
    pass

r1 = Roboter()
r2 = Roboter()

r3 = r2

print("__name__:", __name__)

print(r1 == r2)
print(r3 == r2)
