# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogue.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QTextEdit,
    QWidget)
from exceptions import NullException

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(555, 358)
        self.ok = False
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 300, 351, 41))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.txtPassword = QTextEdit(Dialog)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(70, 70, 371, 41))
        font = QFont()
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtAddress = QTextEdit(Dialog)
        self.txtAddress.setObjectName(u"txtAddress")
        self.txtAddress.setGeometry(QRect(70, 120, 371, 41))
        self.txtAddress.setFont(font)
        self.dt = QDateEdit(Dialog)
        self.dt.setObjectName(u"dt")
        self.dt.setGeometry(QRect(70, 220, 371, 23))
        self.dt.setFont(font)
        self.lblPassword = QLabel(Dialog)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setGeometry(QRect(210, 20, 141, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.lblPassword.setFont(font1)
        self.txtLogin = QTextEdit(Dialog)
        self.txtLogin.setObjectName(u"txtLogin")
        self.txtLogin.setGeometry(QRect(70, 170, 371, 41))
        self.txtLogin.setFont(font)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)


        QMetaObject.connectSlotsByName(Dialog)

        self.buttonBox.accepted.connect(self.btn_accept)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.txtAddress.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441: ", None))
        self.lblPassword.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.txtLogin.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d: ", None))
    # retranslateUi

    def btn_accept(self):
        try:
            self.passtext = self.txtPassword.toPlainText()
            if not self.passtext:
                raise NullException
            self.address = self.txtAddress.toPlainText()
            if not self.address:
                raise NullException
            self.login = self.txtLogin.toPlainText()
            if not self.login:
                raise NullException
            if not self.login:
                raise NullException
            self.date = self.dt.date().toPython()
            if not self.date:
                raise NullException
            self.ok = True
        except ValueError as e:
            print(e)
            self.Error = True
            return
        except NullException as n:
            print(n)
            self.Error = True
            return

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)