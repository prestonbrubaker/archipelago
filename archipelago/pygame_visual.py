import pygame
import ast
import time

pygame.init()

window = pygame.display.set_mode((800, 800))



while True:
  with open('locations.txt', 'r') as file:
      data_string = file.read()
  data_array = ast.literal_eval(data_string)
  window.fill((0, 0, 0))
  for i in range(0, len(data.array)):
    type = data.array[i][0]
    x_unit = data.array[i][1]
    y_unit = data.array[i][2]
    x = x_unit * 800
    y = y_unit * 800
    pygame.draw.rect(window, (255, 0, 0), (x, y, 5, 5))
  pygame.display.flip()
