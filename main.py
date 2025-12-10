
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

def main(): #Menu principal
    archivos_rotor = ["Rotor1.txt", "Rotor2.txt", "Rotor3.txt"] #3txt creados (1, 2, 3)
    configuraciones_ejemplo = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ\nG",  #Rotor 1 
        "AJDKSIRUXBLHWTMCQGZNPYFVOE\nL",  #Rotor 2 
        "BDFHJLCPRTXVZNYEIWGAKMUSQO\nC"   #Rotor 3 
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
        print("1. Xifrar missatge")
        print("2. Desxifrar missatge")
        print("3. Editar rotors")
        print("4. Sortir")
        opcion = input("> ")#Pongo esto q al profe le gusto :)
        print("")
        
        if opcion == "1":
            try: #Falta opcion 1 de cifrar un mensaje dado por el user :)
                 r1 = leer_rotor("Rotor1.txt")
                 r2 = leer_rotor("Rotor2.txt")
                 r3 = leer_rotor("Rotor3.txt")
                 ruedas = [r1, r2, r3]  # Orden: [derecho, medio, izquierdo]
                 clave = input("Posiciones iniciales (3 letras, ej ABC): ").upper()
                 if len(clave) != 3 or not all(letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letra in clave):
                     print("Error! La clave debe tener 3 letras (ej: ABC)")
                     print()
                     continue

            except Exception as e:#Si algo no funciona en vez de que se rompa pues sale esto:
                print(f"Error! Algo salio mal: {e}")
                print("")
            
        elif opcion == "2":
            try: #Falta opcion 2 de descifrar el mensaje dado por el user :)
                a=1
            except Exception as e:#Mas de lo mismo, si se rompe sale esto:
                print(f"Error! Algo salio mal durante el descifrado: {e}")
                print("")
                
        elif opcion == "3":#Falta opcion 3 de poder escoger el rotor y luego editarlo :)
            a=1

        elif opcion == "4": #Terminado (se sale del menu y del programa)
            print("Saliendo...")
            break
            
        else:#Por si pone otra letra o numero
            print("Opcion no valida. Por favor elige 1, 2, 3 o 4")
            print("")

main()