import curses
import subprocess
from pathlib import Path
from time import sleep

# Permite controlar la terminal (capturar teclas, redibujar pantalla, ...)
import requests


def opcion1():
    # 1. Limpiar la pantalla
    terminal.clear()

    # 2. Escribir por pantalla (Feedback visual inmediato)
    terminal.addstr(0, 0, "Has elegido la opción 1")
    terminal.addstr(1, 0, "Enviando mensaje a Discord...", curses.A_DIM)
    terminal.refresh()  # Importante para ver los cambios antes del request

    # 3. Enviar mensaje a Discord (con protección de errores)
    url = "http://192.168.21.21:5678/webhook-test/discord"
    datos = {"mensaje": "Oi macaquinho"}

    try:
        # Añadimos timeout=2 segundos para no congelar la app si falla
        respuesta = requests.post(url, json=datos, timeout=2)

        # Comprobar si el servidor respondió con éxito (Código 200-299)
        if respuesta.status_code == 200:
            terminal.addstr(3, 0, "Mensaje enviado con éxito.", curses.A_BOLD)
        else:
            terminal.addstr(3, 0, f"Error del servidor: {respuesta.status_code}")

    except requests.exceptions.ConnectionError:
        terminal.addstr(3, 0, "Error: No se pudo conectar a localhost:5678")
    except requests.exceptions.Timeout:
        terminal.addstr(3, 0, "Error: El servidor tardó demasiado en responder")
    except Exception as e:
        terminal.addstr(3, 0, f"Error desconocido: {e}")

    # 4. Finalizar
    terminal.addstr(5, 0, "Pulsa una tecla para volver al menú")
    terminal.refresh()  # Refrescar de nuevo para mostrar el resultado
    terminal.getch()

def opcion2():
     # Limpiar la pantalla
    terminal.clear()

    # Escribir por pantalla
    terminal.addstr(0, 0, "Has elegido la opción 2")
    terminal.addstr(1, 0, "Pulsa una tecla para volver al menu")

     # Una pausa
    terminal.getch()


def opcion3():
    # Limpiar la pantalla
    terminal.clear()

    # Escribir por pantalla
    terminal.addstr(0, 0, "Has elegido la opción 3")
    terminal.addstr(1, 0, "Pulsa una tecla para volver al menu")

    # Una pausa
    terminal.getch()

def opcion4():
    opciones = ["Si", "No"]
    seleccion = 0
    # CORRECCIÓN 1: Debe ser True para que el bucle arranque
    bucleActivo = True

    while bucleActivo:
        terminal.clear()
        terminal.addstr(0, 0, "¿Deseas Salir?")

        for i, opcion in enumerate(opciones):
            # Estética: Agregué un espacio " i*5 " para que no estén tan pegados
            if i == seleccion:
                terminal.addstr(4, i*5, opcion, curses.A_REVERSE)
            else:
                terminal.addstr(4, i*5, opcion)

        tecla = terminal.getch()

        if tecla == curses.KEY_RIGHT and seleccion < len(opciones) - 1:
            seleccion += 1
        elif tecla == curses.KEY_LEFT and seleccion > 0:
            seleccion -= 1
        elif tecla == 10: # Enter
            if seleccion == 0:
                return False   # Confirmamos la salida
            elif seleccion == 1:
                # Eligió "No"
                return True


def listar():
    ruta = Path.cwd() / "tienda"
    seleccion = 0
    while True:
        terminal.clear()
        terminal.addstr(0, 0, "HAS ELEGIDO LISTAR")
        elementos = [ruta.parent] + sorted(ruta.iterdir())
        for i, elemento in enumerate(elementos):
            nombre = elemento.name
            if elemento == ruta.parent:
                nombre = "Volver"
            if seleccion == i:
                terminal.addstr(i + 2, 0, nombre, curses.A_REVERSE)
            else:
                terminal.addstr(i + 2, 0, nombre)

        if ruta.name == "Categorias":
            terminal.addstr(len(elementos)+4, 0, "Pulsa la tecla C para crear una nueva categoria")
            terminal.addstr(len(elementos)+5, 0, "Pulsa la tecla B para actualziar una categoria")

        terminal.addstr(len(elementos) + 6, 0, f"El elemento seleccionado es: {elementos[seleccion]} ")
        terminal.addstr(len(elementos)+7, 0, f"El elemento donde me encuentro es: {ruta} ")

        tecla = terminal.getch()
        if tecla == curses.KEY_DOWN and seleccion < len(elementos) - 1:
            seleccion += 1
        elif tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == ord('\n'):
            ruta = elementos[seleccion]
            seleccion = 0
        elif tecla == ord('c') or tecla == ord('C'):
            curses.endwin()
            retorno = subprocess.run(["bash","./scriptBash/crearDirectorio.sh", str(ruta)])
            print("Pulsa una tecla para continuar")
            if retorno.returncode == 10:
                print("La categoria ya existe")
                sleep(4)
            elif retorno.returncode == 0:
                print("Categoria creada con exito!")
                sleep(4)
        elif tecla == ord('B') or tecla == ord('b'):
            curses.endwin()
            retorno = subprocess.run(["bash", "./scriptBash/editar.sh", str(ruta), str(elementos[seleccion])])
            print("Pulsa una tecla para continuar")
            if retorno.returncode == 10:
                print("No fue posible actualziar la categoria")
                sleep(4)
            elif retorno.returncode == 0:
                print("Categoria actualizada con exito!")
                sleep(4)


def menu(terminal):
    opciones = ["Opción 1","Opción 2", "Opción 3", "Listar", "Salir"]
    seleccion = 0
    bucleActivo = True

    while bucleActivo:
        # Limpiar la pantalla
        terminal.clear()

        # Escribir por pantalla
        terminal.addstr("MENÚ PRINCIPAL")

        #Pintar las opciones en la terminal
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                terminal.addstr( i+2 , 0, opcion, curses.A_REVERSE)
            else:
                terminal.addstr( i+2 , 0, opcion)

        terminal.addstr("\n\nElija una opción")

        # Espera a que el usuario pulse una tecla
        tecla = terminal.getch()


        if tecla == curses.KEY_DOWN and seleccion < len(opciones) - 1:
            seleccion += 1
        elif tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == ord('\n'): # Entra aqui si has pulsado la tecla ENTER
            if seleccion == 0:
                opcion1()
            elif seleccion == 1:
                opcion2()
            elif seleccion == 2:
                opcion3()
            elif seleccion == 3:
                listar()
            elif seleccion == 4:
                bucleActivo = opcion4()




if __name__ == '__main__':
    print("inicio")
    # Inicializa curses y obtiene la pantalla (terminal)
    terminal = curses.initscr()

    # Activar detección de teclas especiales (flechas, enter, etc)
    terminal.keypad(True)

    # Desactiva el eco del teclado
    # Las teclas pulsadas no se muestran
    curses.noecho()

    # Activar modo lectura inmediata de teclas (no espera Enter)
    curses.cbreak()

    # Oculta el cursor
    curses.curs_set(0)

    try:
        menu(terminal)
    finally:
        # Libera los recursos de la terminal
        curses.nocbreak()
        terminal.keypad(False)
        curses.echo()
        curses.endwin()
