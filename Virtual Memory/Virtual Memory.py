bitmap = [0] * 1024
bitmap[0] = 1

flag = False
dict = {}
emptyTLB = True

segTable = [0] * 512

memory = [0] * 1024
memory[0] = segTable


class PT:
    def __init__(self, page, seg, add):
        self.page = page
        self.seg = seg
        self.add = add
        self.table = [0] * 1024
        print "PT CREATION"
        print seg
        print page
        print add
        if (not page == -1):
            self.table[page] = add

def checkSeg(seg):
    if (memory[0][seg] == 0):
        return True
    else:
        return False

def checkPT(PT, element):
    if (PT.table[element] == 0):
        return True
    else:
        return False

def checkBitmap(add):
    if (add == -1):
        return True
    if (bitmap[add] == 0):
        return True
    else:
        return False



def addPT(seg, add, page):
    add = add / 512
    if checkSeg(seg):
        if checkBitmap(add) and checkBitmap(add + 1):
            memory[0][seg] = PT(page, seg, add)
            if (not add == -1):
                bitmap[add] = 1
                bitmap[add + 1] = 1
            else:
                print "FAIL at Segment: " + str(seg)
        else:
            print "FAIL at Physical Address: " + str(add) + ", " + str(add + 1)


def editPT(page, seg, add):
    add = add / 512
    if (memory[0][seg] == 0):
        if checkBitmap(add):
            for x in range(1, len(bitmap)):
                if (bitmap[i] == 0 and bitmap[i + 1] == 0):
                    bitmap[i] = 1
                    bitmap[i + 1] = 1
                    break
            memory[0][seg] = PT(page, seg, add)
            if (not add == -1):
                bitmap[add] = 1
            else:
                print "FAIL at Segment: " + str(seg)
        else:
            print "FAIL at Physical Address: " + str(add)
    else:
        if (memory[0][seg].table[page] == 0):
            if checkBitmap(add):
                memory[0][seg].page = add
                memory[0][seg].table[page] = add
                if (not add == -1):
                    bitmap[add] = 1
                else:
                    print "TABLE FAIL at Segment: " + str(seg)
            else:
                print "PAGE FAIL at Physical Address: " + str(add)
        else:
            print "PAGE TABLE FAIL at: " + str(page)
        print "CHECK TABLE"
        print memory[0][seg].table


def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(32)[::-1])

f = open('input1.txt', 'r+')
line = f.readline().split()
for i in xrange(0,len(line),2):
    seg = int(line[i])
    add = int(line[i+1])
    if add == -1:
        memory[0][seg] = -1
    else:
        addPT(seg, add, -1)


print "BITMAP"
print bitmap
print "MEMORY"
print memory

line = f.readline().split()
for i in xrange(0,len(line),3):
    seg = int(line[i + 1])
    page = int(line[i])
    pageTable = memory[0][seg]
    add = int(line[i + 2])


    if (checkBitmap(add / 512)):
        editPT(page, seg, add)
    else:
        print "PAGE FAIL at Physical Address " + str(add / 512)

    print "FINAL BITMAP"
    print bitmap

f.close()

def readVA(num):
    print num
    num = toBinary(num)
    seg = int(num[4:13], 2)
    page = int(num[13:23], 2)
    print page
    off = int(num[23:32], 2)
    global emptyTLB
    global flag


    if (flag):
        if (not emptyTLB):
            for key in dict:
                if (key.page == page and key.seg == seg):
                    LRU = dict[key]
                    for item in dict:
                        if (dict[item] > LRU):
                            dict[item] -= 1
                    dict[key] = 3
                    return "h " + str(key.add * 512 + off)

    if (isinstance(memory[0][seg], int)):
        if (memory[0][seg] == 0):
            if (flag):
                return "m err"
            else:
                return "err"
        elif (memory[0][seg] == -1):
            if flag:
                return "m pf"
            else:
                return "pf"
    else:
        if (memory[0][seg].table[page] == 0):
            if flag:
                return "m err"
            else:
                return "err"
        elif (memory[0][seg].table[page] == -1):
            if flag:
                return "m pf"
            else:
                return "pf"
        else:
            if (not flag):
                return (memory[0][seg].table[page] * 512 + off)
            else:
                if emptyTLB:
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                    emptyTLB = False
                else:
                    for entry in dict.keys():
                        dict[entry] -= 1
                        if (dict[entry] == -1):
                            del dict[entry]
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                return "m " + str(memory[0][seg].table[page] * 512 + off)

def writeVA(num):
    num = toBinary(num)
    seg = int(num[4:13], 2)
    page = int(num[13:23], 2)
    off = int(num[23:32], 2)
    global emptyTLB
    global flag

    if (flag):
        if (not emptyTLB):
            for key in dict:
                if (key.page == page and key.seg == seg):
                    LRU = dict[key]
                    for item in dict:
                        if (dict[item] > LRU):
                            dict[item] -= 1
                    dict[key] = 3
                    return "h " + str(key.add * 512 + off)

    if (isinstance(memory[0][seg], int)):
        if (memory[0][seg] == 0):
            for x in range(1, len(bitmap)):
                if (bitmap[x] == 0 and bitmap[x + 1] == 0):
                    bitmap[x] = 1
                    bitmap[x + 1] = 1
                    memory[0][seg] = PT(page, seg, x)
                    break
            for x in range(1, len(bitmap)):
                if (bitmap[x] == 0):
                    bitmap[x] = 1
                    memory[0][seg].table[page] = x
                    break
            if (flag):
                if (emptyTLB):
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                    emptyTLB = False
                else:
                    for entry in dict.keys():
                        dict[entry] -= 1
                        if (dict[entry] == -1):
                            del dict[entry]
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                return "m " + str(memory[0][seg].table[page] * 512 + off)

            return memory[0][seg].table[page] * 512 + off

        elif (memory[0][seg] == -1):
            if (flag):
                return "m pf"
            else:
                return "pf"
        else:
            return "m " + str(memory[0][seg] * 512 + off)
    else:
        if (memory[0][seg].table[page] == 0):
            for x in range(1, len(bitmap)):
                if (bitmap[x] == 0):
                    bitmap[x] = 1
                    memory[0][seg].table[page] = x
                    break
            if (flag):
                if (emptyTLB):
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                    emptyTLB = False
                else:
                    for entry in dict.keys():
                        dict[entry] -= 1
                        if (dict[entry] == -1):
                            del dict[entry]
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                return "m " + str(memory[0][seg].table[page] * 512 + off)
            return memory[0][seg].table[page] * 512 + off
        elif (memory[0][seg].table[page] == -1):
            if flag:
                return "m pf"
            else:
                return "pf"
        else:
            if (flag):
                if (emptyTLB):
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                    emptyTLB = False
                else:
                    for entry in dict.keys():
                        dict[entry] -= 1
                        if (dict[entry] == -1):
                            del dict[entry]
                    dict[PT(page, seg, memory[0][seg].table[page])] = 3
                return "m " + str(memory[0][seg].table[page] * 512 + off)
            return memory[0][seg].table[page] * 512 + off

print "\n"
input2 = open('input2.txt', 'r+')
line = input2.readline().split()
for i in xrange(0,len(line),2):
    if (line[i] == str(0)):
        output = open('output1.txt', 'a+')
        output.write(str(readVA(line[i + 1])) + " ")
        output.close()
        'if (isinstance(readVA(line[i + 1]), int)):'

    elif (line[i] == str(1)):
        output = open('output1.txt', 'a+')
        output.write(str(writeVA(line[i + 1])) + " ")
        output.close()
    else:
        output = open('output1.txt', 'a+')
        output.write("err ")
        output.close()

input2.close()


bitmap = [0] * 1024
bitmap[0] = 1

segTable = [0] * 512

memory = [0] * 1024
memory[0] = segTable

f = open('input1.txt', 'r+')
line = f.readline().split()
for i in xrange(0,len(line),2):
    seg = int(line[i])
    add = int(line[i+1])
    if add == -1:
        memory[0][seg] = -1
    addPT(seg, add, -1)

line = f.readline().split()
for i in xrange(0,len(line),3):
    seg = int(line[i + 1])
    page = int(line[i])
    pageTable = memory[0][seg]
    add = int(line[i + 2])


    if (checkBitmap(add / 512)):
        editPT(page, seg, add)
    else:
        print "PAGE FAIL at Physical Address " + str(add / 512)


    print "FINAL BITMAP"
    print bitmap

f.close()

flag = True
print "\n"
print "CACHE TIME"
input2 = open('input2.txt', 'r+')
line = input2.readline().split()
print line
for i in xrange(0,len(line),2):
    if (line[i] == str(0)):
        output = open('output2.txt', 'a+')
        output.write(str(readVA(line[i + 1])) + " ")
        output.close()

    elif (line[i] == str(1)):
        output = open('output2.txt', 'a+')
        output.write(str(writeVA(line[i + 1])) + " ")
        output.close()
    else:
        output = open('output2.txt', 'a+')
        output.write("err ")
        output.close()

input2.close()

for key in dict:
    print "HERE'S THE TLB"
    print str(key.seg) + " " + str(key.page) + " " + str(key.add)
    print dict[key]