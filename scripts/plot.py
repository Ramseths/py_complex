from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('plot.html')
    fig = figure()

    total = int(input('Ingresa el total de datos: '))
    x = list(range(total))
    y = []

    for i in x:
        value = int(input(f'Valor para {i}: '))
        y.append(value)

    fig.line(x, y, line_width = 2)
    show(fig)