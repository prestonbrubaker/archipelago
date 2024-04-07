import time
import random

computer_id = [
  0, 0, 0, 0,  0, 0, 0, 0
]
world_id = [
  0, 0, 0, 0,  0, 0, 0, 0
]

# Organism specific global variables

organisms_gene_list = [  #2-D list of organism genes (organism index, genes)

]

organisms_state_list = [  #2-D list of organism state (organism index, state)

]

nodes_state_list = [      #3-D list of nodes (organism index, node index, node info)

]

muscles_state_list = [    #3-D list of muscles (organism index, muscle index, muscle info)

]

# Parameters for the environment or general rules

max_node_offset = 0.05    # Maximum horizontal or vertical distance (as a fraction of the screen) a node can be placed when an action to produce a new node is called
spring_multiplier = 0.01  # Multiplier for the maximum spring constant



def seed_organism():
  initial_state = [
    0, 0, 0, 0,  0, 0, 0, 0,  # Organism ID
    0, 0, 0, 0,  0, 0, 0, 0,  # Organism ID
    0, 0, 0, 0,  0, 0, 0, 0,  # Organism ID
    0, 0, 0, 0,  0, 0, 0, 0,  # Organism ID
    0, 0, 0, 0,  0, 0, 0, 0,  # Organism ID
    0, 0, 0, 0,  0, 0, 0, 0,  # Organism ID
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 1, 0, 0,  0, 0, 0, 0,  # Energy
    0, 0, 0, 0,  0, 0, 0, 0,  # Selected Node 1
    0, 0, 0, 0,  0, 0, 0, 0,  # Selected Node 2
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 1
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 1
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 1
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 2
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 2
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 2
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 3
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 3
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 3
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 4
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 4
    0, 0, 0, 0,  0, 0, 0, 0,  # Register 4
    0, 0, 0, 0,  0, 0, 0, 0,  # Index
    0, 0, 0, 0,  0, 0, 0, 0,  # Time alive
    0, 0, 0, 0,  0, 0, 0, 0,  # Time alive
  ]

  nodes_state = []
  
  node_state = [
    0, 0, 0, 0,  0, 0, 0, 0,  # Node ID
    1, 0, 0, 0,  0, 0, 0, 0,  # Mass of Node
    0, 0, 0, 0,  0, 0, 0, 0,  # Type of node (SOUL)
    0, 0, 0, 0,  0, 0, 0, 0,  # Immutable Data
    0, 0, 0, 0,  0, 0, 0, 0,  # Mutable data
    0, 0, 0, 0,  0, 0, 0, 0,  # Hue
    1, 0, 0, 0,  0, 0, 0, 0,  # Saturation
    1, 0, 0, 0,  0, 0, 0, 0,  # Lighting
    0, 1, 0, 0,  0, 0, 0 ,0,  # X-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # X-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # X-coordinate
    0, 1, 0, 0,  0, 0, 0 ,0,  # Y-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # Y-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # Y-coordinate
  ]
  
  nodes_state.append(node_state)  # Adding the soul node to the seed organism
  genetic_code = [
    0, 0, 0, 0,  1, 1, 0, 0,  # ACTION: Create a Node. The following with further indented comments is relevant data for node, and 2 indents for muscle info
    1, 0, 0, 0,  0, 0, 0, 0,    # Mass of Node
    0, 0, 0, 0,  0, 0, 1, 0,    # Type of node (PHOTOSYNTHESIS)
    0, 0, 0, 0,  0, 0, 0, 0,    # Immutable Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Mutable data
    1, 0, 0, 0,  0, 0, 0, 0,    # Hue  (Hopefully green)
    1, 0, 0, 0,  0, 0, 0, 0,    # Saturation
    1, 0, 0, 0,  0, 0, 0, 0,    # Lighting
    0, 1, 0, 0,  0, 0, 0 ,0,    # X-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # X-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # X-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # Y-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # Y-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # Y-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 1,  0, 0, 0, 0,      # Minimum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Minimum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Minimum Length
    1, 0, 0, 0,  0, 0, 0, 0,      # Maximum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Maximum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Maximum Length
    1, 0, 0, 0,  0, 0, 0, 0,      # Initial Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Initial Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Initial Length
    1, 0, 0, 0,  0, 0, 0, 0,      # Spring Contant
    0, 0, 0, 0,  0, 0, 0, 0,      # Mutable Data
    0, 0, 0, 0,  0, 0, 0, 0,      # Hue
    1, 0, 0, 0,  0, 0, 0, 0,      # Saturation
    1, 0, 0, 0,  0, 0, 0, 0,      # Lighting
    0, 0, 0, 0,  0, 0, 0, 1,  # ACTION: Store following Data (1) in register 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 1,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 1,  # ACTION: Store following Data (32) in register 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 1, 0,  0, 0, 0, 1,    # Data
    0, 0, 0, 0,  0, 1, 1, 0,  # ACTION: Subtract register 2 from register 1, and store the result in register 3
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 0, 0,  # ACTION: Jump forward (92) if register 1 and 2 are equal
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 1, 0, 1,  1, 1, 0, 0,    # Data (92)
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 1,  # ACTION: Clear the first register
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  1, 0, 0, 0,  # ACTION: Swap registers 1 and 2
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 0,  # ACTION: Subtract register 2 from register 1, and store the result in register 3
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 1,  # ACTION: Goto the section (52) where registers 1 and two are being checked
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 1, 1,  0, 1, 0, 0,    # Data  (52)
    0, 0, 0, 0,  1, 1, 0, 0,  # ACTION: Create a Node. The following with further indented comments is relevant data for node, and 2 indents for muscle info
    1, 0, 0, 0,  0, 0, 0, 0,    # Mass of Node
    0, 0, 0, 0,  0, 0, 1, 0,    # Type of node (Gripper)
    0, 0, 0, 0,  0, 0, 0, 0,    # Immutable Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Mutable data
    0, 1, 0, 0,  0, 0, 0, 0,    # Hue  
    1, 0, 0, 0,  0, 0, 0, 0,    # Saturation
    1, 0, 0, 0,  0, 0, 0, 0,    # Lighting
    0, 1, 0, 0,  0, 0, 0 ,0,    # X-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # X-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # X-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 1, 0, 0,  0, 0, 0 ,0,    # Y-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # Y-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 0,  0, 0, 0 ,0,    # Y-coordinate addition (if more than half) or subtraction from selected node, to be scaled by max value
    0, 0, 0, 1,  0, 0, 0, 0,      # Minimum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Minimum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Minimum Length
    1, 0, 0, 0,  0, 0, 0, 0,      # Maximum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Maximum Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Maximum Length
    1, 0, 0, 0,  0, 0, 0, 0,      # Initial Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Initial Length
    0, 0, 0, 0,  0, 0, 0, 0,      # Initial Length
    1, 0, 0, 0,  0, 0, 0, 0,      # Spring Contant
    0, 0, 0, 0,  0, 0, 0, 0,      # Mutable Data
    0, 0, 0, 0,  0, 0, 0, 0,      # Hue
    1, 0, 0, 0,  0, 0, 0, 0,      # Saturation
    1, 0, 0, 0,  0, 0, 0, 0,      # Lighting
    0, 0, 0, 1,  0, 0, 0, 1,  # ACTION: Clear the first register
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 1,  # ACTION: Clear the first register
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 1,  # ACTION: Clear the first register
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 1,  # ACTION: Clear the first register
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 1,  # ACTION: Clear the first register
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 1,  # ACTION: Store following Data (1) in register 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 1,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 1,  # ACTION: Store following Data (32) in register 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 1, 0,  0, 0, 0, 1,    # Data
    0, 0, 0, 0,  0, 1, 1, 0,  # ACTION: Subtract register 2 from register 1, and store the result in register 3
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 0, 0,  # ACTION: Jump forward (228) if register 1 and 2 are equal
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    1, 1, 1, 0,  0, 1, 0, 0,    # Data (228)
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 1,  # ACTION: Clear the first register
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  1, 0, 0, 0,  # ACTION: Swap registers 1 and 2
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 1, 1, 0,  # ACTION: Subtract register 2 from register 1, and store the result in register 3
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION: Cycle the registers forward
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 1, 1,  # ACTION: Goto the section (184) where registers 1 and two are being checked
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    1, 0, 1, 1,  1, 0, 0, 0,    # Data  (184)
    0, 0, 0, 0,  0, 0, 1, 1,  # ACTION: Goto the section (124) where registers 1 and two are being checked
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data
    0, 1, 1, 1,  1, 1, 0, 0,    # Data  (124)
    
    
    
    
    
    
    
    
    
    
    
    
    
  ]
