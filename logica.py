import random

CAMINO_META = {
    "Rojo": [68, 69, 70, 71, 72, 73],      
    "Azul": [74, 75, 76, 77, 78, 79],
    "Amarillo": [80, 81, 82, 83, 84, 85],
    "Verde": [86, 87, 88, 89, 90, 91]
}

casillas = [[] for _ in range(92)]

Zonas_Seguras = [5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63]


# Puntos de inicio para cada color
PUNTOS_INICIO = {"Rojo": 0, "Azul": 17, "Amarillo": 34, "Verde": 51}
jugadores_global = []

def obtener_jugador_por_color(color):
    for jugador in jugadores_global:
        if jugador.color == color:
            return jugador
    return None


class Ficha:
    def __init__(self, color, punto_inicio):
        self.color = color
        self.punto_inicio = punto_inicio
        self.posicion = -1  # En la cárcel

    def mover(self, pasos):
        global casillas

        if self.posicion == -1:
            if pasos == 5:
                self.posicion = self.punto_inicio
                casillas[self.posicion].append(self)
                print(f"{self.color} sacó 5 y sacó ficha de casa en la casilla {self.punto_inicio}.")
            else:
                print(f"{self.color} no puede sacar ficha (necesita 5).")
            return
        else:
            nueva_posicion = self.posicion + pasos

            if nueva_posicion < CAMINO_META[self.color][0]:
                pass
            else:
                pasos_restantes = nueva_posicion - CAMINO_META[self.color][0]
                nueva_posicion = CAMINO_META[self.color][0] + pasos_restantes
                if nueva_posicion > CAMINO_META[self.color][-1]:
                    print(f"{self.color} no puede moverse porque pasaría la meta")
                    return

            casillas[self.posicion].remove(self)
            self.posicion = nueva_posicion
            casillas[self.posicion].append(self)
            print(f"{self.color} avanzó a la casilla {self.posicion}.")

            if self.en_meta():
                print(f"¡{self.color} llegó a la meta! Avanza 10 pasos extra.")

                if pasos != 10:
                    jugador = obtener_jugador_por_color(self.color)
                    # Busca otra ficha que no esté en meta ni en la cárcel
                    for otra_ficha in jugador.fichas:
                        if otra_ficha != self and otra_ficha.posicion != -1 and not otra_ficha.en_meta():
                            print(f"Bonus: {self.color} mueve 10 pasos extra con otra ficha.")
                            otra_ficha.mover(10)
                            break


    def en_meta(self):
        return self.posicion == CAMINO_META[self.color][-1]

    

    
class Jugador:
    def __init__(self, color):
        self.color = color
        self.fichas = [Ficha(color, PUNTOS_INICIO[color]) for _ in range(4)]

    def mostrar_fichas(self):
        for i, ficha in enumerate(self.fichas):
            estado = "En casa" if ficha.posicion == -1 else f"En {ficha.posicion}"
            print(f"  Ficha {i+1}: {estado}")

    def capturar(self, ficha_mia, jugadores):
        if ficha_mia.posicion in Zonas_Seguras:
            return

        for otro in jugadores:
            if otro != self:
                for ficha in otro.fichas:
                    if ficha.posicion == ficha_mia.posicion and ficha.posicion != -1:
                        print(f"¡{self.color} capturó una ficha de {otro.color}!")
                        ficha.posicion = -1
                        ficha_mia.mover(20)
                        return

    def ha_ganado(self):
        return all(f.en_meta() for f in self.fichas)


def tirar_dado():
    return random.randint(1, 6)


def verificar_bloqueo(posicion):
    if posicion < 0 or posicion >= 68:
        return False
    return len(casillas[posicion]) >= 2


def turno_jugador(jugador, jugadores, pares_seguidos, ultima_ficha_movida, modo_desarrollador):
    print(f"\nTurno de {jugador.color}")
    jugador.mostrar_fichas()

    input("Presiona ENTER para tirar el dado...")

    if modo_desarrollador:
        while True:
            try:
                dado = int(input("Introduce el valor del dado (1-6): "))
                if 1 <= dado <= 6:
                    break
                else:
                    print("Valor inválido. Ingresa un número entre 1 y 6.")
            except ValueError:
                print("Entrada no válida. Debes ingresar un número.")
    else:
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
        return False

    print("Elige ficha a mover:")
    for fic in opciones:
        print(f"{fic+1}: Ficha {fic+1}")

    # Validación corregida al elegir ficha
    while True:
        entrada = input("Ficha a mover: ").strip()
        if entrada.isdigit():
            eleccion = int(entrada) - 1
            if eleccion in opciones:
                break
            else:
                print("Número fuera de las opciones disponibles. Intenta de nuevo.")
        else:
            print("Entrada no válida. Debes ingresar un número.")

    jugador.fichas[eleccion].mover(dado)
    ultima_ficha_movida[jugador.color] = jugador.fichas[eleccion]
    jugador.capturar(jugador.fichas[eleccion], jugadores)

    if pares_seguidos[jugador.color] >= 3:
        print(f"{jugador.color} sacó tres pares seguidos. Su última ficha movida regresa a la casa.")
        ficha_penalizada = ultima_ficha_movida[jugador.color]
        if ficha_penalizada and ficha_penalizada.posicion != -1:
            casillas[ficha_penalizada.posicion].remove(ficha_penalizada)
            ficha_penalizada.posicion = -1
        pares_seguidos[jugador.color] = 0
        return False 

    return dado % 2 == 0


def main():
    global jugadores_global
    jugadores = [Jugador("Rojo"), Jugador("Azul"), Jugador("Amarillo"), Jugador("Verde")]
    jugadores_global = jugadores
    jugadores = [Jugador("Rojo"), Jugador("Azul"), Jugador("Amarillo"), Jugador("Verde")]
    turno = 0
    pares_seguidos = {jug.color: 0 for jug in jugadores}
    ultima_ficha_movida = {jug.color: None for jug in jugadores}

    print("Selecciona modo de juego: 1 para Real, 2 para Desarrollador")
    modo = input("Modo: ")
    modo_desarrollador = modo == '2'

    while True:
        jugador = jugadores[turno % len(jugadores)]
        repetir_turno = turno_jugador(jugador, jugadores, pares_seguidos, ultima_ficha_movida, modo_desarrollador)

        if jugador.ha_ganado():
            print(f"\n¡El jugador {jugador.color} ha ganado!")
            break

        if not repetir_turno:
            turno += 1


if __name__ == "__main__":
    main()



#
