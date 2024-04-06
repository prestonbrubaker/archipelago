This program was developed by Preston Brubaker and his compatriat, Bo-Bo (Willoh Robbins).


SUMMARY:
Willoh and I share an interest in evolutionary biology and computer science. Reading various literature by Charles Darwin and Alan Turing, we wanted to see some of the concepts associated with both natural selection and Turing complete computers.
Additionally, We want to find new and exciting uses for radio transmission and server systems. To achieve this, we will make an evolutionary simulation which has organisms use a genetic code which functions mechanistically as a turing complete computer.
Much like machine language, the organism will cycle through a genetic code consisting of 1s and 0s, and will translate the 1s and 0s into both instrucitons and data. Basic functionalities will include addition, goto statements, storing of values in "registers", and more.
The organisms will physically contain nodes and muscles, where each node can have a set of potential purposes, and muscles link nodes together and allow for the contraciton and expansion between nodes. The muscles will have a preset stifness, commanding how stronly the contraction or expanding force will be.
More force will consume more energy, ensuring that efficiency is valued by natural selection. Organisms will be able to reproduce if they have enough energy, and children will potentially recieve mutations.


Lists/Parameters associated with each WORLD





Lists/Parameters associated with each ORGANISM:
Genetic Code:  |Instruction|Data|... x 2^16

Node Info: |ID|Mass|Type of Node|Immutable Data| Mutable Data| Hue | Saturation | Lighting | X-Coord. (x3)| Y-Coord. (x3)|

Muscle Info: |ID| Node 1 ID | Node 2 ID | Min Length | Max Length | Spring Constant | Mutable Data | Hue | Saturation | Lighting |

Oranism Information: | Computer ID | World ID | Organism ID (x5) | Family Name (x5) |

Registers: | Register 1 | Register 2 | Register 3 |

Index: | Index (x2)|

Lifespan: | Time Alive (x3)| 


