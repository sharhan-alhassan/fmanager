"""
Application -- Text file manager
"""

import os
import argparse

# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file formate. %s must be a .txt format"
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist"


def valid_path(path):
    '''
    validate file path
    '''
    return os.path.exists(path)


def valid_filetype(file_name):
    '''
    validate file type
    '''
    return file_name.endswith('.txt')


def validate_file(file_name):
    '''
    valid file name and path
    '''
    if not valid_path(file_name):
        print(INVALID_PATH_MSG % (file_name))
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG % (file_name))
        quit()
    return
        

def read(args):
    file_name = args.read[0]                # Get the file name/path
    validate_file(file_name)                # validate the file name/path
    with open(file_name, 'r') as f:         # read and print the file
        print(f.read())   


def show(args):
    dir_path = args.show[0]                 # get path to directory
    if not valid_path(dir_path):            # validate file path
        print("Error: No such directory found")
        exit()

    files = [f for f in os.listdir(dir_path) if valid_filetype(f)]      # fetech and validate all .txt files in a list
    print("{} text files found.".format(len(files)))                    # give a total count of .txt files
    print('\n'.join(f for f in files))                                  # join and list all .txt files 


def delete(args):
    file_name = args.delete[0]
    validate_file(file_name)
    os.remove(file_name)
    print(f"Successfully deleted {file_name}")


def copy(args):
    file1 = args.copy[0]                                 # file to be copied
    file2 = args.copy[1]                                 # file to receive copy
    validate_file(file1)                                 # validate the file to be copied (file1)

    if not valid_filetype(file2):                        # validate file 2
        print(INVALID_FILETYPE_MSG % (file2))
        exit()

    with open(file1, 'r') as f1:                         # copy file1 to file2
        with open(file2, 'w') as f2:
            f2.write(f1.read())
    print(f"Successfuly copied {file1} to {file2}")


def rename(args):
    old_filename = args.rename[0]
    new_filename = args.rename[1]
    validate_file(old_filename)                            # validate the file to be renamed

    # validate the file to be renamed
    validate_file(old_filename)
  
    # validate the type of new file name
    if not valid_filetype(new_filename):
        print(INVALID_FILETYPE_MSG%(new_filename))
        exit()
  
    # renaming
    os.rename(old_filename, new_filename)
    print("Successfully renamed {} to {}.".format(old_filename, new_filename))

    
def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "A text file manager!")
  
    # defining arguments for parser object
    parser.add_argument("-r", "--read", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Opens and reads the specified text file.")
      
    parser.add_argument("-s", "--show", type = str, nargs = 1,
                        metavar = "path", default = None,
                        help = "Shows all the text files on specified directory path.\
                        Type '.' for current directory.")
      
    parser.add_argument("-d", "--delete", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Deletes the specified text file.")
      
    parser.add_argument("-c", "--copy", type = str, nargs = 2,
                        metavar = ('file1','file2'), help = "Copy file1 contents to \
                        file2 Warning: file2 will get overwritten.")
      
    parser.add_argument("--rename", type = str, nargs = 2,
                        metavar = ('old_name','new_name'),
                        help = "Renames the specified file to a new name.")
  
    # parse the arguments from standard input. This is an array holding all the command line arguments written
    args = parser.parse_args()
      
    # calling functions depending on type of argument
    # "args" absolutely behaving like "sys.argv": It is an array holding all command line arguments
    if args.read != None:
        read(args)
    elif args.show != None:
        show(args)
    elif args.delete !=None:
        delete(args)
    elif args.copy != None:
        copy(args)
    elif args.rename != None:
        rename(args)
  
  
if __name__ == "__main__":
    # calling the main function
    main()

