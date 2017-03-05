class Entry:

    def __init__(self, k1, k2, v):

        if type(k1) != int:
            raise TypeError('k1 must be an integer')
        if type(k2) != int:
            raise TypeError('k2 must be an integer')

        if type(v) != str:
            raise TypeError('The value must be a string')

        key = tuple([k1,k2])
        self.key =key
        self.value =v
        
    def __str__(self):

        return '{0}: "{1}"'.format(self.key, self.value)


    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False
class Lookup:

    def __init__(self, name):
        if name == '':
            raise ValueError('Name cannot be empty')
        self._name = name
        self._container = {}

    def __str__(self):
        return '["{0}": {1} Entries]'.format(self._name,len(self._container))

    def add(self, entry):
        try:
            self._container[entry.key]
        except:
            self._container[entry.key] = entry.value

        else:
            raise KeyError('Entry already exist')


    def update(self, entry):
        try:
            self._container[entry.key]
        except:
            raise KeyError('Entry does not exist')

        else:
            self._container[entry.key] = entry.value


    def addOrUpdate(self, entry):
        try:
            self.add(entry)
        except:
               try:
                   self.update(entry)
               except:
                   pass


    def remove(self, entry):
        try:
            self._container.pop(entry.key)
        except:
            raise KeyError("Can't erase, entry does no texist")

    def count(self):
        return len(self._container)

    def __getitem__(self, item):
        res = []

        try:
            self._container[item]
            return self._container[item]
        except:
              for i in range (0,999):
                  t = tuple([item,i])
                  k = tuple([i,item])
                  try:
                      self._container[t]
                      res.append(self._container[t])
                  except:
                      try:
                        self._container[k]
                        res.append(self._container[k])
                      except:
                        pass
        return res


    def __setitem__(self, key, value):
        a = Entry(key,value)
        self.add(a)

if __name__ == '__main__':

   #a = Entry(1,1,'lel')
   #b = Lookup('lol')
   #b.add(a)
    # b.addOrUpdate(a)
    # print(b.count())
  #   print(b[1])

   pass