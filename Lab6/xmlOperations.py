import re
def convertToAttrib():
    rx = re.compile(r'<X>\S*(.*?)\S*</X>',re.S)
    ry = re.compile(r'<Y>([- +]?[0-9]+\.[0-9]+)')
    rID = re.compile(r'(p\d)')

    f = open ('points_out.xml', 'w+')
    f.write('<?xml version="1.0"?>')
    f.write('\n')
    f.write('<coordinates>')
    f.write('\n')

    with open('points.xml','r') as file:
        all_lines = file.read()


    ID = re.findall(rID,all_lines)
    px = []

    x = re.findall(rx,all_lines)
    for y in x:
        x = re.findall(r'([- +]?[0-9]+\.[0-9]+)',y)
        x[0] = x[0].strip()
        px.append(x[0])

    y = re.findall(ry,str(all_lines))

    for i in range (0, len(ID)):
        f.write('   <point ID="{0}" X="{1}" Y="{2}" />\n'.format(ID[i], px[i], y[i] ))

    f.write('</coordinates>')
    f.close()


    return


def getGenres():
    rgen = re.compile(r'<genre>(\w+)</genre>')
    with open('books.xml','r') as file:
        all_lines = file.read()

    genres = re.findall(rgen,all_lines)
    res =[]
    for x in genres:
        if x in res:
            pass
        else:
            res.append(x)

    res.sort()

    return res

def getAuthorOf(bookName):
    with open('books.xml','r') as file:
        all_lines = file.read()

    rauthor = re.compile(r'<author>(.*?)</author>')
    authors = re.findall(rauthor,all_lines)

    rbooks  = re.compile(r'<title>(.*?)</title>')
    books   = re.findall(rbooks,all_lines)
    res = 'nope'

    for i in range(0, len(books)):
        if books[i] == bookName:
            res = authors[i]

    if res == 'nope':
        return None
    else:
        return res
def getBookInfo(bookID):

    with open('books.xml','r') as file:
        all_lines = file.read()

    rauthor = re.compile(r'<author>(.*?)</author>')
    authors = re.findall(rauthor,all_lines)
    rbooks  = re.compile(r'<title>(.*?)</title>')
    books   = re.findall(rbooks,all_lines)
    rid  = re.compile(r'id="(.*?)">')
    ID   = re.findall(rid,all_lines)
    res = 'nope'

    for i in range(0, len(books)):
        if ID[i] == bookID:
            res = (authors[i], books[i])

    if res == 'nope':
        return None
    else:
        return tuple(res)


def getBooksBy(authorName):
    with open('books.xml','r') as file:
        all_lines = file.read()

    rauthor = re.compile(r'<author>(.*?)</author>')
    authors = re.findall(rauthor,all_lines)
    rbooks  = re.compile(r'<title>(.*?)</title>')
    books   = re.findall(rbooks,all_lines)

    res =[]
    for i in range(0, len(authors)):
        if authors[i] == authorName:
            res.append(books[i])

    return(res)


def getBooksBelow(bookPrice):
     with open('books.xml','r') as file:
        all_lines = file.read()

     rprice = re.compile(r'<price>(.*?)</price>')
     prices = re.findall(rprice,all_lines)

     rbooks  = re.compile(r'<title>(.*?)</title>')
     books   = re.findall(rbooks,all_lines)

     res= []

     for i in range (0, len(prices)):
         if float(prices[i]) < float(bookPrice):
             res.append(books[i])
     res.sort()

     return(res)

def searchForWord(word):

    with open('books.xml','r') as file:
        all_lines = file.read()
    rbooks  = re.compile(r'<title>(.*?)</title>')
    books   = re.findall(rbooks,all_lines)

    rdes    = re.compile(r'<description>(.*?)</description>',re.S)
    des     = re.findall(rdes,all_lines)


    res= []

    for i in range(0, len(books)):
        if re.search(word,des[i]) != None:
            res.append(books[i])
        if  re.search(word,books[i]) != None:
            res.append(books[i])
    res.sort()
    return res


if __name__ == '__main__':

    #a = getBookInfo('bk102')
    #print(type(a))
    pass
