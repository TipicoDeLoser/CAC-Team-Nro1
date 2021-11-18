import string

def displayExercise():
    exerciseId = 0
    emptyexerciseIdMessage = "Ejercicio no implementado"
    askExercise = "Por favor ingrese un numero de ejercicio: "

    while exerciseId == 0:
        exerciseId= int(input(askExercise))

        if exerciseId == 4:
            exercise4()
        else:
            exerciseId = 0
            print (emptyexerciseIdMessage)

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