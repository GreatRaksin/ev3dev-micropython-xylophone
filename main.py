#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# --- XYLOPHONE ---


LM = Motor(Port.B) # определяем левый мотор
RM = Motor(Port.C) # определяем правый мотор

WD = 56 # диаметр колес
AT = 114 # расстояние между колесами

Robot = DriveBase(LM, RM, WD, AT) # переменная для робота

Eyes = ColorSensor(Port.S1) # переменная для датчика цвета

while True:
    Robot.drive(100, 0) # робот постоянно едет вперед со скоростью 100 градусов в секунду и градусом поворота 0
    
    """
    Теперь задача робота воспроизводить различные звуки, если он видит цвета.
    Решение задачи реализуется при помощи обычного условия, где мы сравниваем
    значение цвета, полученного от датчика.
    """
    if Eyes.color() == Color.YELLOW:
        brick.sound.beep(1000, 500, 50)
    elif Eyes.color() == Color.BLUE:
        brick.sound.beep(1500, 500, 50)
    elif Eyes.color() == Color.RED:
        brick.sound.beep(1200, 500, 50)
    elif Eyes.color() == Color.WHITE:
        brick.sound.beep(500, 500, 50)
    elif Eyes.color() == Color.GREEN:
        brick.sound.beep(2000, 500, 50)