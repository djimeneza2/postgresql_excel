#Importar el modulo
import pyautogui

#Se genera un ciclo de 10 veces
for i in range(20000):
        #Se mueve a la coordenada (100,100)
        pyautogui.moveTo(100,100,duration=1)
        #Se mueve a la coordenada (200,100)
        pyautogui.moveTo(300,100,duration=1)
        #Se mueve a la coordenada (200,200)
        pyautogui.moveTo(300,300,duration=1)
        #Se mueve a la coordenada (100;200)
        pyautogui.moveTo(100,300,duration=1)