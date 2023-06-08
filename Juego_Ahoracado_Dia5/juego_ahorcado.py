from random import choice

palabras=['panadero','goku','inteligencia','dentista','desarrollador','tiburon']

letras_correctas=[]
letras_incorrectas=[]
intento=6
aciertos=0
juego_terminado= False

#Se inicia la accion para control de lista de palabras que selecciona
def elegir_palabra(lista_palabras):
    palabra_elegida= choice(lista_palabras)
    letras_unicas= len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario ='abcdefghijklmnñopqrstuvwxyz'
    
    while not es_valida:
       letra_elegida = input("Elige una letra: ").lower()
       if letra_elegida in abecedario and len(letra_elegida)==1:
           es_valida = True
       else:
           print("Esa letra no es valida")
    return letra_elegida       
    