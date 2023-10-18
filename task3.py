#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  
Each cluster of data is the number of points for that particular group.  
Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""
def find(needle = None):
    filename = "task03.txt"
    numList = []
    with open(filename, "r")  as file:
        numtotal = 0
        listNames = file.read().split("\n")
        print(type(listNames))
        for i in listNames:
            try:
                i = int(i)
                numtotal += i
            except Exception as e:
                numList.append(numtotal)
                numtotal = 0
        numList.sort()
        print(numList[-1])

find()