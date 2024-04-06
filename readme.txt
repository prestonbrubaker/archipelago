This program was developed by Preston Brubaker and his compatriat, Bo-Bo (Willoh Robbins).


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

Selected Node: | Selected Node | 2nd Selected Node |


NODE TYPES:
0: Soul/Heart. Only has mass. Required as the first node of an organism, and it is what is shot off from another during reproduction
0: Structual. Only has mass. No activation function
1: Gripper. Mutable data corresponds to how tightly it grips to the environment, increasing the drag force
2: Photosynthesis. Harvests energy from the sunlight



INSTRUCTIONS:
0: Skip this block
1: Store the Data in register 1
2: Cycle the registers forward 1 (e.g. register 1 to 2, 2 to 3, 4 to 1...)
3: Change the Index to the Data so that during the next turn, the organism will read this instruction
4: Check to see if Reister 2 is greater than register 1, and change the index value to Data only if this condition is satisfied
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
17: If there is a muscle between the selected nodes, set it to contraction mode
18: If there is a muscle between the selected nodes, set it to expansion mode
19: Activate the first selected node, with the data being used in accordance with the node type
20: Activate the second selected node, with the data being used in accordance with the node type
21: Attempt reproduction. The first byte is the fraction out of 255 of the stored energy transferred to the child. The second is the angular addition to the angle between the first and second selected nodes it will be shot out from, and the third is the speed the baby is shot out at (energy associated with this will be subtracted from the energy store of the parent)
22: Die instantly





