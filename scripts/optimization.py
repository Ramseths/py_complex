from turtle import back


def backpack(size, w, values, n):
    if n == 0 or size == 0:
        return 0

    if w[n - 1] > size:
        return backpack(size, w, values, n - 1)
    
    return max(values[n - 1] + backpack(size - w[n - 1], w, values, n - 1),
                backpack(size, w, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    w = [10, 20, 30]
    size = 25
    n = len(values)

    result = backpack(size, w, values, n)
    print(result)
