# Binary Search
import random

def binary_search(input_list, start, end, target, iter_bin=0):
    print(f'Buscando {target} entre {input_list[start]} y {input_list[end-1]}')
    iter_bin+=1
    if start > end:
        return [False, iter_bin]
    mid = (start + end) // 2

    if input_list[mid] == target:
        return True
    elif input_list[mid] < target:
        return binary_search(input_list, mid + 1, end, target, iter_bin)
    else:
        return binary_search(input_list, start, mid - 1, target, iter_bin)


def main():
    list_length = int(input('De qué tamaño será la lista?'))
    target = int(input('Ingresa lo que deseas buscar en las lista'))
    input_list = sorted([random.randint(0, 100) for i in range(list_length)])
    find, total = binary_search(input_list, 0, len(input_list), target)



    print(input_list)
    print(f'El elemento {target} {"se encontró" if find else "no se encontró"} en la lista con {total} iteraciones')
    
if __name__ == '__main__':
   main()