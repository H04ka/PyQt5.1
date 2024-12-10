from PyQt5 import QtWidgets
import vid

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = vid.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.amartization)
       


    def amartization(self):
        a = float(self.ui.lineEdit.text())
        b = float(self.ui.lineEdit_2.text())
        c = a * b
        inf1 = float(self.ui.lineEdit_3.text())
        inf2 = str(self.ui.lineEdit_4.text())
        inf3 = str(self.ui.lineEdit_5.text())
        inf4 = float(self.ui.lineEdit_6.text())
        self.ui.label_3.setText((f"Амортизация налогового учёта = {str(c)}\nНомер карты = {str(inf1)}\nИмя владельца = {str(inf2)}\nДействительна до = {str(inf3)}\nЗадние цифры = {str(inf4)}"))
    

       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())