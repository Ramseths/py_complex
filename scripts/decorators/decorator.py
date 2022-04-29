def decorator_function(function):
    def internal_function():
        # Acciones que decoran
        print("Vamos a realizar un cálculo: ")
        function()
        # Más acciones
        print("Se ha terminado el cálculo")
    
    return internal_function


# Cuando se ejecute add() deberá agregar la función decoradora
@decorator_function
def add():
    print(10+10)

def subtract():
    print(20-5)


if __name__ == '__main__':
    add()

