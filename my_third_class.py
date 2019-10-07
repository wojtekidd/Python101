class Barn:
    def __init__(self, open = False):
        self.open=open

    def open(self):
        self.open = True

    def close(self):
        self.open = False

    def is_open(self):
        return self.open

class Hen:
    def __init__(self, name, barn, age = 1, alive = True, hungry = True):
        self.name = name
        self.age = age
        self.alive = alive
        self.hungry = hungry
        self.barn = barn

    def speak(self):
        print("KOKOKO")

    def is_alive(self):
        print("Am I alive?")
        return self.alive

    def kill(self):
        print("You killed me, because teh barn was closed")
        self.alive = False

    def is_hungry(self):
        return self.hungry

    def eat(self):
        print("I'm eating")
        if self.hungry:
            print("I'm hungry!")
            self.hungry = False
        else:
            print("I'm full!")

    def sleep(self):
        print("I'm going to sleep")
        if self.barn.is_open():
            if not self.hungry:
                    self.hungry = True
                    print("I'm hungry again")
        else:
            self.kill()
            print("I'm dead...")


b1 = Barn()
kura1 = Hen("Hela", b1)
kura2 = Hen("Jola", b1)

kura1.speak()
kura1.is_hungry()
kura1.eat()
kura1.is_hungry()
kura1.sleep()
kura1.sleep()
print(kura1.name + " is dead")

