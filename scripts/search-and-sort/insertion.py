import random
# Insertion Sort
def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        current = input_list[i]
        index = i
        while index > 0 and input_list[index-1] > current:
            input_list[index] = input_list[index-1]
            index -= 1
        input_list[index] = current
    
    return input_list

def main():
    list_length = int(input('Ingresa el tamaño de lista: '))
    input_list = [random.randint(0, 100) for i in range(list_length)]
    print(input_list)

    sorted_list = insertion_sort(input_list)
    print(sorted_list)

if __name__ == '__main__':
    main()
