# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zip_form.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_ZipForm(object):
    def setupUi(self, ZipForm):
        if not ZipForm.objectName():
            ZipForm.setObjectName(u"ZipForm")
        ZipForm.resize(317, 197)
        self.gridLayout_2 = QGridLayout(ZipForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(ZipForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.typeZipEdit = QLineEdit(self.widget)
        self.typeZipEdit.setObjectName(u"typeZipEdit")

        self.gridLayout.addWidget(self.typeZipEdit, 1, 0, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_12.setMargin(4)

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_14.setMargin(4)

        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)

        self.articleZipEdit = QLineEdit(self.widget)
        self.articleZipEdit.setObjectName(u"articleZipEdit")

        self.gridLayout.addWidget(self.articleZipEdit, 3, 0, 1, 1)

        self.unitZipEdit = QLineEdit(self.widget)
        self.unitZipEdit.setObjectName(u"unitZipEdit")

        self.gridLayout.addWidget(self.unitZipEdit, 3, 2, 1, 1)

        self.nameZipEdit = QLineEdit(self.widget)
        self.nameZipEdit.setObjectName(u"nameZipEdit")

        self.gridLayout.addWidget(self.nameZipEdit, 1, 2, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_11.setMargin(4)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_9.setMargin(4)

        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)

        self.saveZipBtn = QPushButton(self.widget)
        self.saveZipBtn.setObjectName(u"saveZipBtn")

        self.gridLayout.addWidget(self.saveZipBtn, 4, 0, 1, 3)

        self.deleteZipBtn = QPushButton(self.widget)
        self.deleteZipBtn.setObjectName(u"deleteZipBtn")

        self.gridLayout.addWidget(self.deleteZipBtn, 5, 0, 1, 3)


        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 1)

        self.label = QLabel(ZipForm)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.errorLbl = QLabel(ZipForm)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.errorLbl, 1, 0, 1, 1)


        self.retranslateUi(ZipForm)

        QMetaObject.connectSlotsByName(ZipForm)
    # setupUi

    def retranslateUi(self, ZipForm):
        ZipForm.setWindowTitle(QCoreApplication.translate("ZipForm", u"\u041c\u0443\u043b\u044c\u0442\u0438\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.label_12.setText(QCoreApplication.translate("ZipForm", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_14.setText(QCoreApplication.translate("ZipForm", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("ZipForm", u"\u0422\u0438\u043f", None))
        self.label_9.setText(QCoreApplication.translate("ZipForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.saveZipBtn.setText(QCoreApplication.translate("ZipForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.deleteZipBtn.setText(QCoreApplication.translate("ZipForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("ZipForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0417\u0418\u041f", None))
        self.errorLbl.setText("")
    # retranslateUi

