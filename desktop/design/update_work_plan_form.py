# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_work_plan_form.ui'
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
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_updateWorkPlanForm(object):
    def setupUi(self, updateWorkPlanForm):
        if not updateWorkPlanForm.objectName():
            updateWorkPlanForm.setObjectName(u"updateWorkPlanForm")
        updateWorkPlanForm.resize(351, 453)
        self.verticalLayout = QVBoxLayout(updateWorkPlanForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(updateWorkPlanForm)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_9)

        self.errorLbl = QLabel(updateWorkPlanForm)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.errorLbl)

        self.widget = QWidget(updateWorkPlanForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_15 = QGroupBox(self.widget)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_21 = QGridLayout(self.groupBox_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.employeeEngineerBox = QComboBox(self.groupBox_15)
        self.employeeEngineerBox.setObjectName(u"employeeEngineerBox")

        self.gridLayout_21.addWidget(self.employeeEngineerBox, 3, 1, 1, 1)

        self.label_55 = QLabel(self.groupBox_15)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_21.addWidget(self.label_55, 2, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox_15)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_21.addWidget(self.label_52, 0, 1, 1, 1)

        self.workStatusEngineerBox = QComboBox(self.groupBox_15)
        self.workStatusEngineerBox.setObjectName(u"workStatusEngineerBox")

        self.gridLayout_21.addWidget(self.workStatusEngineerBox, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_15, 1, 2, 1, 3)

        self.groupBox_14 = QGroupBox(self.widget)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(150, 0))
        self.gridLayout_20 = QGridLayout(self.groupBox_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.workStatusResponsibleBox = QComboBox(self.groupBox_14)
        self.workStatusResponsibleBox.setObjectName(u"workStatusResponsibleBox")

        self.gridLayout_20.addWidget(self.workStatusResponsibleBox, 1, 1, 1, 1)

        self.employeeResponsibleBox = QComboBox(self.groupBox_14)
        self.employeeResponsibleBox.setObjectName(u"employeeResponsibleBox")

        self.gridLayout_20.addWidget(self.employeeResponsibleBox, 3, 1, 1, 1)

        self.label_49 = QLabel(self.groupBox_14)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_20.addWidget(self.label_49, 0, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox_14)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_20.addWidget(self.label_50, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_14, 1, 0, 1, 2)

        self.label_48 = QLabel(self.widget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_48, 2, 3, 1, 1)

        self.label_57 = QLabel(self.widget)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_57, 2, 4, 1, 1)

        self.startDateEdit = QDateEdit(self.widget)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setReadOnly(False)
        self.startDateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.startDateEdit, 4, 3, 1, 1)

        self.updateWorkPlanBtn = QPushButton(self.widget)
        self.updateWorkPlanBtn.setObjectName(u"updateWorkPlanBtn")

        self.gridLayout.addWidget(self.updateWorkPlanBtn, 10, 0, 1, 5)

        self.endDateEdit = QDateEdit(self.widget)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setReadOnly(False)
        self.endDateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.endDateEdit, 4, 4, 1, 1)

        self.notesTextEdit = QTextEdit(self.widget)
        self.notesTextEdit.setObjectName(u"notesTextEdit")
        self.notesTextEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.notesTextEdit, 9, 0, 1, 5)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 2)

        self.tasksTextEdit = QTextEdit(self.widget)
        self.tasksTextEdit.setObjectName(u"tasksTextEdit")
        self.tasksTextEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.tasksTextEdit, 6, 0, 1, 5)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 2)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.zipComboBox = QComboBox(self.groupBox)
        self.zipComboBox.setObjectName(u"zipComboBox")

        self.gridLayout_2.addWidget(self.zipComboBox, 1, 0, 1, 3)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.unitZipEdit = QLineEdit(self.groupBox)
        self.unitZipEdit.setObjectName(u"unitZipEdit")
        self.unitZipEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.unitZipEdit, 3, 2, 1, 1)

        self.quantityZipEdit = QLineEdit(self.groupBox)
        self.quantityZipEdit.setObjectName(u"quantityZipEdit")

        self.gridLayout_2.addWidget(self.quantityZipEdit, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 7, 0, 1, 5)

        self.statusBox = QComboBox(self.widget)
        self.statusBox.setObjectName(u"statusBox")

        self.gridLayout.addWidget(self.statusBox, 4, 0, 1, 2)

        self.label_47 = QLabel(self.widget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout.addWidget(self.label_47, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(updateWorkPlanForm)

        QMetaObject.connectSlotsByName(updateWorkPlanForm)
    # setupUi

    def retranslateUi(self, updateWorkPlanForm):
        updateWorkPlanForm.setWindowTitle(QCoreApplication.translate("updateWorkPlanForm", u"\u041c\u0443\u043b\u044c\u0442\u0438\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.label_9.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u043b\u0430\u043d\u0430 \u0440\u0430\u0431\u043e\u0442", None))
        self.errorLbl.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("updateWorkPlanForm", u"\u0418\u043d\u0436\u0435\u043d\u0435\u0440 ", None))
        self.label_55.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))
        self.label_52.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("updateWorkPlanForm", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439", None))
        self.label_49.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_50.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))
        self.label_48.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_57.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430", None))
        self.updateWorkPlanBtn.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("updateWorkPlanForm", u"\u0417\u0418\u041f", None))
        self.label_3.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0417\u0418\u041f", None))
        self.label_8.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u041a\u043e\u043b-\u0432\u043e", None))
        self.label_47.setText(QCoreApplication.translate("updateWorkPlanForm", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
    # retranslateUi

