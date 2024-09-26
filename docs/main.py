import random  # Importa el módulo random, que se usará para generar números aleatorios.

def generar_numero_secreto():
    """Genera un número aleatorio entre 1 y 100."""
    return random.randint(1, 100)  # Retorna un número entero aleatorio entre 1 y 100.

def obtener_adivinanza_jugadora():
    """Solicita a la jugadora una suposición."""
    while True:  # Inicia un ciclo que se repite hasta que la jugadora ingrese un valor válido.
        try:
            print("Turno de la jugadora")
            adivinanza = int(input("Adivina un número entre 1 y 100: "))  # Pide un número y lo convierte en entero para almacenarlo en una variable "adivinanza"
            if 1 <= adivinanza <= 100:  # Verifica que el número esté entre 1 y 100.
                return adivinanza  # Si es válido, lo retorna.
            else:
                print("Por favor, introduce un número entre 1 y 100.")  # Si está fuera del rango, muestra un mensaje de error.
        except ValueError:  # Captura cualquier error que ocurra si la jugadora ingresa algo que no sea un número.
            print("Entrada no válida. Por favor, introduce un número.")  # Muestra un mensaje si el input no es un número válido.

def adivinanza_ordenador_binaria(min_valor, max_valor):
    """Genera una suposición optimizada por parte del ordenador usando búsqueda binaria."""
    return (min_valor + max_valor) // 2  # Calcula el número medio entre min_valor y max_valor, dividiendo el rango por la mitad.

def turno_jugador(numero_secreto, adivinanzas_jugadora):
    """Lógica del turno de la jugadora y registro de su suposición."""
    adivinanza = obtener_adivinanza_jugadora()  # Obtiene la suposición de la jugadora.
    adivinanzas_jugadora.append(adivinanza)  # Guarda la suposición de la jugadora en la lista.
    if adivinanza == numero_secreto:  # Si la suposición es correcta:
        print(f"¡Correcto! La jugadora adivinó el número secreto {numero_secreto}.")  # Informa que la jugadora ganó.
        return True  # Retorna True, lo que indica que ha ganado.
    elif adivinanza < numero_secreto:  # Si la suposición es menor que el número secreto:
        print("El número secreto es mayor.")  # Informa que el número secreto es mayor.
    else:  # Si la suposición es mayor que el número secreto:
        print("El número secreto es menor.")  # Informa que el número secreto es menor.
    return False  # Retorna False si no ha acertado.

def turno_ordenador_inteligente(numero_secreto, min_valor, max_valor, adivinanzas_ordenador):
    """Lógica del turno del ordenador usando búsqueda binaria y registro de su suposición."""
    adivinanza = adivinanza_ordenador_binaria(min_valor, max_valor)  # El ordenador hace su suposición con la estrategia de búsqueda binaria.
    print("Turno del ordenador")
    print(f"El ordenador adivinó: {adivinanza}")  # Muestra la suposición del ordenador.
    adivinanzas_ordenador.append(adivinanza)  # Guarda la suposición del ordenador en la lista.
    if adivinanza == numero_secreto:  # Si la suposición es correcta:
        print(f"¡Correcto! El ordenador adivinó el número secreto {numero_secreto}.")  # Informa que el ordenador ganó.
        return True, min_valor, max_valor  # Retorna True y los valores actuales de min_valor y max_valor.
    elif adivinanza < numero_secreto:  # Si la suposición es menor que el número secreto:
        print("El número secreto es mayor.")  # Informa que el número secreto es mayor.
        print("------------------------------------------")
        min_valor = adivinanza + 1  # Ajusta el valor mínimo para reducir el rango.
    else:  # Si la suposición es mayor que el número secreto:
        print("El número secreto es menor.")  # Informa que el número secreto es menor.
        print("------------------------------------------")
        max_valor = adivinanza - 1  # Ajusta el valor máximo para reducir el rango.
    return False, min_valor, max_valor  # Retorna False si no ha acertado, junto con los nuevos valores de min_valor y max_valor.

def mostrar_suposiciones(ganador, suposiciones):
    """Muestra las suposiciones realizadas por el ganador."""
    print(f"Las suposiciones realizadas por {ganador} fueron: {suposiciones}")  # Muestra todas las suposiciones que hizo el ganador.

def jugar():
    """Función principal para ejecutar el juego."""
    numero_secreto = generar_numero_secreto()  # Genera el número secreto al inicio del juego.
    print("¡Bienvenida al juego de adivinanzas!")
    print("------------------------------------")
    
    turno = "jugadora"  # Define que la jugadora empieza el juego.
    adivinanzas_jugadora = []  # Lista para almacenar las suposiciones de la jugadora.
    adivinanzas_ordenador = []  # Lista para almacenar las suposiciones del ordenador.
    min_valor = 1  # Valor mínimo inicial para las suposiciones del ordenador.
    max_valor = 100  # Valor máximo inicial para las suposiciones del ordenador.
    ganador = None  # Variable para almacenar al ganador del juego.
    
    # El ciclo continúa hasta que haya un ganador.
    while not ganador:
        if turno == "jugadora":  # Si es el turno de la jugadora:
            if turno_jugador(numero_secreto, adivinanzas_jugadora):  # Llama a la función que maneja el turno de la jugadora.
                ganador = "jugadora"  # Si la jugadora acierta, se define como ganadora.
                mostrar_suposiciones(ganador, adivinanzas_jugadora)  # Muestra las suposiciones de la jugadora.
            else:
                turno = "ordenador"  # Si no acierta, pasa el turno al ordenador.
        else:  # Si es el turno del ordenador:
            acierto, min_valor, max_valor = turno_ordenador_inteligente(numero_secreto, min_valor, max_valor, adivinanzas_ordenador)  # Llama a la función que maneja el turno del ordenador.
            if acierto:  # Si el ordenador acierta:
                ganador = "ordenador"  # Define al ordenador como ganador.
                mostrar_suposiciones(ganador, adivinanzas_ordenador)  # Muestra las suposiciones del ordenador.
            else:
                turno = "jugadora"  # Si no acierta, pasa el turno a la jugadora.
    
    print(f"¡El juego ha terminado! El ganador es {ganador}.")  # Informa el final del juego y quién ganó.

def jugar_de_nuevo():
    """Ofrece la opción de jugar nuevamente después de que el juego termine."""
    while True:  # Ciclo que se repite hasta que el jugador decida dejar de jugar.
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()  # Pregunta si quiere jugar de nuevo.
        if respuesta == "s":  # Si la respuesta es "s" (sí):
            jugar()  # Llama a la función jugar nuevamente.
        elif respuesta == "n":  # Si la respuesta es "n" (no):
            print("¡Gracias por jugar!")  # Agradece por jugar.
            break  # Sale del ciclo.
        else:
            print("Por favor, responde con 's' para sí o 'n' para no.")  # Si la respuesta es inválida, pide una respuesta correcta.

if __name__ == "__main__":
    jugar()  # Inicia el juego por primera vez.
    jugar_de_nuevo()  # Llama a la función para preguntar si quiere jugar de nuevo.
