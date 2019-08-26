# System Configuration
Large distributed playback systems require configuration. Furthermore, they ideally have a consistent and reliable configuration methodology that allows for agile adjustments during development as well as during crisis. To this end, many OD Software projects rely on a config file that can be edited outside of the touch environment. This might take the form of JSON or XML, and it’s intention is to provide show and installation systems with the information required for consistent and assignable operation. 

If you’re accustomed to working on smaller scale projects, you may have had the experience of creating two different TOE files for a given event - one for the control machine, and another for the rendering machines. The current aim in Software is to develop single launch files that then self configure based on machine IP or Name. In this scenario, a config file holds a record of roles, appropriate files, and any other essential instructions for consistent operation. This file is read at start, and ensures that a system boots predictably. To this end, we often use variables put into storage to facilitate this process. Some common variables, and their use follow.

## Common Storage Variables

* uri - uniform resource identifier
* Machine op local_ID - sometimes identified in the config as "localID"
* role - controller | node | calibration
* ip - used to populate config data
* group - often used as a plate indicator for large installations
* mediaPath - per machine path for locating the media drive

## Console Window at Startup

### Why
The console is often helpful for identifying errors TouchDesigner before you reach perform mode, or the network editor. While this feature isn’t ideal for performance ready distributions, it can often be helpful during the development process when trying to find stubborn issues that are difficult to diagnose.

### How
Create a new environment variable in windows

variable name: TOUCH_TEXT_CONSOLE
variable value: 1
