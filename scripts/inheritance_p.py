class Animal:

    def __init__(self, sound):
        self.sound = sound
    
    def play(self):
        return self.sound


class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound)

if __name__ == '__main__':
    cat = Animal('Miauuu')
    print(cat.play())

    dog = Dog('Woaf Woaf')
    print(dog.play())
