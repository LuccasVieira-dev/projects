#v0.5
#macro simples e nada preciso pra qualquer tipo de automação, funcional, mas não espere muito dele
#pretendo atualizalo no futuro e talvez até criar um exe


from pynput import keyboard, mouse
import time
import threading
import pydirectinput

# --- Configurações ---
pydirectinput.PAUSE = 0
intervalo = 0.01
teclas_pressionadas = set()
gravando = False
reproduzindo = False
macro = []

# --- Loop de tempo da gravação ---
def loop_tempo():
    global gravando
    while True:
        time.sleep(intervalo)
        if gravando:
            macro.append(f"time.sleep({intervalo})")

# --- Clique do mouse ---
def clique_mouse(x, y, botao, pressionado):
    if pressionado and gravando:
        btn = 'left' if botao == mouse.Button.left else 'right'
        macro.append(f"pydirectinput.click({x}, {y}, button='{btn}')")

# --- Tecla pressionada ---
def tecla_pressionada(tecla):
    global gravando, reproduzindo
    if tecla not in teclas_pressionadas:
        teclas_pressionadas.add(tecla)
        try:
            nome = tecla.char
        except AttributeError:
            nome = tecla.name

        if nome == "g":
            macro.clear()
            gravando = True
            print("[INFO] Gravação INICIADA")
            return
        elif nome == "p":
            gravando = False
            print("[INFO] Gravação PARADA")
            return
        elif nome == "r" and not reproduzindo:
            print("[INFO] Reprodução INICIADA")
            threading.Thread(target=reproduzir_macro, daemon=True).start()
            return

        if gravando:
            macro.append(f"pydirectinput.keyDown('{nome}')")

# --- Tecla solta ---
def tecla_solta(tecla):
    if tecla in teclas_pressionadas:
        teclas_pressionadas.discard(tecla)
    try:
        nome = tecla.char
    except AttributeError:
        nome = tecla.name

    if gravando:
        macro.append(f"pydirectinput.keyUp('{nome}')")

# --- Reprodução da macro ---
def reproduzir_macro():
    global reproduzindo
    reproduzindo = True
    for comando in macro:
        exec(comando)
    reproduzindo = False
    print("[INFO] Reprodução CONCLUÍDA")

# --- Inicialização ---
print("[INFO] Script iniciado! G=gravar, P=parar, R=reproduzir")
threading.Thread(target=loop_tempo, daemon=True).start()

ouvinte_mouse = mouse.Listener(on_click=clique_mouse)
ouvinte_teclado = keyboard.Listener(
    on_press=tecla_pressionada,
    on_release=tecla_solta
)

ouvinte_mouse.start()
ouvinte_teclado.start()

ouvinte_mouse.join()
ouvinte_teclado.join()
