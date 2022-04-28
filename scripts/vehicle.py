class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'stand-by'
        self._motor = Motor(cylinders=4)


    def accelerate(self, type = 'despacio'):
        if type == 'rapida':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)
        
        self._status = 'en movimiento'
    
class Motor:

    def __init__(self, cylinders, type = 'gasolina'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self, lt):
        pass