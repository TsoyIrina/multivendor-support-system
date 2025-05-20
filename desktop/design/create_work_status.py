# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_work_status.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_createWorkStatusForm(object):
    def setupUi(self, createWorkStatusForm):
        if not createWorkStatusForm.objectName():
            createWorkStatusForm.setObjectName(u"createWorkStatusForm")
        createWorkStatusForm.resize(400, 152)
        self.verticalLayout = QVBoxLayout(createWorkStatusForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(createWorkStatusForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.createBtn = QPushButton(self.widget)
        self.createBtn.setObjectName(u"createBtn")

        self.gridLayout.addWidget(self.createBtn, 5, 0, 1, 2)

        self.errorLbl = QLabel(self.widget)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.errorLbl, 1, 0, 1, 1)

        self.permissionCheckBox = QCheckBox(self.widget)
        self.permissionCheckBox.setObjectName(u"permissionCheckBox")

        self.gridLayout.addWidget(self.permissionCheckBox, 4, 0, 1, 2)

        self.nameEdit = QLineEdit(self.widget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout.addWidget(self.nameEdit, 3, 0, 1, 2)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.deleteBtn = QPushButton(self.widget)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.gridLayout.addWidget(self.deleteBtn, 6, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(createWorkStatusForm)

        QMetaObject.connectSlotsByName(createWorkStatusForm)
    # setupUi

    def retranslateUi(self, createWorkStatusForm):
        createWorkStatusForm.setWindowTitle(QCoreApplication.translate("createWorkStatusForm", u"\u041c\u0443\u043b\u044c\u0442\u0438\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("createWorkStatusForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.createBtn.setText(QCoreApplication.translate("createWorkStatusForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.errorLbl.setText("")
        self.permissionCheckBox.setText(QCoreApplication.translate("createWorkStatusForm", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u0434\u043e\u0441\u0442\u0443\u043f", None))
        self.label_2.setText(QCoreApplication.translate("createWorkStatusForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.deleteBtn.setText(QCoreApplication.translate("createWorkStatusForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

