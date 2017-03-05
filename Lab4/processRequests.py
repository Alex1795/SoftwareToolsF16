

import os



def processRequests():

    lst =[]
    dic = getAccessControlByLogin()
    with open('ServerRequests.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:
        line = line.strip('\n')
        line =line.split(':')
        user = line[0]
        user = user.strip()

        url = line[2]
        #url = url.strip('/')
        line = line[2].split('/')
        url = 'http:{0}'.format(url)

        act = line[3]
        page= line [4]
        if act in dic[user]:
            bool = (1==1)
        else:
            bool = (1==0)
        final = (user,url,act,page,bool)
        lst.append(final)
















    return lst

def getAccessControlByLogin():
    h = 2
    dic = {}
    with open('AccessControl.txt','r') as file:
        all_lines = file.readlines()

    for line in all_lines:

         if h != 0:
             h = h-1
             pass
         else:
             line = line.strip('\n')
             line =line.split(':')
             line[0] = line[0].strip()
             line[1] = line[1].strip()
             if line[0] in dic:
                 dic[line[0]].add (line[1])
             else:
                 dic[line[0]] = set()
                 dic[line[0]].add(line[1])





    return dic


def getAccessControlByController():

    h = 2
    dic2 ={}
    with open('Logins.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:

         if h != 0:
             h = h-1
             pass
         else:
             line = line.strip('\n')
             line =line.split('|')
             line[0] = str(line[0]).strip()
             line[1] = str(line[1]).strip()
            # if line[1] in dic2:
             dic2[line[1]] = line[0]
             #else:
                 #dic2[line[1]] = set()
             #    dic2[line[1]] = line[0]


    h = 2
    dic = {}
    with open('AccessControl.txt','r') as file:
        all_lines = file.readlines()

    for line in all_lines:

         if h != 0:
             h = h-1
             pass
         else:
             line = line.strip('\n')
             line =line.split(':')
             user = line[0].strip()
             controller = line[1].strip()


             if controller in dic:
                dic[controller].add (dic2.get(user))


             else:
                 dic[controller] =set()
                 x = dic2[user]


                # print(line[1])
                 dic[controller].add(x)







    return dic


def getActionsOfController():

    dic2 ={}
    with open('ServerRequests.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:
        line = line.strip('\n')
        line =line.split('/')
        #line[0] = str(line[0]).strip()#line[1] = str(line[1]).strip()

        if line[3] in dic2:
            dic2[line[3]].add(line[4])
        else:
            dic2[line[3]] = set()
            dic2[line[3]].add(line[4])

    return dic2

def isAccessAllowedFor(userID, url):

    dic = getAccessControlByLogin()
    url = url.split('/')
    act = url[3]
    if act in dic[userID]:
            bool = (1==1)
    else:
        bool = (1==0)
    return bool


def getRequestsBy(userID):
    lst =[]
    dic = getAccessControlByLogin()
    with open('ServerRequests.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:
        line = line.strip('\n')
        line =line.split(':')
        user = line[0]
        user = user.strip()

        url = line[2]

        line = line[2].split('/')
        url = 'http:{0}'.format(url)
        act = line[3]

        if act in dic[user]:
            bool = (1==1)
        else:
            bool = (1==0)
        if user == userID:

            nxt = (url, bool)
            lst.append(nxt)

    return lst




def aggregateUserRequests():
    lst ={}
    dusers={}
    h =2
    with open('Logins.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:

         if h != 0:
             h = h-1
             pass
         else:
             line = line.strip('\n')
             line =line.split('|')
             line[0] = line[0].strip()
             line[1] = line[1].strip()

             dusers[line[1]] = line[0]


    h = 2

    dic2 ={}


    with open('AccessControl.txt','r') as file:
        all_lines = file.readlines()

    for line in all_lines:

         if h != 0:
             h = h-1
             pass
         else:
             line = line.strip('\n')
             line =line.split(':')
             line[0] = line[0].strip()
             line[1] = line[1].strip()
             person = dusers[line[0]]
             if line[0] in lst:
                 pass
             else:

                 lst[person] =[]
                 lst[person].append(0)
                 lst[person].append(0)
    dic = getAccessControlByLogin()
    with open('ServerRequests.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:

        line = line.strip('\n')
        line =line.split(':')
        user = line[0]
        user = user.strip()



        line = line[2].split('/')
        person = dusers[user]

        act = line[3]

        if act in dic[user]:


            lst[person][0] = lst[person][0]+1



        else:


            lst[person][1] = lst[person][1]+1











    return lst





def aggregateControllerRequests():
    lst ={}
    dic2 = getAccessControlByController()
    dic = getAccessControlByLogin()
    dusers = {}



    h = 2

    with open('Logins.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:

         if h != 0:
             h = h-1
             pass
         else:
             line = line.strip('\n')
             line =line.split('|')
             line[0] = line[0].strip()
             line[1] = line[1].strip()

             dusers[line[1]] = line[0]


    with open('ServerRequests.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:

        line = line.strip('\n')
        line =line.split(':')
        controller = line[2].strip()
        controller = controller.split('/')
        controller = controller[3]
        lst[controller] = []
        lst[controller].append(0)
        lst[controller].append(0)
    with open('ServerRequests.txt', 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:
        l2 = line


        l2 = l2.strip('\n')
        l2 =l2.split(':')

        controller = l2[2].strip()
        controller = controller.split('/')
        controller = controller[3]




        line = line.strip('\n')
        line =line.split(':')
        user = line[0]
        user = user.strip()

        url = line[2]
        #url = url.strip('/')
        line = line[2].split('/')
        url = 'http:{0}'.format(url)

        act = line[3]
        page= line [4]


        person = dusers[user]

        if person in dic2[controller]:
            lst[controller][0] = lst[controller][0]+1



        else:
            lst[controller][1] = lst[controller][1]+1

    return lst

if __name__ == "__main__":

    a = aggregateUserRequests()
    print(a)


    pass
