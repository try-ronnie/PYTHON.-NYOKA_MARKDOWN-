def write_file(file_name, file_content):
    with open(file_name , mode='w' , encoding='UTF-8') as logfile1:
        logfile1.write(file_content)

def append_file(file_name, append_content):
    with open (file_name , mode = 'a' , encoding='UTF-8') as logfile:
        logfile.write(append_content)

def read_file(file_name):
    with open (file_name) as logfile:
        logfile.read()


append_file(file_name = 'logfile' , file_content = 'log1: 5 bananas')
# ok this was just a lab
# in this point we were using open to create a file ...
# so we use with<< to close the files incase they dont close 
# with closes it automatically
# so we give the file name/path 
# mode gives the mode the file is in
    #>> like with mode = 'w' or 'a' 
    # a stands fo appending meaning adding to a file that hasnt been created 
    # w means to overwrite the existing txt content
# using encoding helps python to understand how text is stored in the file 
# Computers don’t store letters.
# They store numbers.


# Encoding tells Python how to convert:
    "H" → 72
    "α" → ???  
    "你" → ???
# Different encodings map characters to numbers differently.
# as is the variable that allows you to read the stored information init by prepending the method you want to use 
# open just lets you connect to that file and its path .... its like picking a book from the shelf and as is the variable you actually use to read the book
