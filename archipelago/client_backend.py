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

nodes_velocity_list = [  #3-D list of node velocity vectors (organism index, node index, [X-Velocity, Y-Velocity])

]

muscles_state_list = [    #3-D list of muscles (organism index, muscle index, muscle info)

]

world_light_values = [  # 2-D list of light values in the cell. For now it will be 10x10,and they will have an initial and max of 2

]
world_res = 100  # Number of rows/columns of the world. Number of cells will be world_res squared.
light_max = 2  # The maximum amount of light. Also the initial amount.

org_counter = 0  # Counter of organisms ever to exist in this world. Iterated for each birth to assign new ID's that have never been used

# Parameters for the environment or general rules

max_node_offset = 0.1    # Maximum horizontal or vertical distance (as a fraction of the screen) a node can be placed when an action to produce a new node is called
spring_multiplier = 1  # Multiplier for the maximum spring constant
mass_multiplier = 0.001
dt = 0.03  # Time Step for Physics
drag_m = 0.0001    # Velocities will be multiplied by (1-drag_m) each turn

sleep_time = 0  # Time between iterations

def make_world(world_res_in, light_max_in):  # Makes a 2_D list of the light values
  list_out = []
  for i in range(0, world_res_in):
    temp_l = []
    for j in range(0, world_res_in):
      temp_l.append(light_max_in)
    list_out.append(temp_l)
  return list_out
      

def seed_organism():
  global org_counter
  
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
  nodes_velocity_state = []







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
  node_velocity_state = [0, 0]
  muscles_state = []




  nodes_state.append(node_state)  # Adding the soul node to the seed organism
  nodes_velocity_state.append(node_velocity_state)

  genetic_code = [
    0, 0, 0, 1,  0, 0, 1, 1,  # ACTION 19: Create a Node. The following with further indented comments is relevant data for node, and 2 indents for muscle info
    1, 1, 1, 1,  1, 1, 1, 1,    # Mass
    0, 0, 0, 0,  0, 0, 1, 1,    # Type Photosynthesis
    1, 1, 1, 1,  1, 1, 1, 1,    # X-offset as a fraction of maximum
    0, 0, 0, 0,  0, 0, 0, 0,    # Y-offset as a fraction of maximum
    0, 1, 0, 0,  0, 0, 0, 0,      # Contracted muscle length
    1, 1, 1, 1,  1, 1, 1, 1,      # Expanded muscle length
    1, 1, 1, 1,  1, 1, 1, 1,      # Spring constant of the muscle
    0, 0, 0, 1,  1, 0, 1, 0,  # Action 26: Attempt Reproduction
    0, 1, 1, 0,  0, 0, 0, 0,    # Data 1
    0, 0, 0, 1,  0, 1, 0, 1,  # ACTION 21: Toggle muscle
    0, 0, 0, 0,  1, 1, 1, 0,  # ACTION 14: Store a random value up to Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1
    0 ,0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 1,  1, 0, 0, 0,    # Data 3 (20)
    0, 0, 0, 0,  0, 1, 0, 0,  # ACTION 4: Swap register 1 and register 2
    0, 0, 0, 0,  0, 0, 0, 1,  # ACTION 1: Store Data in register 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 0,  0, 0, 0, 1,    # Data 3 (1)
    0, 0, 0, 0,  0, 1, 0, 0,  # ACTION 4: Swap register 1 and register 2
    0, 0, 0, 0,  1, 1, 0, 0,  # ACTION 12: Subtract register 2 from register 1 and store the result in register 3
    0, 0, 0, 0,  1, 0, 0, 0,  # ACTION 8: Check to see if the value in register 2 is more than the value in register 1, and change the index by the following is this is true
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1 (first bit of this line indicates backwards travel)
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 0,  1, 1, 1, 0,    # Data 3 (14)
    0, 0, 0, 0,  0, 0, 1, 0,  # ACTION 2: Swap the values in registers 1 and 3
    0, 0, 0, 0,  1, 1, 1, 1,  # ACTION 15: Change the index by Data
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 1 (first bit of this line indicates backwards travel)
    0, 0, 0, 0,  0, 0, 0, 0,    # Data 2
    0, 0, 0, 0,  0, 1, 1, 0,    # Data 3 (6)
  ]
  
  organisms_gene_list.append(genetic_code)
  organisms_state_list.append(initial_state)
  nodes_state_list.append(nodes_state)
  nodes_velocity_list.append(nodes_velocity_state)
  muscles_state_list.append(muscles_state)
  org_counter += 1



def read_byte(list_in, index_in, num_lines_in):    # Converts the "index_in"th and "num_lines_in" following byte(s) to decimal from list list_in
  value = 0
  for i in range(0, 8 * num_lines_in):
    if (i < len(list_in)):
      if(i + index_in * 8 < len(list_in)):
        value += 2**(8 * num_lines_in - 1 - i) * list_in[i + index_in * 8]
      else:
        return 0
  return value



def write_byte(list_in, index_in, num_lines_in, value_in):  # Takes in a list and a value and converts the value to binary and overwrites the current selection with the value
  for i in range(0, 8 * num_lines_in):  # Overwrite current contents with 0
    index_i = i + index_in * 8
    if(index_i == len(list_in)):
      list_in.append(0)      # This will expand the list if new information is being added to the end of list_in
    elif(index_i > len(list_in)):
      return list_in
    else:
      list_in[i + index_in * 8] = 0
  for i in range(0, 8 * num_lines_in):
    value = 2**(8 * num_lines_in - 1 - i)
    if(value_in >= value):
      list_in[i + index_in * 8] = 1
      value_in -= value
  return list_in

def get_positions_of_nodes():
  list_out = []  #Node Type, Unit X, Unit Y
  for i in range(0, len(organisms_state_list)):
    for j in range(0, len(nodes_state_list[i])):
      inner_list = []
      inner_list.append(read_byte(nodes_state_list[i][j], 2, 1))
      node_x = read_byte(nodes_state_list[i][j], 5, 3)
      node_y = read_byte(nodes_state_list[i][j], 8, 3)
      node_x_unit = node_x  / (2**24 - 1)
      node_y_unit = node_y  / (2**24 - 1)
      inner_list.append(node_x_unit)
      inner_list.append(node_y_unit)
      list_out.append(inner_list)
  return list_out
      

seed_organism()
world_light_values = make_world(world_res, light_max)  # Initialize world light values

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
  global org_counter
  
  while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~STATE OF WORLD~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    age_of_world_dec = read_byte(age_of_world, 0, 6)
    print(age_of_world)
    print("AGE OF WORLD: " + str(age_of_world_dec))
    
    for i in range(0, len(organisms_state_list)):    # Iterate through organisms for ACTIONS
      
      
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
      if(index >= len(organisms_gene_list[i])):  # Reset the index if it passes the last action
        index = 0
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
        nodes_velocity_list[i].append([0, 0])  # Initialize the node at rest
        j = len(nodes_state_list[i]) - 1  # Index of the new node in nodes_state_list
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 0, 1, j)  # Add a node index to the new node, incremented by one over the last node
        print("    Index Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 1, 1, mass)  # Add mass to the new node
        print("    Mass Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 2, 1, node_type)  # Add node type to the new node
        print("    Node Type Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 3, 1, 0)  # Add Immutable Data to the new node
        print("    Immutable Data Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 4, 1, 0)  # Add Mutable Data to the new node
        print("    Mutable Data Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))

        selected_node_one = read_byte(organisms_state_list[i], 12, 1) # Retrieve the organism's 1st selected node
        x_value_ref_unit = read_byte(nodes_state_list[i][selected_node_one], 5, 3) / (2**24 - 1)  # X-value of selected node one, in unit form
        y_value_ref_unit = read_byte(nodes_state_list[i][selected_node_one], 8, 3) / (2**24 - 1)  # Y-value of selected node one, in unit form
        print("      X-value of selected node 1 in unit form: " + str(x_value_ref_unit))
        print("      Y-value of selected node 1 in unit form: " + str(y_value_ref_unit))
        x_value_new_unit = x_value_ref_unit + (x_offset / 255 - 0.5) * max_node_offset
        if(x_value_new_unit < 0):
          x_value_new_unit = 0
        elif(x_value_new_unit > 1):
          x_value_new_unit = 1
        y_value_new_unit = y_value_ref_unit + (y_offset / 255 - 0.5) * max_node_offset
        if(y_value_new_unit < 0):
          y_value_new_unit = 0
        elif(y_value_new_unit > 1):
          y_value_new_unit = 1
        print("      X-value of selected new node in unit form: " + str(x_value_new_unit))
        print("      Y-value of selected new node in unit form: " + str(y_value_new_unit))

        x_value_new = int(x_value_new_unit * (2**24 - 1))
        y_value_new = int(y_value_new_unit * (2**24 - 1))
        
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 5, 3, x_value_new)  # Add X-value to the new node
        print("    X-Value data Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))
        nodes_state_list[i][j] = write_byte(nodes_state_list[i][j], 8, 3, y_value_new)  # Add Y-value to the new node
        print("    Y-Value data Added to New Node. Current Contents of New Node State: " + str(nodes_state_list[i][j]))

        # Make the 2nd Selected Node the new Node
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

        print("      Current Node State List for Organism: " + str(nodes_state_list[i]))
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 8)
      
      elif(action == 21):
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

      
      elif(action == 4):
        print("  Action to be Executed: Swap register 1 and 2")
        register_one_value = read_byte(organisms_state_list[i], 14, 3)
        register_two_value = read_byte(organisms_state_list[i], 17, 3)
        print("  Register One Value: " + str(register_one_value))
        print("  Register Two Value: " + str(register_two_value))
        organisms_state_list[i] = write_byte(organisms_state_list[i], 14, 3, register_two_value)
        organisms_state_list[i] = write_byte(organisms_state_list[i], 17, 3, register_one_value)
        print("    Registers Swapped!")
        register_one_value = read_byte(organisms_state_list[i], 14, 3)
        register_two_value = read_byte(organisms_state_list[i], 17, 3)
        print("  Register One Value: " + str(register_one_value))
        print("  Register Two Value: " + str(register_two_value))
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 1)

      
      elif(action == 1):
        print("  Action to be Executed: Store Data in Register 1")
        register_one_value = read_byte(organisms_state_list[i], 14, 3)
        print("  Register One Value: " + str(register_one_value))
        data = read_byte(organisms_gene_list[i], index + 1, 3)
        print("  Data to be Stored in Register 1: " + str(data))
        organisms_state_list[i] = write_byte(organisms_state_list[i], 14, 3, data)
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 4)

      
      elif(action == 12):
        print("  Action to be Executed: Subtract Register 2 from Register 1, and Store the Result in Register 3. Any result less than 0 is made to be zero")
        register_one_value = read_byte(organisms_state_list[i], 14, 3)
        register_two_value = read_byte(organisms_state_list[i], 17, 3)
        print("  Register One Value: " + str(register_one_value))
        print("  Register Two Value: " + str(register_two_value))
        subtraction_result = register_one_value - register_two_value
        if(subtraction_result < 0):
          subtraction_result = 0
        organisms_state_list[i] = write_byte(organisms_state_list[i], 20, 3, subtraction_result)
        print("  Result Stored in Register 3: " + str(subtraction_result))
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 1)

      
      elif(action == 8):
        print("  Action to be Executed: Check if the value in register 2 is more than the value in register 1, and change the index by data if that is the case and proceed otherwise")
        register_one_value = read_byte(organisms_state_list[i], 14, 3)
        register_two_value = read_byte(organisms_state_list[i], 17, 3)
        print("  Register One Value: " + str(register_one_value))
        print("  Register Two Value: " + str(register_two_value))
        data = read_byte(organisms_gene_list[i], index + 1, 3)
        print("  Data Value including jump direction bit: " + str(data))
        if(data >= 2**(8*24 - 1)):  # The first bit of data determines the direction of the jump, where 1 means forwards and 0 means backwards. This bit is then not included in calculating the spaces to jump if the condition is satisfied
          forward_index_jump = 1
          print("  Jump Direction: Forward")
          data -= 2**(8*24 - 1)
        else:
          forward_index_jump = -1
          print("  Jump Direction: Backward")
        print("  Data Value not including jump direction bit: " + str(data))        
        if(register_two_value > register_one_value):
          print("  Register 2 is More Than Register 1")
          print("  Changing Index by: " + str(data * forward_index_jump))
          organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + data * forward_index_jump)
        else:
          organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 4)

      
      elif(action == 2):
        print("  Action to be Executed: Swap the Values in Registers 1 and 3")
        register_one_value = read_byte(organisms_state_list[i], 14, 3)
        register_three_value = read_byte(organisms_state_list[i], 20, 3)
        print("  Register One Value: " + str(register_one_value))
        print("  Register Three Value: " + str(register_three_value))
        organisms_state_list[i] = write_byte(organisms_state_list[i], 14, 3, register_three_value)
        organisms_state_list[i] = write_byte(organisms_state_list[i], 20, 3, register_one_value)
        print("    Registers Swapped!")
        register_one_value = read_byte(organisms_state_list[i], 14, 3)
        register_two_value = read_byte(organisms_state_list[i], 20, 3)
        print("  Register One Value: " + str(register_one_value))
        print("  Register Three Value: " + str(register_three_value))
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 1)

      
      elif(action == 15):
        print("  Action to be Executed: Change the Index by Data")
        data = read_byte(organisms_gene_list[i], index + 1, 3)
        print("  Data Value including jump direction bit: " + str(data))
        if(data >= 2**(8*24 - 1)):  # The first bit of data determines the direction of the jump, where 1 means forwards and 0 means backwards. This bit is then not included in calculating the spaces to jump if the condition is satisfied
          forward_index_jump = 1
          print("  Jump Direction: Forward")
          data -= 2**(8*24 - 1)
        else:
          forward_index_jump = -1
          print("  Jump Direction: Backward")
        print("  Data Value not including jump direction bit: " + str(data))        
        print("  Changing Index by: " + str(data * forward_index_jump))
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + data * forward_index_jump)

      
      

      
      elif(action == 26):
        print("  Action to be Executed: Attempt Reproduction")
        id = read_byte(organisms_state_list[i], 0, 6)
        energy = read_byte(organisms_state_list[i], 11, 1)
        data = read_byte(organisms_gene_list[i], index + 1, 1)
        fraction = data / 255
        print("  Organism " + str(id) + " Has Energy Level: " + str(energy) + " And is Willing to Share " + str(fraction) + " Of Itself With Potential Offspring")
        if(energy >= 32):  # Will Act As a Current Setpoint for allowing reproduction
          print("  Organism Has Sufficient energy for Reproduction. Commencing")
          energy_transfer = int(energy * fraction)
          organisms_state_list[i] = write_byte(organisms_state_list[i], 11, 1, energy - energy_transfer)
          print("  Parent Organism is Left With " + str(energy - energy_transfer) + " Enegy Units")
          new_org_index = org_counter
          org_counter += 1
          print("  The New Organism's ID is: " + str(new_org_index))
          new_org_genes = []
          for k in range(0, len(organisms_gene_list[i])):
            new_org_genes.append(organisms_gene_list[i][k])
          new_org_state = []
          for k in range(0, len(organisms_state_list[i])):
            new_org_state.append(organisms_state_list[i][k])
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
          nodes_state = []
          nodes_state.append(node_state)
          
          muscle_state = []
          muscles_state = []
          muscles_state.append(muscle_state)

          node_velocity_state = [0, 0]
          nodes_velocity_state = []
          nodes_velocity_state.append(node_velocity_state)
          
          
          organisms_gene_list.append(new_org_genes)
          organisms_state_list.append(new_org_state)
          nodes_state_list.append(nodes_state)
          nodes_velocity_list.append(nodes_velocity_state)
          muscles_state_list.append(muscles_state)

          node_x = read_byte(nodes_state_list[i][0], 5, 3)
          node_y = read_byte(nodes_state_list[i][0], 8, 3)

          organisms_state_list[-1] = write_byte(organisms_state_list[-1], 0, 6, new_org_index)
          organisms_state_list[-1] = write_byte(organisms_state_list[-1], 11, 1, energy_transfer)

          # Originate Soul Node at Soul Node of Parent
          nodes_state_list[-1][0] = write_byte(nodes_state_list[-1][0], 5, 3, node_x)
          nodes_state_list[-1][0] = write_byte(nodes_state_list[-1][0], 8, 3, node_y)

          # Start organism off at Index 0
          organisms_state_list[-1] = write_byte(organisms_state_list[-1], 21, 2, 0)
          
          if( r < 0.05):
            r = random.uniform(0, 1)
            print("  Adding a Random Mutation by Setting a Random Bit of Offspring's Geneome to a Random Value")
            random_gene_index = random.randint(0, len(organisms_gene_list[-1]) - 1)
            random_bit_value = random.randint(0, 1)
            organisms_gene_list[-1][random_gene_index] = random_bit_value
        
          
        else:
          print("  Organism Does Not Have Enough Energy For Reproduction. Skipping.")
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 2)
      
      else:
        print("  Action to be Executed: Do Nothing")
        # Increment Genetic Index
        organisms_state_list[i] = write_byte(organisms_state_list[i], 23, 2, index + 1)
        
        
              
        
    print("\n\n~~~~~~~~~~~~~~~~~~~~CHECK FOR LISTS~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    print("  Organism State List: " + str(organisms_state_list))
    print("  Node State List: " + str(nodes_state_list))
    print("  Node Velocity List: " + str(nodes_velocity_list))
    print("  Muscle State List: " + str(muscles_state_list))

    print("\n\n~~~~~~~~~~~~~~~~~~~~ITERATE METABOLISM~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    for i in range(len(organisms_state_list) - 1, -1, -1):    # Iterate through organisms for ITERATE METABOLISM backwards to avoid problems when/if organisms are removed
      energy = read_byte(organisms_state_list[i], 11, 1)
      num_nodes = len(nodes_state_list[i])
      print("Organism " + str(read_byte(organisms_state_list[i], 0, 6)) + " Has Energy: " + str(energy))
      r = random.uniform(0, 1)
      if( r < 0.1):
        energy -= 1 * num_nodes
      if(energy < 0):
        print("Organism has been executed...")
        organisms_state_list.pop(i)
        organisms_gene_list.pop(i)
        nodes_state_list.pop(i)
        muscles_state_list.pop(i)
        nodes_velocity_list.pop(i)
      else:
        organisms_state_list[i] = write_byte(organisms_state_list[i], 11, 1, energy)
    
    print("\n\n~~~~~~~~~~~~~~~~~~~~ALLOW FOR COLLECTION OF LIGHT~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    for i in range(0, len(organisms_state_list)):    # Iterate through organisms for ALLOW FOR COLLECTION OF LIGHT
      for j in range(0, len(nodes_state_list[i])):
        node_type = read_byte(nodes_state_list[i][j], 2, 1)
        if(node_type == 3):
          print("Organism " + str(read_byte(organisms_state_list[i], 0, 6)) + ", Node " + str(read_byte(nodes_state_list[i][j], 0, 1)) + " Is a Photosynthesis Cell")
          node_index = read_byte(nodes_state_list[i][j], 0, 1)
          node_x = read_byte(nodes_state_list[i][node_index], 5, 3)
          node_y = read_byte(nodes_state_list[i][node_index], 8, 3)
          node_x_unit = node_x  / (2**24 - 1)
          node_y_unit = node_y  / (2**24 - 1)
          if(node_x_unit < 0):
            node_x_unit = 0
          elif(node_x_unit >= 1):
            node_x_unit = .999999
          if(node_y_unit < 0):
            node_y_unit = 0
          elif(node_y_unit >= 1):
            node_y_unit = .999999
          print("  Node Unit X: " + str(node_x_unit))
          print("  Node Unit Y: " + str(node_y_unit))
          cell_index_x = int(node_x_unit * world_res)
          cell_index_y = int(node_y_unit * world_res)
          print("  Node World Cell X-Index: " + str(cell_index_x))
          print("  Node World Cell Y-Index: " + str(cell_index_y))
          light = world_light_values[cell_index_x][cell_index_y]
          print("  Light In This Cell: " + str(light))
          if(light > 0):
            energy = read_byte(organisms_state_list[i], 11, 1)
            if( energy + 1 <= 255):
              organisms_state_list[i] = write_byte(organisms_state_list[i], 11, 1, energy + 1)
            world_light_values[cell_index_x][cell_index_y] -= 1
            print("  Organism's Energy Level Increased to: " + str(energy + 1))

    print("\n\n~~~~~~~~~~~~~~~~~~~~ADD LIGHT TO WORLD CELLS~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    for i in range(0, world_res):
      for j in range(0, world_res):
        light = world_light_values[i][j]
        if(light < light_max):
          r = random.uniform(0, 1)
          if( r < 0.05):
            light += 1
        world_light_values[i][j] = light
          
    
    print("\n\n~~~~~~~~~~~~~~~~~~~~PHYSICS~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    for i in range(0, len(organisms_state_list)):    # Iterate through organisms for PHYSICS
      print("Calculating Physics for Organism: " + str(read_byte(organisms_state_list[i], 0, 6)))
      if(len(nodes_state_list[i]) > 1 and len(muscles_state_list[i]) > 0):
        for j in range(0, len(muscles_state_list[i])):
          print("  Calculating Physics for Muscle: " + str(read_byte(muscles_state_list[i][j], 1, 1)))
          node_one_index = read_byte(muscles_state_list[i][j], 1, 1)
          node_two_index = read_byte(muscles_state_list[i][j], 2, 1)
          print("    Node One index: " + str(node_one_index))
          print("    Node Two index: " + str(node_two_index))
          if(node_one_index == node_two_index):
            continue
          node_one_x = read_byte(nodes_state_list[i][node_one_index], 5, 3)
          node_one_y = read_byte(nodes_state_list[i][node_one_index], 8, 3)
          node_two_x = read_byte(nodes_state_list[i][node_two_index], 5, 3)
          node_two_y = read_byte(nodes_state_list[i][node_two_index], 8, 3)
          print("    Node One X-Value: " + str(node_one_x))
          print("    Node One Y-Value: " + str(node_one_y))
          print("    Node Two X-Value: " + str(node_two_x))
          print("    Node Two Y-Value: " + str(node_two_y))

          if(node_one_x == node_two_x and node_one_y == node_two_y):
            continue
  
          # Convert coordinate values to a unit scale
          node_one_x_unit = node_one_x  / (2**24 - 1)
          node_one_y_unit = node_one_y  / (2**24 - 1)
          node_two_x_unit = node_two_x  / (2**24 - 1)
          node_two_y_unit = node_two_y  / (2**24 - 1)
  
          print("    Node One Unit X-Value: " + str(node_one_x_unit))
          print("    Node One Unit Y-Value: " + str(node_one_y_unit))
          print("    Node Two Unit X-Value: " + str(node_two_x_unit))
          print("    Node Two Unit Y-Value: " + str(node_two_y_unit))
  
          # Muscle physics
          node_one_x_v = nodes_velocity_list[i][node_one_index][0]
          node_one_y_v = nodes_velocity_list[i][node_one_index][1]
          node_two_x_v = nodes_velocity_list[i][node_two_index][0]
          node_two_y_v = nodes_velocity_list[i][node_two_index][1]
  
          print("    Node One X-Velocity: " + str(node_one_x_v))
          print("    Node One Y-Velocity: " + str(node_one_y_v))
          print("    Node Two X-Velocity: " + str(node_two_x_v))
          print("    Node Two Y-Velocity: " + str(node_two_y_v))
  
          dx = node_two_x_unit - node_one_x_unit
          dy = node_two_y_unit - node_one_y_unit
          distance = ((dx)**2 + (dy)**2)**0.5
          print("    X-Distance: " + str(dx))
          print("    Y-Distance: " + str(dy))
          print("    Distance Between Nodes: " + str(distance))
  
          spring_constant = read_byte(muscles_state_list[i][j], 5, 1)
  
          print("    Spring Constant: " + str(spring_constant))
  
          toggle_state = read_byte(muscles_state_list[i][j], 6, 1)  # 0 = expanded, 1 = contracted
          if(toggle_state == 0):
            print("    Muscle is in Expanded State")
            muscle_length = read_byte(muscles_state_list[i][j], 4, 1) / 255 * max_node_offset  # Pull the expanded length
          else:
            print("    Muscle is in Contracted State")
            muscle_length = read_byte(muscles_state_list[i][j], 3, 1) / 255 * max_node_offset  # Pull the contracted length
          print("    Muscle length: " + str(muscle_length))
          force_x = spring_multiplier * spring_constant / 255 * dx / (distance) * (distance - muscle_length)
          force_y = spring_multiplier * spring_constant / 255 * dy / (distance) * (distance - muscle_length)
  
          print("    Force Between Nodes in X-direction: " + str(force_x))
          print("    Force Between Nodes in Y-direction: " + str(force_y))
  
          node_one_mass = read_byte(nodes_state_list[i][node_one_index], 1, 1)
          node_two_mass = read_byte(nodes_state_list[i][node_two_index], 1, 1)
          print("    Node 1 Mass: " + str(node_one_mass))
          print("    Node 2 Mass: " + str(node_two_mass))
  
          # Apply the foces to alter the velocities in accordance with Newton's Second Law
          nodes_velocity_list[i][node_one_index][0] += force_x / (node_one_mass * mass_multiplier) * dt
          nodes_velocity_list[i][node_one_index][1] += force_y / (node_one_mass * mass_multiplier) * dt
          nodes_velocity_list[i][node_two_index][0] += -1 * force_x / (node_two_mass * mass_multiplier) * dt
          nodes_velocity_list[i][node_two_index][1] += -1 * force_y / (node_two_mass * mass_multiplier) * dt
  
          # Iterate the positions of the nodes by their velocities
          node_one_x_unit += nodes_velocity_list[i][node_one_index][0] * dt
          node_one_y_unit += nodes_velocity_list[i][node_one_index][1] * dt
          node_two_x_unit += nodes_velocity_list[i][node_two_index][0] * dt
          node_two_y_unit += nodes_velocity_list[i][node_two_index][1] * dt
  
          # Drag force applied to slow all speeds by an amount proportional to their current speed
          nodes_velocity_list[i][node_one_index][0] *= 1 - drag_m
          nodes_velocity_list[i][node_one_index][1] *= 1 - drag_m
          nodes_velocity_list[i][node_two_index][0] *= 1 - drag_m
          nodes_velocity_list[i][node_two_index][1] *= 1 - drag_m
          
          
  
          # Convert coordinate values back to values ready to be stored in 3 bytes
          node_one_x_new = int(node_one_x_unit * (2**24 - 1))
          node_one_y_new = int(node_one_y_unit * (2**24 - 1))
          node_two_x_new = int(node_two_x_unit * (2**24 - 1))
          node_two_y_new = int(node_two_y_unit * (2**24 - 1))
          
          print("    Node One New X-Value: " + str(node_one_x_new))
          print("    Node One New Y-Value: " + str(node_one_y_new))
          print("    Node Two New X-Value: " + str(node_two_x_new))
          print("    Node Two New Y-Value: " + str(node_two_y_new))
          
          # Store new values
          nodes_state_list[i][node_one_index] = write_byte(nodes_state_list[i][node_one_index], 5, 3, node_one_x_new)
          nodes_state_list[i][node_one_index] = write_byte(nodes_state_list[i][node_one_index], 8, 3, node_one_y_new)
          nodes_state_list[i][node_two_index] = write_byte(nodes_state_list[i][node_two_index], 5, 3, node_two_x_new)
          nodes_state_list[i][node_two_index] = write_byte(nodes_state_list[i][node_two_index], 8, 3, node_two_y_new)

    print("\n\n~~~~~~~~~~~~~~~~~~~~OUTPUT~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Output (node type, x, y): " + str(get_positions_of_nodes()))
      
    age_of_world = write_byte(age_of_world, 0, 6, age_of_world_dec + 1)
    with open('locations.txt', 'w') as file:
      file.write(str(get_positions_of_nodes()))
    with open('genes.txt', 'w') as file:
      file.write(str(organisms_gene_list))
    with open('states.txt', 'w') as file:
      file.write(str(organisms_state_list))
    time.sleep(sleep_time)
    # Random Willoh Shoutout heyyyy bestie 

main_loop()
