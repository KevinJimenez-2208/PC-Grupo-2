import random
# Tablero

Zonas_Seguras = [5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63, 68] 

#  Clases principales 

class Ficha:
    def __init__(self, color):
        self.color = color
        self.posicion = -1  

    def mover(self, pasos):
        if self.posicion == -1:
            if pasos == 5:
                self.posicion = 0
                print(f"{self.color} sacó 5 y sacó ficha de casa.")
            else:
                print(f"{self.color} no puede sacar ficha (necesita 5).")
        else:
            self.posicion += pasos
            print(f"{self.color} avanzó a la casilla {self.posicion}.")

    def en_meta(self):
        return self.posicion >= 68 


class Jugador:
    def __init__(self, color):
        self.color = color
        self.fichas = [Ficha(color) for _ in range(4)]

    def mostrar_fichas(self):
        for i, ficha in enumerate(self.fichas):
            estado = "En casa" if ficha.posicion == -1 else f"En {ficha.posicion}"
            print(f"  Ficha {i+1}: {estado}")

    def capturar(self, ficha_mia, jugadores):
        if ficha_mia.posicion in Zonas_Seguras:
            return  # No puedes capturar si estás en zona segura

        for otro in jugadores:
            if otro != self:
                for ficha in otro.fichas:
                    if ficha.posicion == ficha_mia.posicion and ficha.posicion != -1:
                        print(f"¡{self.color} capturó una ficha de {otro.color}!")
                        ficha.posicion = -1  # Manda ficha a casa

    def ha_ganado(self):
        return all(f.en_meta() for f in self.fichas)

# Funciones de juego 

def tirar_dado():
    return random.randint(1, 6)

def turno_jugador(jugador):
    print(f"\nTurno de {jugador.color}")
    jugador.mostrar_fichas()
    input("Presiona ENTER para tirar el dado...")
    dado = tirar_dado()
    print(f"{jugador.color} sacó: {dado}")

    opciones = [i for i, f in enumerate(jugador.fichas)
                if f.posicion != -1 or dado == 5]

    if not opciones:
        print("No puedes mover ninguna ficha.")
        return

    print("Elige ficha a mover:")
    for fic in opciones:
        print(f"{fic+1}: Ficha {fic+1}")

    eleccion = int(input("Ficha a mover: ")) - 1
    jugador.fichas[eleccion].mover(dado)
    jugador.capturar(jugador.fichas[eleccion], jugadores)

# Bucle principal 

def main():
    jugadores = [Jugador("Rojo"), Jugador("Azul"), Jugador("Amarillo"), Jugador("Verde")]
    turno = 0

    while True:
        jugador = jugadores[turno % len(jugadores)]
        turno_jugador(jugador)

        if jugador.ha_ganado():
            print(f"\n¡El jugador {jugador.color} ha ganado!")
            break

        turno += 1


if __name__ == "__main__":
    main()