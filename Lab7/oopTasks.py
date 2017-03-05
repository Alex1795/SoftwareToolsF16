
class Course:

    def __init__(self, courseID, fst, snd, final):

        self.courseID = courseID
        self.fst = fst
        self.snd = snd
        self.final = final
        self.total = (0.25 * float(fst))+(0.25 * float(snd))+(0.5*float(final))
        self.letter = self.getLetterGrade()

    def __str__(self):


        a = self.fst
        u,d = str(a).split('.')
        d = d[:2]
        a = str(u+'.'+d)

        b = self.snd
        u,d = str(b).split('.')
        d = d[:2]
        b = str(u+'.'+d)

        c = self.final
        u,d = str(c).split('.')
        d = d[:2]
        c = str(u+'.'+d)

        e = self.total
        u,d = str(e).split('.')
        d = d[:2]
        e = str(u+'.'+d)


        return ('{0}: ({1}, {2}, {3}) = ({4}, {5})'.format(self.courseID,a,b,c,e,self.letter))

    def getLetterGrade(self):
        if self.total >= 90:
            return 'A'
        else:
            if self.total >= 80:
                return  'B'
            else:
                if self.total >= 70:
                    return  'C'
                else:
                    if self.total >= 60:
                        return  'D'
                    else:
                        return  'F'

class Student:

    def __init__(self, name):

        self.name = name
        self.courses = dict()


    def __str__(self):
        lst =[]
        for _,val in self.courses.items():
            x = '({0}: {1})'.format(val.courseID , val.letter)
            lst.append(x)
        b = ''
        for x in lst:
            b = str(x) +' ' + b
        #lst = str(lst)
        #lst = lst.strip('[]')
        #print(lst)
        return ('{0}: {1}'.format(self.name,b))

    def addCourse(self, course):
        self.courses[course.courseID] = course


    def generateTranscript(self):
        lst =[]
        for _,val in self.courses.items():
            x = str(val)
            lst.append(x)
        lst.sort()
        b = ''
        for x in lst:
            b = x + '\n' + b


        return '{0}\n{1}\n'.format(self.name,b)



class School:

    def __init__(self, name):
        self.name = name
        self.students = dict()


    def __str__(self):
        ct =0
        lst =[]
        for _,val in self.students.items():
            ct = ct + 1
            lst.append(str(val.name))
        lst.sort()
        b = ''

        for x in lst:
            b = x + '\n' +b
        return '{0}: {1} students \n{2}'.format(self.name,ct,b)


    def loadStudentsInfo(self, filename):
        with open(filename, 'r') as file:
            lines = file.read()
            lines =lines.split("\n\n")

            for x in lines:
                x =x.split('\n')
                st =Student(x[0])

                for i in range (2, len(x)):
                    course = x[i][4:10]
                    fst = x[i][12:14]+'.00'
                    snd = x[i][16:18]+'.00'
                    final=x[i][20:22]+'.00'
                    C = Course(course,fst,snd,final)
                    st.addCourse(C)
                self.students[x[0]] = st





    def saveSchoolInfo(self, filename):
        lst =[]
        f = open (filename, 'w+')
        for _,val in self.students.items():
            f.write(val.name)
            f.write('\n')
            for _,i in val.courses.items():
                f.write(str(i))
                f.write('\n')
            f.write('\n')


if __name__ == "__main__":


    pass