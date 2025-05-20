# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_EmployeeForm(object):
    def setupUi(self, EmployeeForm):
        if not EmployeeForm.objectName():
            EmployeeForm.setObjectName(u"EmployeeForm")
        EmployeeForm.resize(319, 249)
        self.verticalLayout = QVBoxLayout(EmployeeForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(EmployeeForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.errorLbl = QLabel(self.widget)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.errorLbl, 2, 1, 1, 2)

        self.saveBtn = QPushButton(self.widget)
        self.saveBtn.setObjectName(u"saveBtn")

        self.gridLayout.addWidget(self.saveBtn, 12, 1, 1, 2)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_24, 4, 2, 1, 1)

        self.birthdateDateEdit = QDateEdit(self.widget)
        self.birthdateDateEdit.setObjectName(u"birthdateDateEdit")
        self.birthdateDateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.birthdateDateEdit, 9, 2, 1, 1)

        self.usernameEdit = QLineEdit(self.widget)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.gridLayout.addWidget(self.usernameEdit, 5, 1, 1, 1)

        self.firstnameEdit = QLineEdit(self.widget)
        self.firstnameEdit.setObjectName(u"firstnameEdit")

        self.gridLayout.addWidget(self.firstnameEdit, 7, 2, 1, 1)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_28, 8, 1, 1, 1)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_22, 8, 2, 1, 1)

        self.patronymicEdit = QLineEdit(self.widget)
        self.patronymicEdit.setObjectName(u"patronymicEdit")

        self.gridLayout.addWidget(self.patronymicEdit, 9, 1, 1, 1)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_27, 10, 2, 1, 1)

        self.workStatusBox = QComboBox(self.widget)
        self.workStatusBox.setObjectName(u"workStatusBox")

        self.gridLayout.addWidget(self.workStatusBox, 11, 1, 1, 1)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_26, 6, 1, 1, 1)

        self.loginLbl = QLabel(self.widget)
        self.loginLbl.setObjectName(u"loginLbl")
        self.loginLbl.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.loginLbl, 4, 1, 1, 1)

        self.passwordEdit = QLineEdit(self.widget)
        self.passwordEdit.setObjectName(u"passwordEdit")

        self.gridLayout.addWidget(self.passwordEdit, 5, 2, 1, 1)

        self.lastnameEdit = QLineEdit(self.widget)
        self.lastnameEdit.setObjectName(u"lastnameEdit")

        self.gridLayout.addWidget(self.lastnameEdit, 7, 1, 1, 1)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_23, 6, 2, 1, 1)

        self.phoneEdit = QLineEdit(self.widget)
        self.phoneEdit.setObjectName(u"phoneEdit")

        self.gridLayout.addWidget(self.phoneEdit, 11, 2, 1, 1)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_25, 10, 1, 1, 1)

        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.deleteBtn = QPushButton(self.widget)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.gridLayout.addWidget(self.deleteBtn, 13, 1, 1, 2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(EmployeeForm)

        QMetaObject.connectSlotsByName(EmployeeForm)
    # setupUi

    def retranslateUi(self, EmployeeForm):
        EmployeeForm.setWindowTitle(QCoreApplication.translate("EmployeeForm", u"EmployeeForm", None))
        self.errorLbl.setText("")
        self.saveBtn.setText(QCoreApplication.translate("EmployeeForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_24.setText(QCoreApplication.translate("EmployeeForm", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.usernameEdit.setPlaceholderText("")
        self.firstnameEdit.setPlaceholderText("")
        self.label_28.setText(QCoreApplication.translate("EmployeeForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_22.setText(QCoreApplication.translate("EmployeeForm", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.patronymicEdit.setPlaceholderText("")
        self.label_27.setText(QCoreApplication.translate("EmployeeForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_26.setText(QCoreApplication.translate("EmployeeForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.loginLbl.setText(QCoreApplication.translate("EmployeeForm", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passwordEdit.setPlaceholderText("")
        self.lastnameEdit.setPlaceholderText("")
        self.label_23.setText(QCoreApplication.translate("EmployeeForm", u"\u0418\u043c\u044f", None))
        self.phoneEdit.setPlaceholderText("")
        self.label_25.setText(QCoreApplication.translate("EmployeeForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.title.setText(QCoreApplication.translate("EmployeeForm", u"TextLabel", None))
        self.deleteBtn.setText(QCoreApplication.translate("EmployeeForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

