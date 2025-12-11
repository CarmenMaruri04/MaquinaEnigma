
def leer_rotor(nombre_archivo): #Funcion para leer rotor desde un archivo
    try: #Try por si no encuentra el archivo
        with open(nombre_archivo, "r") as f:
            lineas = f.readlines()
        conexiones = lineas[0].strip().upper() 
        punto_avance = "Z"  #Z es el valor por defecto
        if len(lineas) > 1:
            punto_avance = lineas[1].strip().upper()
        return conexiones, punto_avance
    except FileNotFoundError: #Error por si no encuentra el archivo
        print(f"Error: Archivo {nombre_archivo} no encontrado")
        #Si no hay archivo, cada letra se transforma en ella misma (mapeo)
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Z"


def cifrar_letra(letra, mapeo, posicion):#Funcion para cifrar letra
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indice = (abecedario.index(letra) + posicion) % 26 #Mira que numero es la letra
    letra_cifrada = mapeo[indice] #Cifra usando el mapeo del rotor
    indice_salida = (abecedario.index(letra_cifrada) - posicion) % 26 #Se converte de vuelta a la posicion normal
    return abecedario[indice_salida]


def descifrar_letra(letra, mapeo, posicion): #Funcion para descifrar la letra 
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indice = (abecedario.index(letra) + posicion) % 26
    inverso = [""] * 26  #Realizar el mapeo inverso (es decir, si A->E, entonces E->A  ^^)
    for i in range(26):
        inverso[abecedario.index(mapeo[i])] = abecedario[i]
    mapeo_inverso = "".join(inverso) 
    letra_cifrada = mapeo_inverso[indice]
    indice_salida = (abecedario.index(letra_cifrada) - posicion) % 26
    return abecedario[indice_salida]


def mover_rotores(posiciones_actuales, rotores): #Mueve los rotores
    posiciones_actuales[0] = (posiciones_actuales[0] + 1) % 26 #Rotor 1 avanza 1 posicion
    if rotores[0][1] == "Z": #Si es Z no se mueve a los otros rotores :3
        return posiciones_actuales
    if chr(posiciones_actuales[0] + 65) == rotores[0][1]: #Cunado rotor1 llega mueve rotor2
        posiciones_actuales[1] = (posiciones_actuales[1] + 1) % 26
        if chr(posiciones_actuales[1] + 65) == rotores[1][1]: #Cuando rotor2 llega mueve rotor3
            posiciones_actuales[2] = (posiciones_actuales[2] + 1) % 26
    return posiciones_actuales


def formatear_grupos(texto): #Divide el texto de 5 en 5
    resultado = ""
    for i in range(0, len(texto), 5): #Del texto se separan cada 5 letras
        if i > 0:
            resultado += " "
        resultado += texto[i:i+5]
    return resultado


def cifrar_texto(texto, rotores, posiciones_iniciales): #Funcion para cifrar el texto ^^
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    posiciones = posiciones_iniciales.copy() #Se hace una copia para no perder las posiciones iniciales
    for letra in texto:
        if letra in abecedario:
            posiciones = mover_rotores(posiciones, rotores) #Se mueven los rotores antes de cifrar la letra
            x = cifrar_letra(letra, rotores[0][0], posiciones[0])  #Rotor1
            x = cifrar_letra(x, rotores[1][0], posiciones[1])      #Rotor2
            x = cifrar_letra(x, rotores[2][0], posiciones[2])      #Rotor3
            resultado += x
    return resultado


def descifrar_texto(texto, rotores, posiciones_iniciales): #Funcion para descifrar el texto :)
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    posiciones = posiciones_iniciales.copy() #Copia las posiciones para no modificar las iniciales
    texto_sin_espacios = "" #Modifica el texto quitando los espacios
    for c in texto:
        if c in abecedario:
            texto_sin_espacios += c
    for letra in texto_sin_espacios:
        posiciones = mover_rotores(posiciones, rotores) #Se mueve el rotor para despues descifrar la letra (por lo tanto del 3 al 1)
        x = descifrar_letra(letra, rotores[2][0], posiciones[2])  #Rotor3 
        x = descifrar_letra(x, rotores[1][0], posiciones[1])      #Rotor2 
        x = descifrar_letra(x, rotores[0][0], posiciones[0])      #Rotor1 
        resultado += x
    return resultado


def editar_rotores():
    print("\n---- EDITAR ROTORES ----")
    while True:
        print("Que rotor quieres editar?")
        print("1. Rotor 1")
        print("2. Rotor 2")
        print("3. Rotor 3")
        print("4. Volver al menu")
        op = input("> ").strip()
        if op == "4":
            return
        if op not in ["1", "2", "3"]: #Por si el usuario pone un numero o letra que no es
            print("Opcion no valida")
            continue
        num_rotor = int(op)
        archivo = f"Rotor{num_rotor}.txt"
        print(f"\nConfiguracion actual de {archivo}:") #Muestra configuracion actual
        try:
            with open(archivo, "r") as f:
                contenido = f.read()
                print(contenido)
        except:
            print("Archivo no existe o no se puede leer") #Por si hay algun error
        print("\n---- Nueva configuracion ----")
        while True:
            cableado = input("Cableado (26 letras A-Z sin repetir): ").upper().strip() #Se pide la nueva configuracion de letras
            if len(cableado) != 26:
                print("ERROR: Debe tener 26 letras")
                continue
            ok = True
            letras_vistas = []
            for c in cableado:
                if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": #Por si el usuario pone una letra que no es o alguna otra cosa
                    print(f"ERROR: '{c}' no es una letra valida") 
                    ok = False
                    break
                if c in letras_vistas:
                    print(f"ERROR: La letra '{c}' esta repetida")
                    ok = False
                    break
                letras_vistas.append(c)
            if ok:
                break
        while True:
            notch = input("Notch (1 letra A-Z): ").upper().strip() #Pide la letra para el rotor
            if len(notch) == 1 and notch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                break
            print("ERROR: Debe ser una sola letra A-Z")
        try:
            with open(archivo, "w") as f: #Para guardar la nueva configuracion
                f.write(cableado + "\n")
                f.write(notch + "\n")
            print(f"Rotor {num_rotor} actualizado correctamente")
        except:
            print(f"Error guardando {archivo}")


def main(): #Menu principal
    archivos_rotor = ["Rotor1.txt", "Rotor2.txt", "Rotor3.txt"] #3txt creados (1, 2, 3)
    configuraciones_ejemplo = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ\nG",  #Rotor1 
        "AJDKSIRUXBLHWTMCQGZNPYFVOE\nL",  #Rotor2 
        "BDFHJLCPRTXVZNYEIWGAKMUSQO\nC"   #Rotor3 
    ]
    for i, archivo in enumerate(archivos_rotor):
        try: #Por si los rotores fallan
            with open(archivo, "r") as f:
                pass  #Verifica que existe
        except FileNotFoundError:#Se crear un nuevo rotor por si no existen
            with open(archivo, "w") as f:
                f.write(configuraciones_ejemplo[i])
            print(f"Creado archivo {archivo} con configuracion por defecto")
    while True: #Lo primero que se ve
         print("\n---- ENIGMA ----")
         print("1. Cifrar mensaje")
         print("2. Descifrar mensaje")
         print("3. Editar rotores")
         print("4. Salir")
         opcion = input("> ")#Pongo esto q al profe le gusto :)
         print("")
         if opcion == "1":
             try: 
                 r1 = leer_rotor("Rotor1.txt")
                 r2 = leer_rotor("Rotor2.txt")
                 r3 = leer_rotor("Rotor3.txt")
                 rotores = [r1, r2, r3]  #Rotores del 1 al 3
                 clave = input("Posiciones iniciales (3 letras, ej ABC): ").upper()
                 if len(clave) != 3 or not all(letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letra in clave):
                     print("Error! La clave debe tener 3 letras (ej: ABC)")
                     print()
                     continue   
                 posiciones = [ord(clave[0]) - 65, ord(clave[1]) - 65, ord(clave[2]) - 65] #Convierte letras a numeros
                 mensaje = input("Escribe tu mensaje: ").upper()
                 if not mensaje:
                     print("Error! El mensaje no puede estar vacio")
                     print()
                     continue
                 mensaje_limpio = ''.join(c for c in mensaje if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") #Solo usa letras de la A a la Z (ignora espacios y otros)
                 if not mensaje_limpio:
                     print("Error! El mensaje debe contener al menos una letra A-Z")
                     print()
                     continue
                 print(f"Mensaje a cifrar: {mensaje_limpio}")
                 print(f"Posiciones usadas: {clave}")
                 print()
                 mensaje_secreto = cifrar_texto(mensaje_limpio, rotores, posiciones)
                 mensaje_formateado = formatear_grupos(mensaje_secreto) #Se formatea en grupos de 5
                 with open("xifrat.txt", "w") as f:  #Guarda el mensaje
                     f.write(mensaje_formateado)
                 num_letras = len(mensaje_secreto)
                 num_grupos = (num_letras + 4) // 5
                 print(f"[OK] Mensaje descifrado en 'xifrat.txt' ({num_letras} letras, {num_grupos} grups de 5)")
                 print(f"Text xifrat: {mensaje_formateado}")
                 print()
             except Exception as e: #Si algo no funciona en vez de que se rompa pues sale esto:
                 print(f"Error. Algo salio mal: {e}")
                 print()
         elif opcion == "2":
             try:
                 r1 = leer_rotor("Rotor1.txt")
                 r2 = leer_rotor("Rotor2.txt")
                 r3 = leer_rotor("Rotor3.txt")
                 rotores = [r1, r2, r3]  #Rotores del 1 al 3
                 clave = input("Posiciones iniciales (mismas que al cifrar, ej ABC): ").upper() #Se pide la clave para poder descifrar el mensaje
                 if len(clave) != 3 or not all(letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letra in clave):
                     print("Error! La clave debe tener 3 letras (ej: ABC)")
                     print()
                     continue
                 posiciones = [ord(clave[0]) - 65, ord(clave[1]) - 65, ord(clave[2]) - 65]
                 try: #Con la existencia del txt
                     with open("xifrat.txt", "r") as f:
                         texto_secreto = f.read().strip()
                     if not texto_secreto:
                         print("Error! El archivo esta vacio")
                         print()
                         continue
                     print(f"Texto xifrat: {texto_secreto}")
                     print(f"Posiciones usadas: {clave}")
                     print()
                     mensaje_normal = descifrar_texto(texto_secreto, rotores, posiciones) #Descifra el mensaje
                     with open("desxifrat.txt", "w") as f:
                         f.write(mensaje_normal) #Guarda el mensaje normal
                     print(f"[OK] Mensaje descifrado en 'desxifrat.txt'")
                     print(f"Text descifrado: {mensaje_normal}")
                     print()
                 except FileNotFoundError:
                     print("Error! Archivo xifrat.txt no encontrado")
                     print("Primero debes cifrar un mensaje (opcion 1)")
                     print()
             except Exception as e: #Mas de lo mismo, si se rompe sale esto:
                 print(f"Error! Algo salio mal durante el descifrado: {e}")
                 print("")
                
         elif opcion == "3": #Opcion de editar los rotores
             editar_rotores()

         elif opcion == "4": #Terminado (se sale del menu)
             print("Saliendo...")
             break
            
         else: #Por si pone otra letra o numero
             print("Opcion no valida. Por favor elige 1, 2, 3 o 4")
             print("")

main()