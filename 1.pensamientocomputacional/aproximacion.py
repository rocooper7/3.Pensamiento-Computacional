objetivo = int(input('Escoge un numero: '))
epsilon = 0.01 #que tan cerca queremos llegar a la respuesta depende que tan exacto se quiera (se agregan 0.0001) pero tarda mucho tiempo
paso = epsilon**2  #que tanto nos vamos a ir acercando a esta respuesta
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta) #Para ver que va pasando
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
