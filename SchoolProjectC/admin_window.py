from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtGui import QIcon
import sqlite3


class AdminWindow(QDialog):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self)
        self.setFixedSize(800, 600)
        self.setFont(QtGui.QFont("MS Shell Dlg 2", 14))
        self.setWindowIcon(QIcon('Images/favicon.ico'))
        self.setWindowTitle('Решения')
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.resize(780, 500)
        self.tableWidget.move(10, 10)
        self.button_update = QtWidgets.QPushButton(self)
        self.button_update.resize(780, 60)
        self.button_update.move(10, 520)
        self.button_update.setText("Обновить")
        self.button_update.clicked.connect(self.update_db)
        self.update_db()

    def update_db(self):  # обновить окно с  просмотра бд
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
