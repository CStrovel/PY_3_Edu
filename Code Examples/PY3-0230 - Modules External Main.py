# Author: Charles Strovel
# This program demonstrates a simple module import to use code from another program

# To use code from a different module (file), first use the keyword "import" followed by 
# the name of the file the code is located in, excluding the .py file extension
import PY3_0230_Modules_External

# This can be used to import your own or someone elses code, or standard library extensions 
# We can also import specific functions from other modules using the 'from' statement 
from PY3_0230_Modules_External import externalFunctionThree, externalFunctionFour

def main():
    """ calls functions from file PY3_0230_Modules_External to demonstrate import functionality"""

    # Calling individual functions requires that you use the module name (that is, the file name
    # without the .py file extension) before the function name, separated by a .  
    PY3_0230_Modules_External.externalFunctionOne()
    PY3_0230_Modules_External.externalFunctionTwo()

    # Functions that are imported using 'from' do not need to be prefixed by the module name
    # Functions from imported modules, using from or import, can be used just like functions
    # That are written locally 
    print("")
    print(externalFunctionThree(5,7))
    print("")
    externalFunctionFour("My Input", 42)

    

# begin main 
main()