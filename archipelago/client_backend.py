import time
import random

computer_id = [
  0, 0, 0, 0,  0, 0, 0, 0
]
world_id = [
  0, 0, 0, 0,  0, 0, 0, 0
]
organisms_gene_list = [  #2-D list of organism genes (organism index, genes)

]

organisms_state_list = [  #2-D list of organism state (organism index, state)

]

nodes_state_list = [      #3-D list of nodes (organism index, node index, node info)

]

muscles_state_list = [    #3-D list of muscles (organism index, muscle index, muscle info)

]




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
    0, 0, 0, 0,  1, 1, 0, 0,  # ACTION: Create a Node. The following with further indented comments is relevant data
    0, 0, 0, 0,  0, 0, 0, 0,    # Node ID
    1, 0, 0, 0,  0, 0, 0, 0,    # Mass of Node
    0, 0, 0, 0,  0, 0, 1, 0,    # Type of node (PHOTOSYNTHESIS)
    0, 0, 0, 0,  0, 0, 0, 0,    # Immutable Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Mutable data
    1, 0, 0, 0,  0, 0, 0, 0,    # Hue  (Hopefully green)
    1, 0, 0, 0,  0, 0, 0, 0,    # Saturation
    1, 0, 0, 0,  0, 0, 0, 0,    # Lighting
    0, 1, 0, 0,  0, 0, 0 ,0,    # X-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,    # X-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,    # X-coordinate
    0, 1, 0, 0,  0, 0, 0 ,0,    # Y-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,    # Y-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,    # Y-coordinate
    
    
    
    
  ]
