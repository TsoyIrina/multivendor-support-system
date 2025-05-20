# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_employee_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_UpdateEmployeeForm(object):
    def setupUi(self, UpdateEmployeeForm):
        if not UpdateEmployeeForm.objectName():
            UpdateEmployeeForm.setObjectName(u"UpdateEmployeeForm")
        UpdateEmployeeForm.resize(361, 205)
        self.verticalLayout = QVBoxLayout(UpdateEmployeeForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Bpv = QLabel(UpdateEmployeeForm)
        self.Bpv.setObjectName(u"Bpv")
        self.Bpv.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.Bpv)

        self.errorLbl = QLabel(UpdateEmployeeForm)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.errorLbl)

        self.widget = QWidget(UpdateEmployeeForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_72 = QLabel(self.widget)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_72, 0, 0, 1, 1)

        self.label_71 = QLabel(self.widget)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_71, 0, 1, 1, 1)

        self.label_69 = QLabel(self.widget)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_69, 0, 2, 1, 1)

        self.idProfileEdit = QLineEdit(self.widget)
        self.idProfileEdit.setObjectName(u"idProfileEdit")
        self.idProfileEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.idProfileEdit, 1, 0, 1, 1)

        self.workStatusProfileEdit = QLineEdit(self.widget)
        self.workStatusProfileEdit.setObjectName(u"workStatusProfileEdit")
        self.workStatusProfileEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.workStatusProfileEdit, 1, 1, 1, 1)

        self.dateJoinedProfileEdit = QDateEdit(self.widget)
        self.dateJoinedProfileEdit.setObjectName(u"dateJoinedProfileEdit")
        self.dateJoinedProfileEdit.setReadOnly(True)
        self.dateJoinedProfileEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateJoinedProfileEdit, 1, 2, 1, 1)

        self.label_74 = QLabel(self.widget)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_74, 2, 0, 1, 1)

        self.label_77 = QLabel(self.widget)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_77, 2, 1, 1, 1)

        self.label_63 = QLabel(self.widget)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_63, 2, 2, 1, 1)

        self.lastnameProfileEdit = QLineEdit(self.widget)
        self.lastnameProfileEdit.setObjectName(u"lastnameProfileEdit")
        self.lastnameProfileEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.lastnameProfileEdit, 3, 0, 1, 1)

        self.firstnameProfileEdit = QLineEdit(self.widget)
        self.firstnameProfileEdit.setObjectName(u"firstnameProfileEdit")
        self.firstnameProfileEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.firstnameProfileEdit, 3, 1, 1, 1)

        self.patronymicProfileEdit = QLineEdit(self.widget)
        self.patronymicProfileEdit.setObjectName(u"patronymicProfileEdit")
        self.patronymicProfileEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.patronymicProfileEdit, 3, 2, 1, 1)

        self.label_70 = QLabel(self.widget)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_70, 4, 0, 1, 1)

        self.label_75 = QLabel(self.widget)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_75, 4, 1, 1, 1)

        self.label_76 = QLabel(self.widget)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_76, 4, 2, 1, 1)

        self.usernameProfileEdit = QLineEdit(self.widget)
        self.usernameProfileEdit.setObjectName(u"usernameProfileEdit")
        self.usernameProfileEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.usernameProfileEdit, 5, 0, 1, 1)

        self.permissionProfileEdit = QLineEdit(self.widget)
        self.permissionProfileEdit.setObjectName(u"permissionProfileEdit")
        self.permissionProfileEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.permissionProfileEdit, 5, 1, 1, 1)

        self.birthdateProfileEdit = QDateEdit(self.widget)
        self.birthdateProfileEdit.setObjectName(u"birthdateProfileEdit")
        self.birthdateProfileEdit.setReadOnly(False)
        self.birthdateProfileEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.birthdateProfileEdit, 5, 2, 1, 1)

        self.label_73 = QLabel(self.widget)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_73, 6, 0, 1, 1)

        self.phoneProfileEdit = QLineEdit(self.widget)
        self.phoneProfileEdit.setObjectName(u"phoneProfileEdit")
        self.phoneProfileEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.phoneProfileEdit, 7, 0, 1, 1)

        self.updateBtn = QPushButton(self.widget)
        self.updateBtn.setObjectName(u"updateBtn")

        self.gridLayout.addWidget(self.updateBtn, 7, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(UpdateEmployeeForm)

        QMetaObject.connectSlotsByName(UpdateEmployeeForm)
    # setupUi

    def retranslateUi(self, UpdateEmployeeForm):
        UpdateEmployeeForm.setWindowTitle(QCoreApplication.translate("UpdateEmployeeForm", u"\u041c\u0443\u043b\u044c\u0442\u0438\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.Bpv.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.errorLbl.setText("")
        self.label_72.setText(QCoreApplication.translate("UpdateEmployeeForm", u"id", None))
        self.label_71.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_69.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.label_74.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_77.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0418\u043c\u044f", None))
        self.label_63.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_70.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_75.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0414\u043e\u0441\u0442\u0443\u043f", None))
        self.label_76.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_73.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.updateBtn.setText(QCoreApplication.translate("UpdateEmployeeForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

