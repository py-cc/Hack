import math

def main():
    
    list_save = []
    salir = False
    while not salir:
        print("Ingrese el comando requerido para una operacion")
        print("1. Calcular la altura máxima del proyectil")
        print("2. Calcular la distancia máxima recorrida")
        print("3. Guardar los resultados en un archivo")
        print("0. EXIT")
    
        opcion = input()
        
        if opcion == "1": 
            list_save = calculo_proyectil()
        elif opcion == "2":
            list_save = calculo_distancia()
        elif opcion == "3":
            save(list_save)
        elif opcion == "0":
            salir = True


def calculo_proyectil():
    list_max = []
    print("Para realizar la siguiente operacion necesitamos")
    print("La velocidad incial (v0)")
    velocidad = input("Ingrese velocidad incial: ")
    velocidad = int(velocidad)
    h_max = (velocidad * velocidad) / (2 * 2)
    print("El resultado es: {}".format(h_max))
    list_max.append(velocidad)
    list_max.append(h_max)
    return list_max

def calculo_distancia():
    list_max = []
    print("Para realizar la siguiente operacion necesitamos")
    print("La velocidad inicial (v0)")
    velocidad = input("Ingrese velocidad incial: ")
    velocidad = int(velocidad)
    a = math.sin(velocidad*(math.pi)/180)
    x_max = (2 * velocidad) * a / 2
    list_max.append(velocidad)
    list_max.append(x_max)
    return list_max

def save(list_max):
    print(list_max)
    file = open("filesData.txt", "a")
    for element in list_max:
        text = element
        text = str(text)
        file.write(text + "\n")
    file.close()
    

if __name__ == "__main__":
        print("Bienvenidos al CLI")
        main()