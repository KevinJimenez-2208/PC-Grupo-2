import random

# Tablero
# Modificación del tablero para incluir 68 casillas y zonas seguras
casillas = [[] for _ in range(68)]  # 68 casillas vacías al inicio

Zonas_Seguras = [5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63]  # se eliminó 68 que está fuera de rango

# Clases principales
class Ficha:
    def __init__(self, color):
        self.color = color
        self.posicion = -1  # La ficha empieza en la cárcel

    def mover(self, pasos):
        global casillas

        if self.posicion == -1:
            if pasos == 5:
                self.posicion = 0
                casillas[self.posicion].append(self)
                print(f"{self.color} sacó 5 y sacó ficha de casa.")
            else:
                print(f"{self.color} no puede sacar ficha (necesita 5).")
            return
        else:
            nueva_posicion = self.posicion + pasos
            if nueva_posicion >= 68:
                print(f"{self.color} no puede moverse porque pasaría la meta.")
                return

            # Verificar bloqueos en el camino
            for paso in range(self.posicion + 1, nueva_posicion + 1):
                if verificar_bloqueo(paso):
                    print(f"{self.color} no puede avanzar porque hay un bloqueo en la casilla {paso}.")
                    return

            # Mover ficha
            casillas[self.posicion].remove(self)
            self.posicion = nueva_posicion
            casillas[self.posicion].append(self)
            print(f"{self.color} avanzó a la casilla {self.posicion}.")

        # Después de mover:
        if self.en_meta():
            print(f"¡{self.color} llegó a la meta! Avanza 10 pasos extra.")
            self.mover(10)

    def en_meta(self):
        return self.posicion == 67  # La casilla 67 es la última


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
                        ficha_mia.mover(20)  # BONUS de 20 pasos
                        return  # Solo se captura una ficha por turno

    def ha_ganado(self):
        return all(f.en_meta() for f in self.fichas)


# Funciones de juego
def tirar_dado():
    return random.randint(1, 6)


def verificar_bloqueo(posicion):
    if posicion < 0 or posicion >= 68:
        return False
    return len(casillas[posicion]) >= 2


def turno_jugador(jugador, jugadores, pares_seguidos, ultima_ficha_movida):  # Se pasan variables necesarias
    print(f"\nTurno de {jugador.color}")
    jugador.mostrar_fichas()
    input("Presiona ENTER para tirar el dado...")
    dado = tirar_dado()
    print(f"{jugador.color} sacó: {dado}")

    if dado % 2 == 0:
        pares_seguidos[jugador.color] += 1
    else:
        pares_seguidos[jugador.color] = 0

    opciones = [i for i, f in enumerate(jugador.fichas)
                if f.posicion != -1 or dado == 5]

    if not opciones:
        print("No puedes mover ninguna ficha.")
        return False  # No repite turno

    print("Elige ficha a mover:")
    for fic in opciones:
        print(f"{fic+1}: Ficha {fic+1}")

    eleccion = int(input("Ficha a mover: ")) - 1
    jugador.fichas[eleccion].mover(dado)
    ultima_ficha_movida[jugador.color] = jugador.fichas[eleccion]
    jugador.capturar(jugador.fichas[eleccion], jugadores)

    # Penalización por 3 pares seguidos
    if pares_seguidos[jugador.color] >= 3:
        print(f"{jugador.color} sacó tres pares seguidos. Su última ficha movida regresa a la casa.")
        ficha_penalizada = ultima_ficha_movida[jugador.color]
        if ficha_penalizada:
            casillas[ficha_penalizada.posicion].remove(ficha_penalizada)
            ficha_penalizada.posicion = -1
        pares_seguidos[jugador.color] = 0

    return dado % 2 == 0  # Repite turno si fue par


# Bucle principal
def main():
    jugadores = [Jugador("Rojo"), Jugador("Azul"), Jugador("Amarillo"), Jugador("Verde")]
    turno = 0
    pares_seguidos = {jug.color: 0 for jug in jugadores}  # lleva la cuenta por jugador para saber si van 3 pares
    ultima_ficha_movida = {jug.color: None for jug in jugadores}

    while True:
        jugador = jugadores[turno % len(jugadores)]
        repetir_turno = turno_jugador(jugador, jugadores, pares_seguidos, ultima_ficha_movida)

        if jugador.ha_ganado():
            print(f"\n¡El jugador {jugador.color} ha ganado!")
            break

        if not repetir_turno:
            turno += 1


if __name__ == "__main__":
    main()

    # Estado actual
    # Se añadió la lista de casillas para definir en qué casilla va cada ficha
    # 1. Solo se saca ficha si sale 5
    # 2. Las fichas pueden ser capturadas
    # 3. Deberían respetarse las zonas seguras (no comprobado)
    # 4. Bloqueos en el tablero (no comprobado)
    # 5. Condiciones de victoria
    # 6. Se añadió el bonus de 20 pasos en la línea 68
    # 7. Se añade bonus 10 pasos dentro de def mover(self, pasos) para llegada a la meta
    # 8. Se añade penalización por 3 pares seguidos


