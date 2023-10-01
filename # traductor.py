# traductor.py
def agregar_traduccion():
    with open("EN-ES.txt", "a") as archivo:
        codigo_origen = input("Ingrese el código de origen (en): ")
        codigo_destino = input("Ingrese el código de destino (es): ")
        palabra = input("Ingrese la palabra a traducir: ")
        archivo.write(f"{codigo_origen},{codigo_destino},{palabra}\n")
def traducir():
    palabra_a_traducir = input("Ingrese la palabra:")
    with open("EN-ES.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            codigo_origen, codigo_destino, palabra = linea.strip().split(',')
            if palabra == palabra_a_traducir:
                print(f"Traducción: {codigo_origen} -> {codigo_destino} -> {palabra}")
                return
        print("La palabra no se encuentra en el diccionario.")
def main():
    while True:
        print("Opciones:")
        print("1. Agregar nueva traducción")
        print("2. Traducir palabra")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_traduccion()
        elif opcion == "2":
            traducir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")