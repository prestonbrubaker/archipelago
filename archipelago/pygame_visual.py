import pygame
import ast
import threading

pygame.init()
size = 1200
window = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
node_size = 2
line_w = 1
font = pygame.font.Font(None, 24)  # Using a default font at size 24

data_array = []
line_data = []
statistics = []

# Descriptions for the statistics
stats_descriptions = [
    "World age: ",
    "Growth rate: ",
    "Population: "
]

def update_data():
    global data_array
    global line_data
    global statistics
    while True:
        try:
            with open('locations.txt', 'r') as file:
                data_string = file.read().strip()
            if data_string:
                new_data_array = ast.literal_eval(data_string)
                if new_data_array != data_array:
                    data_array = new_data_array
            else:
                print("Warning: Data string is empty.")
        except Exception as e:
            print(f"Error reading locations.txt: {e}")

        try:
            with open('muscles.txt', 'r') as file:
                line_string = file.read().strip()
            if line_string:
                new_line_data = ast.literal_eval(line_string)
                if new_line_data != line_data:
                    line_data = new_line_data
            else:
                print("Warning: Line data string is empty.")
        except Exception as e:
            print(f"Error reading muscles.txt: {e}")
        
        try:
            with open('statistics.txt', 'r') as file:
                stats_string = file.read().strip()
            if stats_string:
                new_stats = ast.literal_eval(stats_string)
                if new_stats != statistics:
                    statistics = new_stats
            else:
                print("Warning: Statistics data string is empty.")
        except Exception as e:
            print(f"Error reading statistics.txt: {e}")
        
        pygame.time.wait(10)

# Start the thread that updates data_array, line_data, and statistics
thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False
    
    window.fill((70, 70, 70))
    
    # Draw lines from line_data
    for line in line_data:
        x1, y1, x2, y2, line_type = line
        color = (0, 0, 255) if line_type == 1 else (255, 0, 0)  # Contracting is blue, expanding is red
        pygame.draw.line(window, color, (x1*size, y1*size), (x2*size, y2*size), line_w)
    
    # Draw rectangles from data_array
    for item in data_array:
        obj_type, x_unit, y_unit = item
        x = x_unit * size
        y = y_unit * size
        color = {
            0: (255, 0, 0),
            1: (0, 0, 255),
            2: (0, 255, 255),
            3: (0, 255, 0),
        }.get(obj_type, (255, 255, 0))  # Default color if type is not known
        pygame.draw.rect(window, color, (x - 0.5 * node_size, y - 0.5 * node_size, node_size, node_size))
    
    # Display statistics with descriptions
    for index, stat in enumerate(statistics):
        description = stats_descriptions[index] if index < len(stats_descriptions) else "Stat: "
        text = font.render(f"{description}{stat}", True, (255, 255, 255))
        window.blit(text, (10, 10 + 30 * index))  # Adjust position for each line
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
