This program was developed by Preston Brubaker and Willoh Robbins

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
1: Structual. Only has mass. No activation function
2: Gripper. Mutable data corresponds to how tightly it grips to the environment, increasing the drag force
3: Photosynthesis. Harvests energy from the sunlight
4: Carnivore. Harvests energy from other organisms in the same cell.



INSTRUCTIONS:
| Added? | index of the aciton | bytes of Data to proceed action | description of the action |
|   |  0 | 0 | Skip this block
| X |  1 | 3 | Store the Data in register 1
| X |  2 | 0 | Swap registers 1 and 3
| X |  3 | 0 | Swap registers 2 and 3
| X |  4 | 0 | Swap registers 1 and 2
| X |  5 | 0 | Clear register 1
| X |  6 | 0 | Clear all registers
| X |  7 | 3 | Check to see if Reister 2 is equal to register 1, and change the index value by Data ( first bit of 1 is forward, 0 backwards) only if this condition is satisfied
| X |  8 | 3 | Check to see if Register 2 is greater than register 1, and change the index value by Data ( first bit of 1 is forward, 0 backwards) only if this condition is satisfied
| X |  9 | 3 | Check to see if Register 2 is less than register 1, and change the index value by Data ( first bit of 1 is forward, 0 backwards)  only if this condition is satisfied
| X | 10 | 3 | Check to see if Register 2 is NOT equal to register 1, and change the index value to Data only if this condition is satisfied
| X | 11 | 0 | Add register 1 and register 2, and place the result in register 3
| X | 12 | 0 | Subtract register 2 from register 1, and place the result in register 3. If the result is negative, set register 3 to zero
| X | 13 | 0 | Take the modulus of 1 with respect to 2, and place the result of this in register 3 (e.g. 15, 4 -> 3)
| X | 14 | 3 | Store a random value in register 1 that is between 0 and Data
| X | 15 | 3 | Change the index by a value associated with the Data following this instruction. The first bit of the data indicates direction, where 1 is forward and 0 is backwards
|   | 16 | 6 | Change the values of the DNA an index corresponding to the first three Data bytes ahead or behind, where the first but indicates direction (1 forward, 0 backwards) to the last three bytes of Data
| X | 17 | 0 | Replace register 1's value with the energy value
|   | 18 | 0 | Replace register 1's value with the time alive value
| X | 19 | x | Generate a Node. It will automatically trigger the development of a muscle from the selected node to the new node and set the second selected node to the new node. The index will be changed to after this block of data.
| X | 20 | x | Generate a Muscle. This will generate a muscle between the selected node and the 2nd selected node. The index will be changed to after the block of data
| X | 21 | 0 | If there is a muscle between the selected nodes, toggle it's contraction/extension mode
| X | 22 | 0 | Increment the Selected Node ID by 1. If it goes over the max, it cycles back to the first node
| X | 23 | 0 | Increment the 2nd Selected Node ID by 1. If it goes over the max, it cycles back to the first node
|   | 24 | 0 | Activate the first selected node, with the data being used in accordance with the node type
|   | 25 | 0 | Activate the second selected node, with the data being used in accordance with the node type
| X | 26 | 1 | Attempt reproduction. The first byte is the fraction out of 255 of the stored energy transferred to the child.
|   | 27 | 0 | Die instantly

