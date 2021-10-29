import sys
from random import shuffle
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QDialog, QTableWidgetItem
from PyQt5.QtGui import QIcon
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        self.open_db()
        super().__init__()
        QMainWindow.__init__(self)
        uic.loadUi('design.ui', self)
        self.load_labels()
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
        self.ButtonCheck.clicked.connect(self.check_name)
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

    def load_labels(self):
        labels = open('labels.txt', mode='r', encoding='utf8').readlines()
        self.label.setText(labels[0].strip())
        self.label2.setText(labels[1].strip())
        self.label3.setText(labels[2].strip())
        self.label4.setText(labels[3].strip())

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
        if sum(self.AnsK1) != len(self.ex1):
            while self.AnsK1[self.i1] == 1:
                self.i1 = (self.i1 + 1) % len(self.ex1)
        self.ex1L.setText(self.ex1[self.i1][0])

    def rand2(self):
        self.i2 = (self.i2 + 1) % len(self.ex2)
        if sum(self.AnsK2) != len(self.ex2):
            while self.AnsK2[self.i2] == 1:
                self.i2 = (self.i2 + 1) % len(self.ex2)
        self.ex2L.setText(self.ex2[self.i2][0])
        self.textEdit2.setText(self.ex2[self.i2][1])

    def rand3(self):
        self.i3 = (self.i3 + 1) % len(self.ex3)
        if sum(self.AnsK3) != len(self.ex3):
            while self.AnsK3[self.i3] == 1:
                self.i3 = (self.i3 + 1) % len(self.ex3)
        self.ex3L.setText(self.ex3[self.i3][0])
        self.textEdit3.setText(self.ex3[self.i3][1])

    def rand4(self):
        self.i4 = (self.i4 + 1) % len(self.ex4)
        if sum(self.AnsK4) != len(self.ex4):
            while self.AnsK4[self.i4] == 1:
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
        if self.textEdit2.toPlainText() == "admin":
            self.show_db()
        if self.textEdit2.toPlainText() == "clear db":
            self.clear_db()
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

    def check_name(self):
        name, ok_pressed = QInputDialog.getText(
            self, "TrenajerC", "Введите ваше имя")
        if ok_pressed and name:
            self.result(name)

    def result(self, name):
        self.resultWindow = QDialog()
        self.resultWindow.setFixedSize(500, 325)
        self.resultWindow.setWindowIcon(QIcon('Images/favicon.ico'))
        self.resultWindow.setWindowTitle('Результаты')
        self.resultWindow.setFont(QtGui.QFont("MS Shell Dlg 2", 14))
        self.labelName = QtWidgets.QLabel(self.resultWindow)
        self.labelName.move(20, 30)
        self.labelName.resize(380, 30)
        self.labelName.setText("Имя: " + name)
        self.labelEx1 = QtWidgets.QLabel(self.resultWindow)
        self.labelEx1.move(20, 80)
        self.labelEx1.resize(230, 30)
        self.labelEx1.setText("Задание 1: " + str(sum(self.AnsK1))
                              + " / " + str(len(self.AnsK1)))
        self.labelEx2 = QtWidgets.QLabel(self.resultWindow)
        self.labelEx2.move(20, 130)
        self.labelEx2.resize(230, 30)
        self.labelEx2.setText("Задание 2: " + str(sum(self.AnsK2))
                              + " / " + str(len(self.AnsK2)))
        self.labelEx3 = QtWidgets.QLabel(self.resultWindow)
        self.labelEx3.move(20, 180)
        self.labelEx3.resize(230, 30)
        self.labelEx3.setText("Задание 3: " + str(sum(self.AnsK3))
                              + " / " + str(len(self.AnsK3)))
        self.labelEx4 = QtWidgets.QLabel(self.resultWindow)
        self.labelEx4.move(20, 230)
        self.labelEx4.resize(230, 30)
        self.labelEx4.setText("Задание 4: " + str(sum(self.AnsK4))
                              + " / " + str(len(self.AnsK4)))
        self.summa = sum(self.AnsK1) + sum(self.AnsK2) + sum(self.AnsK3) + sum(self.AnsK4)
        self.lenght = len(self.AnsK1) + len(self.AnsK2) + len(self.AnsK3) + len(self.AnsK4)
        self.labelTotal = QtWidgets.QLabel(self.resultWindow)
        self.labelTotal.move(270, 280)
        self.labelTotal.resize(210, 30)
        self.labelTotal.setText("Итого: " + str(self.summa) + " / " + str(self.lenght))
        self.stamp = QtWidgets.QWidget(self.resultWindow)
        self.stamp.move(260, 80)
        self.stamp.resize(180, 180)
        self.stamp.setStyleSheet("border-image: url('Images/stamp.png') 0 0 0 0;")
        self.resultWindow.show()
        self.safe_data(name.lower())

    def safe_data(self, name):
        try:
            db = sqlite3.connect("decision.db")
            cur1 = db.cursor()
            info = (name, sum(self.AnsK1), sum(self.AnsK2), sum(self.AnsK3), sum(self.AnsK4), self.summa)
            update = cur1.execute("""SELECT title FROM Students WHERE title = ?""", (name,)).fetchall()
            if not update:
                cur1.execute("""INSERT INTO Students VALUES(?, ?, ?, ?, ?, ?)""", info)
            else:
                cur1.execute("""UPDATE Students set Ex1 = ? WHERE title = ?""", (sum(self.AnsK1), name,))
                cur1.execute("""UPDATE Students set Ex2 = ? WHERE title = ?""", (sum(self.AnsK2), name,))
                cur1.execute("""UPDATE Students set Ex3 = ? WHERE title = ?""", (sum(self.AnsK3), name,))
                cur1.execute("""UPDATE Students set Ex4 = ? WHERE title = ?""", (sum(self.AnsK4), name,))
                cur1.execute("""UPDATE Students set total = ? WHERE title = ?""", (self.summa, name,))
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print(error)

    def clear_db(self):
        db = sqlite3.connect("decision.db")
        cur1 = db.cursor()
        cur1.execute("""DELETE FROM Students""")
        db.commit()
        db.close()

    def show_db(self):
        self.adminWindow = QDialog()
        self.adminWindow.setFixedSize(800, 600)
        self.adminWindow.setFont(QtGui.QFont("MS Shell Dlg 2", 14))
        self.adminWindow.setWindowIcon(QIcon('Images/favicon.ico'))
        self.adminWindow.setWindowTitle('Решения')
        self.tableWidget = QtWidgets.QTableWidget(self.adminWindow)
        self.tableWidget.resize(780, 500)
        self.tableWidget.move(10, 10)
        self.button_update = QtWidgets.QPushButton(self.adminWindow)
        self.button_update.resize(780, 60)
        self.button_update.move(10, 520)
        self.button_update.setText("Обновить")
        self.button_update.clicked.connect(self.update_db)
        self.update_db()
        self.adminWindow.show()

    def update_db(self):
        db = sqlite3.connect("decision.db")
        cur = db.cursor()
        result = cur.execute("""SELECT * FROM Students""").fetchall()
        if result:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setHorizontalHeaderLabels(
            ("Имя", "Задание 1", "Задание 2", "Задание 3", "Задание 4", "Итого"))
        db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
