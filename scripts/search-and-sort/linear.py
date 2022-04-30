import random

def linear_search(input_list, target):
    
    # Indicador
    match = False
    
    for element in input_list:
        if element == target:
            match = True
            break

    return match

def main():
    list_length = int(input('De qué tamaño será la lista?'))
    target = int(input('Ingresa lo que deseas buscar en las lista'))
    input_list = [random.randint(0, 100) for i in range(list_length)]
    find = linear_search(input_list, target)
    print(input_list)
    print(f'El elemento {target} {"se encontró" if find else "no se encontró"} en la lista')
    

if __name__ == '__ main__':
   main()