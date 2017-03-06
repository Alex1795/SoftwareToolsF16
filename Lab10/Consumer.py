import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        txt = [self.emailLineEdit, self.zipLineEdit, self.lastNameLineEdit, self.firstNameLineEdit, self.stateLineEdit, self.addressLineEdit, self.cityLineEdit]



        #Text changed
        for t in txt:
            t.textChanged.connect(self.enable)

        #clear
        self.clearButton.clicked.connect(self.clear)

        #Save
        self.saveToTargetButton.clicked.connect(self.validation)

        #Load

        self.loadButton.clicked.connect(self.loadData)


    def validation(self):

        states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

        txt = [self.emailLineEdit, self.zipLineEdit, self.lastNameLineEdit, self.firstNameLineEdit, self.stateLineEdit, self.addressLineEdit, self.cityLineEdit]

        for t in txt:
            if t.text() == '':
                self.errorInfoLabel.setText('Error: Enter all information')
                return

        if self.stateLineEdit.text() not in states:
            self.errorInfoLabel.setText('Error: Enter a valid state')
            return
        if len(self.zipLineEdit.text()) != 5:
            #print(len(self.zipLineEdit.text()))
            self.errorInfoLabel.setText('Error: Enter a valid zip code')
            return
        else:
            try:
                a = int(self.zipLineEdit.text())

            except:
                self.errorInfoLabel.setText('Error: Zip code must be a number')
                return

        remail = re.compile(r'\w+@\w+\.\w+')

        if re.findall(remail,self.emailLineEdit.text()) == []:
            self.errorInfoLabel.setText('Error: Enter a valid email')
            return

        self.errorInfoLabel.setText('')

        f = open('target.xml','w+')
        f.write('<?xml version="1.0" encoding="UTF-8"?>')
        f.write('\n')
        f.write('<user>\n')
        f.write('   <FirstName>{0}</FirstName>\n'.format(self.firstNameLineEdit.text()))
        f.write('   <LastName>{0}</LastName>\n'.format(self.lastNameLineEdit.text()))
        f.write('   <Address>{0}</Address>\n'.format(self.addressLineEdit.text()))
        f.write('   <City>{0}</City>\n'.format(self.cityLineEdit.text()))
        f.write('   <State>{0}</State>\n'.format(self.stateLineEdit.text()))
        f.write('   <ZIP>{0}</ZIP>\n'.format(self.zipLineEdit.text()))
        f.write('   <Email>{0}</Email>\n'.format(self.emailLineEdit.text()))




    def enable(self):

        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setEnabled(False)

    def clear(self):
        self.firstNameLineEdit.setText('')
        self.lastNameLineEdit.setText('')
        self.addressLineEdit.setText('')
        self.cityLineEdit.setText('')
        self.stateLineEdit.setText('')
        self.zipLineEdit.setText('')
        self.emailLineEdit.setText('')

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """

        with open(filePath, 'r') as file:
            all_lines = file.read()
        #refst = re.compile(r'<FirstName>(.*)</FirstName>')
        a = re.findall(r'<FirstName>(.*)</FirstName>',all_lines)
        self.firstNameLineEdit.setText(str(a[0]))

        a = re.findall(r'<LastName>(.*)</LastName>',all_lines)
        self.lastNameLineEdit.setText(str(a[0]))

        a = re.findall(r'<Address>(.*)</Address>',all_lines)
        self.addressLineEdit.setText(str(a[0]))

        a = re.findall(r'<City>(.*)</City>',all_lines)
        self.cityLineEdit.setText(str(a[0]))

        a = re.findall(r'<State>(.*)</State>',all_lines)
        self.stateLineEdit.setText(str(a[0]))

        a = re.findall(r'<ZIP>(.*)</ZIP>',all_lines)
        self.zipLineEdit.setText(str(a[0]))

        a = re.findall(r'<Email>(.*)</Email>',all_lines)
        self.emailLineEdit.setText(str(a[0]))


    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
