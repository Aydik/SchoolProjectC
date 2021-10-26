import sys
from random import shuffle
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        self.open_db()
        super().__init__()
        QMainWindow.__init__(self)
        uic.loadUi('design.ui', self)
        QMainWindow.setFixedSize(self, 1000, 700)
        self.setWindowIcon(QIcon('Images/favicon.ico'))
        self.bg1.setStyleSheet("border-image: url('Images/BackGround.png') 0 0 0 0;")
        self.bg2.setStyleSheet("border-image: url('Images/BackGround.png') 0 0 0 0;")
        self.bg3.setStyleSheet("border-image: url('Images/BackGround.png') 0 0 0 0;")
        self.bg4.setStyleSheet("border-image: url('Images/BackGround.png') 0 0 0 0;")
        self.Logo.setStyleSheet("border-image: url('Images/icon.png') 0 0 0 0;")
        self.Button1.clicked.connect(self.exi1)
        self.Button2.clicked.connect(self.exi2)
        self.Button3.clicked.connect(self.exi3)
        self.Button4.clicked.connect(self.exi4)
        self.i1 = -1
        self.i2 = -1
        self.i3 = -1
        self.i4 = -1
        self.AnsK1 = [0] * len(self.ex1)
        self.AnsK2 = [0] * len(self.ex2)
        self.AnsK3 = [0] * len(self.ex3)
        self.AnsK4 = [0] * len(self.ex4)
        shuffle(self.ex1)
        shuffle(self.ex2)
        shuffle(self.ex3)
        shuffle(self.ex4)
        self.rand1()
        self.rand2()
        self.rand3()
        self.rand4()

    def open_db(self):
        con = sqlite3.connect("Exis.db")
        self.cur = con.cursor()
        self.ex1load()
        self.ex2load()
        self.ex3load()
        self.ex4load()

    def ex1load(self):
        self.ex1 = []
        result = self.cur.execute("""SELECT title, ans FROM Exi1""").fetchall()
        for i in result:
            self.ex1.append(i)

    def ex2load(self):
        self.ex2 = []
        result = self.cur.execute("""SELECT title, code, ans FROM Exi2""").fetchall()
        for i in result:
            f = list(i)
            f[1] = "\n".join(f[1].split("\\n"))
            f[2] = "\n".join(f[2].split("\\n"))
            self.ex2.append(f)

    def ex3load(self):
        self.ex3 = []
        result = self.cur.execute("""SELECT title, code, ans FROM Exi3""").fetchall()
        for i in result:
            f = list(i)
            f[1] = "\n".join(f[1].split("\\n"))
            f[2] = "\n".join(f[2].split("\\n"))
            self.ex3.append(f)

    def ex4load(self):
        self.ex4 = []
        result = self.cur.execute("""SELECT code, ans FROM Exi4""").fetchall()
        for i in result:
            f = list(i)
            f[0] = "\n".join(f[0].split("\\n"))
            self.ex4.append(f)

    def rand1(self):
        self.i1 = (self.i1 + 1) % len(self.ex1)
        self.ex1L.setText(self.ex1[self.i1][0])

    def rand2(self):
        self.i2 = (self.i2 + 1) % len(self.ex2)
        self.ex2L.setText(self.ex2[self.i2][0])
        self.textEdit2.setText(self.ex2[self.i2][1])

    def rand3(self):
        self.i3 = (self.i3 + 1) % len(self.ex3)
        self.ex3L.setText(self.ex3[self.i3][0])
        self.textEdit3.setText(self.ex3[self.i3][1])

    def rand4(self):
        self.i4 = (self.i4 + 1) % len(self.ex4)
        self.ex4L.setText(self.ex4[self.i4][0])
        self.textEdit4.setText("")

    def exi1(self):
        if self.Button1.text() == "Проверить":
            ans = -1
            if self.radioButton.isChecked():
                ans = 0
            if self.radioButton2.isChecked():
                ans = 1
            if ans == self.ex1[self.i1][1]:
                self.ans1.setStyleSheet("border-image: url('Images/Da.png') 0 0 0 0;")
                self.AnsK1[self.i1] = 1
            else:
                self.ans1.setStyleSheet("border-image: url('Images/net.png') 0 0 0 0;")
            self.ans1.show()
            self.Button1.setText("Очистить")
            self.label1count.setText(self.label1count.text()[:-1] + str(sum(self.AnsK1)))
            if sum(self.AnsK1) == len(self.ex1):
                self.label1count.setText("Решено :-)")
        else:
            self.rand1()
            self.ans1.hide()
            self.radioButton.setAutoExclusive(False)
            self.radioButton2.setAutoExclusive(False)
            self.radioButton.setChecked(False)
            self.radioButton2.setChecked(False)
            self.radioButton.setAutoExclusive(True)
            self.radioButton2.setAutoExclusive(True)
            self.Button1.setText("Проверить")

    def exi2(self):
        if self.Button2.text() == "Проверить":
            if self.textEdit2.toPlainText().replace(" ", "") == self.ex2[self.i2][2].replace(" ", ""):
                self.ans2.setStyleSheet("border-image: url('Images/Da.png') 0 0 0 0;")
                self.AnsK2[self.i2] = 1
            else:
                self.ans2.setStyleSheet("border-image: url('Images/net.png') 0 0 0 0;")
            self.ans2.show()
            self.Button2.setText("Очистить")
            self.label2count.setText(self.label2count.text()[:-1] + str(sum(self.AnsK2)))
            if sum(self.AnsK2) == len(self.ex2):
                self.label2count.setText("Решено :-)")
        else:
            self.rand2()
            self.ans2.hide()
            self.Button2.setText("Проверить")

    def exi3(self):
        if self.Button3.text() == "Проверить":
            if self.textEdit3.toPlainText().replace(" ", "") == self.ex3[self.i3][2].replace(" ", ""):
                self.ans3.setStyleSheet("border-image: url('Images/Da.png') 0 0 0 0;")
                self.AnsK3[self.i3] = 1
            else:
                self.ans3.setStyleSheet("border-image: url('Images/net.png') 0 0 0 0;")
            self.ans3.show()
            self.Button3.setText("Очистить")
            self.label3count.setText(self.label3count.text()[:-1] + str(sum(self.AnsK3)))
            if sum(self.AnsK3) == len(self.ex3):
                self.label3count.setText("Решено :-)")
        else:
            self.rand3()
            self.ans3.hide()
            self.Button3.setText("Проверить")

    def exi4(self):
        if self.Button4.text() == "Проверить":
            if self.textEdit4.toPlainText() == str(self.ex4[self.i4][1]):
                self.ans4.setStyleSheet("border-image: url('Images/Da.png') 0 0 0 0;")
                self.AnsK4[self.i4] = 1
            else:
                self.ans4.setStyleSheet("border-image: url('Images/net.png') 0 0 0 0;")
            self.ans4.show()
            self.Button4.setText("Очистить")
            self.label4count.setText(self.label4count.text()[:-1] + str(sum(self.AnsK4)))
            if sum(self.AnsK4) == len(self.ex4):
                self.label4count.setText("Решено :-)")
        else:
            self.rand4()
            self.ans4.hide()
            self.Button4.setText("Проверить")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
