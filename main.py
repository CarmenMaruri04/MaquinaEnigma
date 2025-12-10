def main(): #Menu principal
    archivos_rueda = ["Rotor1.txt", "Rotor2.txt", "Rotor3.txt"] #3txt creados (1, 2, 3)
    configuraciones_ejemplo = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ\nG",  #Rotor 1 
        "AJDKSIRUXBLHWTMCQGZNPYFVOE\nL",  #Rotor 2 
        "BDFHJLCPRTXVZNYEIWGAKMUSQO\nC"   #Rotor 3 
    ]
    
    for i, archivo in enumerate(archivos_rueda):
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
                a=1
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