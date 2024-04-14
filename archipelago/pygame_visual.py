import pygame
import ast
import threading

pygame.init()
size = 1200
window = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()

data_array = []

def update_data():
    global data_array
    while True:
        try:
            with open('locations.txt', 'r') as file:
                data_string = file.read().strip()
            if data_string:  # Ensures that the string is not empty
                new_data_array = ast.literal_eval(data_string)
                if new_data_array != data_array:
                    data_array = new_data_array
            else:
                print("Warning: Data string is empty.")
        except SyntaxError as e:
            print(f"Syntax error in data file: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        pygame.time.wait(10) 

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
        window.fill((70, 70, 70))
        for item in data_array:
            obj_type, x_unit, y_unit = item
            x = x_unit * size
            y = y_unit * size
            color = {
                0: (255, 0, 0),
                1: (0, 0, 255),
                2: (0, 255, 255),
                3: (255, 0, 0),
            }.get(obj_type, (255, 255, 0))  # Default color if type is not known
            
            pygame.draw.rect(window, color, (x, y, 5, 5))
        pygame.display.flip()
    
    clock.tick(60)  # This caps the frame rate at 60 FPS

pygame.quit()
