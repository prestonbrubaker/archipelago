import pygame
import ast
import threading

pygame.init()

window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

data_array = []

def update_data():
    global data_array
    while True:
        with open('locations.txt', 'r') as file:
            data_string = file.read()
        new_data_array = ast.literal_eval(data_string)
        if new_data_array != data_array:
            data_array = new_data_array
        pygame.time.wait(1) 

# Start the thread that updates data_array
thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if data_array:
        window.fill((0, 0, 0))
        for item in data_array:
            obj_type, x_unit, y_unit = item
            x = x_unit * 800
            y = y_unit * 800
            color = (255, 0, 0) if obj_type == 0 else (0, 255, 0)
            pygame.draw.rect(window, color, (x, y, 5, 5))
        pygame.display.flip()
    
    clock.tick(10)  # This caps the frame rate at 10 FPS

pygame.quit()
