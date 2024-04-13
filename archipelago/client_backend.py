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



def write_byte(list_in, index_in, num_lines_in, value_in):  # Takes in a list and a value and converts the value to binary and overwrites the current selection with the value
  for i in range(0, 8 * num_lines_in):  # Overwrite current contents with 0
    index_i = i + index_in * 8
    if(index_i >= len(list_in)):
      list_in.append(0)      # This will expand the list if new information is being added to the end of list_in
    else:
      list_in[i + index_in * 8] = 0
  for i in range(0, 8 * num_lines_in):
    value = 2**(8 * num_lines_in - 1 - i)
    if(value_in >= value):
      list_in[i + index_in * 8] = 1
      value_in -= value
  return list_in

seed_organism()

print("\n~~~~~~~~~~~~~~~~~~~~COMPUTER AND WORLD STATE~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

comp_id_dec = read_byte(computer_id, 0, 1)
print("Computer's ID: " + str(comp_id_dec))
world_id_dec = read_byte(world_id, 0, 1)
print("World's ID: " + str(world_id_dec))

print("\n~~~~~~~~~~~~~~~~~~~~SEED ORANISM INITIAL CONDITIONS~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print("Genetic Code: " + str(organisms_gene_list))
print("Initial State: " + str(organisms_state_list))
print("Initial Nodes States: " + str(nodes_state_list))
print("Initial Muscles States: " + str(muscles_state_list))



def main_loop():
  global age_of_world
  
  while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~STATE OF WORLD~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    age_of_world_dec = read_byte(age_of_world, 0, 6)
    print(age_of_world)
    print("AGE OF WORLD: " + str(age_of_world_dec))
    
    for i in range(0, len(organisms_state_list)):    # Iterate through organisms
      
      
      print("\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~STATE OF ORGANISM~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

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


      print("\n~~~~~~~~~~~~~~~~~~~~~~EXECUTING AN ACTION~~~~~~~~~~~~~~~~~~~~~~~~\n")
      # EXECUTE GENE AT THE CURRENT INDEX

      action = read_byte(organisms_gene_list[i], index, 1)
      print("Current Action of Organism: " + str(action))

      if(action == 19):
        print("  Action to be Executed: Creation of a New Node")
        mass = read_byte(organisms_gene_list[i], index + 1, 1)  # Mass of new node
        print("  Mass of New Node: " + str(mass))
        node_type = read_byte(organisms_gene_list[i], index + 2, 1)  # Node type
        print("  Node Type: " + str(node_type))
        if(node_type == 0):
          print("    Node Type Name: Soul")
        elif(node_type == 1):
          print("    Node Type Name: Structual")
        elif(node_type == 2):
          print("    Node Type Name: Gripper")
        elif(node_type == 3):
          print("    Node Type Name: Photosynthesis")
        x_offset = read_byte(organisms_gene_list[i], index + 3, 1)  # X-Offset
        print("  X-Offset: " + str(x_offset))
        y_offset = read_byte(organisms_gene_list[i], index + 4, 1)  # Y-Offset
        print("  Y-Offset: " + str(y_offset))

        # Add node to nodes_state_list for the organism
        nodes_state_list[i].append([])
        j = len(nodes_state_list[i]) - 1  # Index of the new node in nodes_state_list
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 0, 1, j)  # Add a node index to the new node, incremented by one over the last node
        print("    Index Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 1, 1, mass)  # Add mass to the new node
        print("    Mass Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 2, 1, node_type)  # Add node type to the new node
        print("    Node Type Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 3, 1, 0)  # Add Mutable Data to the new node
        print("    Mutable Data Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 4, 3, x_offset)  # Add X-offset to the new node
        print("    X-Offset Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 7, 3, y_offset)  # Add Y-offset to the new node
        print("    Y-Offset Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))

        # Make the 2nd Selected Node the new Node 13
        organisms_state_list[i] = write_byte(organisms_state_list[i], 13, 1, j)
        selected_node_one = read_byte(organisms_state_list[i], 12, 1) # Retrieve the organism's 1st selected node
        print("Organism's First Selected Node: " + str(selected_node_one))
        selected_node_two = read_byte(organisms_state_list[i], 13, 1) # Retrieve the organism's 2nd selected node, which is now updated
        print("Organism's Second Selected Node: " + str(selected_node_two))
        
        
        contracted_muscle_len = read_byte(organisms_gene_list[i], index + 5, 1)  # Contracted Muscle Length
        print("  Contracted Muscle Length: " + str(contracted_muscle_len))
        expanded_muscle_len = read_byte(organisms_gene_list[i], index + 6, 1)  # Expanded Muscle Length
        print("  Expanded Muscle Length: " + str(expanded_muscle_len))
        spring_constant = read_byte(organisms_gene_list[i], index + 7, 1)  # Spring Constant
        print("  Spring Constant of Muscle: " + str(spring_constant))

        # Add muscle to muscles_state_list
        muscles_state_list[i].append([])
        j = len(muscles_state_list[i]) - 1  # Index of the new muscle in muscles_state_list
        muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 0, 1, j)  # Add a muscle index to the new muscle, incremented by one over the last muscle
        print("    Index Added to New Muscle. Current Contents of New Muscle State: " + str(muscles_state_list[i][j]))
        muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 1, 1, selected_node_one)  # Add first index of which the muscle is connected to
        print("    1st Selected Node Added to New Muscle. Current Contents of New Muscle State: " + str(muscles_state_list[i][j]))
        muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 2, 1, selected_node_two)  # Add second index of which the muscle is connected to
        print("    2nd Selected Node Added to New Muscle. Current Contents of New Muscle State: " + str(muscles_state_list[i][j]))
        muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 3, 1, contracted_muscle_len)  # Add the contracted muscle length
        print("    Contracted Muscle Length Added to New Muscle. Current Contents of New Muscle State: " + str(muscles_state_list[i][j]))
        muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 4, 1, expanded_muscle_len)  # Add the expanded muscle length
        print("    Expanded Muscle Length Added to New Muscle. Current Contents of New Muscle State: " + str(muscles_state_list[i][j]))
        muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 5, 1, spring_constant)  # Add the spring constant
        print("    Spring Constant Added to New Muscle. Current Contents of New Muscle State: " + str(muscles_state_list[i][j]))
        muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 6, 1, 0)  # Add Mutable Data. Set to expanded state to start. 0 = expanded, 1 = contracted. Other bits reserved for future features.
        print("    Mutable Data Added to New Muscle. Current Contents of New Muscle State: " + str(muscles_state_list[i][j]))

        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 8)
      
      if(action == 21):
        print("  Action to be Executed: Toggle Muscle")
        selected_node_one = read_byte(organisms_state_list[i], 12, 1) # Retrieve the organism's 1st selected node
        print("  Organism's First Selected Node: " + str(selected_node_one))
        selected_node_two = read_byte(organisms_state_list[i], 13, 1) # Retrieve the organism's 2nd selected node
        print("  Organism's Second Selected Node: " + str(selected_node_two))
        for j in range(0, len(muscles_state_list[i])):  # Cycle through the muscles to check if any have connections that match the 1st selected node and 2nd selected node
          muscle_index = read_byte(muscles_state_list[i][j], 0, 1)
          muscle_node_one = read_byte(muscles_state_list[i][j], 1, 1)
          muscle_node_two = read_byte(muscles_state_list[i][j], 2, 1)
          print("    Muscle " + str(muscle_index) + " Connected to Nodes " + str(muscle_node_one) + " and " + str(muscle_node_two))
          if(muscle_node_one == selected_node_one and muscle_node_two == selected_node_two or muscle_node_two == selected_node_one and muscle_node_one == selected_node_two):
            print("      Muscle is selected!")
            current_contraction_state = read_byte(muscles_state_list[i][j], 6, 1)
            if(current_contraction_state == 0):
              print("      Muscle is currently expanded")
              muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 6, 1, 1)  # Toggle to contracted state
              print("      Muscle toggled to contracted")
            else:
              print("      Muscle is currently contracted")
              muscles_state_list[i][j] = write_byte(muscles_state_list[i][j], 6, 1, 0)  # Toggle to expanded state
              print("      Muscle toggled to expanded")
        
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 1)
            
              
      if(action == 14):
        print("  Action to be Executed: Store a random value up to Data in register 1")
        data = read_byte(organisms_gene_list[i], index + 1, 3)
        print("    Value found in Data: " + str(data))
        r = random.randint(0, data)
        organisms_state_list[i] = write_byte(organisms_state_list[i], 14, 3, r)
        print("    Random Value " + str(r) + " Stored in Register 1")
        
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 4)
        
      if(action == 4):
        print(" Action to be Executed: Swap register 1 and 2")
        
        

        
        
        
      
      
    age_of_world = write_byte(age_of_world, 0, 6, age_of_world_dec + 1)
    time.sleep(5)
    

main_loop()
