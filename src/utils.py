import string

def displayExercise():
    exerciseId = 0
    emptyexerciseIdMessage = "Ejercicio no implementado"
    askExercise = "Por favor ingrese un numero de ejercicio: "

    while exerciseId == 0:
        exerciseId= int(input(askExercise))

        if exerciseId == 1:
            exercise1()
        elif exerciseId == 2:
            exercise2()
        elif exerciseId == 3:
            exercise3()
        elif exerciseId == 4:
            exercise4()
        elif exerciseId == 6:
            exercise6()
        else:
            exerciseId = 0
            print (emptyexerciseIdMessage)


def exercise1():
    inputStr= input("Ingrese su string: ")
    print(guionXEspacio(inputStr))

def guionXEspacio(parameterStr):
    """Reemplaza los espacios por guion"""

    returnStr = ""
    empryStringMessage = "Error: string no ingresado"

    if not parameterStr:
        return  empryStringMessage
    else:
        returnStr = parameterStr.replace(' ','-')
    return returnStr

def exercise2():
    inputStr= input("Ingrese un texto de hasta 100 caracteres: ")
    print(changeLeters(inputStr))


def changeLeters(parameterStr):
    """Reemplaza mayusculas por minusculas y visceversa"""

    returnStr = ""
    empryStringMessage = "Error: Texto no ingresado"
    toLongStringMessage = "Error: El texto ingresado es mayor a 100 caracteres"

    if not parameterStr:
        return  empryStringMessage
    elif len(parameterStr) > 100:
        return toLongStringMessage
    else:
        for indice in range(0,len(parameterStr)):
            if parameterStr[indice].isupper():
                returnStr += parameterStr[indice].lower()
            else:
                parameterStr[indice].upper()
                returnStr += parameterStr[indice].upper()
    return returnStr


def exercise3():
    text = input("Por favor, ingrese un texto inspirador: ")
    letter = input("Cuál es su letra favorita?: ")
    number = input("Y su número de la suerte?: ")
    print(change_letter(text, letter, number))

def change_letter(t, l, n):

    n = int(n)
    t = str(t)
    l=str(l)

    if n < len(t):
        return t[:n-1] + l + t[n:]
    else:
        print("El número debería ser menor a ", len(t))


def exercise4():
    inputStr= input("Ingrese su nombre y apellido: ")
    print(toPascalCase(inputStr))


def toPascalCase(parameterStr):
    """Reemplaza los primeros caracteres de cada palabra"""

    returnStr = ""
    empryStringMessage = "Error: Nombre y apellido no ingresado"

    if not parameterStr:
        return  empryStringMessage
    else:
        listStr = parameterStr.split(" ")

        for indice in listStr:
            upperStr = indice[0].upper() + indice[1:len(indice)]
            returnStr += upperStr + " "

    return returnStr.rstrip()


def exercise5 (): # Utilizando iteración y condicionales. Si hay mas de dos números iguales lo devuelve en la salida. 
    lista = [2,6,10,10,7,5,6]
    lista.sort(reverse =True)
     
    for i in range (len(lista)):
         if (lista[i + 2]) == (lista[i + 1]):
              print ("Hay mas de dos notas altas iguales")
              break
         elif (lista[i + 1]) == (lista[i]):
               print (lista [i + 2])                
               break
         else:
              print (lista [i + 1])
              break
   
exercise5 ()

def exercise5_b (): # Utilizando metodos de listas y condicionales. Si hay mas de dos números iguales lo devuelve en la salida. 
     lista = [2,6,10,10,7,5,6]
     lista.sort(reverse =True)
     mayor = (max(lista))
     contador = lista.count(mayor)
     if contador <= 1:
         print (lista[1])
     elif contador <=2:
         print (lista [2])
     else:
         print ("Hay mas de dos notas altas iguales")
             
   
    
exercise5_b ()


def exercise6():
    try:
        inputInt= int(input("Ingrese un numero entero: "))
        triangleInt(inputInt)
    except ValueError:
        print("Error: No se ingreso un numero valido")
    

def triangleInt(parameterInt):
    """Recibe un numero entero y imprima por salida estandar(usando print) un triangulo de numeros de altura igual al numero ingresado"""

    for indice in range(1 , parameterInt+1):
        print(str(indice)*indice)
    