# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AuthForm(object):
    def setupUi(self, AuthForm):
        if not AuthForm.objectName():
            AuthForm.setObjectName(u"AuthForm")
        AuthForm.setMinimumSize(QSize(380, 200))
        self.verticalLayout = QVBoxLayout(AuthForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AuthForm)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.authErrorLbl = QLabel(self.widget)
        self.authErrorLbl.setObjectName(u"authErrorLbl")
        self.authErrorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.authErrorLbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.verticalLayout_2.addWidget(self.label)

        self.usernameLineEdit = QLineEdit(self.widget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout_2.addWidget(self.usernameLineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.passwordLineEdit = QLineEdit(self.widget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwordLineEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.authBtn = QPushButton(self.widget)
        self.authBtn.setObjectName(u"authBtn")

        self.verticalLayout_2.addWidget(self.authBtn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(AuthForm)

        QMetaObject.connectSlotsByName(AuthForm)
    # setupUi

    def retranslateUi(self, AuthForm):
        AuthForm.setWindowTitle(QCoreApplication.translate("AuthForm", u"\u041c\u0443\u043b\u044c\u0442\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("AuthForm", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.authErrorLbl.setText("")
        self.label.setText(QCoreApplication.translate("AuthForm", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("AuthForm", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.authBtn.setText(QCoreApplication.translate("AuthForm", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

