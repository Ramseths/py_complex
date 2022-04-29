class Washer:
    
    def __init__(self):
        pass

    def wash(self, temperature = 'caliente'):
        self._fill_water(temperature)
        self._add_soap()
        self._wash()
        self._clean()
    
    def _fill_water(self, temperature):
        print(f'Llenando el tanque con agua {temperature}')

    def _add_soap(self):
        print('Agregando jabón')

    def _wash(self):
        print('Está lavando la ropa')
    
    def _clean(self):
        print('Limpiando...')


if __name__ == '__main__':
    my_washer = Washer()
    my_washer.wash()