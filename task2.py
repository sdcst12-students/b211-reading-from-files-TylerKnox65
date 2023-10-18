"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  
Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
def find(filename = "task02a.txt"):
    num = []
    with open(filename, "r") as file:
        listnum = file.read().split("\n\n")
        #print(listnum)
        count = 0
        for i in listnum:
            numsplit = i.split("\n")
            numsplit.sort()
            try:
                if ((float(numsplit[0])** 2) + (float(numsplit[1]))** 2) == (float(numsplit[2])** 2):
                    print(numsplit)
            except:
                pass
            
find()
find("task02b.txt")
find("task02c.txt")