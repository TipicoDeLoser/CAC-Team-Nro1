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
        elif exerciseId == 4:
            exercise4()
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