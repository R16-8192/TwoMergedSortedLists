import random
def CreateLists(x,y):
    global flist
    global slist
    flist = []
    slist = []
    # x = lists size
    # y = lists value
    while x > 0:
        a = random.randint(0, y)
        b = random.randint(0, y)
        flist.append(a)
        slist.append(b)
        x -= 1
    return flist, slist
def MergeLists(alpha, beta):
    flistSize = len(alpha)
    slistSize = len(beta)
    global llist 
    llist = []
    for i in alpha:
        llist.append(i)
    for i in beta:
        llist.append(i)
    return llist
def SortList(result):
    result.sort()
    print("Merged & Sorted List : ", result)
lsInput = int(input("Enter List Size : "))
lvInput = int(input("Enter List Highest-value : "))
CreateLists(x=lsInput, y=lvInput)
print("First List BEFORE : " , flist)
print("Second List BEFORE : " , slist)
MergeLists(alpha=flist, beta=slist)
SortList(result=llist)
