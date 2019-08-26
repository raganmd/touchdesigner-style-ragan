# od.tools.standards.touch #

## Read Me Author ##
**Matthew Ragan**

**matthew.ragan@obscuradigital.com**

--------------------------------
DATE 2015-11-5 || TIME 11:43:21
--------------------------------

## Wires ##
Curved, straight, dotted, moving, static - the wires in TouchDesigner are a delight, some kind of series of mad scientists spaghetti code it's easy to fall in love with them, and easier still to make a mess of them. There are a few important features of wires to keep in mind when working.

**Animation**
Animated wires help you see, at a glance, that something is cooking. This is a visual reminder that a portion of your network is being processed right before your very eyes. This is often helpful in understanding how to debug a portion of your network as it allows you to find unnecessary cycles visually rather than with print statements.

**Links**
The dotted lines that connect ops are refereed to as links, not wires. Wires are inter-operator connections between data types (families), links, on the other hand, bridge between operator types and between data types. These are often used to drive parameters, or animate some portion of the network. Just like with wires, animated links are an indicator that a process is cooking. This is another important visual debugging mechanism when working on a project.

**Docked**
Docked ops have a straight line, similar to a link in color, that connects an operator to another. Docking an operator keeps it at an established x and y offset from its partner. 

While there isn't a defined flow, there is an implied western bias in a left to right flow in networks. While you certainly can organize your networks right to left, it will make for some backwards flipping lines. Similarly, organizing top to bottom will creating hard snaking S curves in your networks. While none of these things are inherently bad, they can make it difficult for another programmer to interpret your intentions. Top to bottom or bottom to top is perhaps the most dangerous. This particular arrangement makes it difficult to see, at a glance, the intended flow of operations.

### Do ###
* Think carefully about your node arrangement and how this will affect your wires - what will you cross, obscure, or hide?
* Leave room for clear paths and flows in your network. A little more empty spaces is generally better than too little.
* Think about the proximity of export nodes to their targets - are you creating long or confusing export paths that will be difficult to understand visually? 

### Don't ###
* Reverse order in node connections
* Vertically stack operators and connect them with S-curves.
* Dock and hide important nodes - scripts, notes, shaders, are all examples of acceptable items. **NEVER** dock and hide essential network elements. By hiding an essential part of your network, you make it exponentially more difficult for another programmer to debug your network, or understand your process. 
* Arrange your nodes haphazardly