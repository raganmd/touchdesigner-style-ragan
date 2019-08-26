# Recommended TD Preference Settings
From the Edit menu select the Preferences dialog box. Alternatively, you could use the keyboard short-cut Alt + p

Here you’ll find a number of preferences for setting up your TouchDesigner environment. While many of these are the preview of the individual programmer there are some important recommendations worth considering when spending a significant amount of time developing in Touch. You may well find that you have a very specific set of preferences in your work, and that’s great. But, before you get there here are a few good places to start.

## Resize
For the sanity of other programmers, it’s well worth turning off the resize TOP and COMP checkboxes in your Network preferences tab. This keeps a uniform look to all TOPs and COMPs unless you choose to specifically deviate from the normal size. 

This is often an area of spirited discussion, and programmers within the department often have very specific opinions about the right approach for sizing and network organization. That being said, it’s worth remembering that a formal structure to the choices made in sizing and placement help make a TouchDesigner network more readable and navigable. First starting with normed sizes allows the programmer to make specific choices, rather than arbitrary ones - a common byproduct of the use of auto resizing. for both TOPs and COMPs.

## Grid Snap
By default the grid snap setting in TouchDesigner is set to course. Most of the networks you’ll find in our repos have been set with a fine network grid, which means if you re-arrange an operator, it will be difficult to find your way back into alignment with the project. For this reason, it’s worth changing your Snap to Grid to be fine.