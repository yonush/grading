'''
 Bubble sort in Python

 Python command line debugger, pdb, help
 h: help
 w: where are we in the code
 n: next code line ()
 s: step into function 
 c: continue the program until next breakpoint or exit
 p: print [variable]
 l: list the code around the breakpoint area
 q: quite the debugger
 Tutorial: https://realpython.com/python-debugging-pdb/

'''
import random

def average(arr):
    sum = 0
    tally = len(arr)
    for value in arr:
        sum += value

    tally = 0 #uncomment this to generate an exception
    try:
        avg =  sum // tally   
    except:
        print("div error")

    return avg

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    wasSwapped = False

    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element first is larger than the next
            if arr[j] > arr[j + 1]:
                wasSwapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not wasSwapped:
            # if no elementes were swappped then exit
            return
 
if __name__ == "__main__":
    # break on the next line and jump into the pdb debugger (not VScode)
    # uncommenting this line will activate the pdb and not the VScode visual debugger.
    # https://docs.python.org/3/library/pdb.html
    #breakpoint() 

    # generate some range data
    data = [random.randrange(100) for i in range(10)]
    print(f"Unsorted array {data}")
    bubbleSort(data)
    print(f"Array average {average(data)}")

    print("Sorted array is:")
    for i in range(len(data)):
        print("% d" % data[i], end=" ")