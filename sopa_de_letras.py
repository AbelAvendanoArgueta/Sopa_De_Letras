#Baruc Fabián Velasquez Ruíz
#Abel Fernando Avendaño Argueta

        ##################
        #   Importaciones
        ##################
import random
        ##################
        #   Listas  y variables globales
        ##################

abc = "abcdefhijklmnopqrsuvwxyz"

        ##################
        #Funciones
        ##################

def main():
    filas = 20 #int(input("Ingrese el número de filas"))
    columnas = 20 #int(input("Ingrese el número de columnas"))
    crear_matriz = Crear_Matriz()  # Almacena la clase Crear_Matriz en variable


    matriz, boolean_matriz = crear_matriz.crear_matriz(filas,columnas)  # Almacena matriz y boolean_matriz en variables

    dirección = Direcciones(matriz, ocupado=boolean_matriz)
    lista_direcciones = [
                        dirección.izquierda_a_derecha,
                        dirección.derechar_a_izquierda,
                        dirección.arriba_a_abajo,
                        dirección.abajo_a_arriba,
                        dirección.diagonal
                       ]

    for palabra in verificando_lista_txt():

        # Exito al tomar el valor booleano, la matriz tomará el resultado de la matriz después de 
        # colocar la palabra, y boolean_matriz toma el resultado de la matriz ocupada
        dirección_aleatoria = lista_direcciones[random.randint(0, len(lista_direcciones)-1)]
        success, matriz, boolean_matriz = dirección_aleatoria(matriz, boolean_matriz, palabra)

        if not success:  # Si la palabra no encaja, el éxito será falso
            print(f"{palabra} no encajaba")
    print(crear_matriz.arreglar_matriz(matriz))  # Esto es lo que el usuario verá como resultado final

    def ejecución_del_juego():  # Desde aquí, el usuario empezara el juego.
        palabras_encontradas = []  # Lista vacía para almacenar cualquier palabra encontrada por el usuario
        while len(palabras_encontradas) < len(verificando_lista_txt()):
            debería_continuar = input("¿Quieres continuar? S o N: "). upper()  # Opción para finalizar el juego cada vez que se encuentra una palabra
            if debería_continuar == "N":
                print("¡Gracias por jugar! (っ ͡⚈ ᴗ ͡⚈)っ")
                break
            else:
                usuario_adivina = input("Ingrese la palabra que vio: ").lower()
                if usuario_adivina in palabras_encontradas: 
                    # Si la palabra ya está en palabras_encontradas, informe al usuario. no avanzará
                    # hasta que la palabra sea diferente
                    print(f"{usuario_adivina} ya fue encontrado")
                else:
                    if usuario_adivina in verificando_lista_txt(): # Si la palabra es diferente y está en un archivo txt con palabras, continúe
                        print(f"Encontraste el {usuario_adivina}!")
                        letra_encontrada_por_usuario = "" 
                        # Con esta lista, la función puede comparar la longitud de la palabra
                        # registrado en usuario_adivina con la longitud de esta lista. Esto permitirá que el siguiente tiempo
                        # el bucle se ejecuta hasta que letra_encontrada_por_usuario tenga la misma longitud que len(usuario_adivina)

                        while len(letra_encontrada_por_usuario) < len(usuario_adivina):
                            letra_encontrada = input("Ingresa la letra que encontraste: ").lower()
                            ubicación_fila = int(input("Introduzca el número de fila: ")) - 1
                            ubicación_columna = int(input("Ingrese el número de columna: ")) - 1
                            caracter_en_matriz = matriz[ubicación_fila][ubicación_columna] 
                            # Se accede a letra en la posición
                            # registrado en ubicación_fila y ubicación_columna
                            valor_en_boolean_matriz = boolean_matriz[ubicación_fila][ubicación_columna] 
                            # Se accede a la posición registrada en ubicación_fila y ubicación_columna
                            if letra_encontrada == caracter_en_matriz and valor_en_boolean_matriz:
                                print("La letra es correcta")
                                letra_encontrada_por_usuario += letra_encontrada
                                matriz[ubicación_fila][ubicación_columna] = letra_encontrada.upper()
                                print(crear_matriz.arreglar_matriz(matriz))
                            else:
                                print("La letra no es correcta")
                        palabras_encontradas.append(usuario_adivina)
                        print(f"Encontro una de las letras de la palbra {usuario_adivina}")
                    else:
                        print("Esta palabra no esta en la sopa de letras")
        if len(palabras_encontradas) == len(verificando_lista_txt()):
            print("Encontraste todas las palabras")
            for palabra_encontrada in verificando_lista_txt():
                print(palabra_encontrada)
        elif len(palabras_encontradas) < len(verificando_lista_txt()):
            print("Solo encontraste estas palabras")
            for palabra_encontrada in palabras_encontradas:
                print(palabra_encontrada)
        else:
            print("No se encontró ninguna palabra")
    ejecución_del_juego()

def verificando_lista_txt():
    # Extraer palabras del archivo txt
    with open("palabras.txt", "r") as f:
        return f.read().splitlines()

        ##################
        #Fin de Funciones
        ##################
        #Clases
        ##################

class Crear_Matriz: # Matriz que rellenara los espacios no ocupados con caracteres aleatorios 

    def __init__(self):
        self.matriz = []
        self.boolean_matriz = []

    def crear_matriz(self, filas, columnas):
        # matriz es donde se colocarán los caracteres aleatorios y lo que verán los usuarios
        # La matriz booleana es para identificar dónde
        # las palabras del archivo txt pueden tener lugar dependiendo de si el lugar está disponible (Verdadero) o no (Falso)

        for fila in range(filas):  # Iterando en filas de matriz
            # Aquí estamos agregando una nueva lista vacía a matriz y boolean_matriz:
            self.matriz.append([]), self.boolean_matriz.append([])

            # Iterando en columnas de matriz y matriz booleana
            for columna in range(columnas):

                # Generar caracteres aleatorios para columnas de matriz
                carácter_aleatorio = abc[random.randint(0, len(abc) - 1)] 

                # Acceso al número de fila donde se colocará un carácter aleatorio en cada
                self.matriz[fila].append(carácter_aleatorio) # columna. "?" debe reemplazarse por var carácter_aleatorio si se desea comprobar #####!#### debug

                # Acceso al número de fila donde se colocará un valor Falso en cada columna
                self.boolean_matriz[fila].append(False)

        return self.matriz, self.boolean_matriz

    def arreglar_matriz(self, matriz):
        filas = len(self.matriz)  # Acceso a filas en matriz
        columnas = len(self.matriz[0])  # Acceso a columnas en matriz
        matriz_arreglada = " "  # Cadena vacía para almacenar caracteres en matriz
        for fila in range(filas):
            for columna in range(columnas):
                # Acceda a cada fila en la matriz, luego acceda a cada columna donde
                # caracter(string) se encuentra
                matriz_arreglada += matriz[fila][columna] + "|"
                
                # Una vez que iteró sobre todas las columnas, agregue un salto 
                # de linea y vaya a la siguiente fila:
            matriz_arreglada += "\n "
        return matriz_arreglada

class Direcciones:

    def __init__(self, matriz, ocupado):
        self.ocupado = ocupado  # Obtener la matriz booleana creada en el archivo principal
        self.matriz = matriz  # Obtiene la matriz creada en el archivo principal
        self.filas = len(matriz)  # Acceso a las filas de la matriz
        self.columnas = len(matriz[0])  # Acceso a la primera lista en self.filas

    def check_if_available_columnas(self, ocupado, longitud_palabra, fila, columna):
        for letra in range(longitud_palabra):  
            # Para columnas, verifique cada letra en palabra
            # si los espacios no están ocupados (Falso) para sobrescribirlos en la matriz
            if ocupado[fila][columna]:
                return True
            elif columna >= longitud_palabra:
                return True
        return False

    def check_if_available_filas(self,ocupado, fila, columna, word_lenght): 
            # Para filas, verifique cada letra en palabra
            # si los espacios no están ocupados (False) para sobrescribirlos en la matriz
            for fila in range(word_lenght):
                if ocupado[fila][columna]:
                    return True
                elif fila >= word_lenght:
                    return True
            return False

    def izquierda_a_derecha(self, matriz, ocupado, palabra):  # Sobrescribir palabras de izquierda a derecha en la matriz
        random_index = random.randint(0, self.columnas - 2)  # Genera números aleatorios para colocar palabras al azar en la matriz

        def write_left_to_right(matriz, fila, columna, palabra): 
            # Obtiene el índice y la letra para sobrescribir espacios en la matriz en consecuencia
            for index, letra in enumerate(palabra):
                matriz[fila][columna + index] = letra
            return matriz

        for fila in range(self.filas):
            for columna in range(self.columnas):
                if not self.check_if_available_columnas(ocupado, len(palabra), fila+random_index, columna):  
                    # Siempre que check_if_available_columnas sea False, entonces puede continuar
                    matriz = write_left_to_right(matriz, fila+random_index, columna, palabra)
                    ocupado = write_left_to_right(ocupado, fila+random_index, columna, [True] * len(palabra))
                    return True, matriz, ocupado  # Si tiene éxito, devuelve True con matriz y boolean_matriz modificados
        return False, matriz, ocupado  # Si no tiene éxito, devuelve True con matriz y boolean_matriz modificados

    def derechar_a_izquierda(self, matriz, ocupado, palabra): # Sobrescribir palabras de derecha a izquierda en la matriz
        random_index = random.randint(0, self.columnas - 2) # Generates random number to place words randomly in matriz

        def write_right_to_left(matriz, fila, columna, palabra): # Genera números aleatorios para colocar palabras al azar en la matriz
            # accordingly
            for index, letra in enumerate(palabra):
                matriz[fila][columna + index] = letra
            return matriz

        reversed_word = palabra[::-1]
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if not self.check_if_available_columnas(ocupado, len(reversed_word), fila + random_index, columna):  
                    # Siempre que check_if_available_columnas sea False, entonces puede continuar
                    matriz = write_right_to_left(matriz, fila + random_index, columna, reversed_word)
                    ocupado = write_right_to_left(ocupado, fila + random_index, columna, [True] * len(palabra))
                    return True, matriz, ocupado # Si tiene éxito, devuelve True con matriz y boolean_matriz modificados
        return False, matriz, ocupado # Si no tiene éxito, devuelve True con matriz y boolean_matriz modificados

    def arriba_a_abajo(self, matriz, ocupado, palabra): # Sobrescribir palabras de arriba a abajo en la matriz
        random_index = random.randint(0, self.filas - 2) # Genera números aleatorios para colocar palabras al azar en la matriz

        def overwrite_top_to_bottom(matriz, palabra, fila, columna):  # Obtiene el índice y la letra para sobrescribir los espacios en la matriz
            for index, letra in enumerate(palabra):
                matriz[fila + index][columna] = letra
            return matriz

        for fila in range(self.filas):
            for columna in range(self.columnas):
                if not self.check_if_available_filas(ocupado, fila, columna + random_index, len(palabra)): 
                    # Siempre que check_if_available_columnas sea False, entonces puede continuar
                    matriz = overwrite_top_to_bottom(matriz, palabra, fila, columna + random_index)
                    ocupado = overwrite_top_to_bottom(ocupado, [True] * len(palabra), fila, columna + random_index)
                    return True, matriz, ocupado  # Si tiene éxito, devuelve True con matriz y boolean_matriz modificados
        return False, matriz, ocupado  # Si no tiene éxito, devuelve True con matriz y boolean_matriz modificados


    def abajo_a_arriba(self, matriz, ocupado, palabra): # Sobrescribir palabras de arriba a abajo en la matriz
        reversed_word = palabra[::-1]
        random_index = random.randint(0, self.filas - 2) # Genera números aleatorios para colocar palabras al azar en la matriz

        def overwrite_bottom_to_top(matriz, fila, columna, palabra): # Obtiene el índice y la letra para sobrescribir los espacios en la matriz
            for index, letra in enumerate(palabra):
                matriz[fila+index][columna] = letra
            return matriz

        for fila in range(self.filas):
            for columna in range(self.columnas):
                if not self.check_if_available_filas(ocupado, len(reversed_word), fila + random_index, columna): 
                    # Siempre que check_if_available_columnas sea False, entonces puede continuar
                    matriz = overwrite_bottom_to_top(matriz, fila + random_index, columna, reversed_word)
                    ocupado = overwrite_bottom_to_top(ocupado, fila + random_index, columna, [True] * len(reversed_word))
                    return True, matriz, ocupado # Si no tiene éxito, devuelve True con matriz y boolean_matriz modificados
        return False, matriz, ocupado

    def diagonal(self, matriz, ocupado, palabra):
        def verificar_si_esta_disponible(ocupado, longitud_palabra, fila, columna):
            for index, letra in enumerate(longitud_palabra):
                if ocupado[fila+index][columna+index]:
                    return True
                elif columna >= len(longitud_palabra):
                    return True
            return False

        def sobrescribir_diagonal(matriz, palabra, fila, columna):
            for index, letra in enumerate(palabra):
                matriz[fila+index][columna+index] = letra
            return matriz

        for fila in range(self.filas):
            for columna in range(self.columnas):
                if not verificar_si_esta_disponible(ocupado, palabra, fila, columna):
                    matriz = sobrescribir_diagonal(matriz, palabra, fila, columna)
                    ocupado = sobrescribir_diagonal(ocupado, [True] * len(palabra), fila, columna)
                    return True, matriz, ocupado
        return False, matriz, ocupado


        ##################
        #Fin de Clases
        ##################
        #Inicio de ejecución del programa
        ##################

if __name__ == '__main__':
    main()  # Llamar a la función principal "main"