# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_only_name_form.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_UpdateOnlyNameForm(object):
    def setupUi(self, UpdateOnlyNameForm):
        if not UpdateOnlyNameForm.objectName():
            UpdateOnlyNameForm.setObjectName(u"UpdateOnlyNameForm")
        UpdateOnlyNameForm.resize(400, 108)
        self.verticalLayout = QVBoxLayout(UpdateOnlyNameForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLbl = QLabel(UpdateOnlyNameForm)
        self.titleLbl.setObjectName(u"titleLbl")
        self.titleLbl.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.titleLbl)

        self.errorLbl = QLabel(UpdateOnlyNameForm)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.errorLbl)

        self.nameLineEdit = QLineEdit(UpdateOnlyNameForm)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.verticalLayout.addWidget(self.nameLineEdit)

        self.updateBtn = QPushButton(UpdateOnlyNameForm)
        self.updateBtn.setObjectName(u"updateBtn")

        self.verticalLayout.addWidget(self.updateBtn)

        self.deleteBtn = QPushButton(UpdateOnlyNameForm)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.verticalLayout.addWidget(self.deleteBtn)


        self.retranslateUi(UpdateOnlyNameForm)

        QMetaObject.connectSlotsByName(UpdateOnlyNameForm)
    # setupUi

    def retranslateUi(self, UpdateOnlyNameForm):
        UpdateOnlyNameForm.setWindowTitle(QCoreApplication.translate("UpdateOnlyNameForm", u"\u041c\u0443\u043b\u044c\u0442\u0438\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.titleLbl.setText(QCoreApplication.translate("UpdateOnlyNameForm", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None))
        self.errorLbl.setText("")
        self.nameLineEdit.setPlaceholderText(QCoreApplication.translate("UpdateOnlyNameForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.updateBtn.setText(QCoreApplication.translate("UpdateOnlyNameForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.deleteBtn.setText(QCoreApplication.translate("UpdateOnlyNameForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

