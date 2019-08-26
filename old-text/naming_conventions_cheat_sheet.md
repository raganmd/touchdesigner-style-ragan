# Naming Conventions Cheat Sheet

## Operator Names
* Names lead with operator type, names are lowercase and underscore separated

#### Examples
* base_info
* base_system_configuration or base_system_config
* container_ui

## Operator Shortcuts
* Pascal case formatting

#### Examples
* SystemConfig
* Node

## Python Classes
* Pascal case- first letter capitalized, camelcase following 
* Include docstrings 

#### Examples
* SystemConfiguration
* ProjectorCalibration
* Watch for  problems with this

## Python Methods / Functions
* First letter capital, underscores
* Include docstrings

### Variable Names
* No capitals, all underscores
* Ops as variables should carry capital letters indicated op type ( _DAT, _COMP, _CHOP, _SOP, _MAT, _TOP, _OP for all other cases)
* my_variable_name
* my_variable_CHOP

#### Example
* Tox_drop()

Namespace Examples on BitBucket


**Doc Strings Examples**

```python
class SampleClass:
    '''
    This is a sample class.

    This sample class has several important features that can be described here.

    Notes
    ---------------
    Your notes about the class go here


    Side FX
    ---------------


    Args
    ---------------
    Args and descriptions would go here, see sample_method for an example


    Returns
    ---------------
    none
    '''

    def __init__( self ):

        print( "sample_class initialized" )

        return


    def Sample_method( self, name, age, height ):
        ''' This is a sample method.

        This sample method is intended to help illustrate what method docstrings should look like.
                        
        Notes
        ---------------
        'self' does not need to be included in the Args section.

        Args
        ---------------
        name (str): A string name, with spaces as underscores
        age (int): Age as full year measurements
        height (float): Height in meters to 2 significant digits, ex: 1.45

        Examples
        ---------------

        Returns
        ---------------
        formatted_profile (str) : A formatted string populated with the with the supplied information
        '''

        # profile (str): preformatted text with placeholders
        profile = '''
        The following was submitted for review:
        name : {}
        age : {}
        height : {}
        ''' 

        formatted_profile = profile.format( name, age, height )
                    
        return formatted_profile
```