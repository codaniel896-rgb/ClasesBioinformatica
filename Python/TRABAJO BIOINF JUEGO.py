#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Primero correr la cuarta y luego la tercera, la segunda son solo anotaciones propias


# In[ ]:


#!Tengo que crear algún tipo de variable que englobe al juego, quizás una función


#/t para tabular // /n para línea en blanco

#Las variables deben de estar escritas antes de que se intenten ejecutar
    ##Para utilizar una variable en una función: "{Variable}"
#Se pone + para concatenar y " " entre cada cosa a juntar para que no queden pegados -> Carlos+Perez vs Carlos+" "+Perez
#No poner () entre los nombres de la variable
    ##Poner == para decir que el input que se quiere recibir es ese, si es solo = significa que cambiamos el valor de la variable
#title() => Primera letra x palabra en MAYÚSCULA // capitalize() => Solo primera letra en MAYÚSCULA

#UPPER/LOWER van seguidos de "()" para que pille la palabra
    ##El () se utiliza para activar el comando método sobre la string
    ##En vez de poner "x.upper() or x.lower()" poner directamente -> "if x.lower() == y.lower():"

#f": Nos permite usar las variables con {} en la string, que se reemplazarán directamente por el valor que se indique al llamar a la función

#respuesta == "XXXXXX": -> Para que la respuesta tenga que ser eso en concreto
#respuesta in ("XX", "xX", "xx", "Xx"): -> Para que la respuesta pueda ser cualquiera de esas opciones

# "{}" para crear diccionarios

#input() solo devuelve texto, las "" hacen que sea texto, no números
    ## edad = input("¿Cuántos años tienes?") -> "25"
    ## edad = int(input("¿Cuántos años tienes?") -> 25

    ## Podemos convertir string a entero con:
        ### int("25") -> 25 // str(25) -> "25"
        ### Si estamos en un diccionario: respuestas["edad"] = edad -> Cogerá el valor del diccionario con la variable de nombre edad y le quitará las comillas

# Display(): Función nativa de Jupyter, reemplaza print(). 
    ## print() solo muestra strings
    ## display() renderiza imágenes, vídeos, tablas y url

#html()_ Contenedor, dice que no es un texto normal y que se ejecute como página web
    ## <span: abre 
    ## </span>: cierra
    # Se utilizan para no realizar saltos de línea y poder escribir parámetros entre ambos

#Global: palabra clave que permite modificar una variable desde dentro de una función (Usar con moderación)

#return: Devuelve la función actual y el control a quien la llamó
#break: termina un bucle


# ***BIENVENINO A TERROR EN LA UAX***

# In[ ]:


while True: #Bucle menú principal
    Juego()
    modalidad = input("* Selecciona: " + Jugar() + ", " + Idioma() + ", " + Reglas() + ", " + Exit() + ": ")

    if modalidad.strip().lower() == Jugar().lower() or modalidad.strip().lower() in "juga":
        print_neon_caos("🎃👻BIENVENIDO A TERROR EN LA UAX👻🎃", color="#6A00FF", font="Courier New", vel_temblar="0.8s", vel_parpadeo="10s", duracion=5)
        print()
        import time
        print("", end="")
        for i in range (5):
            time.sleep(1)
            print(".\n", end="")
        print("\n")
        inicializar_partida()
        ejecutar_partida()


    elif modalidad.strip().lower() == Idioma().lower() or modalidad.strip().lower() in "idioma":

        def Opciones():
            return "¿Castellano o alienígena?"
            #Qué significa que la devuelva?

        def Salir():
            return "Salir"

        while True: #bucle submenú_Idioma
            respuesta_idioma = input("*Actualmente estás jugando en castellano, ¿Quieres cambiar de idioma?: " + Opciones() + ", " + Salir() + ": ")

            def Castellano():
                print("Ya sabía yo...")
                return Salir() #Saca a menú principal?

            if respuesta_idioma.strip().lower() in "cstellno":
                Castellano()
                print()
                break #return si quiero un resultado como respuesta, break si quiero que me saque a la dirección anterior
            elif respuesta_idioma.lower() in "alienígena" or "alienigena":
                print("Con que alienígena... okay...")
                print()
                #Crea línea en blanco
                escribir_lento("☊⏃⟟⌇⏁⟒ ⟒⋏ ⋔⟟ ⏁⍀⏃⋔⌿⏃ ⋔⎍⏃⟊⏃⟊⏃⟊⏃⟊⏃") #Caiste en mi trampa muajajajaja
                print()
                escribir_lento("⟒⌇ ⏚⍀⍜⋔⏃, ⌇⍜⌰⍜ ⟒⌇⏁⏃⍀⏃⌇ ⏃⍾⎍⟟ ⎍⋏ ⋔⍜⋔⟒⋏⏁⍜ ⎅⟒ ⏁⎍ ⌇⎍☊⟟⏃ ⟒ ⟟⋏⌇⟟☌⋏⟟⎎⟟☊⏃⋏⏁⟒ ⟒⌖⟟⌇⏁⟒⋏☊⟟⏃") #Es broma, solo estarás aquí un momento de tu sucia e insignificante existencia
                print()
                escribir_lento("?⏁⏃⋏ ⍀⏃⌿⟟⎅⍜ ⏁⟒ ⏃⍀⍀⟒⌿⟟⟒⋏⏁⟒⌇ ⎅⟒ ⏁⎍⌇ ⎅⟒☊⟟⌇⟟⍜⋏⟒⌇?") #¿Tan rápido te arrepientes de tus decisiones?
                escribir_lento("?⍾⎍⟟⟒⍀⟒⌇ ⎐⍜⌰⎐⟒⍀ ⏃⌰ ☊⏃⌇⏁⟒⌰⌰⏃⋏⍜?") #¿Quieres volver al Castellano?
                print()
                escribir_lento("-(No entiendo nada... Quizás debería volver a Castellano...) ¿Castellano?")

                import time
                print("Loading", end="")
                for i in range (3):
                    time.sleep(1)
                    print(".", end="")
                print("", end="")
                for i in range (3):
                    time.sleep(2)
                    print(".", end="")
                    #Delay doble, para dar dramatismo...
                    ## for i range(X): Para i en rango(veces que quiero que se repita)
                        #time.sleep(X): Para de hacer cosas (X) segundos
                    ##1º: Print Loading y añade un punto más cada segundo, hasta llegar a los 3 segundos
                    ##2º: Print "." 3 veces cada 2 seegundos

                print("\n\nHas seleccionado Castellano, muchas gracias")
                print()
                break
            elif respuesta.strip().lower() in "salir":
                print()
                break 
            else:
                print ("Opción no válida. Por favor, aprende a leer y a escribrir...")
                #El bucle del submenú_Idioma continúa?

    elif modalidad.strip().lower() == Reglas().lower() or modalidad.strip().lower() in "rglas": 
        print("\tEsto es algo parecido a una novela visual interactiva:")
        print("\t\t-Para todos los inputs donde puedas usar versiones cortas, por ejemplo [Jugar = j], se indicará al final de la frase con un *, si no ves esa marca asume que tienes que poner la palabra completa")
        print()

    elif modalidad.strip().lower() == Exit().lower() or modalidad.strip().lower() in "exit":
        print()
        print("Ten cuidado ahí fuera...")
        break

    else:
        print()
        print("Opción no válida. Por favor, selecciona una opción del menú")
        #El bucle del menú continúa hasta que se escriba "EXIT" (Fin) o "JUGAR" (Empieza el juego)



# In[ ]:


def Juego():
    print("BIENVENIDO A LOS JUEGOS DEL HAMBRE... Digo, a la UAX")

#Menú
def Jugar():
    return "Jugar"

def Idioma():
    return "Idioma"

def Reglas():
    return "Reglas"

def Exit():
    return "Exit"

import sys
import time
from IPython.display import HTML, display
# Python permite que se importe desde HTML y se enseñe

from IPython.display import display, Image, HTML

def mostrar_imagen(ruta, ancho=650):
    display(HTML(
        f"""
        <div style="text-align:center; margin:20px 0;">
            <img src="{ruta}"
                 style="width:100%; max-width:{ancho}px;
                        height:auto; border-radius:12px;
                        box-shadow:0 0 25px #a00000;">
        </div>
        """
    ))



def print_parpadeo(texto, color="red", font="Arial", weight="bold", velocidad="0.8s"):
    # 1. Definimos la animación de parpadeo en CSS
    animacion_css = f"""
    <style>
    @keyframes parpadear {{
      0% {{ opacity: 1; }}
      49% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
      99% {{ opacity: 0; }}
      100% {{ opacity: 1; }}
    }}
    .efecto-parpadeo {{
      display: inline-block;
      animation: parpadear {velocidad} infinite; /* Controla la velocidad */
    }}
    </style>
    """

    # 2. Aplicamos tus estilos de diseño habituales
    estilo_texto = f'color: {color}; font-family: {font}; font-weight: {weight};'

    # 3. Renderizamos todo en el notebook
    html_final = f'{animacion_css}<span class="efecto-parpadeo" style="{estilo_texto}">{texto}</span>'
    display(HTML(html_final))


def print_temblor(texto, color="black", font="Arial", weight="normal", vel_temblar="0.8s"):
    # 1. Definimos la animación de temblor en CSS
    animacion_css = """
    <style>
    @keyframes temblar {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      20% { transform: translate(-3px, 0px) rotate(1deg); }
      30% { transform: translate(0px, 2px) rotate(0deg); }
      40% { transform: translate(1px, -1px) rotate(1deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      60% { transform: translate(-3px, 1px) rotate(0deg); }
      70% { transform: translate(2px, 1px) rotate(-1deg); }
      80% { transform: translate(-1px, -1px) rotate(1deg); }
      90% { transform: translate(2px, 2px) rotate(0deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    .efecto-temblor {
      display: inline-block;
      animation: temblar {vel_temblar} infinite linear; /* Hace que tiemble rápido y para siempre */
    }
    </style>
    """

    # 2. Aplicamos tus estilos personalizados junto con la animación
    #estilo_texto = f'color: {color}; font-family: {font}; font-weight: {weight};'

    estilo_texto = (
        f'color: {color}; '
        f'font-family: {font}; '
        f'font-weight: {weight}; '
        f'display: inline-block; '
        f'animation: temblar_dinamico {vel_temblar} infinite linear, '
    )

    # 3. Juntamos todo y lo mostramos
    html_final = f'{animacion_css}<span class="efecto-temblor" style="{estilo_texto}">{texto}</span>'
    display(HTML(html_final))


from IPython.display import Javascript
import uuid

def print_neon_caos(
    texto,
    color="#00ffff",
    font="Arial",
    weight="900",
    vel_temblar="0.8s",
    vel_parpadeo="1.5s",
    duracion=None
):
    # Animaciones CSS
    css_animaciones = """
    <style>
    @keyframes temblar_dinamico {
      0%   { transform: translate(1px, 1px) rotate(0deg); }
      20%  { transform: translate(-1px, -2px) rotate(-1deg); }
      40%  { transform: translate(-2px, 0px) rotate(1deg); }
      60%  { transform: translate(0px, 2px) rotate(0deg); }
      80%  { transform: translate(1px, -1px) rotate(1deg); }
      100% { transform: translate(1px, 1px) rotate(0deg); }
    }

    @keyframes parpadear_dinamico {
      0%, 49% { opacity: 1; }
      50%, 99% { opacity: 0.1; }
      100% { opacity: 1; }
    }

    @keyframes desaparecer {
      0%   { visibility: visible; }
      99%  { visibility: visible; }
      100% { visibility: hidden; }
    }
    </style>
    """

    brillo_neon = (
        f"text-shadow: 0 0 5px {color}, "
        f"0 0 10px {color}, "
        f"0 0 20px {color}, "
        f"0 0 40px {color};"
    )

    animaciones = (
        f"temblar_dinamico {vel_temblar} infinite linear, "
        f"parpadear_dinamico {vel_parpadeo} infinite"
    )

    # La desaparición solo se añade si se solicita
    if duracion is not None:
        if duracion < 0:
            raise ValueError("duracion no puede ser negativa")

        animaciones += (
            f", desaparecer 0.01s linear {duracion}s forwards"
        )

    estilo_inline = (
        f"color: {color}; "
        f"font-family: {font}; "
        f"font-weight: {weight}; "
        f"{brillo_neon} "
        "display: inline-block; "
        f"animation: {animaciones};"
    )

    elemento_id = "neon_" + uuid.uuid4().hex

    html_final = (
        f'<div id="{elemento_id}">'
        f'{css_animaciones}'
        f'<span style="{estilo_inline}">{texto}</span>'
        f'</div>'
    )

    display(HTML(html_final))

    if duracion is not None:
        display(Javascript(f"""
            setTimeout(() => {{
                const elemento = document.getElementById("{elemento_id}");
                if (elemento) elemento.remove();
            }}, {duracion * 1000});
        """))
#Uffff, a ver... 
    ## uuid: genera identificadores únicos para cada mensaje, importante para que se elimine el correcto y no uno random sin querer
    ## se ha creado "elemento_id" prefijo de la def + indicador id.indicador concreto.codificado en hex
    ## <div id=" "> abre el contenedor con un id concreto // </div> lo cierra
    ## La duración está en milisegundos (3 * 1000 = 3s) -> Python procesa en segundos, pero Java en milisegundos
    ## Llaves {{}} se quieren conservar


def mensaje_concreto_donde_si_no_no_funciona_mierda(
    texto,
    velocidad=0.1,
    color="red",
    font="Arial",
    weight="bold",
    vel_temblar="0.2s 50"
):
    animacion_css = """
    <style>
    @keyframes temblar_dinamico {
        0%   { transform: translate(1px, 1px) rotate(0deg); }
        20%  { transform: translate(-2px, -1px) rotate(-2deg); }
        40%  { transform: translate(2px, 1px) rotate(2deg); }
        60%  { transform: translate(-1px, 2px) rotate(-1deg); }
        80%  { transform: translate(2px, -1px) rotate(1deg); }
        100% { transform: translate(1px, 1px) rotate(0deg); }
    }
    </style>
    """

    estilo = (
        f"color: {color}; "
        f"font-family: {font}; "
        f"font-weight: {weight}; "
        "display: inline-block; "
        f"animation: temblar_dinamico {vel_temblar} infinite linear;"
    )

    salida = display(
        HTML(animacion_css + f'<span style="{estilo}"></span>'),
        display_id=True
    )

    contenido = ""

    for letra in texto:
        contenido += letra

        html = (
            animacion_css
            + f'<span style="{estilo}">{contenido}</span>'
        )

        salida.update(HTML(html))
        time.sleep(velocidad)

def print_custom(texto, color="black", font="Arial", weight="normal"):
    # Construimos el estilo dinámico con el nuevo parámetro font-weight
    estilo = f'color: {color}; font-family: {font}; font-weight: {weight};'
    display(HTML(f'<span style="{estilo}">{texto}</span>'))
    #Si no se especifica un color se escribe en negro arial normal, si no, se especifica y cambia

    #TEXTO, COLOR, FONT, WEIGHT


def print_fondo(texto, color="black", font="Arial", weight="normal", fondo="transparent"):
    # Añadimos 'background-color' y un pequeño espacio de relleno (padding) para que se vea bien
    estilo = f'color: {color}; font-family: {font}; font-weight: {weight}; background-color: {fondo}; padding: 2px 6px; border-radius: 4px;'
    display(HTML(f'<span style="{estilo}">{texto}</span>'))

    #TEXTO, COLOR, FONT, WEIGHT, FONDO

def escribir_lento(texto, velocidad=0.03, color=None, font="Arial", weight="normal"):
    # Si no se especifica color, utiliza la salida de texto normal
    if color is None:
        for letra in texto:
            sys.stdout.write(letra) # Imprime la letra sin dar un salto de línea automático
            sys.stdout.flush() # Fuerza a la terminal a mostrar el carácter inmediatamente
            time.sleep(velocidad) # Pausa en segundos antes de la siguiente letra
        print()

    # Si se especifica color, utiliza HTML
    else:
        contenido = ""
        salida = display(HTML(""), display_id=True)

        for letra in texto:
            contenido += letra
            estilo = (
                f'color: {color}; '
                f'font-family: {font}; '
                f'font-weight: {weight};'
            )
            salida.update(
                HTML(f'<span style="{estilo}">{contenido}</span>')
            )
            time.sleep(velocidad)
        print()

def escribir_miedo(texto, velocidad=0.1, color=None, font="Arial", weight="normal"):
    # Si no se especifica color, utiliza la salida de texto normal
    if color is None:
        for letra in texto:
            sys.stdout.write(letra) # Imprime la letra sin dar un salto de línea automático
            sys.stdout.flush() # Fuerza a la terminal a mostrar el carácter inmediatamente
            time.sleep(velocidad) # Pausa en segundos antes de la siguiente letra
        print()

    # Si se especifica color, utiliza HTML
    else:
        contenido = ""
        salida = display(HTML(""), display_id=True)

        for letra in texto:
            contenido += letra
            estilo = (
                f'color: {color}; '
                f'font-family: {font}; '
                f'font-weight: {weight};'
            )
            salida.update(
                HTML(f'<span style="{estilo}">{contenido}</span>')
            )
            time.sleep(velocidad)
        print()

def preguntar_lento(variable, pregunta, tipo=str, velocidad=0.03):
    escribir_lento(pregunta, velocidad)
    respuesta = tipo(input())
    respuestas[variable] = respuesta
    return respuesta




#Datos actuales de la partida
respuestas = {} #Diccionario de respuestas del jugador (clave:valor)
    ## print(respuestas) -> ver todo el árbol de decisiones adjunto
    ## print(respuestas["variable"]) -> Consultar una concreta

#Datos del último checkpoint
punto_guardado = "inicio" #Indica desde qué escena se reanuda
estado_guardado = None #COPIA DEL ESTADO EN EL ÚLTIMO CHECKPOINT

#Datos que pueden cambiar durante la partida
estado_juego = {
    "respuestas": {},
    "inventario": [],
    "decisiones": {},
}

# Escena que debe ejecutar el bucle principal
escena_actual = "inicio"


def inicializar_partida(): #ESTA DEF REINICIA TODOS LOS DATOS
    global respuestas
    global estado_juego
    global estado_guardado
    global punto_guardado
    global escena_actual

    respuestas = {}

    estado_juego = {
        "respuestas": respuestas,
        "inventario": [],
        "decisiones": {},
    }

    estado_guardado = None
    punto_guardado = "inicio"
    escena_actual = "inicio"


tocar_los_huevos = 0

def procesar_tocar_los_huevos(detectado):
    global tocar_los_huevos
    if detectado:
        escribir_miedo(f"Cuidado... llevas {tocar_los_huevos} aviso, no habrá más, a la próxima vas a sufrir las consecuencias.")
        intentos_detectado += 1        
        # Comprobamos si ha llegado al límite de 2
        if intentos_detectado >= 2:
            escribir_miedo("TE LO ADVERTÍ. PIEDRA PARA TI. PIEDRA")
            game_over()


def guardar_punto(nombre_punto): #Def CheckPoint
    global punto_guardado #Modifica "punto_guardado" en lugar de crear una variable local
    punto_guardado = nombre_punto 
    guardar_estado()
    print()
    print_fondo(f"[Punto de guardado: {nombre_punto}]", color="black", font="Times New Roman", weight="300", fondo="gray")
    print()

import copy

def guardar_checkpoint(nombre, escena):
    global estado_guardado, punto_guardado, estado_juego
    estado_juego.setdefault("respuestas", {})
    estado_juego["respuestas"].update(respuestas)
    punto_guardado = escena.strip().lower()
    estado_guardado = copy.deepcopy(estado_juego)
    print(f"[Checkpoint guardado: {nombre}]")


def restaurar_checkpoint():
    global estado_juego, respuestas, escena_actual
    if estado_guardado is None:
        print("No existe checkpoint guardado.")
        escena_actual = "inicio"
        return
    estado_juego = copy.deepcopy(estado_guardado) #Copia exacta del CP
    respuestas = estado_juego.get("respuestas", {}) #Mala optimización que no pienso cambiar, pero si no actualizamos la variable seguirá apuntando al diccionario antiguo y las respuestas no se sincronizarán, así preguntar_lento puede seguir con respuestas sin sobreescribirlo
    escena_actual = punto_guardado


def guardar_estado(): #Def que Guarda Datos CheckPoint
    global estado_guardado
    estado_guardado = copy.deepcopy(respuestas) #Esto permite que cuando el usuario muere se mantengan sus decisiones hasta ese punto

def cargar_estado():
    global respuestas

    if estado_guardado is not None:
        respuestas = copy.deepcopy(estado_guardado) #Esto evita que se mantengan cosas del futuro después de morir y volver a CP
        #Guardar estado =! guardar punto

def game_over(): #Muestra mensaje y carga estado, pero aún no devuelve a la escena cargada
    print()
    print_neon_caos( #NO LA CAGUES DANI, DESPUÉS DE CADA GAME OVER() PON RETURN, ASÍ NO CONTINUA
        "GAME OVER",
        color="red",
        vel_temblar="0.2s",
        vel_parpadeo="0.5s",
    )
    print()
    input("Pulsa Enter para volver al último checkpoint...")
    restaurar_checkpoint() #Último punto con las decisiones tomadas, no se sobreescribe y se recibe copia exacta
    print("Escena restaurada:", escena_actual)




def ejecutar_partida(): #MENÚ DE CAPÍTULOS, SUPER IMPORTANTE TERMINARLO
    global escena_actual

    while True:
        if escena_actual == "inicio":
            escena_inicio()
        elif escena_actual == "hall":
            escena_hall()
        elif escena_actual == "pasillo":
            escena_pasillo()
        elif escena_actual == "pasillo_superado":
            escena_pasillo_superado()
        elif escena_actual == "combate_monstruo":
            escena_combate_monstruo()
            break
        else:
            print("Escena desconocida:", escena_actual)
            break







#ESTOS SON LOS CHECKPOINTS (Poner árbol de decisiones de cada parte)
def escena_inicio():
    global escena_actual #No olvidar, para que cambie el capitulo en caso de morir

    personaje = preguntar_lento("Personaje", "*¿Quien... quien soy?: Profesor // Alumno")
    nombre = preguntar_lento("Nombre", "Ah... mi cabeza... ¿Cómo me llamo?")
    escribir_lento(f'Cierto, mi nombre es {nombre}...')
    print()
    print()

    if personaje.lower() in "profesor":
        escribir_lento(f"(Era una noche de otoño, recuerdo que había niebla... cómo olvidarla...)")
        escribir_lento("- Ahhhh otro día más en la UAX...")
        escribir_lento("- Encima otra de esas reuniones donde no dicen nada y me hacen perder mi tiempo...")
        escribir_lento("- Espero que no haya mucho tráfico a estas horas. Por favor, quiero tomarme una cerveza en cuanto llegue a casa")
        escribir_lento("- Se suponía que acabaría a las 8:30, pero ya son las 9 de la noche, mierda")
        escribir_lento("- Ya no queda nadie por aquí. Hmmm, qué raro, no se ve ni gente de las residencias")
        escribir_lento("- Bueno, voy a pasarme por el edificio A antes de salir, necesito usar el baño")
    # Puedo hacer que luego se mantenga el árbol de decisiones dependiendo de si se ha elegido profesor o alumno?

    elif personaje.lower() in "alumno":
        escribir_lento(f"(Era una noche de otoño, recuerdo que había niebla... cómo olvidarla...)")
        escribir_lento("(Una tarde más, tube que ir a la UAX...) - Para esto me podría haber quedado en casa, espero que el puto bus no llegue tarde")
        escribir_lento("(No recuerdo por qué, pero ese día me quedé hasta tarde.)")
        escribir_lento("(Seguramente uno de esos trabajos de 15 páginas que luego corrigen con ChatGPT)")
        escribir_lento("- Puta uax de mierda, voy a pasarme por el baño del A y me piro de una vez")

    elif personaje not in ("profesor", "alumno"):
        escribir_lento("No, algo no está bien... ¿Quién soy?")
        return
#Algo que indique que se tiene un mapa, ver el mapa y explicar cómo moverse por el mapa
    print()
    guardar_checkpoint("Hall del edificio A", "hall") #Guarda la escena, me guarda las decisiones y dice que si muero vuelva aquí
    escena_actual = "hall" #La escena deja de ser "inicio" -> pasamos del if al elif -> elif == hall -> corre hall()




def escena_hall():
    global escena_actual

    estado_juego.setdefault("inventario", [])

    print("*Entras al hall del edificio A*")
    time.sleep(2)
    escribir_lento("Qué raro, pensé que ya estaría cerrado a esta hora")
    guardar_punto("hall")
    print()
    time.sleep(3)
    escribir_lento("(De repente, el sonido de la puerta se vió opacado por un fuerte estruendo)")
    print_custom("*PUUUM*", color="red", font="Arial", weight="bold")
    time.sleep(2)
    mensaje_concreto_donde_si_no_no_funciona_mierda("\tAyudAaAAa...", vel_temblar="3s")
    escribir_lento("AH ¡¿QUÉ HA SIDO ESO?! Venía de la 105")
    print("(Me acerqué lentamente. No sabía qué había sido ese ruido, pero fuera lo que fuera no sonó nada bien...)")
    time.sleep(3)
    print("(El aire se sentía pesado. Un olor metalico inundaba el hall y una sensación que me ponía los pelos de punta invadía mi cuerpo.")

    dec2x1 = preguntar_lento("Capitulo 2, Decisión 1", "¿Debería (1)huir, (2)acercarme o (3)gritar?").strip().lower()
    print()
    if dec2x1 in ("huir", "1"):
        print("- No sé qué cojones ha sido eso, pero no pienso quedarme para averiguarlo")
        time.sleep(3)
        print("(Corro, corro tan rápido como me dejan mis piernas, sabía que tenía que volver al gymnasio, pero joder, no pensé que tanto")
        time.sleep(3)
        print("(Me quedo sin aliento, el aire se me escapa, casi parece que me robasen el oxígeno directamente de los pulmones)")
        time.sleep(3)
        print("(Cuando llego al parking, las farolas están apagadas, incluso las de las canchas, pero creo que logro ver una figura a lo lejos)")
        time.sleep(3)
        print("- ¿Ho Hola, perdona, sabes qué pasa? Está todo el campus a osc—")
        time.sleep(4)
        escribir_lento("(De repente, mi voz se extingue, intento hablar, pero no salen palabras...)")
        escribir_lento("(Me llevo la mano a la garganta y noto algo cálido...)")
        escribir_lento("(Qué extraño, la sombra que antes estaba a 10 metros ahora se encuentra en frente mía)")
        escribir_lento("(Un líquido rojo sale de mi garganta mientras la sombra se aleja en la oscuridad...)")
        escribir_miedo("(Pierdo la consciencia... ¿Por qué...? ¿Por qué alguien haría esto...?)", color="gray", weight="200")
        game_over()
        return
    elif dec2x1 in ("acercarme", "2"):
        print("- Mierda, tengo que hacer algo... ¿Pero el qué?, estoy casi seguro de que huele a sangre, mierda mierda mierda")
        dec2x1xa = preguntar_lento("Capitulo 2, Decisión 1 subdecisión A", "Voy a: (1)ir por el camino largo y rodear, (2)ir por el camino corto y directo, (3)necesito ir al baño...").strip().lower()
        if dec2x1xa in ("1", "largo", "rodear"):
            escribir_lento("(No puedo ir de frente o me verá, necesito cruzar sigilosamente)")
            print()
            escribir_lento("(Me deslizo hasta un pasillo lateral. La oscuridad apenas me permite distinguir el suelo...)")
            # CHECKPOINT: justo antes de comenzar el minijuego
            guardar_checkpoint("Inicio del pasillo", "pasillo")
            escena_actual = "pasillo"
            return

        elif dec2x1xa in ("2", "corto", "directo"):
            escribir_lento("(Necesito saber qué está pasando. Ese grito... parecía que alguien necesitaba ayuda, tengo que ir ahora mismo)")
            print("(Me acerco hasta la esquina, pero antes de poder acercarme más me paralizo...)")
            escribir_miedo("- ¿Qué cojones es esa cosa?")
            escribir_lento("(No es por sonar ofensivo, pero ese ser, si acaso persona, que se alzaba ante mi)")
            escribir_lento("(Nunca había visto nada como aquello)")
            escribir_lento("(Un ser de 2 metros de alto, y tan ancho que podría ser 3 veces yo)")
            escribir_lento("(Sus ojos rojos como la sangre y su piel casi diría que parecía caerse a pedazos, con un tono verde podrido)")
            print()
            escribir_lento("(Por un momento mi vista se desplazó hacia el relativamente pequeño cuerpo desmembrado que yacía a sus pies)")
            escribir_lento("(El pobre diablo tenía las piernas reventadas, pero ¿Qué podría causarle eso?)")
            escribir_miedo("- Parece que se las hubieran arrancado atándole las piernas a una cuerda")
            mensaje_concreto_donde_si_no_no_funciona_mierda("\tSocORRoOOOooO...", vel_temblar="3s")
            print("(Mierda, me ha visto, eso solo significa que ESO me ha visto)")
            time.sleep(3)
            print("(Casi sin terminar de procesar el pensamiento, aquel Frankenstein putrefacto se abalanza sobre mi)")
            escribir_lento("¿Qué cojones hago?")
            print("(Lo cierto, es que no había nada que hacer...)")
            time.sleep(3)
            print("(No puedes hacer nada más que sentir lo que se siente ser aplastado por un piano, si fuera una serie de televisión sería hasta cómico)")
            time.sleep(3)
            print("(Pero aquí... solo has muerto...)")
            game_over()



        elif dec2x1xa in ("3", "baño", "ir al baño"):
            print("Entras al baño")
            escribir_lento(f"Eres solo tú, {nombre}")
            estado_juego["inventario"].append("DETERMINACIÓN")
            escribir_lento("Verte en el espejo te llena de determinación para afrontar esta situación")
            print("Usas el baño")
            time.sleep(10)
            lavarse_manos = preguntar_lento("¿Te lavas las manos?", "¿Me lavo las manos?")
            if lavarse_manos in ("sí", "si", "SI", "SÍ"):
                time.sleep(10)
                escribir_lento("(Te miras al espejo, te sientes limpio)")
                return dec2x1xa
            elif lavarse_manos in ("no", "NO"):
                print("Sabía que debía lavarme las manos, pero ni que me fueran a juzgar a través de un videojuego, ¿No?")
                escribir_lento("(Te miras al espejo, te sientes mal por no haberte lavado las manos)")
                game_over()
        else:
            print("NO, PIENSA PIENSA")
            return
    elif dec2x1 in ("gritar", "3"):
        mensaje_concreto_donde_si_no_no_funciona_mierda("AHHHHHHHHHHHH, SANGRE, ES SANGREEEE, AYUDAAAAA")
        print("(En un abrir y cerrar de ojos, algo, un monstruo, o el mal personificado)")
        time.sleep(3)
        print("(Fuera lo que fuera, se abalanzó contra mi. Cuando mi cuerpo quiso correr, esa cosa ya estaba a 2 centímetros de mi cara)")
        time.sleep(2)
        escribir_lento("(Piensa piensa cerebro, ¿Hablar?, creo que no ¿Suplicar? quizás sea mi mejor opción)")
        time.sleep(1)
        escribir_lento("(Quise suplicar, pero esa cosa me tiró por los aires con la misma facilidad con la que el viento arrastra una mota de polvo)")
        time.sleep(2)
        escribir_lento("(Conmocionado por el golpe, de repente, vi al monstruo a lo lejos... ¿Pero qué sostenía? Parecían unos brazos...)")
        escribir_lento("(No tiene sentido pensar en eso ahora... tengo sueño... y empieza a hacer un poco de frío... ayuda... quién sea)")
        time.sleep(3)
        game_over()
        return
    return
    #La lógica del juego va aquí, después break




def escena_pasillo():
    global escena_actual

    import random
    print()
    print("=" * 45)
    print_parpadeo("\t\tEL COWORKING DE LA MUERTE", color="red", font="Arial", weight="900", velocidad="1s")
    print("=" * 45)
    print()
    print()

    escribir_lento("Tienes que cruzar el pasillo sin que te detecten.", font="Times New Roman", weight="200", color="black")
    escribir_lento("Debes superar cinco obstáculos. Cuidado, un solo error y estás muerto.", font="Times New Roman", weight="200", color="black")
    escribir_lento("Solo puedes avanzar por un carril cada vez.", font="Times New Roman", weight="200", color="black")
    escribir_lento("Las X bloquean tu paso, mientras que las O te salvarán.", font="Times New Roman", weight="200", color="black")
    print()
    escribir_lento("Para IZQUIERDA: (1, i, izquierda); Para CENTRO: (2, c, centro); Para DERECHA: (3, d, derecha)", font="Times New Roman", weight="100", color="gray")

    guardar_checkpoint("Inicio del pasillo", "pasillo")
    escena_actual = "pasillo"
    guardar_punto("pasillo")

    input("\nPulsa Enter para comenzar...")

    carriles = ["izquierda", "centro", "derecha"]
    total_obstaculos = 2

    for numero in range(1, total_obstaculos + 1):

        # Elegimos aleatoriamente el único carril seguro
        carril_seguro = random.choice(carriles)

        print()
        print(f"--- OBSTÁCULO {numero}/{total_obstaculos} ---")
        print()
        print("      IZQUIERDA    CENTRO    DERECHA")

        # Dibujamos el obstáculo: X = bloqueado, O = seguro
        dibujo = []

        for carril in carriles:
            if carril == carril_seguro:
                dibujo.append("     [ O ]")
            else:
                dibujo.append("     [ X ]")

        # print("".join(dibujo))
        print()
        print("X = obstáculo")
        print("O = camino libre")

        while True:
            eleccion = input("¿Por dónde pasas?: (izquierda / centro / derecha): ").strip().lower()

            equivalencias = {
                "1": "izquierda",
                "i": "izquierda",
                "izquierda": "izquierda",
                "2": "centro",
                "c": "centro",
                "centro": "centro",
                "3": "derecha",
                "d": "derecha",
                "derecha": "derecha"
            }

            if eleccion in equivalencias:
                eleccion = equivalencias[eleccion]
                break

            print("Una más así y te tiro una piedra a la cabeza")
            procesar_tocar_los_huevos(detectado=True)

        # Comprobamos si ha esquivado el obstáculo
        if eleccion != carril_seguro:
            print()
            escribir_lento(
                "*CRACK...* (Has pisado algo en la oscuridad.)"
            )
            print_neon_caos(
                "TE HA ESCUCHADO, SE ESTÁ ACERCANDO",
                color="red",
                vel_temblar="0.2s",
                vel_parpadeo="0.4s"
            )
            escribir_miedo(
                "UNA SOMBRA SE ABALANZA SOBRE TI"
            )

            game_over()

            # No continuar con los obstáculos restantes.
            # El checkpoint restaura la escena "pasillo".
            return

        else:
            print()
            escribir_lento(
                "Esquivas el obstáculo y avanzas lentamente..."
            )
            time.sleep(2)

    print()
    print_neon_caos(
        "¡HAS SOBREVIVIDO!",
        color="#00D154",
        vel_temblar="0.3s",
        vel_parpadeo="0.8s"
    )
    escribir_lento(
        "(Has conseguido llegar al final del coworking)"
    )

    escena_actual = "pasillo_superado"
    guardar_checkpoint("Final del pasillo", "pasillo_superado")
    escena_actual = "pasillo_superado"
    return

def escena_pasillo_superado(): #AQUÍ TIENES QUE PONER UN CHECKPOINT, BÚSCATE LA VIDA GUAPO
    global escena_actual

    guardar_punto("pasillo_superado")

    print()
    escribir_lento("(Apoyé la espalda contra la pared. Por fin podía respirar, aunque solo fuera un segundo...)")
    escribir_lento("Al fondo ves una puerta entreabierta...")
    print()
    print("(Por fin pude pasar del coworking...)")
    escribir_lento("¿Dónde está ese monstruo que vi antes?")
    print("(Te acercas un poco al aula 105, aunque no logras verla)")
    time.sleep(2)
    print("(Cuando por fin te das cuenta, ya es demasiado tarde, no es que no pudieras ver el aula, sino que ALGO te tapaba la vista)")
    time.sleep(3)
    print("(El monstruo se gira y solo queda una opción... sobrevivir a cómo de lugar... suerte...)")

    guardar_checkpoint("COMBATE FINAL", "combate_monstruo")
    escena_actual = "combate_monstruo"
    guardar_punto("combate_monstruo")
    return

import random
import time

def escena_combate_monstruo():
    global escena_actual

    mostrar_imagen("monstruo_uax.png", ancho=650)


    total_turnos = 5
    turnos_superados = 0

    ataques = [
        "La criatura lanza una garra hacia tu cara.",
        "El monstruo se abalanza sobre ti desde un lateral.",
        "Una extremidad golpea la mesa donde te escondes.",
        "La criatura ruge y carga directamente contra ti.",
        "El monstruo intenta atraparte entre sus brazos."
    ]

    print()
    print("=" * 55)
    print_neon_caos(
        "COMBATE: PROYECTO UAX-0",
        color="red",
        vel_temblar="0.2s",
        vel_parpadeo="0.5s"
    )
    print("=" * 55)

    escribir_lento(
        "El laboratorio informático está a oscuras."
    )
    escribir_lento(
        "Los monitores parpadean. Algo respira al otro lado de la sala."
    )
    escribir_miedo(
        "LA CRIATURA SE PREPARA PARA ATACAR."
    )

    input("\nPulsa Enter para enfrentarte a ella...")

    # Cinco turnos que debes sobrevivir
    for turno in range(1, total_turnos + 1):

        print("\n" + "-" * 45)
        print(f"              TURNO {turno}/{total_turnos}")
        print("-" * 45)

        barra = "█" * turnos_superados + "░" * (
            total_turnos - turnos_superados
        )
        print(f"SUPERVIVENCIA: [{barra}]")
        print()

        escribir_miedo(random.choice(ataques))

        print("\n¿Qué haces?")
        print("1. Esquivar el ataque")
        print("2. Esconderte detrás de una mesa")
        print("3. Usar DETERMINACIÓN")

        while True:
            eleccion = input(
                "\nElige una acción (1/2/3): "
            ).strip().lower()

            if eleccion in ("1", "2", "3"):
                break

            print("¡Decide rápido! No tienes tiempo para dudar.")

        # Cada acción tiene una probabilidad de funcionar.
        if eleccion == "1":
            if random.random() < 0.80:
                escribir_lento(
                    "\n¡Esquivas el ataque por centímetros!"
                )
            else:
                escribir_miedo(
                    "\nLa criatura anticipa tu movimiento y te golpea."
                )
                game_over()
                return

        elif eleccion == "2":
            if random.random() < 0.65:
                escribir_lento(
                    "\nTe ocultas justo a tiempo. La criatura pasa de largo."
                )
            else:
                escribir_miedo(
                    "\n¡La mesa sale despedida por los aires!"
                )
                game_over()
                return

        elif eleccion == "3":
            inventario = estado_juego.setdefault("inventario", [])

            if "DETERMINACIÓN" not in inventario:
                escribir_lento(
                    "\nIntentas reunir valor, pero no tienes ningún objeto "
                    "que te ayude a resistir el ataque."
                )
                escribir_miedo(
                    "La criatura aprovecha tu vacilación y te alcanza."
                )
                game_over()
                return

            else:
                inventario.remove("DETERMINACIÓN")
                escribir_lento(
                    "\nRecuerdas tu reflejo en el baño y recuperas el valor."
                )
                escribir_lento(
                    "Aguantas el ataque sin retroceder."
                )

        turnos_superados += 1

        barra = "█" * turnos_superados + "░" * (
            total_turnos - turnos_superados
        )

        print(f"\nSUPERVIVENCIA: [{barra}]")
        escribir_lento(
            f"Has sobrevivido al turno {turno}."
        )
        time.sleep(1)

    # Plot twist: después del quinto turno
    print("\n" + "=" * 55)
    print_neon_caos(
        "ERROR DEL SISTEMA",
        color="red",
        vel_temblar="0.2s",
        vel_parpadeo="0.3s"
    )
    print("=" * 55)

    escribir_lento(
        "La criatura se detiene en seco."
    )
    escribir_lento(
        "Todos los monitores del laboratorio se encienden a la vez."
    )
    escribir_lento(
        "En la pantalla aparece un archivo oculto:"
    )

    print()
    print_neon_caos(
        "PROYECTO UAX-0: ENTIDAD AUTÓNOMA",
        color="#00D154",
        vel_temblar="0.1s",
        vel_parpadeo="0.5s"
    )

    escribir_miedo(
        "El monstruo no ha venido a cazarte."
    )
    escribir_miedo(
        "Está intentando impedir que llegues al servidor."
    )

    escribir_lento(
        "Una grabación comienza a reproducirse..."
    )
    escribir_lento(
        '"Si alguien está escuchando esto, el experimento ha escapado. '
        'No apaguéis el sistema: la entidad está conectada a él..."'
    )

    escribir_lento(
        "Entonces lo comprendes: el cuerpo de la criatura es una "
        "manifestación de la inteligencia artificial del laboratorio."
    )
    escribir_lento(
        "Y el servidor que la mantiene viva está justo detrás de ella."
    )

    print()
    escribir_miedo(
        "LA CRIATURA VUELVE A LEVANTARSE."
    )

    input(
        "\nPulsa Enter para correr hacia el interruptor de emergencia..."
    )

    escribir_lento(
        "Te lanzas hacia el cuadro eléctrico mientras la criatura "
        "intenta alcanzarte."
    )

    input(
        "\nPulsa Enter para desconectar el servidor..."
    )

    print()
    print_neon_caos(
        "SISTEMA DESCONECTADO",
        color="#00D154",
        vel_temblar="0.2s",
        vel_parpadeo="0.4s"
    )

    escribir_lento(
        "Las luces se apagan."
    )
    escribir_lento(
        "La criatura se queda inmóvil y se deshace en una nube de polvo."
    )
    escribir_lento(
        "Durante unos segundos solo escuchas tu propia respiración."
    )

    print()
    print_neon_caos(
        "HAS SOBREVIVIDO",
        color="#00D154",
        vel_temblar="0.2s",
        vel_parpadeo="0.5s"
    )

    escribir_lento(
        "Pero en uno de los monitores aparece una última línea:"
    )

    print()
    print(
        '"COPIA DE SEGURIDAD RESTAURADA. '
        'INICIANDO PROYECTO UAX-1..."'
    )

    escribir_miedo(
        "EL EXPERIMENTO NO HA TERMINADO."
    )

    # Cambia este destino si tu historia utiliza otra escena.
    escena_actual = "combate_superado"


    escribir_lento("(Después de todo esto... te despiertas. Te despiertas y descubres que el cansancio te había podido una vez más)")
    time.sleep(3)
    escribir_lento("(Hacía mucho que no te dormías en la UAX, encima has tenido un sueño super raro, aunque no eres capaz de recordar exactamente qué pasaba en él)")
    time.sleep(3)
    escribir_lento("(Solo eres capaz de recordar que había una especie de Hulk gris en la universidad...)")
    time.sleep(2)
    escribir_lento("(Quizás sea hora de volver a casa...)")
    escribir_lento("(¿Por cierto, mañana no había niebla...?)")






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import time
import threading
import ipywidgets as widgets
from IPython.display import display, HTML


def decision_con_tiempo(pregunta, opciones, segundos=15):
    """
    opciones: diccionario como {"Esconderme": "esconderme",
                                 "Correr": "correr"}
    Devuelve la opción elegida o "tiempo" si se agota el plazo.
    """

    evento = threading.Event()
    resultado = {"valor": None}
    #Inicialmente apagado, si nadie responde, Python espera, cuando jugador pulsa un botón se activa, si se acaba t también se activa

    def elegir(valor): #Registra decisión, al ser not, solo se ejecuta si no se toma una decisión
        if not evento.is_set():
            resultado["valor"] = valor #Se registra el resultado del botón que se pulsa
            evento.set()

    # Creamos los botones que se verán
    botones = []

    for texto, valor in opciones.items(): #.items() para obtener las parejas clave-valor
        boton = widgets.Button( #Crea botón
            description=texto, #Con la descripción del texto que contenga
            button_style="danger", #Estilo rojo peligro
            layout=widgets.Layout(width="150px")
        )

        boton.on_click( #Registra cuando se ha pulsado un botón
            lambda b, v=valor: elegir(v) #Definir una pequeña función sin tener que escribir un def completo, ni puta idea vamos
        )

        botones.append(boton)

    # Mensaje que desaparece visualmente
    mensaje = HTML(f"""
    <div style="font-family: Arial; color: red;">
        <h3>{pregunta}</h3> #Título
        <p>¡Decide antes de que se agote el tiempo!</p> #Párrafo
        <div style="
            height: 6px;
            background: red;
            animation: desaparecer_barra {segundos}s linear forwards;
        "></div>
        <style>
        @keyframes desaparecer_barra {{
            from {{ width: 100%; opacity: 1; }}
            to   {{ width: 0%; opacity: 0; }}
        }}
        </style>
    </div>
    """)

    display(mensaje)
    display(widgets.HBox(botones))

    def agotar_tiempo():
        elegir("tiempo")

    temporizador = threading.Timer(
        segundos, agotar_tiempo
    )
    temporizador.start()

    # Esperamos hasta que el jugador responda o se agote el tiempo
    evento.on_click()
    temporizador.cancel()

    # Desactivamos los botones después de la decisión
    for boton in botones:
        boton.disabled = True

    return resultado["valor"]




dec2x1xb = decision_con_tiempo(
    "¡Oyes algo detrás de ti! ¿Qué haces?",
    {
        "Esconderme": "esconderme",
        "Correr": "correr",
        "Quedarme quieto": "quieto"
    },
    segundos=30
)

# Guardamos la decisión en tus variables actuales
respuestas["Decisión bajo presión"] = dec2x1xb

if dec2x1xb == "tiempo":
    escribir_lento(
        "Dudas demasiado. La sombra ya está detrás de ti..."
    )
    game_over()
    return

elif dec2x1xb == "esconderme":
    escribir_lento(
        "Te escondes detrás de un armario. "
        "La sombra pasa de largo."
    )

elif dec2x1xb == "correr":
    escribir_lento(
        "Sales corriendo por el pasillo..."
    )

elif dec2x1xb == "quieto":
    escribir_lento(
        "Contienes la respiración, esperando que no te vea."
    )


# In[ ]:


import random
import time

def combate_monstruo():
    global escena_actual

    total_turnos = 5
    turnos_superados = 0

    ataques = [
        "La criatura lanza una garra hacia tu cara.",
        "El monstruo se abalanza sobre ti desde un lateral.",
        "Una extremidad golpea la mesa donde te escondes.",
        "La criatura ruge y carga directamente contra ti.",
        "El monstruo intenta atraparte entre sus brazos."
    ]

    print()
    print("=" * 55)
    print_neon_caos(
        "COMBATE: PROYECTO UAX-0",
        color="red",
        vel_temblar="0.2s",
        vel_parpadeo="0.5s"
    )
    print("=" * 55)

    escribir_lento(
        "El laboratorio informático está a oscuras."
    )
    escribir_lento(
        "Los monitores parpadean. Algo respira al otro lado de la sala."
    )
    escribir_miedo(
        "LA CRIATURA SE PREPARA PARA ATACAR."
    )

    input("\nPulsa Enter para enfrentarte a ella...")

    # Cinco turnos que debes sobrevivir
    for turno in range(1, total_turnos + 1):

        print("\n" + "-" * 45)
        print(f"              TURNO {turno}/{total_turnos}")
        print("-" * 45)

        barra = "█" * turnos_superados + "░" * (
            total_turnos - turnos_superados
        )
        print(f"SUPERVIVENCIA: [{barra}]")
        print()

        escribir_miedo(random.choice(ataques))

        print("\n¿Qué haces?")
        print("1. Esquivar el ataque")
        print("2. Esconderte detrás de una mesa")
        print("3. Usar DETERMINACIÓN")

        while True:
            eleccion = input(
                "\nElige una acción (1/2/3): "
            ).strip().lower()

            if eleccion in ("1", "2", "3"):
                break

            print("¡Decide rápido! No tienes tiempo para dudar.")

        # Cada acción tiene una probabilidad de funcionar.
        if eleccion == "1":
            if random.random() < 0.80:
                escribir_lento(
                    "\n¡Esquivas el ataque por centímetros!"
                )
            else:
                escribir_miedo(
                    "\nLa criatura anticipa tu movimiento y te golpea."
                )
                game_over()
                return

        elif eleccion == "2":
            if random.random() < 0.65:
                escribir_lento(
                    "\nTe ocultas justo a tiempo. La criatura pasa de largo."
                )
            else:
                escribir_miedo(
                    "\n¡La mesa sale despedida por los aires!"
                )
                game_over()
                return

        elif eleccion == "3":
            inventario = estado_juego.setdefault("inventario", [])

            if "DETERMINACIÓN" not in inventario:
                escribir_lento(
                    "\nIntentas reunir valor, pero no tienes ningún objeto "
                    "que te ayude a resistir el ataque."
                )
                escribir_miedo(
                    "La criatura aprovecha tu vacilación y te alcanza."
                )
                game_over()
                return

            else:
                inventario.remove("DETERMINACIÓN")
                escribir_lento(
                    "\nRecuerdas tu reflejo en el baño y recuperas el valor."
                )
                escribir_lento(
                    "Aguantas el ataque sin retroceder."
                )

        turnos_superados += 1

        barra = "█" * turnos_superados + "░" * (
            total_turnos - turnos_superados
        )

        print(f"\nSUPERVIVENCIA: [{barra}]")
        escribir_lento(
            f"Has sobrevivido al turno {turno}."
        )
        time.sleep(1)

    # Plot twist: después del quinto turno
    print("\n" + "=" * 55)
    print_neon_caos(
        "ERROR DEL SISTEMA",
        color="red",
        vel_temblar="0.2s",
        vel_parpadeo="0.3s"
    )
    print("=" * 55)

    escribir_lento(
        "La criatura se detiene en seco."
    )
    escribir_lento(
        "Todos los monitores del laboratorio se encienden a la vez."
    )
    escribir_lento(
        "En la pantalla aparece un archivo oculto:"
    )

    print()
    print_neon_caos(
        "PROYECTO UAX-0: ENTIDAD AUTÓNOMA",
        color="#00D154",
        vel_temblar="0.1s",
        vel_parpadeo="0.5s"
    )

    escribir_miedo(
        "El monstruo no ha venido a cazarte."
    )
    escribir_miedo(
        "Está intentando impedir que llegues al servidor."
    )

    escribir_lento(
        "Una grabación comienza a reproducirse..."
    )
    escribir_lento(
        '"Si alguien está escuchando esto, el experimento ha escapado. '
        'No apaguéis el sistema: la entidad está conectada a él..."'
    )

    escribir_lento(
        "Entonces lo comprendes: el cuerpo de la criatura es una "
        "manifestación de la inteligencia artificial del laboratorio."
    )
    escribir_lento(
        "Y el servidor que la mantiene viva está justo detrás de ella."
    )

    print()
    escribir_miedo(
        "LA CRIATURA VUELVE A LEVANTARSE."
    )

    input(
        "\nPulsa Enter para correr hacia el interruptor de emergencia..."
    )

    escribir_lento(
        "Te lanzas hacia el cuadro eléctrico mientras la criatura "
        "intenta alcanzarte."
    )

    input(
        "\nPulsa Enter para desconectar el servidor..."
    )

    print()
    print_neon_caos(
        "SISTEMA DESCONECTADO",
        color="#00D154",
        vel_temblar="0.2s",
        vel_parpadeo="0.4s"
    )

    escribir_lento(
        "Las luces se apagan."
    )
    escribir_lento(
        "La criatura se queda inmóvil y se deshace en una nube de polvo."
    )
    escribir_lento(
        "Durante unos segundos solo escuchas tu propia respiración."
    )

    print()
    print_neon_caos(
        "HAS SOBREVIVIDO",
        color="#00D154",
        vel_temblar="0.2s",
        vel_parpadeo="0.5s"
    )

    escribir_lento(
        "Pero en uno de los monitores aparece una última línea:"
    )

    print()
    print(
        '"COPIA DE SEGURIDAD RESTAURADA. '
        'INICIANDO PROYECTO UAX-1..."'
    )

    escribir_miedo(
        "EL EXPERIMENTO NO HA TERMINADO."
    )

    # Cambia este destino si tu historia utiliza otra escena.
    escena_actual = "combate_superado"
    return

combate_monstruo()


# In[ ]:


import sys
import time

def escribir_lento(texto, velocidad=0.03):
    for letra in texto:
        # Imprime la letra sin dar un salto de línea automático
        sys.stdout.write(letra)
        # Fuerza a la terminal a mostrar el carácter inmediatamente
        sys.stdout.flush()
        # Pausa en segundos antes de la siguiente letra
        time.sleep(velocidad)
    input()
    print()  # Al terminar, da un salto de línea final - Added proper indentation
escribir_lento("Hola, me llamo Daniel, estoy viendo si esta cosa funciona para intentar ponerla en el juego")


# In[ ]:


import sys
import time

def escribir_sorpresa(texto, velocidad=0.001):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()  # Al terminar, da un salto de línea final - Added proper indentation
escribir_lento("Qué ha sido esosssssssssssssssssssssssssssssssssssssssssssss?")


# In[ ]:


def preguntar_lento(pregunta, velocidad=0.03):
    escribir_lento(pregunta, velocidad)
    respuesta = input()
    return respuesta
nombre = preguntar_lento("¿Cómo te llamas? ")
edad = preguntar_lento("¿Cuántos años tienes? ")

escribir_lento(f"Hola, {nombre}. Tienes {edad} años.")

# Creo una variable -> Le paso la condición de preguntar con una string, un enunciado -> Recibo respuesta
    ## Variable -> XXXXXXXXXXX -> Respuesta/valor


# In[ ]:


NO CORRER, EJEMPLO DE COMO HACER DECISIONES

estado_juego["inventario"].append("llave")
estado_juego["decisiones"]["abrio_puerta"] = True


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import time
import uuid
from IPython.display import HTML, Javascript, display

def mensaje_concreto_donde_si_no_no_funciona_mierda(
    texto,
    velocidad=0.1,
    color="red",
    font="Arial",
    weight="bold",
    vel_temblar="0.2s 50",
    duracion=None
):
    animacion_css = """
    <style>
    @keyframes temblar_dinamico {
        0%   { transform: translate(1px, 1px) rotate(0deg); }
        20%  { transform: translate(-2px, -1px) rotate(-2deg); }
        40%  { transform: translate(2px, 1px) rotate(2deg); }
        60%  { transform: translate(-1px, 2px) rotate(-1deg); }
        80%  { transform: translate(2px, -1px) rotate(1deg); }
        100% { transform: translate(1px, 1px) rotate(0deg); }
    }
    </style>
    """

    estilo = (
        f"color: {color}; "
        f"font-family: {font}; "
        f"font-weight: {weight}; "
        "display: inline-block; "
        f"animation: temblar_dinamico {vel_temblar} infinite linear;"
    )

    # Identificador único para este mensaje
    elemento_id = "mensaje_" + uuid.uuid4().hex

    # Creamos un contenedor identificable
    salida = display(
        HTML(
            animacion_css
            + f'<div id="{elemento_id}">'
            + f'<span style="{estilo}"></span>'
            + '</div>'
        ),
        display_id=True
    )

    contenido = ""

    for letra in texto:
        contenido += letra

        html = (
            animacion_css
            + f'<div id="{elemento_id}">'
            + f'<span style="{estilo}">{contenido}</span>'
            + '</div>'
        )

        salida.update(HTML(html))
        time.sleep(velocidad)

    # Programamos la eliminación únicamente si se ha indicado duración
    if duracion is not None:
        if duracion < 0:
            raise ValueError("duracion no puede ser negativa")

        display(Javascript(f"""
            setTimeout(() => {{
                const elemento = document.getElementById("{elemento_id}");
                if (elemento) {{
                    elemento.remove();
                }}
            }}, {duracion * 1000});
        """))

mensaje_concreto_donde_si_no_no_funciona_mierda("\tAyudAaAAa...", vel_temblar="3s 3", duracion=8)


# In[ ]:


from IPython.display import HTML, display
from IPython.display import Javascript
import uuid

def print_neon_caos(
    texto,
    color="#00ffff",
    font="Arial",
    weight="bold",
    vel_temblar="0.8s",
    vel_parpadeo="1.5s",
    duracion=None
):
    # Animaciones CSS
    css_animaciones = """
    <style>
    @keyframes temblar_dinamico {
      0%   { transform: translate(1px, 1px) rotate(0deg); }
      20%  { transform: translate(-1px, -2px) rotate(-1deg); }
      40%  { transform: translate(-2px, 0px) rotate(1deg); }
      60%  { transform: translate(0px, 2px) rotate(0deg); }
      80%  { transform: translate(1px, -1px) rotate(1deg); }
      100% { transform: translate(1px, 1px) rotate(0deg); }
    }

    @keyframes parpadear_dinamico {
      0%, 49% { opacity: 1; }
      50%, 99% { opacity: 0.1; }
      100% { opacity: 1; }
    }

    @keyframes desaparecer {
      0%   { visibility: visible; }
      99%  { visibility: visible; }
      100% { visibility: hidden; }
    }
    </style>
    """

    brillo_neon = (
        f"text-shadow: 0 0 5px {color}, "
        f"0 0 10px {color}, "
        f"0 0 20px {color}, "
        f"0 0 40px {color};"
    )

    animaciones = (
        f"temblar_dinamico {vel_temblar} infinite linear, "
        f"parpadear_dinamico {vel_parpadeo} infinite"
    )

    # La desaparición solo se añade si se solicita
    if duracion is not None:
        if duracion < 0:
            raise ValueError("duracion no puede ser negativa")

        animaciones += (
            f", desaparecer 0.01s linear {duracion}s forwards"
        )

    estilo_inline = (
        f"color: {color}; "
        f"font-family: {font}; "
        f"font-weight: {weight}; "
        f"{brillo_neon} "
        "display: inline-block; "
        f"animation: {animaciones};"
    )

    elemento_id = "neon_" + uuid.uuid4().hex

    html_final = (
        f'<div id="{elemento_id}">'
        f'{css_animaciones}'
        f'<span style="{estilo_inline}">{texto}</span>'
        f'</div>'
    )

    display(HTML(html_final))

    if duracion is not None:
        display(Javascript(f"""
            setTimeout(() => {{
                const elemento = document.getElementById("{elemento_id}");
                if (elemento) elemento.remove();
            }}, {duracion * 1000});
        """))




print_neon_caos(
    "Bienvenido...",
    color="#00ffff"
)

print_neon_caos(
    "¡CORRE!",
    color="red",
    duracion=3
)

print_neon_caos(
    "GAME OVER",
    color="red",
    vel_temblar="0s",
    vel_parpadeo="0s",
)


# In[ ]:


def game_over(duracion=5):
    print_neon_caos(
        "GAME OVER",
        color="red",
        vel_temblar="0s",
        vel_parpadeo="0s",
        duracion=duracion
    )


# In[ ]:


from IPython.display import HTML, display

def print_neon_caos(texto, color="#00ffff", font="Arial", weight="bold", vel_temblar="0.8s", vel_parpadeo="1.5s"):
    # Generamos el brillo neón usando múltiples capas de sombra
    brillo_neon = f"text-shadow: 0 0 5px {color}, 0 0 10px {color}, 0 0 20px {color}, 0 0 40px {color};"

    # Animaciones base fijas (solo los movimientos, sin velocidades fijas)
    css_animaciones = """
    <style>
    @keyframes temblar_dinamico {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      20% { transform: translate(-1px, -2px) rotate(-1deg); }
      40% { transform: translate(-2px, 0px) rotate(1deg); }
      60% { transform: translate(0px, 2px) rotate(0deg); }
      80% { transform: translate(1px, -1px) rotate(1deg); }
      100% { transform: translate(1px, 1px) rotate(0deg); }
    }

    @keyframes parpadear_dinamico {
      0%, 49% { opacity: 1; }
      50%, 99% { opacity: 0.1; }
      100% { opacity: 1; }
    }
    </style>
    """

    # Aquí está el truco: metemos 'vel_temblar' y 'vel_parpadeo' directamente en el estilo inline
    estilo_inline = (
        f'color: {color}; '
        f'font-family: {font}; '
        f'font-weight: {weight}; '
        f'{brillo_neon} '
        f'display: inline-block; '
        f'animation: temblar_dinamico {vel_temblar} infinite linear, '
        f'           parpadear_dinamico {vel_parpadeo} infinite;'
    )

    html_final = f'{css_animaciones}<span style="{estilo_inline}">{texto}</span>'
    display(HTML(html_final))

# 1. Movimiento súper lento y parpadeo pausado (Cartel viejo)
print_neon_caos("CARTEL LENTO", color="#ff007f", vel_temblar="2.0s", vel_parpadeo="3.0s")

# 2. Movimiento rápido y parpadeo rápido (Alerta urgente)
print_neon_caos("ALERTA RÁPIDA", color="#39ff14", vel_temblar="0.2s", vel_parpadeo="0.4s")

# 3. Solo tiembla a velocidad media, casi no parpadea
print_neon_caos("ESTABLE", color="#00ffff", vel_temblar="0.8s", vel_parpadeo="10s")


# In[ ]:


from IPython.display import HTML, display

def print_neon_caos(texto, color="#00ffff", font="Arial", weight="bold", vel_temblar="0.8s", vel_parpadeo="1.5s"):
    """
    Imprime texto con efecto Neón, temblor y parpadeo ajustables.
    - vel_temblar: Mayor tiempo (ej: '0.8s', '1s') hace que se mueva más lento.
    - vel_parpadeo: Mayor tiempo (ej: '1.5s', '2s') hace que parpadee más despacio.
    """
    # Definimos el color de la sombra (usamos el mismo color del texto para el brillo)
    brillo_neon = f"text-shadow: 0 0 5px {color}, 0 0 10px {color}, 0 0 20px {color}, 0 0 40px {color};"

    css_combinado = f"""
    <style>
    @keyframes temblar_lento {{
      0% {{ transform: translate(1px, 1px) rotate(0deg); }}
      20% {{ transform: translate(-1px, -2px) rotate(-1deg); }}
      40% {{ transform: translate(-2px, 0px) rotate(1deg); }}
      60% {{ transform: translate(0px, 2px) rotate(0deg); }}
      80% {{ transform: translate(1px, -1px) rotate(1deg); }}
      100% {{ transform: translate(1px, 1px) rotate(0deg); }}
    }}

    @keyframes parpadear_lento {{
      0%, 49% {{ opacity: 1; }}
      50%, 99% {{ opacity: 0.2; }} /* En lugar de 0, baja a 0.2 para que no desaparezca del todo */
      100% {{ opacity: 1; }}
    }}

    .efecto-neon-caos {{
      display: inline-block;
      /* Pasamos las nuevas variables de velocidad */
      animation: temblar_lento {vel_temblar} infinite linear, parpadear_lento {vel_parpadeo} infinite;
    }}
    </style>
    """

    # Estilos del texto incluyendo el brillo neón
    estilo_texto = f'color: {color}; font-family: {font}; font-weight: {weight}; {brillo_neon}'

    html_final = f'{css_combinado}<span class="efecto-neon-caos" style="{estilo_texto}">{texto}</span>'
    display(HTML(html_final))

# 1. Neón cian clásico (Movimiento pausado y parpadeo lento de cartel antiguo)
print_neon_caos("OPEN 24 HOURS", color="#00ffff", font="Courier New", vel_temblar="1.2s", vel_parpadeo="2.0s")

# 2. Neón rosa estilo Cyberpunk
print_neon_caos("🔮 MODO CYBERPUNK ACTIVADO", color="#ff007f", font="Arial", vel_temblar="0.7s", vel_parpadeo="1.3s")

# 3. Neón verde químico (Solo tiembla lento, sin parpadear - ponemos un tiempo de parpadeo gigante para anularlo)
print_neon_caos("☢️👻 CARGANDO NÚCLEO", color="#39ff14", weight="900", vel_temblar="1.5s", vel_parpadeo="999s")


# In[ ]:


from IPython.display import HTML, display

def print_parpadeo(texto, color="red", font="Arial", weight="bold", velocidad="0.8s"):
    # 1. Definimos la animación de parpadeo en CSS
    animacion_css = f"""
    <style>
    @keyframes parpadear {{
      0% {{ opacity: 1; }}
      49% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
      99% {{ opacity: 0; }}
      100% {{ opacity: 1; }}
    }}
    .efecto-parpadeo {{
      display: inline-block;
      animation: parpadear {velocidad} infinite; /* Controla la velocidad */
    }}
    </style>
    """

    # 2. Aplicamos tus estilos de diseño habituales
    estilo_texto = f'color: {color}; font-family: {font}; font-weight: {weight};'

    # 3. Renderizamos todo en el notebook
    html_final = f'{animacion_css}<span class="efecto-parpadeo" style="{estilo_texto}">{texto}</span>'
    display(HTML(html_final))

# 1. Alerta clásica estilo "Cargando..." o error
print_parpadeo("⚠️ PROCESANDO DATOS...", color="orange", weight="bold")

# 2. Parpadeo ultra rápido cambiando el parámetro de velocidad
print_parpadeo("¡ERROR CRÍTICO!", color="red", weight="900", velocidad="0.3s")

# 3. Un mensaje sutil y más lento
print_parpadeo("Pulsa Shift + Enter para continuar", color="gray", font="Courier New", velocidad="1.5s")


# In[ ]:


from IPython.display import HTML, display

def print_temblor(texto, color="red", font="Arial", weight="bold"):
    # 1. Definimos la animación de temblor en CSS
    animacion_css = """
    <style>
    @keyframes temblar {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      20% { transform: translate(-3px, 0px) rotate(1deg); }
      30% { transform: translate(0px, 2px) rotate(0deg); }
      40% { transform: translate(1px, -1px) rotate(1deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      60% { transform: translate(-3px, 1px) rotate(0deg); }
      70% { transform: translate(2px, 1px) rotate(-1deg); }
      80% { transform: translate(-1px, -1px) rotate(1deg); }
      90% { transform: translate(2px, 2px) rotate(0deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    .efecto-temblor {
      display: inline-block;
      animation: temblar 0s infinite; /* Hace que tiemble rápido y para siempre */
    }
    </style>
    """

    # 2. Aplicamos tus estilos personalizados junto con la animación
    estilo_texto = f'color: {color}; font-family: {font}; font-weight: {weight};'

    # 3. Juntamos todo y lo mostramos
    html_final = f'{animacion_css}<span class="efecto-temblor" style="{estilo_texto}">{texto}</span>'
    display(HTML(html_final))

# Alerta sísmica o error crítico
print_temblor("¡ALERTA: EL SISTEMA ESTÁ FALLANDO!", color="red", weight="900")

# Un texto divertido en verde
print_temblor("¡Tengo escalofríos!", color="#2ecc71", font="Courier New")



# In[ ]:


# from IPython.display import HTML, display

# def print_color(texto, color="black", weight="normal"):
#     display(HTML(f'<span style="color: {color}; font-weight: bold;">{texto}</span>'))

from IPython.display import HTML, display

def print_custom(texto, color="black", font="Arial", weight="normal"):
    # Construimos el estilo dinámico con el nuevo parámetro font-weight
    estilo = f'color: {color}; font-family: {font}; font-weight: {weight};'
    display(HTML(f'<span style="{estilo}">{texto}</span>'))

# Ejemplos de uso (admite nombres de colores o códigos Hex #HEX)
print_custom("Este texto es rojo brillante", "red", "Times New Roman", "400")
print_custom("Este texto es un azul personalizado", "#1a73e8", "Lucida Console", "bold")
print_color("green")


# In[ ]:


from IPython.display import HTML, display

def print_fondo(texto, color="black", font="Arial", weight="normal", fondo="transparent"):
    # Añadimos 'background-color' y un pequeño espacio de relleno (padding) para que se vea bien
    estilo = f'color: {color}; font-family: {font}; font-weight: {weight}; background-color: {fondo}; padding: 2px 6px; border-radius: 4px;'
    display(HTML(f'<span style="{estilo}">{texto}</span>'))

print_fondo("ÉXITO: El modelo se entrenó correctamente.", color="white", weight="bold", fondo="#2e7d32")
print_fondo("ERROR: No se encontraron valores en la columna.", color="white", weight="bold", fondo="#c62828")
print_fondo("ADVERTENCIA: Esta operación puede tardar unos minutos.", color="black", weight="normal", fondo="#fff9c4")
print_fondo("BIENVENIDOA A TERROR EN LA UAX", color="white", weight="bold", fondo="#852EFF")


# In[ ]:


nombre = "Carlos"
apellido = "Pérez"

# Si no pones " ", saldría "CarlosPérez"
nombre_completo = nombre + apellido 
print(nombre_completo) 
# Salida: Carlos Pérez


# In[ ]:


#time.sleep()
import time
print("Loading", end="")
for i in range (3):
    time.sleep(1)
    print(".", end="")
print("\n\nDone")


# In[ ]:


import time
print("Loading", end="")
for i in range (3):
    time.sleep(1)
    print(".", end="")
    print("", end="")
for i in range (3):
        time.sleep(2)
        print(".", end="")


# In[ ]:


escribir_lento(f"Hace mucho mucho tiempo")
escribir_lento("En una tierra muy muy lejana...")

