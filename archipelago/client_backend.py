import time
import random

computer_id = [
  0, 0, 0, 0,  0, 0, 0, 0
]
world_id = [
  0, 0, 0, 0,  0, 0, 0, 0
]

age_of_world = [
  0, 0, 0, 0,  0, 0, 0, 0,
  0, 0, 0, 0,  0, 0, 0, 0,
  0, 0, 0, 0,  0, 0, 0, 0,
  0, 0, 0, 0,  0, 0, 0, 0,
  0, 0, 0, 0,  0, 0, 0, 0,
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
    0, 0, 0, 0,  0, 1, 1, 0,  # Organism ID
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  0, 0, 0, 0,  # Family Name
    0, 0, 0, 0,  1, 0, 0, 1,  # Family Name
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
    0, 0, 0, 0,  0, 0, 0, 0,  # Index
    0, 0, 0, 0,  0, 0, 0, 0,  # Index
    0, 0, 0, 0,  0, 0, 0, 0,  # Time alive
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
    0, 1, 0, 0,  0, 0, 0 ,0,  # X-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # X-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # X-coordinate
    0, 1, 0, 0,  0, 0, 0 ,0,  # Y-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # Y-coordinate
    0, 0, 0, 0,  0, 0, 0 ,0,  # Y-coordinate
  ]

  muscles_state = []
  
  nodes_state.append(node_state)  # Adding the soul node to the seed organism

  genetic_code = [
    0, 0, 0, 1,  0, 0, 1, 1,  # ACTION 19: Create a Node. The following with further indented comments is relevant data for node, and 2 indents for muscle info
    1, 1, 1, 1,  1, 1, 1, 1,    # Mass
    0, 0, 0, 0,  0, 0, 1, 1,    # Type Photosynthesis
    1, 1, 1, 1,  1, 1, 1, 1,    # X-offset as a fraction of maximum
    0, 0, 0, 0,  0, 0, 0, 0,    # Y-offset as a fraction of maximum
    0, 1, 0, 0,  0, 0, 0, 0,      # Contracted muscle length
    1, 1, 1, 1,  1, 1, 1, 1,      # Expanded muscle length
    1, 1, 1, 1,  1, 1, 1, 1,      # Spring constant of the muscle
    0, 0, 0, 1,  0, 1, 0, 1,  # ACTION 21: Toggle muscle
    0, 0, 0, 0,  1, 1, 1, 0,  # ACTION 14: Store a random value up to Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1
    0 ,0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 1,  1, 0, 0, 0,    # Data 3 (20)
    0, 0, 0, 0,  1, 0, 0, 0,  # ACTION 4: Swap register 1 and register 2
    0, 0, 0, 0,  0, 0, 0, 1,  # ACTION 1: Store Data in register 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 0,  0, 0, 0, 1,    # Data 3 (1)
    0, 0, 0, 0,  0, 1, 0, 0,  # ACTION 4: Swap register 1 and register 2
    0, 0, 0, 0,  1, 1, 0, 0,  # ACTION 12: Subtract register 2 from register 1 and store the result in register 3
    0, 0, 0, 0,  1, 0, 0, 0,  # ACTION 8: Check to see if the value in register 2 is more than the value in register 1, and change the index by the following is this is true
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1 (first bit of this line indicates backwards travel)
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 1,  0, 0, 0, 0,    # Data 3 (16)
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION 2: Swap the values in registers 1 and 3
    0, 0, 0, 0,  1, 1, 1, 1,  # ACTION 15: Change the index by Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1 (first bit of this line indicates backwards travel)
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 0,  1, 0, 1, 0,    # Data 3 (10)
  ]
  
  organisms_gene_list.append(genetic_code)
  organisms_state_list.append(initial_state)
  nodes_state_list.append(nodes_state)
  muscles_state_list.append(muscles_state)


def read_byte(list_in, index_in, num_lines_in):    # Converts the "index_in"th and "num_lines_in" following byte(s) to decimal from list list_in
  value = 0
  for i in range(0, 8 * num_lines_in):
    if (i < len(list_in)):
      value += 2**(8 * num_lines_in - 1 - i) * list_in[i + index_in * 8]
  return value

seed_organism()

comp_id_dec = read_byte(computer_id, 0, 1)
print("Computer's ID: " + str(comp_id_dec))
world_id_dec = read_byte(world_id, 0, 1)
print("World's ID: " + str(world_id_dec))

print("Genetic Code: " + str(organisms_gene_list))
print("Initial State: " + str(organisms_state_list))
print("Initial Nodes States: " + str(nodes_state_list))
print("Initial Muscles States: " + str(muscles_state_list))



def main_loop():
  while True:
    for i in range(0, len(organisms_state_list)):    # Iterate through organisms

      age_of_world_dec = read_byte(age_of_world, 0, 6)
      print("AGE OF WORLD: " + str(age_of_world))
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

      # READ THROUGH THE STATE OF THE ORGANISM
      org_id = read_byte(organisms_state_list[i], 0, 6)    # Retrieve the organism's ID
      print("Organism's ID: " + str(org_id))
      org_fam_id = read_byte(organisms_state_list[i], 6, 5)  # Retrieve the organism's family ID
      print("Organism's Family ID: " + str(org_fam_id))
      org_energy = read_byte(organisms_state_list[i], 11, 1)  # Retrieve the organism's energy level
      print("Organism's Energy Level: " + str(org_energy))
      selected_node_one = read_byte(organisms_state_list[i], 12, 1) # Retrieve the organism's 1st selected node
      print("Organism's First Selected Node: " + str(selected_node_one))
      selected_node_two = read_byte(organisms_state_list[i], 13, 1) # Retrieve the organism's 2nd selected node
      print("Organism's Second Selected Node: " + str(selected_node_two))
      register_one = read_byte(organisms_state_list[i], 14, 3) # Retrieve the organism's 1st register value
      print("Organism's First Register Value: " + str(register_one))
      register_two = read_byte(organisms_state_list[i], 17, 3) # Retrieve the organism's 2nd register value
      print("Organism's Second Register Value: " + str(register_two))
      register_three = read_byte(organisms_state_list[i], 20, 3) # Retrieve the organism's 3rd register value
      print("Organism's Third Register Value: " + str(register_three))
      index = read_byte(organisms_state_list[i], 23, 2)  # Retrieve the organism's index for it's genes
      print("Organism's Index: " + str(index))
      time_alive = read_byte(organisms_state_list[i], 25, 3) # Retrieve the time the organism has been alive
      print("Time Organisms Has Been Alive: " + str(time_alive))


      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
      # EXECUTE GENE AT THE CURRENT INDEX

      action = read_byte(organisms_gene_list[i], index, 1)
      print("Current Action of Organism: " + str(action))

      if(action == 19):
        print("Action to be Executed: Creation of a New Node")
        mass = read_byte(organisms_gene_list[i], index + 1, 1)  # Mass of new node
        print("Mass of New Node: " + str(mass))
        node_type = read_byte(organisms_gene_list[i], index + 2, 1)  # Node type
        print("Node Type: " + str(node_type))
        if(node_type == 0):
          print("Node Type Name: Soul")
        elif(node_type == 1):
          print("Node Type Name: Structual")
        elif(node_type == 2):
          print("Node Type Name: Gripper")
        elif(node_type == 3):
          print("Node Type Name: Photosynthesis")
        x_offset = read_byte(organisms_gene_list[i], index + 3, 1)  # X-Offset
        print("X-Offset: " + str(x_offset))
        y_offset = read_byte(organsims_gene_list[i], index + 4, 1)  # Y-Offset
        print("Y-Offset: " + str(y_offset))
        contracted_muscle_len = read_byte(organisms_gene_list[i], index + 5, 1)  # Contracted Muscle Length
        print("Contracted Muscle Length: " + str(contracted_muscle_len))
        expanded_muscle_len = read_byte(organisms_gene_list[i], index + 6, 1)  # Expanded Muscle Length
        print("Expanded Muscle Length: " + str(expanded_muscle_len))
        spring_constant = read_byte(organisms_gene_list[i], index + 7, 1)  # Spring Constant
        print("Spring Constant of Muscle: " + str(spring_constant))

        
        
        
      
      
      
    time.sleep(10)

main_loop()
