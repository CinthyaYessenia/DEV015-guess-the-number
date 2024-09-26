import random  # Importa el módulo random para generar números aleatorios.

# Clase Player que representa a una jugadora
class Player:
    def __init__(self, name):
        """Inicializa a la jugadora con su nombre y una lista de suposiciones."""
        self.name = name  # Asigna el nombre de la jugadora.
        self.guesses = []  # Inicializa una lista vacía para almacenar sus suposiciones.

    def make_guess(self):
        """Solicita a la jugadora que ingrese un número como su suposición."""
        while True:  # Bucle infinito para pedir suposiciones hasta que se introduzca un número válido.
            try:
                # Pide a la jugadora que adivine un número entre 1 y 100.
                guess = int(input(f"{self.name}, adivina un número entre 1 y 100: "))
                if 1 <= guess <= 100:  # Verifica si el número está en el rango permitido.
                    self.guesses.append(guess)  # Añade la suposición a la lista de suposiciones.
                    return guess  # Devuelve la suposición válida.
                else:
                    print("Por favor, introduce un número entre 1 y 100.")  # Mensaje si el número no está en el rango.
            except ValueError:
                # Maneja el error si el usuario no introduce un número entero.
                print("Entrada no válida. Por favor, introduce un número.")

# Subclase ComputerPlayer que hereda de Player y representa al ordenador
class ComputerPlayer(Player):
    def __init__(self, name="Ordenador"):
        """Inicializa al ordenador con su nombre, un rango de valores y una lista de suposiciones."""
        super().__init__(name)  # Llama al constructor de la clase base Player.
        self.min_valor = 1  # Rango mínimo de suposiciones del ordenador.
        self.max_valor = 100  # Rango máximo de suposiciones del ordenador.

    def make_guess(self):
        """El ordenador hace una suposición basada en el rango ajustado."""
        guess = random.randint(self.min_valor, self.max_valor)  # Genera un número aleatorio en el rango actual.
        self.guesses.append(guess)  # Añade la suposición del ordenador a su lista de suposiciones.
        print(f"{self.name} adivinó: {guess}")  # Muestra la suposición del ordenador.
        return guess  # Devuelve la suposición.

# Clase Game que representa el juego de adivinanzas
class Game:
    def __init__(self):
        """Inicializa el juego con una jugadora, un ordenador y un número secreto."""
        self.player = Player("Jugadora")  # Crea una instancia de la clase Player (jugadora humana).
        self.computer = ComputerPlayer()  # Crea una instancia de la clase ComputerPlayer (ordenador).
        self.secret_number = random.randint(1, 100)  # Genera el número secreto aleatorio que ambos deben adivinar.
        self.turn = "player"  # Define quién tiene el turno inicial (jugadora).

    def check_guess(self, guess):
        """Verifica si la suposición es correcta y ajusta el rango del ordenador."""
        if guess == self.secret_number:  # Si la suposición es correcta.
            return True  # Retorna True si se adivinó el número secreto.
        elif guess < self.secret_number:  # Si la suposición es menor que el número secreto.
            print("El número secreto es mayor.")  # Mensaje de pista.
            if self.turn == "computer":  # Si es el turno del ordenador.
                self.computer.min_valor = guess + 1  # Ajusta el valor mínimo para las futuras suposiciones del ordenador.
        else:  # Si la suposición es mayor que el número secreto.
            print("El número secreto es menor.")  # Mensaje de pista.
            if self.turn == "computer":  # Si es el turno del ordenador.
                self.computer.max_valor = guess - 1  # Ajusta el valor máximo para las futuras suposiciones del ordenador.
        return False  # Retorna False si la suposición no es correcta.

    def play_turn(self):
        """Juega un turno alternando entre la jugadora y el ordenador."""
        if self.turn == "player":  # Si es el turno de la jugadora.
            guess = self.player.make_guess()  # La jugadora hace una suposición.
            if self.check_guess(guess):  # Verifica si la suposición es correcta.
                return f"¡Correcto! {self.player.name} adivinó el número secreto {self.secret_number}."  # Mensaje de victoria de la jugadora.
            self.turn = "computer"  # Cambia el turno al ordenador.
        else:  # Si es el turno del ordenador.
            guess = self.computer.make_guess()  # El ordenador hace una suposición.
            if self.check_guess(guess):  # Verifica si la suposición es correcta.
                return f"¡Correcto! {self.computer.name} adivinó el número secreto {self.secret_number}."  # Mensaje de victoria del ordenador.
            self.turn = "player"  # Cambia el turno a la jugadora.
        return None  # Retorna None si nadie ha adivinado el número aún.

    def start(self):
        """Inicia el juego hasta que alguien adivine el número secreto."""
        print("¡Bienvenida al juego de adivinanzas!")  # Mensaje de bienvenida.
        while True:  # Bucle del juego que se repite hasta que alguien gane.
            result = self.play_turn()  # Juega un turno y verifica si hay un ganador.
            if result:  # Si alguien adivinó el número secreto.
                print(result)  # Muestra el mensaje de victoria.
                break  # Termina el juego.
        # Muestra todas las suposiciones realizadas por la jugadora y el ordenador.
        print(f"Las suposiciones de {self.player.name}: {self.player.guesses}")
        print(f"Las suposiciones de {self.computer.name}: {self.computer.guesses}")

# Inicia el juego si este archivo se ejecuta directamente
if __name__ == "__main__":
    game = Game()  # Crea una instancia del juego.
    game.start()  # Inicia el juego.
