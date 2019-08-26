# od.tools.standards.touch #

## Read Me Author ##
**Matthew Ragan**

**matthew.ragan@obscuradigital.com**

--------------------------------
DATE 2015-11-5 || TIME 11:43:21
--------------------------------

## Sizing ##
Like in any paradigm, programmers have strong feelings about the best way to format their programming space. With something like Touchdesigner, the spatialized element of this development platform creates another layer of potential meaning making and organizational space. This also creates opportunities for messy and disorganized habits to crop up. Touch makes it easier to quickly change the size of node to better see it - you might find yourself doing this for comments, rendering elements, control panels, chop channels, geometry - just about anything in fact. While there is some great utility in this, and you may find that you're able to create abstract art pieces with your network, if possible you should avoid unnecessary resizing. Why?! Perhaps the most important consideration is how multiple sizes change the legibility of your network. While it's not uncommon that you may find yourself enlarging elements in your network to better see them, it changes your ability to see the network from at a glance - to read the flow of the network without unhindered by an imposed frame of importance. Your decision to enlarge a particular TOP or DAT may have been in response to a pragmatic need - to an outsider, however, this choice reads - visually - as an indicator of significance. This injection of priority can undermine your fellow programmers ability to unbiasedly read the flow of information in your network - because they're trying to decode the implied meaning what may well be perceived as a indication of significance. 

Sometimes, however, you may find that you want to change the size of an operator for that very reason. What then are you to do? Consider using a command to set the size of your node - this can ensure consistent sizes that can be standardized across your networks. This is accessible from the op class:
```python
op( 'opName' ).nodeHeight = int
op( 'opName' ).nodeWidth = int
```
Height and width are expressed as network editor units. One square on the network is equal to 100 network editor units.

## Examples ##

### Do ###
* Use consistent spacing, sizing, and clear organizational flows.
Rely on the default sizes of nodes as a starting point
* Consider turning off the adaptive sizing for nodes in the options dialogue box
* Group operations together and consider when you might create modules for a particular process in your network

### Don't ###
* Resize your nodes willy nilly (sorry Willy)
* Use multiple sizes in your organization structure without providing a key to your viewer or fellow programmers
* Use extremely large sized nodes. If another programmer resets your node sizes to better read your network, they'll be placed at great network distances from one another, making the first step in debugging your code an act of organization
* Forget that your network is something someone else will invariably see, interact with, and need to understand - be nice to your future self, or to those that will come after you.
