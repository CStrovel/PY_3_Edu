# Author: Mark Dencler
# Description: This program demonstrates how to read data from a file.

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
    inHandle = open('PY3-0300 - Data File.txt', 'r')

    # READ all of the data from the file and store it in a buffer.
    buffer = inHandle.read()

    # display the file contents on the screen
    print(buffer)

    # Reset the read position back to the beginning of the file.
    inHandle.seek(0)
    print('')

    # READ the data from the file one line at a time.
    strHold = inHandle.readline()           # contains a newline
    strHold = strHold.rstrip('\n')          # strip the newline
    intHold = int(inHandle.readline())
    floatHold = float(inHandle.readline())
    boolHold = bool(inHandle.readline())

    # Note: All calls to file reading methods return strings.  It is the
    #    programmer's job to know the type of data that will be coming
    #    out of the file and to perform the appropriate cast.  Also be
    #    aware that newline characters will be transferred directly
    #    from the data file to the buffers.  Most of the casting
    #    operations will stop parsing when the newline is encountered,
    #    but if the data being read is naturally a string, it is the
    #    programmer's responsibility to strip the newline when appropriate.

    # display the variale contents on the screen
    DisplayVarContents(strHold, intHold, floatHold, boolHold)
    print('')
    
    # CLOSE the data file.
    inHandle.close()

def DisplayVarContents(var_1, var_2, var_3, var_4):
    print('The 1st variable contains: {}'.format(var_1))
    print('The 2nd variable contains: {}'.format(var_2))
    print('The 3rd variable contains: {}'.format(var_3))
    print('The 4th variable contains: {}'.format(var_4))
    
# Begin MAIN()
main()
