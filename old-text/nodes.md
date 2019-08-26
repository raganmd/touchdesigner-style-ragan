# Nodes

## Naming
This section stands as an expansion on the above naming convention style guide. After much discussion, the current practice for operator naming follows the python style guide of using underscores rather than camel case. This appears in a number of various locations in your network, and requires special attention when it comes to renaming nodes. When renaming an operator or when terminating with a null the following naming convention should be used:

operator_descriptor_name#

The above can be decoded:
    **operator** - the operator type
    **descriptor_name** - whatever descriptor is used for the node, using underscores in place of spaces
    **#** - any digit that might be associated with the node

A few examples as reference:

At the end of a rendering chain a null is added inside of a base:
    null_final

A movie player uses two movie file in TOPs in order to facilitate seamless switching between videos. The two movie file in TOPs might be renamed in order to specify that they are the A or B deck:
    moviefilein_a
    moviefilein_b

A series of TOP chains are used in order to composite a variety of thumbnails used for instancing geometry. Each TOP chain terminates in a null, and needs to be differentiated with a digit to allow for texture instancing:
    null_ui_thumbnail1
    null_ui_thumbnail2
    null_ui_thumbnail3
    null_ui_thumbnail4

TOX Components should also follow this naming convention

## Notable Exceptions
The most apparent exceptions to this rule are found in local/modules. Mods have the benefit of being accessible with the short hand:
mod.textDATname.functionName

This excellent feature can be ham-stringed by long text DAT names. As an example, we might imagine that we have a module we'd like to use with the mod. shorthand. THat module's name might easily be something like "text_system_configuration" when using our standard naming convention, inside of this module we might want to use a function called "start_up". This would mean that we'd need to write something akin to:

```python
mod.text_system_configuration.start_up()
```

in order to call this function. The shortening of this by the prefix "text_" may not be a huge number of characters, but it helps provide a little bit of clarity in the reading a of the expression:

```python
mod.system_configuration.start_up()
```

This also helps distinguish our module - which is essentially being accessed as a library - and a regular text DAT. 

## Sizing
Like in any paradigm, programmers have strong feelings about the best way to format their programming space. With something like Touchdesigner, the spatialized element of this development platform creates another layer of potential meaning making and organizational space. This also creates opportunities for messy and disorganized habits to crop up. Touch makes it easier to quickly change the size of node to better see it - you might find yourself doing this for comments, rendering elements, control panels, chop channels, geometry - just about anything in fact. While there is some great utility in this, and you may find that you’re able to create abstract art pieces with your network, if possible you should avoid unnecessary resizing. Why?! Perhaps the most important consideration is how multiple sizes change the legibility of your network. While it’s not uncommon that you may find yourself enlarging elements in your network to better see them, it changes your ability to see the network from at a glance - to read the flow of the network without unhindered by an imposed frame of importance. Your decision to enlarge a particular TOP or DAT may have been in response to a pragmatic need - to an outsider, however, this choice reads - visually - as an indicator of significance. This injection of priority can undermine your fellow programmers ability to unbiasedly read the flow of information in your network - because they’re trying to decode the implied meaning what may well be perceived as a indication of significance. 

Sometimes, however, you may find that you want to change the size of an operator for that very reason. What then are you to do? Consider using a command to set the size of your node - this can ensure consistent sizes that can be standardized across your networks. This is accessible from the op class:

```python
op( ‘opName’ ).nodeHeight = int
op( ‘opName’ ).nodeWidth = int
```

Height and width are expressed as network editor units. One square on the network is equal to 100 network editor units.

### Examples

**Do**
* Use consistent spacing, sizing, and clear organizational flows.
* Rely on the default sizes of nodes as a starting point
* Consider turning off the adaptive sizing for nodes in the options dialogue box
* Group operations together and consider when you might create modules for a particular process in your network

**Don’t**
* Resize your nodes willy nilly (sorry Willy)
* Use multiple sizes in your organization structure without providing a key to your viewer or fellow programmers
* Use extremely large sized nodes. If another programmer resets your node sizes to better read your network, they’ll be placed at great network distances from one another, making the first step in debugging your code an act of organization
* Forget that your network is something someone else will invariably see, interact with, and need to understand - be nice to your future self, or to those that will come after you.

## Wires
Curved, straight, dotted, moving, static - the wires in TouchDesigner are a delight, some kind of series of mad scientists spaghetti code it's easy to fall in love with them, and easier still to make a mess of them. There are a few important features of wires to keep in mind when working.

**Animation**
Animated wires help you see, at a glance, that something is cooking. This is a visual reminder that a portion of your network is being processed right before your very eyes. This is often helpful in understanding how to debug a portion of your network as it allows you to find unnecessary cycles visually rather than with print statements.

**Links**
The dotted lines that connect ops are refereed to as links, not wires. Wires are inter-operator connections between data types (families), links, on the other hand, bridge between operator types and between data types. These are often used to drive parameters, or animate some portion of the network. Just like with wires, animated links are an indicator that a process is cooking. This is another important visual debugging mechanism when working on a project.

**Docked**
Docked ops have a straight line, similar to a link in color, that connects an operator to another. Docking an operator keeps it at an established x and y offset from its partner. 

While there isn't a defined flow, there is an implied western bias in a left to right flow in networks. While you certainly can organize your networks right to left, it will make for some backwards flipping lines. Similarly, organizing top to bottom will creating hard snaking S curves in your networks. While none of these things are inherently bad, they can make it difficult for another programmer to interpret your intentions. Top to bottom or bottom to top is perhaps the most dangerous. This particular arrangement makes it difficult to see, at a glance, the intended flow of operations.

**Do**
* Think carefully about your node arrangement and how this will affect your wires - what will you cross, obscure, or hide?
Leave room for clear paths and flows in your network. A little more empty spaces is generally better than too little.
* Think about the proximity of export nodes to their targets - are you creating long or confusing export paths that will be difficult to understand visually? 

**Don’t**
* Reverse order in node connections
* Vertically stack operators and connect them with S-curves.
* Dock and hide important nodes - scripts, notes, shaders, are all examples of acceptable items. NEVER dock and hide essential network elements. By hiding an essential part of your network, you make it exponentially more difficult for another programmer to debug your network, or understand your process.
* Arrange your nodes haphazardly

## Network Organization
A network’s re-usability lives and dies in its organization and structuring. While there are limits to a modular approach, it's well worth considering the larger implications around cultivating a forward focused temperament when building new systems. Every project will eventually come up against deadlines, changes orders, and the necessities of project delivery. To the best of our abilities, however, we might consider a tempered approach to thinking about how a particular element might be able to be used and re-used in future projects.

To that end, clear organization and careful planning help facilitate this process. For the sake of a simple case study, let's for a moment consider instancing networks. For the uninitiated, instancing allows you to reuse a single piece of geometry once it's been passed to the GPU. This method of drawing geometry is significantly cheaper, computationally, than drawing additional copies of the geometry on the CPU. In principle, you only draw the geometry once, then create a transformation matrix for subsequent copies of the original geometry. The transformation of the copies is most efficiently done in CHOP channels, sometimes initially fed by a geometry converted to channel data. 

If we develop the transformation channels in the same network as the rendering system, we're able to quickly see what's happening in the process. This also allows for less complicated paths, in a network that is generally flatter. The trade off here is re-usability. This approach typically makes it more difficult to identify how to break apart a network for re-use. The alternative, would be to build the rendering engine as a separate directory from the networking focused on object transformation. It's difficult to say which is the "better" choice, as both have their merits. Rather, it's important to understand that one approach has a shorter potential shelf life. 

This brings us to a larger question of organization - in what manner should one organize their network. While there aren't any hard and fast rules, it's worth considering how you might construct a network as specific to it's given role. In the example above, you might build a network that was focused on transformational information, while another was focused on texture's, and finally a network that was the rendering engine. This modular division creates more layers, but also allows for the reuse of any one of those elements - save just the texture building system, or the instances. This also creates space to consider how you might externalize those elements - in this respect a git history would allow the programmer to trace back through various iterations of one element while still preserving the current developments of another - keep all of your advances in texture building, but go back to an earlier transformation system - for example.

If you're not yet sold on this idea, at the very least consider dividing up your network, spatially, into regions responsible for a given task. Create territories for rendering, texture building, and instance translation. The most difficult to parse networks a wandering collision of every element in a single space. When possible, it is essential that you avoid this kind of programming. All of us invariably work fast and hard, creating functional but not elegant code - that, however, should not be our primary modus operandi.

**Do**
*Break apart your networks into modular pieces when possible
*Create easily visually navigable networks.
*Avoid mixtures of sizes, distributions, and complex nodal arraignments\
*Think ahead - what organizational method best sets you up for success in the future?
*Limit the complexity of any given network - if you find a network is growing to be too sprawling, how might you re-organize or compartmentalize your implementation?
*Think of your work in terms of a test against the other members of the team - would this structure and approach pass a Barry test? a Vlad test? a Bryant test? 

**Don’t**
* Make messes you never attend to - "I'll clean it up later" is the mantra of every creative coder at one point or another. If you have have enough time to have that thought, you have enough time to make a plan to refactor your code for a cleaner implementation.
* Be happy with your first draft - you built it fast and hard on the first pass to rough out the idea, but that shouldn't be good enough for the final implementation. 
* Forget to ask for another set of eyes
* Forget to learn from your mistakes - we all make them, it's the joy of working on projects at large scales. It's okay to fall down, just remember to get up and avoid that same trap the next time around.
* Forget that you might not be the person to implement your code - we sometimes have to hand off a project to another team member, or are only in charge of developing a small piece of a larger project. There's a good chance that what you make will need to be decipherable by another team member. Don't assume that you will always be available to describe what's in your network - write it (and document it) so that another could pick it up, and continue with minimal effort.
* Forget to ask for help - we have one of the most remarkable TouchDesigner teams in the world - perhaps the most remarkable collection of them. There's a good chance that the answers are in the room.

Take a moment to review the Dos and Don’ts TOE file

## Comments
Comments are an essential part of any project. While it may often feel like the time it takes to leave a comment in your network slows down the flow of the project, leaving yourself a trail of breadcrumbs can help you find your way back to what you were thinking when you were first working. Comments are not only for the other programmers that you’re collaborating with, they’re also for your future self. At some point you’re bound to come back to a project and need to decode what you were originally thinking. The more time has elapsed between your last commit, and opening your project again, the more likely you are to feel lost and enraged at what you find. Good documentation is always the best case scenario, but not always feasible. At the very least, you should always strive to leave at least a few bullet points about how your network functions, and the the logic behind your approach.

Commenting in TouchDesigner is notoriously frustrating. Unlike other visual programming environments, Touch does not have the same kind of resolution dependent fielding options you might find in something like Max/MSP. Instead, right now the best commenting options that exist are to use Text DATs in your network. This can often become unwieldy, however, so there are some important things you might keep in mind.

First and foremost, please consider adding a readme DAT to any major component. A read me can act as an overview for your entire module - this is an excellent place for a little more narrative about what a particular element does, and what problems it’s striving to solve. A TOX called base_network_documentation lives in the repo od.tools.sharedtox. Dropping this into your project makes adding read me and comments as easy as alt + n. It loads a light weight interface that allows you a quick and easy way to add comments to your network in a standardized format. 

Unlike a readme, comments should focus on a particular element in your network. Avoid the temptation to write one large text DAT with all of your thoughts as bullet points. While this may initially seem efficient, it divorces your thoughts and explanations form the nodes which they refer to. Instead consider a multiple text DATs with comments close to their relevant procedures. It’s also important to include a name, contact solution, and a date in your comments. Knowing who and when a particular idea or approach came from is often helpful in understanding a given network - it also gives you a person to ask about how a particular problem was solved if you’re confused about what’s happening in a given project. It’s also worth considering a color schema for your comments. This makes it easy to scan a network for nodes immediately recognizable as comments - another programmer new to your network can quickly scan for nodes with a non standard color coding in order to get a sense of what’s happening. Finally, for comments and readme text DATs make sure you’ve turned on word wrap in your text DAT - this located on the common page in the ops parameters.

**Do**
* Color code your comments to make them easier to find
* Use a standard format for your comments - make sure to include your name, a way to contact you, and a time stamp.
* Use a text friendly formatting approach. Avoid using something like Word or google docs to write your comments - you’ll end up with non standard characters that won’t display correctly.
* Place your thoughts close to the relevant portion of the network.
* Use the word wrap feature on text DATs.

**Don’t**
* Take all of your notes in a single DAT - this can make it difficult to connect your thoughts with your network.
* Make your text DAT in largely disproportionately sized from your other operators.
* Make no comments at all - always write something. Any hint at what you were thinking and doing is better than having nothing at all. 

## Logging - Events and Debugging
External event logging is often essential in determining what’s happening on a machine when a command executes. Even simple networks can often prove difficult to debug and inspect, and in large complex systems it’s essential to build in logging mechanisms for tracking performance, system events, and system errors. While there isn’t a foolproof way to format these messages, there are some general considerations to be kept when building or adapting a logging system. 

#### Timestamps
Messages without timestamps are far less effective than those with one. While logging without time stamps still provides for a chronological record, it doesn’t tell you when an event happened in relation to another - seconds, minutes, hours. These things are important for considered debugging, and also help differentiate between system launches. When building system logging messages, day, month, year, hour, minute, second are all essential pieces of a good time stamp. 

#### Operator Name and Network Location
Errors or problems that relate to a specific operator are extremely useful when debugging, but without the name and location of a given operator it can be difficult to know what happened. Be mindful to include operator names, and addresses (TouchDesigner network location) in logged messages. This makes for much faster diagnosis and resolution during the tracking process.

#### Machine Name or IP
Distributed systems often deal with messages and commands between machines. To that end, sound logging also means including some information about what machine is generating the error, message, trigger, or the like. It’s helpful, for example, to see that the control machine sent a message triggering an event on a node before the node generated an error message. Ideally, Name or IP would also be grouped with the role of the machine. Was it two nodes that were talking with one another that generated an error, or did the error occur as the result of a controller and node exchange? 

#### External Files
Log files should be written to an external file separate from the application TOE file. This helps ensure that the logging mechanism can be retrieved without opening a given toe file, and it also makes for easy network retrieval from another machine. 

Logging should include:
* Errors
* Warnings
* Tiggered Events
* Select Network Traffic
* Start Up
* Shut Down

Logging Examples Worth Reviewing
* AT&T 2015
* Santou Arena 2016