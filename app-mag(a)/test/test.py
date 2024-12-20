from PyQt5 import QtWidgets
import pravo

class MyWindow(QtWidgets.QWidget) :
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = pravo.Ui_Form()
        self.ui.setupUi(self)
        self.a = 0
        self.ui.pushButton.clicked.connect(self.startTest)+
        self.ui.pushButton_3.clicked.connect(self.vopros1)
        self.ui.pushButton_100.clicked.connect(self.vopros2)
        self.ui.pushButton_8.clicked.connect(self.vopros3)
        self.ui.pushButton_12.clicked.connect(self.vopros4)
        self.ui.pushButton_278.clicked.connect(self.dom)
    def startTest(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def vopros1(self):
        if self.ui.radioButton_10.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(2)
    def vopros2(self):
        if self.ui.radioButton_31.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(3)
    def vopros3(self):
        if self.ui.radioButton.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(4)
    def vopros4(self):
        if self.ui.radioButton_69.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(5)
        ocenka = {
            0: 2,
            1: 3,
            2: 4,
            3: 5,
        }
        self.ui.label_10.setText(f"Баллы: {self.a}")
        self.ui.label_11.setText(f"Оценка: {ocenka[self.a]}")
    def dom(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.a = 0
        for i in range(1,10):
            btn = getattr(self.ui, "radioButton_{}". format(i))
            btn.setAutoExcLusiive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExcLusiive(True)
            btn.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())



