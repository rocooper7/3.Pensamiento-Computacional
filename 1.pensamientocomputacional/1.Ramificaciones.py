name_1 = input('Introduce tu nombre: ')
name_2 = input('Introduce el nombre de un amigo: ')
num_1 = int(input('Introduce tu edad: '))
num_2 = int(input('Introduce la edad de tu amigo: '))

if num_1 > num_2:
    print(f'{name_1} es mayor que {name_2}') #f'' se utiliza para jalar los nombres o variables directamente en el string
elif num_1 < num_2:
    print(f'{name_2} es mayor que {name_1}')
else:
    print(f'{name_1} y {name_2} tienen la misma edad')
