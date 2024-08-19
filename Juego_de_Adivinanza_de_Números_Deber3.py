import random

rango_min = 1
rango_max = 100
intentos_max = 5

def configurar_juego():
    global rango_min, rango_max, intentos_max
    try:
        rango_min = int(input("Ingresa el valor mínimo del rango: "))
        rango_max = int(input("Ingresa el valor máximo del rango: "))
        if rango_min >= rango_max:
            raise ValueError("El valor mínimo debe ser menor que el valor máximo.")
        
        intentos_max = int(input("Ingresa el número máximo de intentos: "))
        if intentos_max <= 0:
            raise ValueError("El número máximo de intentos debe ser positivo.")
    except ValueError as e:
        print(f"Entrada inválida: {e}. Por favor, intenta de nuevo.")
        configurar_juego()

def pedir_adivinanza():
    try:
        return int(input(f"Adivina el número (entre {rango_min} y {rango_max}): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return pedir_adivinanza()

def juego_adivinanza():
    numero_secreto = random.randint(rango_min, rango_max)
    intentos = 0
    while intentos < intentos_max:  
        adivinanza = pedir_adivinanza()
        intentos += 1
        
        if adivinanza < numero_secreto:  
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
    else:
        print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")

def main():
    configurar_juego()  
    juego_adivinanza()  

main()