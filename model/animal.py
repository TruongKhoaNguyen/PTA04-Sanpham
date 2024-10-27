class animal:
    def __init__(self,_n = "Unknown",_a = 0,_s = 0,_h = 0):
        self.name = _n
        self.age = _a
        self.specie = _s
        self.habitat = _h
    def show(self):
        print(self.__dict__)
    def make_sound():
        print("...")
    def feed(food):
        print("ABCD")
## LOP CON
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
    def fly(self):
        print("I'm flying !")
    def make_sound(self):
        print("Mammal !!!")
class reptile(animal):
    def walk(self):
        print("Unknown")
    def make_sound(self):
        print("Mammal !!!")
class fish(animal):
    def swim(self):
        print("Just swim")
    def make_sound(self):
        print("Mammal !!!")

anm1 = bird("Chim",4)
anm1.show()
anm1.make_sound()
anm1.fly()
anm2 = fish("Ca",50)
anm2.show()
anm2.make_sound()
anm2.swim()
