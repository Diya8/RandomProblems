# Source: https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python

def recoverSecret(triplets):
    throwList = []
    s = ""
    n = len(triplets)
    lst = [[] for _ in range(n)]
    while triplets != lst:
        myList, myThrowAways = [], []
        i = 0
        for x in triplets:
            if throwList != []:
                if throwList[-1] in x:
                    #print(k, triplets[i], x)
                    triplets[i].remove(throwList[-1])
            if x!=[]:
                if x[0] not in myList and x[0] not in myThrowAways:
                    myList.append(x[0])
                for j in myList:
                    if j in x[1:]:
                        myList.remove(j)
                        myThrowAways.append(j)
            i += 1
        if myList != []:
            s = s+myList[0]
            throwList.append(myList[0])
        # print("letter is", myList)
        # print(triplets)
    return s
