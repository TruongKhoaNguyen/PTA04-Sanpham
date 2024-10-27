class animal:
    def __init__(self,_n = "Unknown",_a = 0):
        self.name = _n
        self.age = _a
    def show(self):
        print(self.__dict__)
    def make_sound(self):
        print("...")

class dog(animal):
    # Co roi :)
    def make_sound(self):
        print("RUN !!!")
class cat(animal):
    # Co roi :)
    def make_sound(self):
        print("SLEEP !!!")
class mammal(animal):
    def fur_color(self):
        print("???")
    def eat(self):
        print("Yuck!")
    def make_sound(self):
        print("I'm not a robot")
class bird(animal):
    def wing_span(self):
        print("In mid-air")
    def make_sound(self):
        print("F-")
    def fly(self):
        print("I'm FLYING !!")
class reptile(animal):
    def walk(self):
        print("Unknown")
    def make_sound(self):
        print("GOAH !!!")
class fish(animal):
    def swim(self):
        print("Just swim")
    def make_sound(self):
        print("Fish !!!")

list_animal = [
    dog("A",15),
    cat("B",12),
    bird("C",10),
    fish("D",85),
    mammal("E",85),
    reptile("F",85),
    mammal("G",99)
]
# In ra tu list
print("Welcome to Playtime zoo")
print("!@#$%^&*()_+!%$^&*(%#$%^&(!@#$%^&*()_+!%$^&*(%#$%^&(!@#$%^&*()_+!%$^&*(%#$%^&(")
print(f"We have got {len(list_animal)} here")
print("!@#$%^&*()_+!%$^&*(%#$%^&(!@#$%^&*()_+!%$^&*(%#$%^&(!@#$%^&*()_+!%$^&*(%#$%^&(")
for anm in list_animal:
    print(f"Hello, my name is {anm.name} || Speaker :")
    anm.make_sound()
print("!@#$%^&*()_+!%$^&*(%#$%^&(!@#$%^&*()_+!%$^&*(%#$%^&(!@#$%^&*()_+!%$^&*(%#$%^&(")

exit()
anm1 = dog("Dogday",500)
anm1.show()
anm1.make_sound()
anm2 = bird("Kickin",100)
anm2.show()
anm2.make_sound()
anm3 = cat("Catnap",999)
anm3.show()
anm3.make_sound()
