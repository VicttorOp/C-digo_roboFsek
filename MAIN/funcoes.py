#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

# ---------- Cria os motores do objeto
motorA = LargeMotor(OUTPUT_A) # Setando o motor na saida A como motorA
motorB = LargeMotor(OUTPUT_B) # Setando o motor na saida B como motorB
#motorC = LargeMotor(OUTPUT_C) # setando o motor na saída C como motorC
#motorD = LargeMotor(OUTPUT_D) # setando o motor na saída D como motorD

left_motor = motorA # Traduzindo que o motorA como motor da esquerda
right_motor = motorB # Traduzindo que o motorB como motor da direita
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B) # Setando o comando Tank_drive para utilizar os motores A e B juntos
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B) # Setando o comando steering_drive para utilizar a curva com os motores A e B

#spkr = Sound() # Setando a variavel som
#btn = Button() # Setando a variavel botao
#radio = Radio()  # Setando a variavel radio

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 
IS = InfraredSensor(INPUT_4)
##US = UltrasonicSensor(INPUT_4)  # setando sensor ultrasonico na entrada 
GS = GyroSensor(INPUT_3) # setando o sensor de giro na entra 
#TS = TouchSensor(INPUT_4) # setando o sensor de toque na entrada 
#color_sensor_in5 = ColorSensor(INPUT_5) # setando sensor de cor na entrada
SEM_COR = 0
PRETO = 1
AZUL = 2
VERDE = 3
AMARELO = 4
VERMELHO = 5
BRANCO = 6
MARROM = 7

global rotina
rotina = 0 
cores = 0

corCS1 = 0
corCS2 = 0

CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'
#US.mode = 'US-DIST-CM'
IS.mode = 'IR-PROX'
GS.mode = 'GYRO-ANG'
#TS.mode = 'TOUCH'


# -----------------------------------------------------------

"""def parede():
    global rotina
    if (CS1.color == 1 or 4) and (CS2.color == 1 or 4):
        if CS1.color == 1 and CS2.color == 4: # se o sensor 1 for igual a preto e o sensor 2 for igual a amarelo, o robo vira 90 graus
            tank_drive.on(0,0)
            arruma()
            time.sleep(.1)
            volta90()
            print("preto, amarelo")
            print("volta 90 graus")
        elif CS2.color == 1 and CS1.color == 4: # se o sensor 2 for igual a preto e o sensor 1 for igual amarelo, o robo vira 90 graus
            tank_drive.on(0,0)
            arruma()
            time.sleep(.1)
            volta90()
            print("amarelo, preto")
            print("volta 90 graus")
        elif CS1.color == 1 and CS2.color == 1: # se os 2 sensores forem iguais a preto, o robo vira 90 graus
            tank_drive.on(0,0)
            arruma()
            time.sleep(.1)
            volta90()
            print("preto, preto")
            print("volta 90 graus")
        elif CS1.color == 4 and CS2.color == 4: # se os 2 sensores forem iguais a amarelo, o robo vira 90 graus
            tank_drive.on(0,0)
            time.sleep(.1)
            volta90()   
            print("amarelo, amarelo")
            print("volta 90 graus")
    elif CS1.color == 5 and CS2.color == 5: # se os sensores forem iguais a vermelho, o robo vira 180 graus
        tank_drive.on(0,0)
        time.sleep(.1)
        volta180()
        print("vermelho, vermelho")
        print("volta 180 graus")
    else: # depois q ele realiza uma dessas tarefas, ele volta a procurar o azul
        print("sai da parede")
        time.sleep(0.1)    """

# -----------------------------------------------------------

def procurando_azul(): # caso a rotina seja igual a 1, ele começa a a procurar a zona azul
    global rotina
    if (corCS1 and corCS2) == 6: # caso os 2 sensores sejam iguais a branco, ele começa a andar para frente
        tank_drive.on(10,10)
    elif corCS1 and corCS2 == 2: # caso os sensores sejam iguais a azul, ele para e printa o "achei!!!!"
        print("achei!!!!")
        rotina += 2
    elif (corCS1 or corCS2) != 6 or (CS1.color or CS2.color) != 2: # caso os sensores detectem alguma parede, ele aumenta 1 a rotina
        print("parede a frente")

# -----------------------------------------------------------

    