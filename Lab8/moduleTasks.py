import re


def isIdValid(pin):
    reg = re.compile(r'\w')
    for x in pin:

        if re.findall(reg,x) != []:
            pass
        else:

            return False

    return True


def parseAssignment(assignment):


    Port = ''
    Pin = ''

    if assignment[0] != '.':
        raise ValueError(assignment)
    x = False
    y = False
    for x in assignment:
        if x == '(':
            x = True
        if x == ')':
            y = True

    if x == False or y == False:
        raise ValueError(assignment)

    for i in range(1,len(assignment)):
        if assignment[i] == '(':
            break
        else:
            Port += assignment[i]

    for i in range(len(Port)+2,len(assignment)):
        if assignment[i] == ')':
            break
        else:
            Pin += assignment[i]


    if isIdValid(Port) == False:
        raise ValueError(assignment)
    if isIdValid(Pin)  == False:
        raise ValueError(assignment)

    lst = [Port, Pin]
    return tuple(lst)


def parseLine(line):

    Comp = ''
    Ins = ''
    lst = ''

#    if line[len(line)-1] != ')':
#        raise ValueError(line)



    x = False

    for x in line:
        if x == '(':
            x = True


    if x == False:
        raise ValueError(line)
    #-----------------------------------------

    for i in range(2,len(line)):
        if line[i] == ' ':
            break
        else:
            Comp += line[i]

    if isIdValid(Comp)  == False:
        raise ValueError(Comp)

    #------------------------------------------

    for i in range(len(Comp)+1,len(line)):
        if line[i] == '(':
            break
        else:
            Ins += line[i]
            Ins = Ins.strip(' ')


    if isIdValid(Ins)  == False:
        raise ValueError(Ins)
    #-------------------------------------------

    for i in range(len(Comp)+len(Ins)+3,len(line)):
         
        lst += line[i]
   
    lst = lst.split(',')
    l=[]
    for x in lst:
        x = x.strip(' ')
        x = x.strip('(')

        x = x.strip(' ')

        l.append(parseAssignment(x))

    if isIdValid(lst)  == False:
        raise ValueError(lst)
    #--------------------------------------------

    res = [Comp,Ins,l]
    return tuple(res)






if __name__ == "__main__":

    # a =parseAssignment('.port1(pin1)')
    # print(a)
    #
    # b = parseLine('Comp1 Ins1 (.port1(pin1),.port2(pin2))')
    # print(b)
    pass