# TouchDesigner Style Guide | Ragan

## Read Me Author ##
[**Matthew Ragan**](https://matthewragan.com/)

## A Simple Disclaimer ##
Style guides are just that, guides. The suggestions outlined below aren’t hard and fast rules. For any standard there are likely to be exceptions, challenges, and issues. Code the way you want to code, but also remember that you’re making something that other programmers (your future self included) are going to return to, pull apart, question, interrogate, curse, praise, and judge. Your act of fixing an idea in an operational structure is both a creative act, as well as measured and considered one. TouchDesigner networks are challenging to share and collaborate in - they are sprawling, nested, multi-layered collections of signal flows. That is to say that they are already challenging to decode - you don’t have to use this standard, but cultivate and implement one for your own sake, and for the sake of your collaborators. 

## Overview ##
There are many variations of TouchDesigner project here at Obscura, but it's often helpful when you're getting started to have an anchor point for some general best practices, structures, and methodologies. Here you'll find several different example networks to look through, and use as touchstones. Here you'll see the following directories with sample projects:

* **dos_and_donts** - This is a generalized look at network structures and organization. The hard and fast take aways go something like - keep your work organized, keep your work neat, mostly move left to right, be conservative with changing size, keep notes in your networks, and most importantly be consistent (deviations happen, but be consistent in your deviant behavior.)
* **example.structure** - This network looks at a typical structure you might find on any given project. Here there's an emphasis on building a single file that dynamically loads the appropriate elements based on a config file. This example forgoes complexity for the sake of seeing some simple ideas illustrated as clearly as possible. Some of this will only make sense with time, but at the least it should be a start. 
* **plates_and_channels** - This TOE file looks to help clarify some of our conventions in terminology. We think media in terms of plates, channels, and projectors. Understanding how those ideas intersect and overlap is important as it's the foundation for much of our architectural model of thinking about projection mapping.