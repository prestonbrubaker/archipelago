This program was developed by Preston Brubaker and Willoh Robbins



SUMMARY:
Willoh and I share an interest in evolutionary biology and computer science. Reading various literature by Charles Darwin and Alan Turing, we wanted to see some of the concepts associated with both natural selection and Turing complete computers.
Additionally, We want to find new and exciting uses for radio transmission and server systems. To achieve this, we will make an evolutionary simulation which has organisms use a genetic code which functions mechanistically as a turing complete computer.
Much like machine language, the organism will cycle through a genetic code consisting of 1s and 0s, and will translate the 1s and 0s into both instrucitons and data. Basic functionalities will include addition, goto statements, storing of values in "registers", and more.
The organisms will physically contain nodes and muscles, where each node can have a set of potential purposes, and muscles link nodes together and allow for the contraciton and expansion between nodes. The muscles will have a preset stifness, commanding how stronly the contraction or expanding force will be.
More force will consume more energy, ensuring that efficiency is valued by natural selection. Organisms will be able to reproduce if they have enough energy, and children will potentially recieve mutations.


Each block "| Name |" is associated with a byte, but "(x4)" means that the object is associated with that multiple of bytes, meaning that "| Name (x4) |" would take up 32 bits.


Lists/Parameters associated with each WORLD





Lists/Parameters associated with each ORGANISM:
Genetic Code:  |Instruction|Data(x3)|... x 2^16  ( Each instruction and associated data can be reffered to as a block. Each block, therefore, takes up 32 bits.)

Node Info: |ID|Mass|Type of Node|Immutable Data| Mutable Data| Hue | Saturation | Lighting | X-Coord. (x3)| Y-Coord. (x3)|

Muscle Info: |ID| Selected Node ID | 2nd Selected Node (or current new node) | Min Length (x3) | Max Length (x3) | Current Length (x3) | Spring Constant | Mutable Data | Hue | Saturation | Lighting |


Oranism Information: | Computer ID | World ID | Organism ID (x5) | Family Name (x5) |

Registers: | Register 1(x3) | Register 2(x3) | Register 3(x3) | Register 4(x3) |

Index: | Index (x2)|

Lifespan: | Time Alive (x3)| 

Energy: |Energy|




NODE TYPES:
0: Soul/Heart. Only has mass. Required as the first node of an organism, and it is what is shot off from another during reproduction
0: Structual. Only has mass. No activation function
1: Gripper. Mutable data corresponds to how tightly it grips to the environment, increasing the drag force
2: Photosynthesis. Harvests energy from the sunlight



INSTRUCTIONS: Note... when referring to Data with a capital "D", it refers to the following bytes reserved for data
0: Skip this block
1: Store the Data in register 1
2: Cycle the registers forward 1 (e.g. register 1 to 2, 2 to 3, 4 to 1...)
3: Change the Index to the Data so that during the next turn, the organism will read this instruction
4: Check to see if Reister 2 is equal to register 1, and change the index value to Data only if this condition is satisfied
5: Store the Energy value in register 1
6: Add register 1 and register 2, and place the result in register 3
7: Clear register 1
7: Subtract register 2 from register 1, and place the result in register 3. If the result is negative, set register 3 to zero
8: Swap the values of registers 1 and 2
9: Take the modulus of 1 with respect to 2, and place the result of this in register 3 (e.g. 15, 4 -> 3)
10: Place the energy value in register 1
11: Place the Time Alive value register 1
12: Generate a Node. This will use the next several bytes of the gene to initialize the node. It will automatically trigger the development of a muscle from the selected node to the new node and set the second selected node to the new node. The index will be changed to after this block of data.
13: Generate a Muscle. This will generate a muscle between the selected node and the 2nd selected node. The index will be changed to after the block of data
14: Increment the Selected Node ID by 1. If it goes over the max, it cycles back to the first node
15: Increment the 2nd Selected Node ID by 1. If it goes over the max, it cycles back to the first node
16: Store a random value in register 1
17: If there is a muscle between the selected nodes, toggle it's contraction/extension mode
18: RESERVED
19: Activate the first selected node, with the data being used in accordance with the node type
20: Activate the second selected node, with the data being used in accordance with the node type
21: Attempt reproduction. The first byte is the fraction out of 255 of the stored energy transferred to the child. The second is the angular addition to the angle between the first and second selected nodes it will be shot out from, and the third is the speed the baby is shot out at (energy associated with this will be subtracted from the energy store of the parent)
22: Die instantly
23: Check to see if Register 2 is greater than register 1, and change the index value to Data only if this condition is satisfied
24: Check to see if Register 2 is less than register 1, and change the index value to Data only if this condition is satisfied
25: Check to see if Register 2 is NOT equal to register 1, and change the index value to Data only if this condition is satisfied


--------------------------------------------------------------------------------------------------------------------------------------------------

After further thought and research, I found it to be probably possible to use only three registers. With the ability write the contents of a register elsewhere, or even to encode it into the state of the organism, I think the system is has enough degrees of freedom to be Turing Complete. With only three registers, it is not as taxing to reserve action items for all three modes of shuffling the registers, and one can reach any desired organisation of the registers with only two actions. 
I can provide a mechanism for which it is possible for the organism to record and retrieve information, so that there is hardly a limit as to the logic that is able to be performed.

I now lean more on the side of allowing mutable information in the genetic code of the organism. One might consider this information, if used, to be analogous to epigenetics used by real organisms.

I think it will be easier for mutations to produce favorable traits if any pointers/GoTo statements are relative to current position, rather than to point to absolute position. The first 1 or 0 should indicate direction, be it backwards or forward in the gene from its current position.

I will have instead all actions be mapped to a certain amount of information to follow. Using this method, there will be many actions that need not contain any following bytes for informaiton.

All information about the organism:

GENOME: | Action | Information (if appicable) | ...   Repeats up to any length

AGE: | Age (x3) |   The total of the 3 bytes allows for the organism to live for around 16 million iterations as a maximum

INDEX: | Index (x3) |   The total of the 3 bytes allows for the organism to proceed through a genome up to around 16 million lines long. In reality, skips, jumping, and data allocation will use up a large percentage of the gene space.

REGISTERS: | Register 1 (x3) | Register 2 (x3) | Register 3 (x3) |

NODE INFO: | ID | Mass | Type of Node | Immutable Data | Mutable Data | X-Coord. (x3)| Y-Coord. (x3)|

MUSCLE INFO: |ID| Selected Node ID | 2nd Selected Node (or current new node) | Min Length (x3) | Max Length (x3) | Current Length (x3) | Spring Constant | Mutable Data |
When a muscle is generated by an action, it will be made between the selected nodes if there is not one already there, and otherwise it will replace the current one. If a node is being generated, the muscle to it will be from selected node 1.

ENERGY: | Energy level |  The organsim shall die if their energy level reaches or falls below a certain threshold

SELECTED NODE: | Selected Node | 2nd Selected Node |
If a new node is created, 2nd selected node will be made to have the index of the new node

NODE TYPES:
0: Soul/Heart. Only has mass. Required as the first node of an organism, and it is what is shot off from another during reproduction
0: Structual. Only has mass. No activation function
1: Gripper. Mutable data corresponds to how tightly it grips to the environment, increasing the drag force
2: Photosynthesis. Harvests energy from the sunlight



INSTRUCTIONS:
| index of the aciton | bytes of Data to proceed action | description of the action |
|  0 | 0 | Skip this block
|  1 | 3 | Store the Data in register 1
|  2 | 0 | Swap registers 1 and 3
|  3 | 0 | Swap registers 2 and 3
|  4 | 0 | Swap registers 1 and 2
|  5 | 0 | Clear register 1
|  6 | 0 | Clear all registers
|  7 | 3 | Check to see if Reister 2 is equal to register 1, and change the index value by Data ( first bit of 1 is forward, 0 backwards) only if this condition is satisfied
|  8 | 3 | Check to see if Register 2 is greater than register 1, and change the index value by Data ( first bit of 1 is forward, 0 backwards) only if this condition is satisfied
|  9 | 3 | Check to see if Register 2 is less than register 1, and change the index value by Data ( first bit of 1 is forward, 0 backwards)  only if this condition is satisfied
| 10 | 3 | Check to see if Register 2 is NOT equal to register 1, and change the index value to Data only if this condition is satisfied
| 11 | 0 | Add register 1 and register 2, and place the result in register 3
| 12 | 0 | Subtract register 2 from register 1, and place the result in register 3. If the result is negative, set register 3 to zero
| 13 | 0 | Take the modulus of 1 with respect to 2, and place the result of this in register 3 (e.g. 15, 4 -> 3)
| 14 | 3 | Store a random value in register 1 that is between 0 and Data
| 15 | 3 | Change the index by a value associated with the Data following this instruction. The first bit of the data indicates direction, where 1 is forward and 0 is backwards
| 16 | 6 | Change the values of the DNA an index corresponding to the first three Data bytes ahead or behind, where the first but indicates direction (1 forward, 0 backwards) to the last three bytes od Data
| 17 | 0 | Replace register 1's value with the energy value
| 18 | 0 | Replace register 1's value with the time alive value
| 19 | x | Generate a Node. It will automatically trigger the development of a muscle from the selected node to the new node and set the second selected node to the new node. The index will be changed to after this block of data.
| 20 | x | Generate a Muscle. This will generate a muscle between the selected node and the 2nd selected node. The index will be changed to after the block of data
| 21 | 0 | If there is a muscle between the selected nodes, toggle it's contraction/extension mode
| 22 | 0 | Increment the Selected Node ID by 1. If it goes over the max, it cycles back to the first node
| 23 | 0 | Increment the 2nd Selected Node ID by 1. If it goes over the max, it cycles back to the first node
| 24 | 0 | Activate the first selected node, with the data being used in accordance with the node type
| 25 | 0 | Activate the second selected node, with the data being used in accordance with the node type
| 26 | 3 | Attempt reproduction. The first byte is the fraction out of 255 of the stored energy transferred to the child. The second is the angular addition to the angle between the first and second selected nodes it will be shot out from, and the third is the speed the baby is shot out at (energy associated with this will be subtracted from the energy store of the parent)
| 27 | 0 | Die instantly

