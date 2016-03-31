priority2 = []
priority1 = []
priority0 = []

scheduler = []
blocked = []
scheduler.append(priority0)
scheduler.append(priority1)
scheduler.append(priority2)

procs = []
procs.append("init")

pri = 0
p2 = 0
p1 = 0
p0 = 0

R1 = 1
R2 = 2
R3 = 3
R4 = 4


def Priorities():
    global pri
    global p2
    global p1
    global p0

    if (pri == 2):
        return p2
    elif (pri == 1):
        return p1
    else:
        return p0

class Process(object):

    resources = {"R1": 0, "R2": 0, "R3": 0, "R4": 0}

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    def printName(self):
        return self.name
    def printProcess(self):
        print self.name + " ",
        print self.priority

    children = []
    rblock = ""

def Init():
    global priority2
    priority2 = []
    global priority1
    priority1 = []
    global priority0
    priority0 = []

    global scheduler
    scheduler = []
    global blocked
    blocked = []

    global procs
    procs = []
    procs.append("init")

    scheduler.append(priority0)
    scheduler.append(priority1)
    scheduler.append(priority2)

    global pri
    global p2
    global p1
    global p0
    pri = 0
    p2 = 0
    p1 = 0
    p0 = 0

    global R1
    global R2
    global R3
    global R4

    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4

    Create("init", 0)



def Create(name, priority):
    global pri
    global p2
    global p1
    global p0

    global scheduler

    p = Process(name, priority)
    scheduler[priority].append(p)

    if (name != "init"):
        childs = scheduler[0][0].children[:]
        childs.append(name)
        scheduler[0][0].children = childs

        if (pri != 0):
            childs = scheduler[pri][Priorities()].children[:]
            childs.append(name)
            scheduler[pri][Priorities()].children = childs
        procs.append(name)
    return p

def Schedule():
    fw = open('output.txt', 'a+')
    global scheduler
    global pri

    if (scheduler[2]):
        pri = 2
    elif (pri == 0 and scheduler[1]):
        pri = 1
    elif (pri == 1):
        pri = 1
    else:
        pri = 0

    print "PRI IS " + str(pri)

    if (pri == 2):
        print "P2 is NOW " + str(p2)
        print scheduler[2]
        fw.write(scheduler[2][p2].printName() + " ")
    elif (pri == 1):
        fw.write(scheduler[1][p1].printName() + " ")
    if (pri == 0):
        fw.write(scheduler[0][p0].printName() + " ")

def TimeOut():
     global pri
     global p2
     global p1
     global p0

     if not len(scheduler[pri]):
         fw.write("error ",)
     else:
         if (pri == 2):
            if (p2 == len(scheduler[pri]) - 1):
                p2 = 0
                'print "TIME OUT 0"'
            else:
                p2 = p2 + 1
                'print "TIME OUT 1"'
         if (pri == 1):
            if (p1 == len(scheduler[pri]) - 1):
                p1 = 0
                print "TIME OUT 0"
            else:
                p1 = p1 + 1
                print "TIME OUT 1"

def EndOfSched():
     global pri
     global p2
     global p1
     global p0
     global scheduler

     if(Priorities() == len(scheduler[pri])):
        if (pri == 2):
            p2 = 0
        elif (pri == 1):
            p1 = 0
        else:
            p0 = 0


def Request(name, amount):
    global R1
    global R2
    global R3
    global R4

    global pri
    global p2
    global p1
    global p0
    error = True

    fw = open('output.txt', 'a+')

    if (amount > 4 and amount < 1):
        fw.write("error ")
        return error
    elif (pri == 0):
        fw.write("error ")
        return error
    else:
        if name in ("R1", "R2", "R3", "R4"):
            if (name == "R1" and amount <= R1):
                R1 = 0
                d = scheduler[pri][Priorities()].resources.copy()
                d["R1"] = d["R1"] + amount
                scheduler[pri][Priorities()].resources = d
            elif (name == "R1" and amount > 1):
                fw.write("error ")
                return error
            elif (name == "R1" and amount > R1):
                d2 = scheduler[pri][Priorities()].resources.copy()
                d2["R1"] = amount
                scheduler[pri][Priorities()].resources = d2
                scheduler[pri][Priorities()].rblock = name
                blocked.append(scheduler[pri][Priorities()])
                scheduler[pri].pop(Priorities())

                EndOfSched()

            if (name == "R2" and amount <= R2):
                R2 = R2 - amount

                d = scheduler[pri][Priorities()].resources.copy()
                d["R2"] = d["R2"] + amount
                scheduler[pri][Priorities()].resources = d
            elif (name == "R2" and amount > 2):
                fw.write("error ")
                return error
            elif (name == "R2" and amount > R2):
                d2 = scheduler[pri][Priorities()].resources.copy()
                d2["R2"] = amount
                scheduler[pri][Priorities()].resources = d2
                scheduler[pri][Priorities()].rblock = name
                blocked.append(scheduler[pri][Priorities()])
                scheduler[pri].pop(Priorities())

                EndOfSched()

            if (name == "R3" and amount <= R3):
                R3 = R3 - amount

                d = scheduler[pri][Priorities()].resources.copy()
                d["R3"] = d["R3"] + amount
                scheduler[pri][Priorities()].resources = d
            elif (name == "R3" and amount > 3):
                fw.write("error ")
                return error
            elif (name == "R3" and amount > R3):
                d2 = scheduler[pri][Priorities()].resources.copy()
                d2["R3"] = amount
                scheduler[pri][Priorities()].resources = d2
                scheduler[pri][Priorities()].rblock = name
                blocked.append(scheduler[pri][Priorities()])
                scheduler[pri].pop(Priorities())

                EndOfSched()

            if (name == "R4" and amount <= R4):
                R4 = R4 - amount

                d = scheduler[pri][Priorities()].resources.copy()
                d["R4"] = d["R4"] + amount
                scheduler[pri][Priorities()].resources = d
            elif (name == "R4" and amount > 4):
                fw.write("error ")
                return error
            elif (name == "R4" and amount > R4):
                d2 = scheduler[pri][Priorities()].resources.copy()
                d2["R4"] = amount
                scheduler[pri][Priorities()].resources = d2
                scheduler[pri][Priorities()].rblock = name
                blocked.append(scheduler[pri][Priorities()])
                scheduler[pri].pop(Priorities())

                EndOfSched()
        else:
            fw.write("error ")

    fw.close()

def Free(name, amount):
    global R1
    global R2
    global R3
    global R4

    d = scheduler[pri][Priorities()].resources.copy()
    d[name] -= amount
    scheduler[pri][Priorities()].resources = d

    if (name == "R1"):
        R1 += amount
    elif (name == "R2"):
        R2 += amount
    elif (name == "R3"):
        R3 += amount
    else:
        R4 += amount

def Release(name, amountString):
    global R1
    global R2
    global R3
    global R4
    global scheduler
    global p2

    amount = int(amountString)
    fw = open('output.txt', 'a+')

    if (amount > 4):
        fw.write("error ")
    elif (amount < 1):
        fw.write("error ")
    elif (name not in scheduler[pri][Priorities()].resources):
        fw.write("error ")
    elif (amount > scheduler[pri][Priorities()].resources[name]):
        fw.write("error ")
    elif (not blocked):
        Free(name, amount)
        fw.write(scheduler[pri][Priorities()].name + " ")
    else:
        d = scheduler[pri][Priorities()].resources.copy()
        d[name] -= amount
        scheduler[pri][Priorities()].resources = d
        Free(name, amount)

        for i in range(0, len(blocked)):
            if(blocked[i].resources[name] == 0):
                pass
            elif(blocked[i].resources[name] > amount):
                fw.write(scheduler[pri][Priorities()].name)
                break
            else:
                if (name == "R1" and name == blocked[i].rblock):
                    R1 = amount - blocked[i].resources[name]
                elif (name == "R2" and name == blocked[i].rblock):
                    R2 = amount - blocked[i].resources[name]
                elif (name == "R3" and name == blocked[i].rblock):
                    R3 = amount - blocked[i].resources[name]
                elif (name == "R4" and name == blocked[i].rblock):
                    R4 = amount - blocked[i].resources[name]

                scheduler[blocked[i].priority].append(blocked[i])
                blocked.pop(i)

    fw.close()

def FreeAll(name):

    global R1
    global R2
    global R3
    global R4
    global blocked

    if (name.resources["R1"] != 0):
        if (R1 + name.resources["R1"] <= 1):
            R1 += name.resources["R1"]
        name.resources["R1"] = 0

    if (name.resources["R2"] != 0):
        if (R2 + name.resources["R2"] <= 2):
            R2 += name.resources["R2"]
        name.resources["R2"] = 0

    if (name.resources["R3"] != 0):
        if (R3 + name.resources["R3"] <= 3):
            R3 += name.resources["R3"]
        name.resources["R3"] = 0

    if (name.resources["R4"] != 0):
        if (R4 + name.resources["R4"] <= 4):
            R4 += name.resources["R4"]
        name.resources["R4"] = 0

    if (blocked):
        for x in range(0, len(blocked)):
            if (blocked[x].resources["R1"]):
                if (blocked[x].resources["R1"] <= R1 and blocked[x].rblock == "R1"):
                    R1 -= blocked[x].resources["R1"]
                    scheduler[blocked[x].priority].append(blocked[x])
                    blocked.pop(x)

            elif (blocked[x].resources["R2"]):
                if (blocked[x].resources["R2"] <= R2 and blocked[x].rblock == "R2"):
                    R2 -= blocked[x].resources["R2"]
                    scheduler[blocked[x].priority].append(blocked[x])
                    blocked.pop(x)

            elif (blocked[x].resources["R3"]):
                if (blocked[x].resources["R3"] <= R3 and blocked[x].rblock == "R3"):
                    R3 -= blocked[x].resources["R3"]
                    scheduler[blocked[x].priority].append(blocked[x])
                    blocked.pop(x)

            elif (blocked[x].resources["R4"]):
                if (blocked[x].resources["R4"] <= R4 and blocked[x].rblock == "R4"):
                    R4 -= blocked[x].resources["R4"]
                    scheduler[blocked[x].priority].append(blocked[x])
                    blocked.pop(x)
def Rec(string):
    global R1
    global R2
    global R3
    global R4

    if (string == "R1"):
        return R1
    elif (string == "R2"):
        return R2
    elif (string == "R3"):
        return R3
    else:
        return R4

def UnBlock():
    global R1
    global R2
    global R3
    global R4
    name = ["R1", "R2", "R3", "R4"]


    for i in blocked:
        for n in name:
            if(i.resources[n] == 0):
                pass
            elif(i.resources[n] > Rec(n)):
                print "NOT Enough"
            else:
                if (i in blocked):
                    blocked.pop(blocked.index(i))
                    if (n == "R1" and i.rblock == "R1"):
                        R1 = Rec(n) - i.resources[n]
                    elif (n == "R2" and i.rblock == "R2"):
                        R2 = Rec(n) - i.resources[n]
                    elif (n == "R3" and i.rblock == "R3"):
                        R3 = Rec(n) - i.resources[n]
                    elif (n == "R4" and i.rblock == "R4"):
                        R4 = Rec(n) - i.resources[n]

                    scheduler[i.priority].append(i)

def Delete(name):
    global pri
    global p2
    global p1
    global p0

    global blocked
    global scheduler

    for i in blocked:
        print "ALL ARE IN THE BLOCKED LIST: " + i.name

    fw = open('output.txt', 'a+')
    pointed2 = scheduler[pri][p2]
    pointed1 = scheduler[pri][p1]

    for i in range(0, len(scheduler[2])):
        if(scheduler[2]):
            if(scheduler[2][i].name == name):
                found = scheduler[2][i]
                if (not found.children):
                   FreeAll(found)
                   procs.pop(procs.index(found.name))
                   UnBlock()
                   scheduler[2].pop(i)


                   if (p2 >= len(scheduler[2])):
                       p2 = 0

                   elif (pointed2 != scheduler[pri][p2] and len(scheduler[pri]) != 1):
                       p2 -= 1
                else:
                    for i in range(0, len(found.children)):
                        for c in found.children:
                            Delete(c)
                    FreeAll(found)
                    procs.pop(procs.index(found.name))

                    UnBlock()
                    scheduler[2].pop(scheduler[2].index(found))


                    if (p2 >= len(scheduler[2])):
                       p2 = 0

                    elif (pointed2 != scheduler[pri][p2] and len(scheduler[pri]) != 1):
                       p2 -= 1


    for i in range(0, len(scheduler[1])):
        if (scheduler[1]):
            if (scheduler[1][i].name == name):
                found1 = scheduler[1][i]
                if (not found1.children):
                   FreeAll(found1)
                   procs.pop(procs.index(found1.name))
                   UnBlock()
                   scheduler[1].pop(i)
                   if (p1 >= len(scheduler[1])):
                       p1 = 0

                   elif (pointed1 != scheduler[pri][p1] and len(scheduler[pri]) != 1):
                       p1 -= 1
                else:
                    for i in range(0, len(found1.children)):
                        for c in found1.children:
                            Delete(c)
                    FreeAll(found1)
                    UnBlock()
                    procs.pop(procs.index(found1.name))
                    scheduler[1].pop(scheduler[1].index(found1))

                    if (p1 >= len(scheduler[1])):
                       p1 = 0

                    elif (pointed1 != scheduler[pri][p1] and len(scheduler[pri]) != 1):
                       p1 -= 1

    for proc in blocked:
        if (blocked):
            if (proc.name == name):
                foundb = proc
                if (not foundb.children):
                   FreeAll(foundb)
                   procs.pop(procs.index(foundb.name))

                   blocked.pop(blocked.index(foundb))
                   UnBlock()
                else:
                    for i in range(0, len(foundb.children)):
                        for c in foundb.children:
                            Delete(c)
                    FreeAll(foundb)
                    procs.pop(procs.index(foundb.name))

                    blocked.pop(blocked.index(foundb))
                    UnBlock()


    fw.close()

Init()
Schedule()
f = open('input.txt', 'r+')
for line in f:
    if line.split().__len__() > 0:
        print line.split()[0]
        if line.split()[0] == 'init':
            fw = open('output.txt', 'a+')
            Init()
            fw.write("\n")
            fw.write("init ")
            fw.close()
        if line.split()[0] == '...':
            fw = open('output.txt', 'a+')
            fw.write("...")
            fw.close()
        if line.split()[0] == 'cr':
            fw = open('output.txt', 'a+')
            print "CHECK DIS OUT"
            if (int(line.split()[2]) < 3 and int(line.split()[2] > 0)):
                Create(line.split()[1], int(line.split()[2]))
                Schedule()
                fw.close()
            else:
                Schedule()
                fw.write("error ")
                fw.close()
        if line.split()[0] == 'to':
            fw = open('output.txt', 'a+')
            if (not scheduler[pri]):
                fw.write("error ",)
            else:
                TimeOut()
                Schedule()
            fw.close()
        if line.split()[0] == 'req':
            if (Request(line.split()[1], int(line.split()[2]))):
                print "ERROR REQUEST"
            else:
                Schedule()
        if line.split()[0] == 'rel':
            Release(line.split()[1], line.split()[2])
        if line.split()[0] == 'de':
            fw = open('output.txt', 'a+')
            if (line.split()[1] == "init"):
                fw.write("error ")
            elif (line.split()[1] not in procs):
                fw.write("error ")
            else:
                Delete(line.split()[1])
                Schedule()
            fw.close()
f.close()
fw.close()


print "SCHEDULER IS : "
print scheduler

print "BLOCKED : "
for i in blocked:
    print i.name


print "SCHEDULED : "

print R1
print R2
print R3
print R4