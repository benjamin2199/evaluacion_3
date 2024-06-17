import random


def mostrar_bienvenida():
    print("¡Bienvenido al juego del Gato!")


def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Nueva partida (Player 1 VS COM)")
    print("2. Versus (P1 VS P2)")
    print("3. Salir")


def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]


def mostrar_tablero(tablero):
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")


def marcar_casilla(tablero, jugador, posicion):
    tablero[posicion[0]][posicion[1]] = jugador


def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False


def verificar_empate(tablero):
    return all(casilla != " " for fila in tablero for casilla in fila)


def turno_jugador(tablero, jugador):
    while True:
        try:
            print(f"Turno de {jugador}")
            fila, col = map(int, input("Ingresa tu posición (fila,columna): ").split(","))
            if tablero[fila][col] == " ":
                marcar_casilla(tablero, jugador, (fila, col))
                break
            else:
                print("Casilla ocupada. Inténtalo de nuevo.")
        except (ValueError, IndexError):
            print("Posición inválida. Inténtalo de nuevo.")


def turno_computadora(tablero, jugador):
    print(f"Turno de {jugador}")
    while True:
        fila, col = random.randint(0, 2), random.randint(0, 2)
        if tablero[fila][col] == " ":
            marcar_casilla(tablero, jugador, (fila, col))
            break


def iniciar_partida_vs_com():
    tablero = crear_tablero()
    jugador, computadora = "X", "O"
    turno = random.choice([jugador, computadora])


    while True:
        mostrar_tablero(tablero)
       
        if turno == jugador:
            turno_jugador(tablero, jugador)
        else:
            turno_computadora(tablero, computadora)


        if verificar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"¡{jugador} ha ganado!")
            break
        elif verificar_empate(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break
       
        turno = computadora if turno == jugador else jugador


def iniciar_partida_vs_jugador():
    tablero = crear_tablero()
    jugador1, jugador2 = "X", "O"
    turno = random.choice([jugador1, jugador2])


    while True:
        mostrar_tablero(tablero)
       
        if turno == jugador1:
            turno_jugador(tablero, jugador1)
        else:
            turno_jugador(tablero, jugador2)


        if verificar_ganador(tablero, jugador1):
            mostrar_tablero(tablero)
            print(f"¡{jugador1} ha ganado!")
            break
        elif verificar_ganador(tablero, jugador2):
            mostrar_tablero(tablero)
            print(f"¡{jugador2} ha ganado!")
            break
        elif verificar_empate(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break
       
        turno = jugador2 if turno == jugador1 else jugador1


def main():
    mostrar_bienvenida()
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")


        if opcion == "1":
            iniciar_partida_vs_com()
        elif opcion == "2":
            iniciar_partida_vs_jugador()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
