def pascals_triangle(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1), end='')
        coef = 1 
        for j in range(i + 1):
            print(coef, end=' ')
            coef = coef * (i - j) // (j + 1)
        print() 
pascals_triangle(5)
