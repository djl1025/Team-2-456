#Author: Naresh Adh
#Date: 03/26/2021
#Through this program, students will learn to:
    #1. validate an input file and contents in it using regular expression.
    #2. Handle file opening in a mode
    #2.1. Handle file exceptions, etc.
    #3. Search file contents
    #4. Use tools to check is a regular expression is 'evil'

#function-1
def classify_settings(filename):

    # implement function-1 as instructed
    f = open(filename, "r")
    seton = []
    setoff = []
    setdefault = []
    read = f.readlines()

    for row in read:
        if 'true' in row:
            val = (row.split(":")[0])
            seton = val
            #print(seton)
        #elif 'false' in row:
        #    setoff = row.split(":")
        #    setoff = setoff[0]
        #    #print(setoff)
        #elif 'default' in row:
        #    setdefault = row.split(":")
        #    setdefault = setdefault[0]
        #    #print(setdefault)
    print(seton)


#function-2
def  print_settings(setonlist, setofflist, setdefaultlist) :

    #implement function-2 as instructed

    pass

#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    setonlist, setofflist, setdefaultlist=classify_settings(filename)

    #call function to print items in the lists.
    if setonlist or setofflist or setdefaultlist:
        print_settings(setonlist, setofflist, setdefaultlist)
    else:
        print("No settings found on the file.")
