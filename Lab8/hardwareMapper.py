
from moduleTasks import parseLine

def mapHardwareLine(line):

    # Ins = ''
    # Comp = ''
    # for x in line:
    #     if x == ':':
    #         break
    #     else:
    #         Ins += x
    #
    # for i in range(len(Ins)+2,len(line)):
    #     if line[i] == ' ':
    #         break
    #     else:
    #         Comp += line[i]
    # lst =''
    # l = []
    # for i in range (len(Ins)+11+len(Comp),len(line)):
    #     lst += line[i]
    # lst = lst.strip('()')
    # lst = lst.split(',')
    # for x in lst:
    #     x = x.split('=>')
    #     x[0] = x[0].strip(' ')
    #     x[1] = x[1].strip(' ')
    #     a = '.'+x[0]+'('+x[1]+')'
    #     l.append(a)
    # out = ''
    # for x in l:
    #     out += str(x)+','
    # out = out.strip('),')
    #
    #
    # res = Comp+' '+Ins+' '+'('+out+')'
    #
    # try:
    #     parseLine(res)
    # except:
    #     return 'Error: Bad Line'
    # else:
    #     return res

    try:
        l = parseLine(line)
    except:
        return('Error: Bad line')


    l = list(l)
    s = ''
    t = '('
    for x in l[2]:

        x = list(x)
        s = x[0] + '=>' + x[1]
        t += s+','
    t = t.strip(',')
    t += ')'
    res = l[1] + ': '+l[0]+' PORT MAP'+t+';'
    return(res)

def mapFile(sourceFile, targetFile):
    lst =[]
    f = open(targetFile,'w+')
    with open(sourceFile, 'r') as file1:
        all_lines = file1.readlines()

        for line in all_lines:
            a = mapHardwareLine(line)
            lst.append(a+'\n')
            #f.write(a)
            #f.write('\n')

    #lst.sort(reverse=True)

    for w in lst:
        f.write(w)

if __name__ == "__main__":

    #a = mapHardwareLine('Comp1 Ins1 (.port1(pin1),.port2(pin2))')#'ins1: comp1 PORT MAP(port1=>pin1, port2=>pin2);')
    #mapFile('verilog_test.v', 'patito')
    #print(a)
    pass