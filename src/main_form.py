# -*- coding: utf-8 -*-
from mailbox import Message

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget, QMessageBox)

from password import Password
from password_table import PasswordTable
from dialog_form import Dialog
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 600)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblName = QLabel(self.centralwidget)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setGeometry(QRect(260, 10, 361, 41))
        font = QFont()
        font.setPointSize(18)
        self.lblName.setFont(font)
        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(520, 450, 141, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.btnRun.setFont(font1)
        self.btnLog = QPushButton(self.centralwidget)
        self.btnLog.setObjectName(u"btnLog")
        self.btnLog.setGeometry(QRect(690, 450, 141, 51))
        self.btnLog.setFont(font1)
        self.tablePassword = QTableWidget(self.centralwidget)
        if (self.tablePassword.columnCount() < 4):
            self.tablePassword.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tablePassword.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tablePassword.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tablePassword.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tablePassword.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablePassword.setObjectName(u"tablePassword")
        self.tablePassword.setGeometry(QRect(480, 80, 411, 141))
        self.txtRemove = QTextEdit(self.centralwidget)
        self.txtRemove.setObjectName(u"txtRemove")
        self.txtRemove.setGeometry(QRect(660, 240, 231, 41))
        self.txtRemove.setFont(font1)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 80, 411, 421))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnRemove = QPushButton(self.centralwidget)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setGeometry(QRect(480, 240, 161, 41))
        self.btnFind = QPushButton(self.centralwidget)
        self.btnFind.setObjectName(u"btnFind")
        self.btnFind.setGeometry(QRect(480, 290, 161, 41))
        self.txtFind = QTextEdit(self.centralwidget)
        self.txtFind.setObjectName(u"txtFind")
        self.txtFind.setGeometry(QRect(660, 290, 231, 41))
        self.txtFind.setFont(font1)
        self.btnChange = QPushButton(self.centralwidget)
        self.btnChange.setObjectName(u"btnChange")
        self.btnChange.setGeometry(QRect(480, 340, 161, 41))
        self.txtNewPass = QTextEdit(self.centralwidget)
        self.txtNewPass.setObjectName(u"txtNewPass")
        self.txtNewPass.setGeometry(QRect(660, 340, 141, 41))
        self.txtNewPass.setFont(font1)
        self.txtIndex = QTextEdit(self.centralwidget)
        self.txtIndex.setObjectName(u"txtIndex")
        self.txtIndex.setGeometry(QRect(810, 340, 81, 41))
        self.txtIndex.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 912, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionAdd)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.actionAdd.triggered.connect(self.btn_action_click)
        self.btnRemove.clicked.connect(self.remove_password)
        self.btnFind.clicked.connect(self.find_password)
        self.btnChange.clicked.connect(self.change_password)
        self.btnLog.clicked.connect(self.log)
        self.btnRun.clicked.connect(self.run)

        self.MainPassTable = PasswordTable([])
        self.table_rows = 0

        if self.tablePassword.rowCount() < 9: self.tablePassword.setRowCount(9)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setGeometry(0, 0, 400, 300)

        self.graphWidget.setBackground('w')

        self.gridLayout.addWidget(self.graphWidget)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.lblName.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442 9 : \u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439 ", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.btnLog.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433", None))
        ___qtablewidgetitem = self.tablePassword.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Passtext", None));
        ___qtablewidgetitem1 = self.tablePassword.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem2 = self.tablePassword.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Login", None));
        ___qtablewidgetitem3 = self.tablePassword.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.txtRemove.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnFind.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.txtFind.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.btnChange.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.txtNewPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.txtIndex.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0434\u0435\u043a\u0441", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi

    def refresh_table(self):
        self.tablePassword.clearContents()
        #self.tablePassword.clear()
        self.table_rows = 0

        for j in self.MainPassTable.password_array:
            temp = list()
            temp.append(str(j.passtext))
            temp.append(str(j.address))
            temp.append(str(j.login))
            temp.append(str(j.date))
            print(temp)
            for i in range(0, 4):
                item = QTableWidgetItem()
                self.tablePassword.setItem(self.table_rows, i, item)
                item.setText(temp[i])
            self.table_rows += 1

    def btn_action_click(self):
        dlg = Dialog()
        dlg.exec()
        if dlg.ok:
            password = Password(dlg.passtext, dlg.address, dlg.login, dlg.date)
            self.MainPassTable.add_password(password)
            self.refresh_table()

    def change_password(self):
        if self.MainPassTable.change_password(self.txtNewPass.toPlainText(), int(self.txtIndex.toPlainText())):
            self.refresh_table()
        else:
            QMessageBox(self, "hren", "tebe")


    def remove_password(self):
        print(self.MainPassTable.password_array)
        if self.MainPassTable.rem_password(self.txtRemove.toPlainText()):
            self.refresh_table()
        else:
            QMessageBox(self, "hren", "tebe")

    def find_password(self) -> None:
        #print(self.MainPassTable.password_array)
        if self.MainPassTable.find_password(self.txtFind.toPlainText()):
            QMessageBox.information(self, 'Result', "Da")
        else:
            QMessageBox.information(self, 'Result', "Net")

    def log(self):
        file = open("my_log.txt", "w+")
        for i in self.MainPassTable.password_array:
            file.write(str(i))
            file.write("\n")
        file.close()

    def get_dates(self):
        temp = []
        counts = []
        for i in self.MainPassTable.password_array:
            try:
                counts[temp.index(i.date.day)] += 1
            except ValueError:
                temp.append(i.date.day)
                counts.append(1)

        return temp, counts

    def run(self):
        pen = pg.mkPen(color=(255, 0, 0))
        count, dates = self.get_dates()
        self.graphWidget.plot(count, dates, pen=pen)