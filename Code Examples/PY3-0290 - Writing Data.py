# Author: Mark Dencler
# Modified for python 3.7 by Charles strovel 
# Description: This program demonstrates how to write data to a file.

# NOTE - FILE ACCESS MODES
# w - Write Mode - A new file is created and contents are written to it.  If
#    the file already exists, a new file is made with the same name.  The
#    contents of the old file are overwritten with the new contents.
# r - Read Mode - An existing file is opened so its contents can be read.  If
#    the file does not exist, an exception is thrown.  The file cannot be
#    modified in this mode.
# a - Append Mode - Open an existing file, but preserves the contents.  The
#    file can be written to, but the new data will be placed at the end of
#    the already existing file.

def main():
    # CREATE a file handle to access the file.  The first argument to open()
    #    is the name of the file to be opened.  The second argument indicates
    #    the access mode used to bind the file to the handle.
    outHandle = open('PY3-0290 - Data File.txt', 'w')

    # WRITE some data to the file.
    outHandle.write('Here is some data that will be written to the file.\n')
    outHandle.write('Here is some more data.  Notice this is on another line.\n')
    outHandle.write('When there are multiple items of related data in the ')
    outHandle.write('same file, it is common to seperate these data items ')
    outHandle.write('with a newline character.\n')

    intVariable = 5
    floatVariable = 5.0
    stringVariable = 'This string is stored in a variable.'

    # When writing data to the file, only strings can be written.  If data takes
    #    the form of a data type besides string, it must be cast as a string.  If
    #    the data needs to be seperated from everything else, be sure to concatenate
    #    the newline character to the end.
    outHandle.write(str(intVariable) + '\n')
    outHandle.write(str(floatVariable) + '\n')
    outHandle.write(stringVariable + '\n')
    
    # CLOSE the data file.
    outHandle.close()
    
# Begin MAIN()
main()
