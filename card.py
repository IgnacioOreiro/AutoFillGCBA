import pyautogui 
print("/t", pyautogui.displayMousePosition())
from screeninfo import get_monitors

monitor_width = monitor.width
monitor_height = monitor.height

# Calcula los puntos cardinales en función de las dimensiones del monitor
north = (monitor_width // 2, 0)
south = (monitor_width // 2, monitor_height)
east = (monitor_width, monitor_height // 2)
west = (0, monitor_height // 2)

# Simula clics en los puntos cardinales
pyautogui.click(north)
pyautogui.click(south)
pyautogui.click(east)
pyautogui.click(west)