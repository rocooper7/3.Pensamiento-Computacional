from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file = 'graficado_simple.html'
    fig = figure()

    valores_totales = int(input('Cual es el rango de x?'))
    x_valores = list(range(valores_totales))
    y_valores = []

    for x in x_valores:
        valor_y = int(input(f'x:{x} and y:'))
        y_valores.append(valor_y)

    fig.line(x_valores,y_valores,line_width=2)
    show(fig)

