

# The following variable(s) are the only lines of code that should be outside of a function.

accounts = [
    'Mark Thomas:    $11.99   $52.08   $81.15   $79.16   $16.23   $88.11   $21.20   $0.02   ',
    'Gregory Powell:      $97.42     $96.05     $71.82     $24.79     $14.42     $60.84     $35.46     ',
    'Kevin Wood:     $93.37    $16.73    $97.05    $14.57    $53.29    ',
    'Martin Watson:     $20.53    $90.58    $22.07    $1.28    $75.40    $48.98    $36.46    $42.65    $5.01  $52.62  ',
    'Frank Young:     $32.02    $51.20    $0.99    $51.85    $88.38    $67.26    $62.72    $47.36    $38.89    ',
    'Michelle Thompson:     $2.44    $100.72    $81.44    $48.07    $68.71    $23.11    $79.23    $71.02    ',
    'Anne Harris:     $30.10    $58.32    $6.22    $3.67    $30.02    $37.65    $6.17    $41.30    $51.15    ',
    'Kelly Cooper:      $73.74     $57.63     $91.94     $42.94     $59.26     $64.30     $13.59     $19.69     $4.11 ',
    'Benjamin Foster:      $4.22     $63.02     $73.07     $99.73     $24.00     $77.79     $20.30     ',
    'Marie Perry:    $32.90   $80.27   $70.18   $68.74   $14.11   $7.38   ',
    'Cynthia Simmons:      $91.64     $56.95     $40.73     $61.28     $53.88     $77.05     $6.88     $23.37     ']

def getRowSum(accList):

    lng = len(accList)
    total = [ "" for i in range(lng)]
    tot=0
    for i in range (0,lng):
        a = accList[i].split('$')
        l = len(a)
        for j in range (1, l):

            tot = tot+float(a[j])
            #tot = [tot+y for y in a if type(y) == type(1.0)]
        tot = round(tot,2)
        #tot = sum(tot)
        total[i]=tot

    return total


def getDoublePalindromes():
    lst= [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    k=0
    for i in range (10,1000000):

        a=str(i)
        x=[]
        for h in a:
            x.append(h)
        x.reverse()
        x=''.join(x)

        b=[]

        c=bin(i)
        c=str(c)

        for h in c:
            b.append(h)
        del b[0:2]
        b=''.join(b)
        y=[]
        for h in b:
            y.append(h)
        y.reverse()

        y=''.join(y)



        if y == b and a == x:

            lst[k] = i
            k=k+1




    return lst


def scaleVector(s, vList):

    if type(s) != int and type(s) != float:
        return None


    if type(vList) != list:
        return None


    lgt = len(vList)
    res=[]
    for i in range (0,lgt):

        res.append(vList[i] * s)



    return res


def convertToBoolean(num):

    if type(num) != int or num < 0 or num > 255:
        return None

    res=[]

    c = bin(num)
    c = str(c)

    for h in c:
        res.append(h)

    del res[0:2]
    lgt = len(res)
    for i in range (0,lgt):

        x = bool(int(res[i]))
        res[i] = x



    return res


def convertToInteger(boolList):

    lgt = len(boolList)
    res=[]
    b = boolList
    for i in range (0, lgt):
       if b[i] == True:
           res.append('1')
       else:
           res.append('0')

    #res.insert(0,'0')
    #res.insert(1,'b')
    res = ''.join(res)
    res = int(res,2)
    return res



def getWords(sentence, n):

    lst = sentence.split()
    res=[]
    for y in lst:
        if len(y) == n:

            res.append(y)



    return res



def isSubListOf(superList, subList):

    l1 = len(superList)
    l2 = len(subList)



    for i in range (0, l1):

        if subList == superList[i:i+l2]:
            return True



    return False




def getElementsAt(l, i):

    res=[]
    for j in range (0,lgt):
        if i > len(l[j]):
            res.append(0)
        else:
         res.append(l[j][i])


    return res


if __name__ == "__main__":

    pass
