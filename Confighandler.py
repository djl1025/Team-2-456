#Author: David Leiden
#Date: 03/31/2021
#Through this program, students will learn to:
#1. validate an input file and contents in it.
#2. Handle file opening in a mode
#2.1. Handle file exceptions, etc.
#3. Search file contents



def parse_file(filename):
    f = open(filename, "r")
    read = f.readlines()
    check = False

    for row in read:
        if 'true' in row:
            val = row.split(":")
            print(val[0])

    f.close()



def validate_file(filename):
    if filename.endswith('.txt'):
        return True




#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    valid=validate_file(filename)

    #print all the setting values set to ON/true on the configuration file.
    if valid:
        print("File %s is a valid text file. Now printing all the settings set ON" %filename)
        parse_file(filename)
    else:
        print("File %s is NOT a valid text file. Program aborted!" % filename)
