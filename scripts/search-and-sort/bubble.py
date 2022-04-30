import random

def bubble_sort(input_list):
    n = len(input_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] =  input_list[j + 1], input_list[j]
    
    return input_list
    


def main():
    list_length = int(input('De qué tamaño será la lista?'))

    input_list = [random.randint(0, 100) for i in range(list_length)]
    print(input_list)

    sorted_list = bubble_sort(input_list)
    print(sorted_list)
    
if __name__ == '__main__':
   main()