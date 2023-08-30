#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import *

from procurando_azul import * # importando tudo da biblioteca ev3dev2.sensor.lego
from curva import *
from comeco import *
from arruma import *
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

corCS1 = 0
corCS2 = 0

CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'
#US.mode = 'US-DIST-CM'
IS.mode = 'IR-PROX'
GS.mode = 'GYRO-ANG'
#TS.mode = 'TOUCH'


def comeco(): # para evitar alguns erros, fizemos isso para começar o robo resetando o sensor de gyro
    global rotina
    if IS.proximity <= 10: # quando o sensor infravermelho detectar algo a frente, ele da sequencia ao código
        GS.reset() # reseta o sensor de gyro
        time.sleep(.2) #espera
    else:
        print("aguardando")