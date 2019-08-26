# od.tools.standards.touch #

## Read Me Author ##
**Matthew Ragan**

**matthew.ragan@obscuradigital.com**

--------------------------------
DATE 2015-11-5 || TIME 11:43:21
--------------------------------

## Comments ##
Comments are an essential part of any project. While it may often feel like the time it takes to leave a comment in your network slows down the flow of the project, leaving yourself a trail of breadcrumbs can help you find your way back to what you were thinking when you were first working. Comments are not only for the other programmers that you're collaborating with, they're also for your future self. At some point you're bound to come back to a project and need to decode what you were originally thinking. The more time has elapsed between your last commit, and opening your project again, the more likely you are to feel lost and enraged at what you find. Good documentation is always the best case scenario, but not always feasible. At the very least, you should always strive to leave at least a few bullet points about how your network functions, and the the logic behind your approach.

Commenting in TouchDesigner is notoriously frustrating. Unlike other visual programming environments, Touch does not have the same kind of resolution independent fielding options you might find in something like Max/MSP. Instead, right now the best commenting options that exist are to use Text DATs in your network. This can often become unwieldy, however, so there are some important things you might keep in mind.

First and foremost, please consider adding a readme DAT to any major component. A read me can act as an overview for your entire module - this is an excellent place for a little more narrative about what a particular element does, and what problems it's striving to solve. A TOX called base_network_documentation lives in the repo od.tools.sharedtox. Dropping this into your project makes adding read me and comments as easy as alt + n. It loads a light weight interface that allows you a quick and easy way to add comments to your network in a standardized format. 

Unlike a readme, comments should focus on a particular element in your network. Avoid the temptation to write one large text DAT with all of your thoughts as bullet points. While this may initially seem efficient, it divorces your thoughts and explanations form the nodes which they refer to. Instead consider a multiple text DATs with comments close to their relevant procedures. It's also important to include a name, contact solution, and a date in your comments. Knowing who and when a particular idea or approach came from is often helpful in understanding a given network - it also gives you a person to ask about how a particular problem was solved if you're confused about what's happening in a given project. It's also worth considering a color schema for your comments. This makes it easy to scan a network for nodes immediately recognizable as comments - another programmer new to your network can quickly scan for nodes with a non standard color coding in order to get a sense of what's happening. Finally, for comments and readme text DATs make sure you've turned on word wrap in your text DAT - this located on the common page in the ops parameters.

### Do ###
* Color code your comments to make them easier to find
* Use a standard format for your comments - make sure to include your name, a way to contact you, and a time stamp.
* Use a text friendly formatting approach. Avoid using something like Word or google docs to write your comments - you'll end up with non standard characters that won't display correctly.
*  Place your thoughts close to the relevant portion of the network.
Use the word wrap feature on text DATs.

### Don't ###
* Take all of your notes in a single DAT - this can make it difficult to connect your thoughts with your network.
* Make your text DAT in largely disproportionately sized from your other operators.
* Make no comments at all - always write something. Any hint at what you were thinking and doing is better than having nothing at all. 
