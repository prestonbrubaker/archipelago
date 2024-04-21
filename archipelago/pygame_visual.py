import pygame
import ast
import threading

pygame.init()
size = 1000
window = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
node_size = 2
line_w = 1
font = pygame.font.Font(None, 24)

data_array = []
line_data = []
statistics = []
light_values = []

# Lock for synchronizing access to shared data
data_lock = threading.Lock()

# Flag to indicate when it's safe to draw light values
draw_light_values_flag = False

stats_descriptions = [
    "World age: ",
    "Population: ",
    "Total Food: "
]

def update_data():
    global data_array, line_data, statistics, light_values
    while True:
        try:
            with data_lock:
                with open('locations.txt', 'r') as file:
                    data_string = file.read().strip()
                new_data_array = ast.literal_eval(data_string) if data_string else []
                if new_data_array != data_array:
                    data_array = new_data_array

                with open('muscles.txt', 'r') as file:
                    line_string = file.read().strip()
                new_line_data = ast.literal_eval(line_string) if line_string else []
                if new_line_data != line_data:
                    line_data = new_line_data

                with open('statistics.txt', 'r') as file:
                    stats_string = file.read().strip()
                new_stats = ast.literal_eval(stats_string) if stats_string else []
                if new_stats != statistics:
                    statistics = new_stats

                with open('light_values.txt', 'r') as file:
                    light_string = file.read().strip()
                new_light_values = ast.literal_eval(light_string) if light_string else []
                if new_light_values != light_values:
                    light_values = new_light_values

        except Exception as e:
            print(f"Error reading file: {e}")
        
        pygame.time.wait(10)

thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

def draw_light_values(light_values):
    if not draw_light_values_flag or not light_values:
        return

    rows = len(light_values)
    cols = len(light_values[0]) if rows > 0 else 0
    rect_width = size / cols
    rect_height = size / rows
    min_val = min(min(row) for row in light_values) if light_values else 0
    max_val = max(max(row) for row in light_values) if light_values and min_val != max(max(row) for row in light_values) else min_val + 1

    for y in range(rows):
        for x in range(cols):
            value = light_values[y][x]
            intensity = int(128 * (value - min_val) / (max_val - min_val)) if max_val > min_val else 0
            color = (intensity, intensity, intensity)
            pygame.draw.rect(window, color, (x * rect_width, y * rect_height, rect_width, rect_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False

    window.fill((70, 70, 70))
    draw_light_values_flag = False  # Reset the flag
    
    with data_lock:
        for line in line_data:
            x1, y1, x2, y2, line_type = line
            color = (0, 0, 255) if line_type == 1 else (255, 0, 0)
            pygame.draw.line(window, color, (x1 * size, y1 * size), (x2 * size, y2 * size), line_w)
        for item in data_array:
            obj_type, x_unit, y_unit = item
            x = x_unit * size
            y = y_unit * size
            color = {0: (255, 0, 0), 1: (0, 0, 255), 2: (0, 255, 255), 3: (0, 255, 0)}.get(obj_type, (255, 255, 0))
            pygame.draw.rect(window, color, (x - 0.5 * node_size, y - 0.5 * node_size, node_size, node_size))

        # All nodes and muscles have been drawn, now it's safe to draw the light values
        draw_light_values_flag = True

    if draw_light_values_flag:
        draw_light_values(light_values)
    
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
