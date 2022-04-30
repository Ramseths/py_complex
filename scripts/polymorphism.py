class Person:
    def __init__(self, name):
        self.name = name

    def progress(self):
        print('Estoy caminando')

class Runner(Person):
    
    def __init__(self, name):
        super().__init__(name)
    
    def progress(self):
        print('Estoy corriendo')

def main():
    person = Person('John')
    person.progress()

    runner = Runner('Ramseths')
    runner.progress()

if __name__ == '__main__':
    main()
