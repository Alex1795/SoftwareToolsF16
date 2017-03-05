import re



def getsensor(filename):


    rID = re.compile(r'<(\w*?)>')
    with open(filename,'r') as file:
        all_lines = file.read()

    ID = re.findall(rID,all_lines)

    return ID


def getFloatData(sensorID):
    #slst = getsensor('sensors.xml')

    filename = 'sensors.xml'

    with open(filename,'r') as file:
        all_lines = file.read()

    rline = re.compile(r'<{0}>\S*(.*)\S*</{0}>'.format(sensorID),re.S)
    rfloats = re.compile((r'([-+]?\d*\.\d*)?'))
    floats = re.findall(rline,all_lines)

    if floats == []: return []


    numbers = re.findall(rfloats,str(floats))
    res = []


    for x in numbers:
        n = re.findall(rfloats,x)
        if n != ['']:
            res.append(n[0])

    return res





    pass

def getScientificData(sensorID):
    filename = 'sensors.xml'

    with open(filename,'r') as file:
        all_lines = file.read()

    rline = re.compile(r'<{0}>\S*(.*)\S*</{0}>'.format(sensorID),re.S)
    rfloats = re.compile((r'([-+]?\d*\.\d*e?E?[-+]?\d)?'))
    floats = re.findall(rline,all_lines)

    if floats == []: return []


    numbers = re.findall(rfloats,str(floats))
    res = []


    for x in numbers:
        n = re.findall(rfloats,x)
        if n != ['']:
            res.append(n[0])

    return(res)

def getOptions(commandline):

    rnumber = re.compile(r'-(\w \d+)')
    raddress = re.compile((r'-(\w /.*)-'),re.S)
    numb = re.compile(r'\d*')
    options = re.findall(rnumber,commandline)
    options2 = re.findall(raddress,commandline)


    res =  []
    for x in options:
        n = re.findall(numb,x)
        add = [x[0] , n[2]]
        res.append(tuple(add))

    for x in options2:
        var = x[1:]
        add = [x[0],var]
        res.append(tuple(add))
    return(res)

if __name__ == "__main__":



    #print(getOptions('alex.bash -v -i 2 -p /local/bin/alex -o -i 89'))
    pass