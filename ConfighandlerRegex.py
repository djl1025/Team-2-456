#Author: David Leiden
#Date: 04/2/2021
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
            tru = row.split(":", 1)
            seton += tru[::2]
        if 'false' in row:
            fal = row.split(":", 1)
            setoff += fal[::2]
        if 'default' in row:
            defa = row.split(":", 1)
            setdefault += defa[::2]
    return seton, setoff, setdefault

#function-2
def  print_settings(setonlist, setofflist, setdefaultlist) :
    # implement function-2 as instructed
    tlength = len(setonlist)
    flength = len(setofflist)
    deflength = len(setdefaultlist)
    print("1) Set On keywords: ")
    for i in range(0, tlength):
        print("\t",f"{i+1})", setonlist[i])
    print("2) Set Off keywords: ")
    for i in range(0, flength):
        print("\t",f"{i+1})", setofflist[i])
    print("3) Set Default keywords: ")
    for i in range(0, deflength):
        print("\t", f"{i + 1})", setdefaultlist[i])

#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    setonlist, setofflist, setdefaultlist=classify_settings(filename)

    #call function to print items in the lists.
    if setonlist or setofflist or setdefaultlist:
        print_settings(setonlist, setofflist, setdefaultlist)
    else:
        print("No settings found on the file.")
