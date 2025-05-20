# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_company.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CreateCompanyForm(object):
    def setupUi(self, CreateCompanyForm):
        if not CreateCompanyForm.objectName():
            CreateCompanyForm.setObjectName(u"CreateCompanyForm")
        CreateCompanyForm.resize(400, 136)
        self.verticalLayout = QVBoxLayout(CreateCompanyForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(CreateCompanyForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.usernameCompanyEdit = QLineEdit(self.widget)
        self.usernameCompanyEdit.setObjectName(u"usernameCompanyEdit")

        self.gridLayout.addWidget(self.usernameCompanyEdit, 5, 0, 1, 1)

        self.passwordCompanyEdit = QLineEdit(self.widget)
        self.passwordCompanyEdit.setObjectName(u"passwordCompanyEdit")

        self.gridLayout.addWidget(self.passwordCompanyEdit, 5, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.nameCompanyEdit = QLineEdit(self.widget)
        self.nameCompanyEdit.setObjectName(u"nameCompanyEdit")

        self.gridLayout.addWidget(self.nameCompanyEdit, 3, 0, 1, 2)

        self.errorLbl = QLabel(self.widget)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.errorLbl, 1, 0, 1, 1)

        self.createBtn = QPushButton(self.widget)
        self.createBtn.setObjectName(u"createBtn")

        self.gridLayout.addWidget(self.createBtn, 6, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(CreateCompanyForm)

        QMetaObject.connectSlotsByName(CreateCompanyForm)
    # setupUi

    def retranslateUi(self, CreateCompanyForm):
        CreateCompanyForm.setWindowTitle(QCoreApplication.translate("CreateCompanyForm", u"\u041c\u0443\u043b\u044c\u0442\u0438\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("CreateCompanyForm", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label.setText(QCoreApplication.translate("CreateCompanyForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("CreateCompanyForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("CreateCompanyForm", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.errorLbl.setText("")
        self.createBtn.setText(QCoreApplication.translate("CreateCompanyForm", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

