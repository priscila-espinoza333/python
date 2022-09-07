#RETO 1 - Crear una función llamada sumatoriaArray(arreglo) y regrese la sumatoria de todos los elementos del arreglo
#arreglo = [2, 3, 4, 5]
#total = 0
#num = 2
#total = total + num = 0 + 2 = 2

#num = 3
#total = 2 + 3 = 5

#num = 4
#total = 5 + 4 = 9

#num = 5
#total = 9 + 5 = 14

#RETURN 14
def sumatoriaArray(arreglo):
    total = 0

    for num in arreglo:
        total += num

    return total


total_sumatoria = sumatoriaArray([2, 3, 4, 5]) #total_sumatoria = 14
print(total_sumatoria)
#RETO 2: Crear una función que reciba un arreglo y que me regrese el promedio de los elementos del arreglo.
def promedio(arreglo):
    #CODIGO

    return cant_promedio

total_promedio = promedio([1, 2, 3])

#RETO 2: Crear una función que reciba un arreglo y que me regrese el promedio de los elementos del arreglo.
#arreglo = [1, 2, 3]
#sum = 0
#num = 1
#sum = 0 + 1 = 1

#num = 2
#sum = 1 + 2 = 3

#num = 3
#sum = 3 + 3 = 6

#cant_promedio = 6 / 3 = 2
#RETURN 2
def promedio(arreglo):
    sum = 0
    for num in arreglo: #Suma todos los números
        sum += num
    
    cant_promedio = sum / len(arreglo) #La sumatoria la divido entre el tamaño total del arreglo

    return cant_promedio

total_promedio = promedio([1, 2, 3]) # total_promedio = 2
print(total_promedio)


#RETO 3: Crear una función que reciba un arreglo y que sume todos los números SIEMPRE Y CUANDO sean positivos
def sumaPositivos(arreglo):
    total = 0

    for num in arreglo:
        if num > 0:
            total += num


   return total

total_suma = sumaPositivos([-2, 3, 4, -1]) #solo me va a sumar 1 +2 + 3           


    return sum


total_suma = sumaPositivos([1, 2, 3, -1]) #Solo me va a sumar 1 + 2 + 3

