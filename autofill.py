import pyautogui as pg
import time
import json

with open('csvjson.json', encoding='utf-8') as file:
    data = json.load(file)

for datos in data["votantes"]:
    pg.moveTo(493, 430, 0)
    pg.click()
    pg.moveTo(67, 355, 0)
    pg.click()
    pg.write(datos['Nombre'])
    pg.moveTo(67, 431, 0)
    pg.click()
    pg.write(datos['Apellido'])
    pg.moveTo(72, 673, 1)
    pg.click()
    pg.moveTo(78, 733, 1)  
    pg.click()
    pg.moveTo(556, 830, 0)
    pg.click()
    pg.moveTo(492, 430, 0)
    time.sleep(2)