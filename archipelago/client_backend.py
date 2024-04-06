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
    0, 1, 0, 0,  0, 0, 0, 0,  # x-position
    0, 0, 0, 0,  0, 0, 0, 0,  # x-position
    0, 0, 0, 0,  0, 0, 0, 0,  # x-position
    0, 1, 0, 0,  0, 0, 0, 0,  # y-position
    0, 0, 0, 0,  0, 0, 0, 0,  # y-position
    0, 0, 0, 0,  0, 0, 0, 0,  # y-position
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

  node_state = [
  
  ]
  
  genetic_code = [
    0, 0, 0, 0
  ]
