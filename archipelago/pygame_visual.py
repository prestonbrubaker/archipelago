import pygame
import ast
import threading
import sys

pygame.init()
size = 1000
window = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
node_size = 4
line_w = 2
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
    "Total Food: ",
    "Birth Rate: ",
    "Sunlight Intake Rate: ",
    "Metabolism Rate: ",
    "Distance Change Rate: ",
    "Net Speed Rate: ",
    "Average Current Nodes: ",
    "Average Current Muscles: ",
    "Current Epoch Time (seconds): ",
    "Average Net Force: ",
    "Average Muscle Length: ",
    "Death Rate: ",
    "Average Age: "
]

def safely_evaluate_data(file_path, default):
    """Safely read and evaluate data from a file, returning the default if an error occurs."""
    try:
        with open(file_path, 'r') as file:
            data_string = file.read().strip()
        return ast.literal_eval(data_string) if data_string else default
    except Exception as e:
        print(f"Error reading or parsing {file_path}: {e}", file=sys.stderr)
        return default

def update_data():
    global data_array, line_data, statistics, light_values, draw_light_values_flag
    while True:
        try:
            with data_lock:
                data_updated = False

                new_data_array = safely_evaluate_data('locations.txt', data_array)
                if new_data_array != data_array:
                    data_array = new_data_array
                    data_updated = True

                new_line_data = safely_evaluate_data('muscles.txt', line_data)
                if new_line_data != line_data:
                    line_data = new_line_data
                    data_updated = True

                new_stats = safely_evaluate_data('statistics.txt', statistics)
                if new_stats != statistics:
                    statistics = new_stats
                    data_updated = True

                new_light_values = safely_evaluate_data('light_values.txt', light_values)
                if new_light_values != light_values:
                    light_values = new_light_values
                    data_updated = True

                if data_updated:
                    draw_light_values_flag = True

        except Exception as e:
            print(f"Unhandled error in update_data: {e}", file=sys.stderr)
        
        pygame.time.wait(10)

thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

def draw_light_values(light_values):
    rows = len(light_values)
    cols = len(light_values[0]) if rows > 0 else 0
    if cols == 0:  # Prevent division by zero
        return
    rect_width = size / cols
    rect_height = size / rows
    min_val = min(min(row) for row in light_values) if light_values else 0
    max_val = max(max(row) for row in light_values) if light_values and min_val != max(max(row) for row in light_values) else min_val + 1

    for y in range(rows):
        for x in range(cols):
            value = light_values[y][x]
            intensity = int(128 * (value - min_val) / (max_val - min_val)) if max_val > min_val else 0
            color = (intensity, intensity, intensity)
            pygame.draw.rect(window, color, (y * rect_width, x * rect_height, rect_width, rect_height))

def draw_statistics(statistics):
    y_offset = 10
    for idx, stat in enumerate(statistics):
        text = stats_descriptions[idx] + str(stat)
        label = font.render(text, 1, (255, 255, 255))
        window.blit(label, (10, y_offset))
        y_offset += label.get_height() + 5

running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False

    if draw_light_values_flag:
        window.fill((70, 70, 70))

        with data_lock:
            draw_light_values(light_values)
            for line in line_data:
                x1, y1, x2, y2, line_type = line
                color = (0, 0, 255) if line_type == 1 else (255, 0, 0)
                pygame.draw.line(window, color, (x1 * size, y1 * size), (x2 * size, y2 * size), line_w)
            for item in data_array:
                obj_type, x_unit, y_unit = item
                x = x_unit * size
                y = y_unit * size
                color = {0: (255, 0, 0), 1: (0, 0, 255), 2: (0, 255, 255), 3: (0, 255, 0), 4: (255, 255, 0)}.get(obj_type, (255, 255, 0))
                pygame.draw.rect(window, color, (x - 0.5 * node_size, y - 0.5 * node_size, node_size, node_size))
            draw_statistics(statistics)
        
            pygame.display.flip()
            clock.tick(20)
            draw_light_values_flag = False

pygame.quit()
