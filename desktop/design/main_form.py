# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(723, 478)
        self.verticalLayout = QVBoxLayout(MainForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(MainForm)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setIconSize(QSize(25, 25))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.tab)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_29 = QVBoxLayout(self.widget_23)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.tabWidget_5 = QTabWidget(self.widget_23)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_22 = QGridLayout(self.tab_13)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_59 = QLabel(self.tab_13)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_59, 1, 0, 1, 1)

        self.label_61 = QLabel(self.tab_13)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_61, 5, 2, 1, 1)

        self.lastnameProfileEdit = QLineEdit(self.tab_13)
        self.lastnameProfileEdit.setObjectName(u"lastnameProfileEdit")
        self.lastnameProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.lastnameProfileEdit, 7, 0, 1, 1)

        self.firstnameProfileEdit = QLineEdit(self.tab_13)
        self.firstnameProfileEdit.setObjectName(u"firstnameProfileEdit")
        self.firstnameProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.firstnameProfileEdit, 7, 1, 1, 1)

        self.patronymicProfileEdit = QLineEdit(self.tab_13)
        self.patronymicProfileEdit.setObjectName(u"patronymicProfileEdit")
        self.patronymicProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.patronymicProfileEdit, 7, 2, 1, 1)

        self.dateJoinedProfileEdit = QDateEdit(self.tab_13)
        self.dateJoinedProfileEdit.setObjectName(u"dateJoinedProfileEdit")
        self.dateJoinedProfileEdit.setReadOnly(True)
        self.dateJoinedProfileEdit.setCalendarPopup(True)

        self.gridLayout_22.addWidget(self.dateJoinedProfileEdit, 4, 2, 1, 1)

        self.label_65 = QLabel(self.tab_13)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_65, 1, 2, 1, 1)

        self.label_60 = QLabel(self.tab_13)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_60, 5, 0, 1, 1)

        self.label_66 = QLabel(self.tab_13)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_66, 1, 1, 1, 1)

        self.workStatusProfileEdit = QLineEdit(self.tab_13)
        self.workStatusProfileEdit.setObjectName(u"workStatusProfileEdit")
        self.workStatusProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.workStatusProfileEdit, 4, 1, 1, 1)

        self.label_58 = QLabel(self.tab_13)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_58, 5, 1, 1, 1)

        self.idProfileEdit = QLineEdit(self.tab_13)
        self.idProfileEdit.setObjectName(u"idProfileEdit")
        self.idProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.idProfileEdit, 4, 0, 1, 1)

        self.usernameProfileEdit = QLineEdit(self.tab_13)
        self.usernameProfileEdit.setObjectName(u"usernameProfileEdit")
        self.usernameProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.usernameProfileEdit, 9, 0, 1, 1)

        self.label_62 = QLabel(self.tab_13)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_62, 8, 0, 1, 1)

        self.label_64 = QLabel(self.tab_13)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_64, 8, 1, 1, 1)

        self.permissionProfileEdit = QLineEdit(self.tab_13)
        self.permissionProfileEdit.setObjectName(u"permissionProfileEdit")
        self.permissionProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.permissionProfileEdit, 9, 1, 1, 1)

        self.label_67 = QLabel(self.tab_13)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_67, 8, 2, 1, 1)

        self.birthdateProfileEdit = QDateEdit(self.tab_13)
        self.birthdateProfileEdit.setObjectName(u"birthdateProfileEdit")
        self.birthdateProfileEdit.setReadOnly(True)
        self.birthdateProfileEdit.setCalendarPopup(True)

        self.gridLayout_22.addWidget(self.birthdateProfileEdit, 9, 2, 1, 1)

        self.updateProfileBtn = QPushButton(self.tab_13)
        self.updateProfileBtn.setObjectName(u"updateProfileBtn")

        self.gridLayout_22.addWidget(self.updateProfileBtn, 11, 2, 1, 1)

        self.label_68 = QLabel(self.tab_13)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_22.addWidget(self.label_68, 10, 0, 1, 1)

        self.phoneProfileEdit = QLineEdit(self.tab_13)
        self.phoneProfileEdit.setObjectName(u"phoneProfileEdit")
        self.phoneProfileEdit.setReadOnly(True)

        self.gridLayout_22.addWidget(self.phoneProfileEdit, 11, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_13, "")

        self.verticalLayout_29.addWidget(self.tabWidget_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_7)


        self.verticalLayout_3.addWidget(self.widget_23)

        icon = QIcon()
        icon.addFile(u":/res/res/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab, icon, "")
        self.widget_1 = QWidget()
        self.widget_1.setObjectName(u"widget_1")
        self.verticalLayout_5 = QVBoxLayout(self.widget_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.widget_1)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.widget_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(0)
        self.widget_4 = QWidget(self.tab_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.WorkStatusTableWidget = QTableWidget(self.widget_4)
        if (self.WorkStatusTableWidget.columnCount() < 4):
            self.WorkStatusTableWidget.setColumnCount(4)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.WorkStatusTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.WorkStatusTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.WorkStatusTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.WorkStatusTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.WorkStatusTableWidget.setObjectName(u"WorkStatusTableWidget")
        self.WorkStatusTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.WorkStatusTableWidget.setStyleSheet(u"")
        self.WorkStatusTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.WorkStatusTableWidget.setAlternatingRowColors(False)
        self.WorkStatusTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.WorkStatusTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.WorkStatusTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.WorkStatusTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.WorkStatusTableWidget)


        self.gridLayout_2.addWidget(self.widget_4, 1, 1, 2, 1)

        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox = QGroupBox(self.widget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label.setMargin(4)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.nameWorkStatusEdit = QLineEdit(self.groupBox)
        self.nameWorkStatusEdit.setObjectName(u"nameWorkStatusEdit")

        self.gridLayout_3.addWidget(self.nameWorkStatusEdit, 1, 0, 1, 2)

        self.acceptFilterWorkStatusBtn = QPushButton(self.groupBox)
        self.acceptFilterWorkStatusBtn.setObjectName(u"acceptFilterWorkStatusBtn")

        self.gridLayout_3.addWidget(self.acceptFilterWorkStatusBtn, 4, 0, 1, 2)

        self.inactiveWorkStatusCheckBOx = QCheckBox(self.groupBox)
        self.inactiveWorkStatusCheckBOx.setObjectName(u"inactiveWorkStatusCheckBOx")

        self.gridLayout_3.addWidget(self.inactiveWorkStatusCheckBOx, 2, 1, 1, 1)

        self.activeWorkStatusCheckBox = QCheckBox(self.groupBox)
        self.activeWorkStatusCheckBox.setObjectName(u"activeWorkStatusCheckBox")

        self.gridLayout_3.addWidget(self.activeWorkStatusCheckBox, 2, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.createWorkStatusBtn = QPushButton(self.widget_3)
        self.createWorkStatusBtn.setObjectName(u"createWorkStatusBtn")

        self.verticalLayout_9.addWidget(self.createWorkStatusBtn)

        self.updateWorkStatusBtn = QPushButton(self.widget_3)
        self.updateWorkStatusBtn.setObjectName(u"updateWorkStatusBtn")

        self.verticalLayout_9.addWidget(self.updateWorkStatusBtn)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 2, 1)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout = QGridLayout(self.tab_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_5 = QWidget(self.tab_6)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.widget_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_4 = QGroupBox(self.widget_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_5.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_5.addWidget(self.label_4, 0, 1, 1, 1)

        self.acceptFilterEmployeeBtn = QPushButton(self.groupBox_4)
        self.acceptFilterEmployeeBtn.setObjectName(u"acceptFilterEmployeeBtn")

        self.gridLayout_5.addWidget(self.acceptFilterEmployeeBtn, 7, 1, 1, 2)

        self.lastnameEdit = QLineEdit(self.groupBox_4)
        self.lastnameEdit.setObjectName(u"lastnameEdit")

        self.gridLayout_5.addWidget(self.lastnameEdit, 1, 1, 1, 1)

        self.firstnameEdit = QLineEdit(self.groupBox_4)
        self.firstnameEdit.setObjectName(u"firstnameEdit")

        self.gridLayout_5.addWidget(self.firstnameEdit, 1, 2, 1, 1)

        self.inactiveEmployeeCheckBox = QCheckBox(self.groupBox_4)
        self.inactiveEmployeeCheckBox.setObjectName(u"inactiveEmployeeCheckBox")

        self.gridLayout_5.addWidget(self.inactiveEmployeeCheckBox, 6, 2, 1, 1)

        self.activeEmployeeCheckBox = QCheckBox(self.groupBox_4)
        self.activeEmployeeCheckBox.setObjectName(u"activeEmployeeCheckBox")

        self.gridLayout_5.addWidget(self.activeEmployeeCheckBox, 6, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_5.addWidget(self.label_6, 2, 1, 1, 1)

        self.WorkStatusBox = QComboBox(self.groupBox_4)
        self.WorkStatusBox.setObjectName(u"WorkStatusBox")

        self.gridLayout_5.addWidget(self.WorkStatusBox, 3, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.groupBox_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.createEmployeeBtn = QPushButton(self.widget_5)
        self.createEmployeeBtn.setObjectName(u"createEmployeeBtn")

        self.verticalLayout_11.addWidget(self.createEmployeeBtn)

        self.updateEmployeeBtn = QPushButton(self.widget_5)
        self.updateEmployeeBtn.setObjectName(u"updateEmployeeBtn")

        self.verticalLayout_11.addWidget(self.updateEmployeeBtn)


        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.tab_6)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_15 = QVBoxLayout(self.widget_6)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.EmployeeTableWidget = QTableWidget(self.widget_6)
        if (self.EmployeeTableWidget.columnCount() < 9):
            self.EmployeeTableWidget.setColumnCount(9)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font);
        self.EmployeeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.EmployeeTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        self.EmployeeTableWidget.setObjectName(u"EmployeeTableWidget")
        self.EmployeeTableWidget.setStyleSheet(u"")
        self.EmployeeTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.EmployeeTableWidget.setAlternatingRowColors(False)
        self.EmployeeTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.EmployeeTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.EmployeeTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.EmployeeTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.EmployeeTableWidget)


        self.gridLayout.addWidget(self.widget_6, 0, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.verticalLayout_4.addWidget(self.tabWidget_2)


        self.verticalLayout_5.addWidget(self.widget_2)

        icon1 = QIcon()
        icon1.addFile(u":/res/res/group.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.widget_1, icon1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.tab_3)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_8 = QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_8 = QVBoxLayout(self.widget_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.CompanyTableWidget = QTableWidget(self.widget_9)
        if (self.CompanyTableWidget.columnCount() < 4):
            self.CompanyTableWidget.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font);
        self.CompanyTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.CompanyTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.CompanyTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.CompanyTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.CompanyTableWidget.setObjectName(u"CompanyTableWidget")
        self.CompanyTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.CompanyTableWidget.setStyleSheet(u"")
        self.CompanyTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.CompanyTableWidget.setAlternatingRowColors(False)
        self.CompanyTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.CompanyTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.CompanyTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.CompanyTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.CompanyTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.CompanyTableWidget)


        self.gridLayout_8.addWidget(self.widget_9, 0, 1, 3, 1)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.widget_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_3 = QGroupBox(self.widget_8)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.acceptFilterCompanyBtn = QPushButton(self.groupBox_3)
        self.acceptFilterCompanyBtn.setObjectName(u"acceptFilterCompanyBtn")

        self.gridLayout_6.addWidget(self.acceptFilterCompanyBtn, 5, 0, 1, 4)

        self.inactiveCompanyCheckBox = QCheckBox(self.groupBox_3)
        self.inactiveCompanyCheckBox.setObjectName(u"inactiveCompanyCheckBox")

        self.gridLayout_6.addWidget(self.inactiveCompanyCheckBox, 3, 2, 1, 2)

        self.activeCompanyCheckBox = QCheckBox(self.groupBox_3)
        self.activeCompanyCheckBox.setObjectName(u"activeCompanyCheckBox")

        self.gridLayout_6.addWidget(self.activeCompanyCheckBox, 3, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_8.setMargin(4)

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.nameCompanyFilterEdit = QLineEdit(self.groupBox_3)
        self.nameCompanyFilterEdit.setObjectName(u"nameCompanyFilterEdit")

        self.gridLayout_6.addWidget(self.nameCompanyFilterEdit, 1, 0, 1, 4)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.addressTableWidget = QTableWidget(self.widget_8)
        if (self.addressTableWidget.columnCount() < 5):
            self.addressTableWidget.setColumnCount(5)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.addressTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.addressTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.addressTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.addressTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.addressTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        self.addressTableWidget.setObjectName(u"addressTableWidget")

        self.verticalLayout_12.addWidget(self.addressTableWidget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_2)

        self.createCompanyBtn = QPushButton(self.widget_8)
        self.createCompanyBtn.setObjectName(u"createCompanyBtn")

        self.verticalLayout_12.addWidget(self.createCompanyBtn)

        self.updateCompanyBtn = QPushButton(self.widget_8)
        self.updateCompanyBtn.setObjectName(u"updateCompanyBtn")

        self.verticalLayout_12.addWidget(self.updateCompanyBtn)


        self.gridLayout_8.addWidget(self.widget_8, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_7)

        icon2 = QIcon()
        icon2.addFile(u":/res/res/urbanization.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_3, icon2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_28 = QVBoxLayout(self.tab_4)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.tabWidget_4 = QTabWidget(self.tab_4)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_25 = QVBoxLayout(self.tab_11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_22 = QWidget(self.tab_11)
        self.widget_22.setObjectName(u"widget_22")
        self.gridLayout_18 = QGridLayout(self.widget_22)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(0)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_22)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(400, 0))
        self.widget_20.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widget_20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_11 = QGroupBox(self.widget_20)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_14 = QGridLayout(self.groupBox_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.acceptWorkPlanFilterBtn = QPushButton(self.groupBox_11)
        self.acceptWorkPlanFilterBtn.setObjectName(u"acceptWorkPlanFilterBtn")

        self.gridLayout_14.addWidget(self.acceptWorkPlanFilterBtn, 4, 0, 1, 2)

        self.label_26 = QLabel(self.groupBox_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_14.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_14.addWidget(self.label_24, 0, 0, 1, 1)

        self.lastnameWorkPlanEdit = QLineEdit(self.groupBox_11)
        self.lastnameWorkPlanEdit.setObjectName(u"lastnameWorkPlanEdit")

        self.gridLayout_14.addWidget(self.lastnameWorkPlanEdit, 1, 1, 1, 1)

        self.companyWorkPlanEdit = QLineEdit(self.groupBox_11)
        self.companyWorkPlanEdit.setObjectName(u"companyWorkPlanEdit")

        self.gridLayout_14.addWidget(self.companyWorkPlanEdit, 1, 0, 1, 1)

        self.priorityWorkPlanEdit = QComboBox(self.groupBox_11)
        self.priorityWorkPlanEdit.setObjectName(u"priorityWorkPlanEdit")

        self.gridLayout_14.addWidget(self.priorityWorkPlanEdit, 3, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_11)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_14.addWidget(self.label_25, 0, 1, 1, 1)

        self.statusWorkPlanEdit = QComboBox(self.groupBox_11)
        self.statusWorkPlanEdit.setObjectName(u"statusWorkPlanEdit")

        self.gridLayout_14.addWidget(self.statusWorkPlanEdit, 3, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_14.addWidget(self.label_27, 2, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_11)

        self.chatWidget = QTabWidget(self.widget_20)
        self.chatWidget.setObjectName(u"chatWidget")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_23 = QGridLayout(self.tab_14)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.messageToEmployeeEdit = QLineEdit(self.tab_14)
        self.messageToEmployeeEdit.setObjectName(u"messageToEmployeeEdit")

        self.gridLayout_23.addWidget(self.messageToEmployeeEdit, 2, 0, 1, 1)

        self.sendMessageToEmployeeBtn = QPushButton(self.tab_14)
        self.sendMessageToEmployeeBtn.setObjectName(u"sendMessageToEmployeeBtn")

        self.gridLayout_23.addWidget(self.sendMessageToEmployeeBtn, 2, 1, 1, 1)

        self.chatEmployeeListWidget = QListWidget(self.tab_14)
        self.chatEmployeeListWidget.setObjectName(u"chatEmployeeListWidget")
        self.chatEmployeeListWidget.setAutoScroll(True)
        self.chatEmployeeListWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chatEmployeeListWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout_23.addWidget(self.chatEmployeeListWidget, 0, 0, 1, 2)

        self.chatWidget.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_4 = QGridLayout(self.tab_15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.messageToClientEdit = QLineEdit(self.tab_15)
        self.messageToClientEdit.setObjectName(u"messageToClientEdit")

        self.gridLayout_4.addWidget(self.messageToClientEdit, 2, 0, 1, 1)

        self.sendMesageToClientBtn = QPushButton(self.tab_15)
        self.sendMesageToClientBtn.setObjectName(u"sendMesageToClientBtn")

        self.gridLayout_4.addWidget(self.sendMesageToClientBtn, 2, 1, 1, 1)

        self.chatClientListWidget = QListWidget(self.tab_15)
        self.chatClientListWidget.setObjectName(u"chatClientListWidget")
        self.chatClientListWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chatClientListWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout_4.addWidget(self.chatClientListWidget, 0, 0, 1, 2)

        self.chatWidget.addTab(self.tab_15, "")

        self.verticalLayout_10.addWidget(self.chatWidget)


        self.gridLayout_18.addWidget(self.widget_20, 0, 0, 1, 1)

        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_20 = QVBoxLayout(self.widget_24)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.WorkPlanTableWidget = QTableWidget(self.widget_24)
        if (self.WorkPlanTableWidget.columnCount() < 7):
            self.WorkPlanTableWidget.setColumnCount(7)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font);
        self.WorkPlanTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        self.WorkPlanTableWidget.setObjectName(u"WorkPlanTableWidget")
        self.WorkPlanTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.WorkPlanTableWidget.setStyleSheet(u"")
        self.WorkPlanTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.WorkPlanTableWidget.setAlternatingRowColors(False)
        self.WorkPlanTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.WorkPlanTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.WorkPlanTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.WorkPlanTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_20.addWidget(self.WorkPlanTableWidget)


        self.gridLayout_18.addWidget(self.widget_24, 0, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.widget_22)

        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_27 = QVBoxLayout(self.tab_12)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_19 = QWidget(self.tab_12)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_17 = QGridLayout(self.widget_19)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.widget_19)
        self.widget_21.setObjectName(u"widget_21")
        self.gridLayout_15 = QGridLayout(self.widget_21)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(4)
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.groupBox_12 = QGroupBox(self.widget_21)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_16 = QGridLayout(self.groupBox_12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(6)
        self.gridLayout_16.setContentsMargins(6, 6, 6, 6)
        self.serialNumberApplicationEdit = QLineEdit(self.groupBox_12)
        self.serialNumberApplicationEdit.setObjectName(u"serialNumberApplicationEdit")
        self.serialNumberApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.serialNumberApplicationEdit, 11, 0, 1, 1)

        self.label_39 = QLabel(self.groupBox_12)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_39, 10, 1, 1, 1)

        self.IPApplicationEdit = QLineEdit(self.groupBox_12)
        self.IPApplicationEdit.setObjectName(u"IPApplicationEdit")
        self.IPApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.IPApplicationEdit, 11, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_12)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_40, 12, 0, 1, 1)

        self.label_41 = QLabel(self.groupBox_12)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_41, 12, 1, 1, 1)

        self.equipmentNameApplicationEdit = QLineEdit(self.groupBox_12)
        self.equipmentNameApplicationEdit.setObjectName(u"equipmentNameApplicationEdit")
        self.equipmentNameApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.equipmentNameApplicationEdit, 13, 0, 1, 1)

        self.locationApplicationEdit = QLineEdit(self.groupBox_12)
        self.locationApplicationEdit.setObjectName(u"locationApplicationEdit")
        self.locationApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.locationApplicationEdit, 13, 1, 1, 1)

        self.funcLimitedApplicationEdit = QLineEdit(self.groupBox_12)
        self.funcLimitedApplicationEdit.setObjectName(u"funcLimitedApplicationEdit")
        self.funcLimitedApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.funcLimitedApplicationEdit, 16, 0, 1, 1)

        self.logicalErrorsApplicationEdit = QLineEdit(self.groupBox_12)
        self.logicalErrorsApplicationEdit.setObjectName(u"logicalErrorsApplicationEdit")
        self.logicalErrorsApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.logicalErrorsApplicationEdit, 16, 1, 1, 1)

        self.nonOperationalApplicationCheckBox = QCheckBox(self.groupBox_12)
        self.nonOperationalApplicationCheckBox.setObjectName(u"nonOperationalApplicationCheckBox")
        self.nonOperationalApplicationCheckBox.setCheckable(True)
        self.nonOperationalApplicationCheckBox.setTristate(False)

        self.gridLayout_16.addWidget(self.nonOperationalApplicationCheckBox, 14, 0, 1, 2)

        self.label_42 = QLabel(self.groupBox_12)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_42, 15, 0, 1, 1)

        self.label_44 = QLabel(self.groupBox_12)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_44, 17, 0, 1, 2)

        self.label_38 = QLabel(self.groupBox_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_38, 10, 0, 1, 1)

        self.label_43 = QLabel(self.groupBox_12)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_43, 15, 1, 1, 1)

        self.descriptionApplicationEdit = QTextEdit(self.groupBox_12)
        self.descriptionApplicationEdit.setObjectName(u"descriptionApplicationEdit")
        self.descriptionApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.descriptionApplicationEdit, 18, 0, 1, 2)

        self.label_35 = QLabel(self.groupBox_12)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_35, 8, 1, 1, 1)

        self.emailApplicationEdit = QLineEdit(self.groupBox_12)
        self.emailApplicationEdit.setObjectName(u"emailApplicationEdit")
        self.emailApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.emailApplicationEdit, 9, 0, 1, 1)

        self.label_31 = QLabel(self.groupBox_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_31, 2, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_12)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_32, 4, 0, 1, 1)

        self.label_37 = QLabel(self.groupBox_12)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_37, 2, 0, 1, 1)

        self.addressApplicationEdit = QLineEdit(self.groupBox_12)
        self.addressApplicationEdit.setObjectName(u"addressApplicationEdit")
        self.addressApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.addressApplicationEdit, 3, 0, 1, 1)

        self.label_34 = QLabel(self.groupBox_12)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_34, 6, 0, 1, 1)

        self.phoneApplicationEdit = QLineEdit(self.groupBox_12)
        self.phoneApplicationEdit.setObjectName(u"phoneApplicationEdit")
        self.phoneApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.phoneApplicationEdit, 9, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_33 = QLabel(self.groupBox_12)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_33, 4, 1, 1, 1)

        self.label_36 = QLabel(self.groupBox_12)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_36, 8, 0, 1, 1)

        self.priorityApplicationEdit = QLineEdit(self.groupBox_12)
        self.priorityApplicationEdit.setObjectName(u"priorityApplicationEdit")
        self.priorityApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.priorityApplicationEdit, 3, 1, 1, 1)

        self.patronymicApplicationEdit = QLineEdit(self.groupBox_12)
        self.patronymicApplicationEdit.setObjectName(u"patronymicApplicationEdit")
        self.patronymicApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.patronymicApplicationEdit, 7, 0, 1, 1)

        self.firstNameApplicationEdit = QLineEdit(self.groupBox_12)
        self.firstNameApplicationEdit.setObjectName(u"firstNameApplicationEdit")
        self.firstNameApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.firstNameApplicationEdit, 5, 1, 1, 1)

        self.lastNameApplicationEdit = QLineEdit(self.groupBox_12)
        self.lastNameApplicationEdit.setObjectName(u"lastNameApplicationEdit")
        self.lastNameApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.lastNameApplicationEdit, 5, 0, 1, 1)

        self.companyApplicationEdit = QLineEdit(self.groupBox_12)
        self.companyApplicationEdit.setObjectName(u"companyApplicationEdit")
        self.companyApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.companyApplicationEdit, 1, 0, 1, 1)

        self.label_56 = QLabel(self.groupBox_12)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_16.addWidget(self.label_56, 0, 1, 1, 1)

        self.createdApplicationEdit = QLineEdit(self.groupBox_12)
        self.createdApplicationEdit.setObjectName(u"createdApplicationEdit")
        self.createdApplicationEdit.setReadOnly(True)

        self.gridLayout_16.addWidget(self.createdApplicationEdit, 1, 1, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_12, 1, 2, 1, 1)

        self.groupBox_13 = QGroupBox(self.widget_21)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_19 = QGridLayout(self.groupBox_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.tasksTextEdit = QTextEdit(self.groupBox_13)
        self.tasksTextEdit.setObjectName(u"tasksTextEdit")
        self.tasksTextEdit.setReadOnly(True)

        self.gridLayout_19.addWidget(self.tasksTextEdit, 6, 0, 1, 3)

        self.statusLineEdit = QLineEdit(self.groupBox_13)
        self.statusLineEdit.setObjectName(u"statusLineEdit")
        self.statusLineEdit.setReadOnly(True)

        self.gridLayout_19.addWidget(self.statusLineEdit, 2, 1, 1, 1)

        self.label_47 = QLabel(self.groupBox_13)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_19.addWidget(self.label_47, 1, 1, 1, 1)

        self.groupBox_15 = QGroupBox(self.groupBox_13)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_21 = QGridLayout(self.groupBox_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.lastnameSmartHandLineEdit = QLineEdit(self.groupBox_15)
        self.lastnameSmartHandLineEdit.setObjectName(u"lastnameSmartHandLineEdit")
        self.lastnameSmartHandLineEdit.setReadOnly(True)

        self.gridLayout_21.addWidget(self.lastnameSmartHandLineEdit, 1, 2, 1, 1)

        self.label_52 = QLabel(self.groupBox_15)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_21.addWidget(self.label_52, 0, 1, 1, 1)

        self.firstnameSmartHandLineEdit = QLineEdit(self.groupBox_15)
        self.firstnameSmartHandLineEdit.setObjectName(u"firstnameSmartHandLineEdit")
        self.firstnameSmartHandLineEdit.setReadOnly(True)

        self.gridLayout_21.addWidget(self.firstnameSmartHandLineEdit, 3, 1, 1, 1)

        self.patronymicSmartHandLineEdit = QLineEdit(self.groupBox_15)
        self.patronymicSmartHandLineEdit.setObjectName(u"patronymicSmartHandLineEdit")
        self.patronymicSmartHandLineEdit.setReadOnly(True)

        self.gridLayout_21.addWidget(self.patronymicSmartHandLineEdit, 3, 2, 1, 1)

        self.label_53 = QLabel(self.groupBox_15)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_21.addWidget(self.label_53, 2, 2, 1, 1)

        self.label_54 = QLabel(self.groupBox_15)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_21.addWidget(self.label_54, 0, 2, 1, 1)

        self.label_55 = QLabel(self.groupBox_15)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_21.addWidget(self.label_55, 2, 1, 1, 1)

        self.idSmartHandLineEdit = QLineEdit(self.groupBox_15)
        self.idSmartHandLineEdit.setObjectName(u"idSmartHandLineEdit")
        self.idSmartHandLineEdit.setReadOnly(True)

        self.gridLayout_21.addWidget(self.idSmartHandLineEdit, 1, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_15, 0, 2, 1, 3)

        self.groupBox_14 = QGroupBox(self.groupBox_13)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_20 = QGridLayout(self.groupBox_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.firstnameResponsibleLineEdit = QLineEdit(self.groupBox_14)
        self.firstnameResponsibleLineEdit.setObjectName(u"firstnameResponsibleLineEdit")
        self.firstnameResponsibleLineEdit.setReadOnly(True)

        self.gridLayout_20.addWidget(self.firstnameResponsibleLineEdit, 3, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_14)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_20.addWidget(self.label_45, 0, 1, 1, 1)

        self.lastnameResponsibleLineEdit = QLineEdit(self.groupBox_14)
        self.lastnameResponsibleLineEdit.setObjectName(u"lastnameResponsibleLineEdit")
        self.lastnameResponsibleLineEdit.setReadOnly(True)

        self.gridLayout_20.addWidget(self.lastnameResponsibleLineEdit, 1, 2, 1, 1)

        self.label_50 = QLabel(self.groupBox_14)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_20.addWidget(self.label_50, 2, 2, 1, 1)

        self.label_46 = QLabel(self.groupBox_14)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_20.addWidget(self.label_46, 0, 2, 1, 1)

        self.idResponsibleLineEdit = QLineEdit(self.groupBox_14)
        self.idResponsibleLineEdit.setObjectName(u"idResponsibleLineEdit")
        self.idResponsibleLineEdit.setReadOnly(True)

        self.gridLayout_20.addWidget(self.idResponsibleLineEdit, 1, 1, 1, 1)

        self.label_49 = QLabel(self.groupBox_14)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_20.addWidget(self.label_49, 2, 1, 1, 1)

        self.patronymicResponsibleLineEdit = QLineEdit(self.groupBox_14)
        self.patronymicResponsibleLineEdit.setObjectName(u"patronymicResponsibleLineEdit")
        self.patronymicResponsibleLineEdit.setReadOnly(True)

        self.gridLayout_20.addWidget(self.patronymicResponsibleLineEdit, 3, 2, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_14, 0, 0, 1, 2)

        self.endDateEdit = QDateEdit(self.groupBox_13)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setReadOnly(True)
        self.endDateEdit.setCalendarPopup(True)

        self.gridLayout_19.addWidget(self.endDateEdit, 2, 4, 1, 1)

        self.label_57 = QLabel(self.groupBox_13)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_19.addWidget(self.label_57, 1, 4, 1, 1)

        self.isagreedCheckBox = QCheckBox(self.groupBox_13)
        self.isagreedCheckBox.setObjectName(u"isagreedCheckBox")
        self.isagreedCheckBox.setCheckable(True)

        self.gridLayout_19.addWidget(self.isagreedCheckBox, 2, 0, 1, 1)

        self.ZipTableWidget_2 = QTableWidget(self.groupBox_13)
        if (self.ZipTableWidget_2.columnCount() < 7):
            self.ZipTableWidget_2.setColumnCount(7)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFont(font);
        self.ZipTableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        self.ZipTableWidget_2.setObjectName(u"ZipTableWidget_2")
        self.ZipTableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_19.addWidget(self.ZipTableWidget_2, 5, 0, 1, 5)

        self.label_48 = QLabel(self.groupBox_13)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_19.addWidget(self.label_48, 1, 3, 1, 1)

        self.startDateEdit = QDateEdit(self.groupBox_13)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setReadOnly(True)
        self.startDateEdit.setCalendarPopup(True)

        self.gridLayout_19.addWidget(self.startDateEdit, 2, 3, 1, 1)

        self.notesTextEdit = QTextEdit(self.groupBox_13)
        self.notesTextEdit.setObjectName(u"notesTextEdit")
        self.notesTextEdit.setReadOnly(True)

        self.gridLayout_19.addWidget(self.notesTextEdit, 6, 3, 1, 2)

        self.updateWorkPlanBtn = QPushButton(self.groupBox_13)
        self.updateWorkPlanBtn.setObjectName(u"updateWorkPlanBtn")

        self.gridLayout_19.addWidget(self.updateWorkPlanBtn, 7, 0, 1, 5)


        self.gridLayout_15.addWidget(self.groupBox_13, 1, 3, 1, 1)


        self.gridLayout_17.addWidget(self.widget_21, 0, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.widget_19)

        self.tabWidget_4.addTab(self.tab_12, "")

        self.verticalLayout_28.addWidget(self.tabWidget_4)

        icon3 = QIcon()
        icon3.addFile(u":/res/res/writing.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_4, icon3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_13 = QVBoxLayout(self.tab_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tabWidget_3 = QTabWidget(self.tab_5)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_10 = QWidget(self.tab_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.widget_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_6 = QGroupBox(self.widget_10)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_11.setMargin(4)

        self.gridLayout_7.addWidget(self.label_11, 2, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_9.setMargin(4)

        self.gridLayout_7.addWidget(self.label_9, 2, 2, 1, 1)

        self.acceptFilterWorkStatusBtn_3 = QPushButton(self.groupBox_6)
        self.acceptFilterWorkStatusBtn_3.setObjectName(u"acceptFilterWorkStatusBtn_3")

        self.gridLayout_7.addWidget(self.acceptFilterWorkStatusBtn_3, 14, 0, 1, 3)

        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_12.setMargin(4)

        self.gridLayout_7.addWidget(self.label_12, 5, 0, 1, 2)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_14.setMargin(4)

        self.gridLayout_7.addWidget(self.label_14, 5, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox_6)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_7.addWidget(self.lineEdit_11, 3, 2, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_6)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_7.addWidget(self.lineEdit_12, 3, 0, 1, 2)

        self.lineEdit_16 = QLineEdit(self.groupBox_6)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_7.addWidget(self.lineEdit_16, 9, 2, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox_6)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_7.addWidget(self.lineEdit_14, 9, 0, 1, 2)


        self.verticalLayout_14.addWidget(self.groupBox_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.createZipBtn = QPushButton(self.widget_10)
        self.createZipBtn.setObjectName(u"createZipBtn")

        self.verticalLayout_14.addWidget(self.createZipBtn)

        self.updateZipBtn = QPushButton(self.widget_10)
        self.updateZipBtn.setObjectName(u"updateZipBtn")

        self.verticalLayout_14.addWidget(self.updateZipBtn)


        self.horizontalLayout_2.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.tab_7)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_16 = QVBoxLayout(self.widget_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.ZipTableWidget = QTableWidget(self.widget_11)
        if (self.ZipTableWidget.columnCount() < 6):
            self.ZipTableWidget.setColumnCount(6)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font);
        self.ZipTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.ZipTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        self.ZipTableWidget.setObjectName(u"ZipTableWidget")
        self.ZipTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.ZipTableWidget.setStyleSheet(u"")
        self.ZipTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ZipTableWidget.setAlternatingRowColors(False)
        self.ZipTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ZipTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.ZipTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.ZipTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_16.addWidget(self.ZipTableWidget)


        self.horizontalLayout_2.addWidget(self.widget_11)

        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_10 = QGridLayout(self.tab_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget_13 = QWidget(self.tab_8)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_11 = QGridLayout(self.widget_13)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(4)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_18 = QVBoxLayout(self.widget_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_7 = QGroupBox(self.widget_14)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_22.setMargin(4)

        self.gridLayout_9.addWidget(self.label_22, 0, 0, 1, 1)

        self.namePriorityEdit = QLineEdit(self.groupBox_7)
        self.namePriorityEdit.setObjectName(u"namePriorityEdit")

        self.gridLayout_9.addWidget(self.namePriorityEdit, 1, 0, 1, 2)

        self.acceptFilterPriorityBtn = QPushButton(self.groupBox_7)
        self.acceptFilterPriorityBtn.setObjectName(u"acceptFilterPriorityBtn")

        self.gridLayout_9.addWidget(self.acceptFilterPriorityBtn, 4, 0, 1, 2)

        self.activePriorityBtn = QCheckBox(self.groupBox_7)
        self.activePriorityBtn.setObjectName(u"activePriorityBtn")

        self.gridLayout_9.addWidget(self.activePriorityBtn, 2, 0, 1, 1)

        self.inactivePriorityBtn = QCheckBox(self.groupBox_7)
        self.inactivePriorityBtn.setObjectName(u"inactivePriorityBtn")

        self.gridLayout_9.addWidget(self.inactivePriorityBtn, 2, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.groupBox_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)

        self.groupBox_8 = QGroupBox(self.widget_14)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.priorityLineEdit = QLineEdit(self.groupBox_8)
        self.priorityLineEdit.setObjectName(u"priorityLineEdit")

        self.verticalLayout_19.addWidget(self.priorityLineEdit)

        self.addPriorityBtn = QPushButton(self.groupBox_8)
        self.addPriorityBtn.setObjectName(u"addPriorityBtn")

        self.verticalLayout_19.addWidget(self.addPriorityBtn)


        self.verticalLayout_18.addWidget(self.groupBox_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_4)

        self.updatePriorityBtn = QPushButton(self.widget_14)
        self.updatePriorityBtn.setObjectName(u"updatePriorityBtn")

        self.verticalLayout_18.addWidget(self.updatePriorityBtn)


        self.gridLayout_11.addWidget(self.widget_14, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.vboxLayout = QVBoxLayout(self.widget_15)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.PriorityTableWidget = QTableWidget(self.widget_15)
        if (self.PriorityTableWidget.columnCount() < 3):
            self.PriorityTableWidget.setColumnCount(3)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem42.setFont(font);
        self.PriorityTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.PriorityTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.PriorityTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        self.PriorityTableWidget.setObjectName(u"PriorityTableWidget")
        self.PriorityTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.PriorityTableWidget.setStyleSheet(u"")
        self.PriorityTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.PriorityTableWidget.setAlternatingRowColors(False)
        self.PriorityTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PriorityTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.PriorityTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.PriorityTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.PriorityTableWidget.horizontalHeader().setStretchLastSection(False)

        self.vboxLayout.addWidget(self.PriorityTableWidget)


        self.gridLayout_11.addWidget(self.widget_15, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_13, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_24 = QVBoxLayout(self.tab_10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_16 = QWidget(self.tab_10)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_13 = QGridLayout(self.widget_16)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.widget_17)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_9 = QGroupBox(self.widget_17)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_12 = QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_23 = QLabel(self.groupBox_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_23.setMargin(4)

        self.gridLayout_12.addWidget(self.label_23, 0, 0, 1, 1)

        self.nameWorkPlanStatusEdit = QLineEdit(self.groupBox_9)
        self.nameWorkPlanStatusEdit.setObjectName(u"nameWorkPlanStatusEdit")

        self.gridLayout_12.addWidget(self.nameWorkPlanStatusEdit, 1, 0, 1, 2)

        self.acceptFilterWorkPlanStatusBtn = QPushButton(self.groupBox_9)
        self.acceptFilterWorkPlanStatusBtn.setObjectName(u"acceptFilterWorkPlanStatusBtn")

        self.gridLayout_12.addWidget(self.acceptFilterWorkPlanStatusBtn, 4, 0, 1, 2)

        self.activeWorkPlanStatusBtn = QCheckBox(self.groupBox_9)
        self.activeWorkPlanStatusBtn.setObjectName(u"activeWorkPlanStatusBtn")

        self.gridLayout_12.addWidget(self.activeWorkPlanStatusBtn, 2, 0, 1, 1)

        self.inactiveWorkPlanStatusBtn = QCheckBox(self.groupBox_9)
        self.inactiveWorkPlanStatusBtn.setObjectName(u"inactiveWorkPlanStatusBtn")

        self.gridLayout_12.addWidget(self.inactiveWorkPlanStatusBtn, 2, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.groupBox_9)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_5)

        self.groupBox_10 = QGroupBox(self.widget_17)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.workPlanStatusLineEdit = QLineEdit(self.groupBox_10)
        self.workPlanStatusLineEdit.setObjectName(u"workPlanStatusLineEdit")

        self.verticalLayout_22.addWidget(self.workPlanStatusLineEdit)

        self.addWorkPlanStatusBtn = QPushButton(self.groupBox_10)
        self.addWorkPlanStatusBtn.setObjectName(u"addWorkPlanStatusBtn")

        self.verticalLayout_22.addWidget(self.addWorkPlanStatusBtn)


        self.verticalLayout_21.addWidget(self.groupBox_10)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_21.addItem(self.horizontalSpacer_5)

        self.updateWorkPlanStatusBtn = QPushButton(self.widget_17)
        self.updateWorkPlanStatusBtn.setObjectName(u"updateWorkPlanStatusBtn")

        self.verticalLayout_21.addWidget(self.updateWorkPlanStatusBtn)


        self.gridLayout_13.addWidget(self.widget_17, 0, 0, 1, 1)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_23 = QVBoxLayout(self.widget_18)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.WorkPlanStatusTableWidget = QTableWidget(self.widget_18)
        if (self.WorkPlanStatusTableWidget.columnCount() < 3):
            self.WorkPlanStatusTableWidget.setColumnCount(3)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem45.setFont(font);
        self.WorkPlanStatusTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanStatusTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.WorkPlanStatusTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem47)
        self.WorkPlanStatusTableWidget.setObjectName(u"WorkPlanStatusTableWidget")
        self.WorkPlanStatusTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.WorkPlanStatusTableWidget.setStyleSheet(u"")
        self.WorkPlanStatusTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.WorkPlanStatusTableWidget.setAlternatingRowColors(False)
        self.WorkPlanStatusTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.WorkPlanStatusTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.WorkPlanStatusTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.WorkPlanStatusTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.WorkPlanStatusTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_23.addWidget(self.WorkPlanStatusTableWidget)


        self.gridLayout_13.addWidget(self.widget_18, 0, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.widget_16)

        self.tabWidget_3.addTab(self.tab_10, "")

        self.verticalLayout_13.addWidget(self.tabWidget_3)

        icon4 = QIcon()
        icon4.addFile(u":/res/res/dots.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_5, icon4, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_17 = QVBoxLayout(self.tab_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_12 = QWidget(self.tab_9)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_25 = QGridLayout(self.widget_12)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.groupBox_2 = QGroupBox(self.widget_12)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(450, 170))
        self.gridLayout_24 = QGridLayout(self.groupBox_2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_10.setMargin(4)

        self.gridLayout_24.addWidget(self.label_10, 1, 0, 1, 1)

        self.diagramStartDate = QDateEdit(self.groupBox_2)
        self.diagramStartDate.setObjectName(u"diagramStartDate")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diagramStartDate.sizePolicy().hasHeightForWidth())
        self.diagramStartDate.setSizePolicy(sizePolicy)
        self.diagramStartDate.setDateTime(QDateTime(QDate(2024, 11, 1), QTime(0, 0, 0)))
        self.diagramStartDate.setMinimumDateTime(QDateTime(QDate(2023, 9, 14), QTime(0, 0, 0)))
        self.diagramStartDate.setCalendarPopup(True)

        self.gridLayout_24.addWidget(self.diagramStartDate, 2, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_8, 0, 0, 1, 2)

        self.diagramEndDate = QDateEdit(self.groupBox_2)
        self.diagramEndDate.setObjectName(u"diagramEndDate")
        sizePolicy.setHeightForWidth(self.diagramEndDate.sizePolicy().hasHeightForWidth())
        self.diagramEndDate.setSizePolicy(sizePolicy)
        self.diagramEndDate.setDateTime(QDateTime(QDate(2024, 11, 1), QTime(0, 0, 0)))
        self.diagramEndDate.setMinimumDateTime(QDateTime(QDate(2023, 9, 14), QTime(0, 0, 0)))
        self.diagramEndDate.setCalendarPopup(True)

        self.gridLayout_24.addWidget(self.diagramEndDate, 2, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_13.setMargin(4)

        self.gridLayout_24.addWidget(self.label_13, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_6, 5, 0, 1, 3)

        self.diagramDateFilterCheckBox = QCheckBox(self.groupBox_2)
        self.diagramDateFilterCheckBox.setObjectName(u"diagramDateFilterCheckBox")

        self.gridLayout_24.addWidget(self.diagramDateFilterCheckBox, 4, 0, 1, 2)


        self.gridLayout_25.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_16 = QGroupBox(self.widget_12)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_26 = QGridLayout(self.groupBox_16)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_7 = QLabel(self.groupBox_16)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_26.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_16)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_26.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_16)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_26.addWidget(self.label_17, 3, 0, 1, 1)

        self.diagramFinalEdit = QLineEdit(self.groupBox_16)
        self.diagramFinalEdit.setObjectName(u"diagramFinalEdit")
        self.diagramFinalEdit.setReadOnly(True)

        self.gridLayout_26.addWidget(self.diagramFinalEdit, 0, 1, 1, 1)

        self.diagramExpireEdit = QLineEdit(self.groupBox_16)
        self.diagramExpireEdit.setObjectName(u"diagramExpireEdit")
        self.diagramExpireEdit.setReadOnly(True)

        self.gridLayout_26.addWidget(self.diagramExpireEdit, 2, 1, 1, 1)

        self.diagramProcessEdit = QLineEdit(self.groupBox_16)
        self.diagramProcessEdit.setObjectName(u"diagramProcessEdit")
        self.diagramProcessEdit.setReadOnly(True)

        self.gridLayout_26.addWidget(self.diagramProcessEdit, 3, 1, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_16, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.widget_12)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.diagramZipTableWidget = QTableWidget(self.groupBox_5)
        if (self.diagramZipTableWidget.columnCount() < 6):
            self.diagramZipTableWidget.setColumnCount(6)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem48.setFont(font);
        self.diagramZipTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.diagramZipTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.diagramZipTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.diagramZipTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.diagramZipTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.diagramZipTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem53)
        self.diagramZipTableWidget.setObjectName(u"diagramZipTableWidget")
        self.diagramZipTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.diagramZipTableWidget.setStyleSheet(u"")
        self.diagramZipTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.diagramZipTableWidget.setAlternatingRowColors(False)
        self.diagramZipTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.diagramZipTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.diagramZipTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.diagramZipTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_31.addWidget(self.diagramZipTableWidget)


        self.gridLayout_25.addWidget(self.groupBox_5, 3, 1, 1, 3)

        self.groupBox_18 = QGroupBox(self.widget_12)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_15 = QLabel(self.groupBox_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_15.setMargin(4)

        self.verticalLayout_26.addWidget(self.label_15)

        self.diagramStatusWorkComboBox = QComboBox(self.groupBox_18)
        self.diagramStatusWorkComboBox.setObjectName(u"diagramStatusWorkComboBox")

        self.verticalLayout_26.addWidget(self.diagramStatusWorkComboBox)

        self.label_16 = QLabel(self.groupBox_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.label_16.setMargin(4)

        self.verticalLayout_26.addWidget(self.label_16)

        self.diagramEmployeeTableWidget = QTableWidget(self.groupBox_18)
        if (self.diagramEmployeeTableWidget.columnCount() < 5):
            self.diagramEmployeeTableWidget.setColumnCount(5)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem54.setFont(font);
        self.diagramEmployeeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.diagramEmployeeTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.diagramEmployeeTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.diagramEmployeeTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.diagramEmployeeTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem58)
        self.diagramEmployeeTableWidget.setObjectName(u"diagramEmployeeTableWidget")
        self.diagramEmployeeTableWidget.setStyleSheet(u"")
        self.diagramEmployeeTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.diagramEmployeeTableWidget.setAlternatingRowColors(False)
        self.diagramEmployeeTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.diagramEmployeeTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.diagramEmployeeTableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.diagramEmployeeTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_26.addWidget(self.diagramEmployeeTableWidget)

        self.diagramAcceptFilter = QPushButton(self.groupBox_18)
        self.diagramAcceptFilter.setObjectName(u"diagramAcceptFilter")

        self.verticalLayout_26.addWidget(self.diagramAcceptFilter)

        self.diagramClearFilter = QPushButton(self.groupBox_18)
        self.diagramClearFilter.setObjectName(u"diagramClearFilter")

        self.verticalLayout_26.addWidget(self.diagramClearFilter)


        self.gridLayout_25.addWidget(self.groupBox_18, 1, 0, 3, 1)

        self.groupBox_17 = QGroupBox(self.widget_12)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(400, 0))
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, -1)
        self.diagramTasksCountChartView = QChartView(self.groupBox_17)
        self.diagramTasksCountChartView.setObjectName(u"diagramTasksCountChartView")

        self.verticalLayout_34.addWidget(self.diagramTasksCountChartView)


        self.gridLayout_25.addWidget(self.groupBox_17, 0, 2, 3, 2)

        self.groupBox_20 = QGroupBox(self.widget_12)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setMaximumSize(QSize(300, 70))
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.diagramPercentFinalTask = QLabel(self.groupBox_20)
        self.diagramPercentFinalTask.setObjectName(u"diagramPercentFinalTask")
        font1 = QFont()
        font1.setPointSize(14)
        self.diagramPercentFinalTask.setFont(font1)
        self.diagramPercentFinalTask.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.diagramPercentFinalTask)


        self.gridLayout_25.addWidget(self.groupBox_20, 1, 1, 2, 1)


        self.verticalLayout_17.addWidget(self.widget_12)

        icon5 = QIcon()
        icon5.addFile(u":/res/res/data-analytics.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tabWidget.addTab(self.tab_9, icon5, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(MainForm)

        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        self.chatWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"\u041c\u0443\u043b\u044c\u0442\u0438\u0432\u0435\u043d\u0434\u043e\u0440\u043d\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.label_59.setText(QCoreApplication.translate("MainForm", u"id", None))
        self.label_61.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_65.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.label_60.setText(QCoreApplication.translate("MainForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_66.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_58.setText(QCoreApplication.translate("MainForm", u"\u0418\u043c\u044f", None))
        self.label_62.setText(QCoreApplication.translate("MainForm", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_64.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0441\u0442\u0443\u043f", None))
        self.label_67.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.updateProfileBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_68.setText(QCoreApplication.translate("MainForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), QCoreApplication.translate("MainForm", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
        ___qtablewidgetitem = self.WorkStatusTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem1 = self.WorkStatusTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.WorkStatusTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0441\u0442\u0443\u043f", None));
        ___qtablewidgetitem3 = self.WorkStatusTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.acceptFilterWorkStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.inactiveWorkStatusCheckBOx.setText(QCoreApplication.translate("MainForm", u"\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.activeWorkStatusCheckBox.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.createWorkStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.updateWorkStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainForm", u"\u0418\u043c\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.acceptFilterEmployeeBtn.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lastnameEdit.setPlaceholderText("")
        self.firstnameEdit.setPlaceholderText("")
        self.inactiveEmployeeCheckBox.setText(QCoreApplication.translate("MainForm", u"\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u0435\u043d", None))
        self.activeEmployeeCheckBox.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u0435\u043d", None))
        self.label_6.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.createEmployeeBtn.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.updateEmployeeBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem4 = self.EmployeeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem5 = self.EmployeeTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem6 = self.EmployeeTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainForm", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem7 = self.EmployeeTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem8 = self.EmployeeTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem9 = self.EmployeeTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem10 = self.EmployeeTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None));
        ___qtablewidgetitem11 = self.EmployeeTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem12 = self.EmployeeTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u0435\u043d", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainForm", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_1), "")
        ___qtablewidgetitem13 = self.CompanyTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem14 = self.CompanyTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem15 = self.CompanyTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem16 = self.CompanyTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.acceptFilterCompanyBtn.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.inactiveCompanyCheckBox.setText(QCoreApplication.translate("MainForm", u"\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.activeCompanyCheckBox.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.label_8.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem17 = self.addressTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem18 = self.addressTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainForm", u"\u0423\u043b\u0438\u0446\u0430", None));
        ___qtablewidgetitem19 = self.addressTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u043c", None));
        ___qtablewidgetitem20 = self.addressTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem21 = self.addressTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None));
        self.createCompanyBtn.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.updateCompanyBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.acceptWorkPlanFilterBtn.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_26.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.label_24.setText(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f", None))
        self.label_25.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439", None))
        self.label_27.setText(QCoreApplication.translate("MainForm", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.sendMessageToEmployeeBtn.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.chatWidget.setTabText(self.chatWidget.indexOf(self.tab_14), QCoreApplication.translate("MainForm", u"\u0427\u0430\u0442 \u0441 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u043c", None))
        self.sendMesageToClientBtn.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.chatWidget.setTabText(self.chatWidget.indexOf(self.tab_15), QCoreApplication.translate("MainForm", u"\u0427\u0430\u0442 \u0441 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u043c", None))
        ___qtablewidgetitem22 = self.WorkPlanTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem23 = self.WorkPlanTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem24 = self.WorkPlanTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None));
        ___qtablewidgetitem25 = self.WorkPlanTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439", None));
        ___qtablewidgetitem26 = self.WorkPlanTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainForm", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem27 = self.WorkPlanTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None));
        ___qtablewidgetitem28 = self.WorkPlanTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), QCoreApplication.translate("MainForm", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainForm", u"\u0417\u0430\u044f\u0432\u043a\u0430", None))
        self.label_39.setText(QCoreApplication.translate("MainForm", u"IP Management Interface ", None))
        self.label_40.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label_41.setText(QCoreApplication.translate("MainForm", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.nonOperationalApplicationCheckBox.setText(QCoreApplication.translate("MainForm", u"\u041e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u043d\u0435\u0440\u0430\u0431\u043e\u0442\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e ", None))
        self.label_42.setText(QCoreApplication.translate("MainForm", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u0430", None))
        self.label_44.setText(QCoreApplication.translate("MainForm", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_38.setText(QCoreApplication.translate("MainForm", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_43.setText(QCoreApplication.translate("MainForm", u"\u041b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438 ", None))
        self.label_35.setText(QCoreApplication.translate("MainForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_31.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.label_32.setText(QCoreApplication.translate("MainForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_37.setText(QCoreApplication.translate("MainForm", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.label_34.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_30.setText(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f", None))
        self.label_33.setText(QCoreApplication.translate("MainForm", u"\u0418\u043c\u044f", None))
        self.label_36.setText(QCoreApplication.translate("MainForm", u"Email", None))
        self.label_56.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainForm", u"\u041f\u043b\u0430\u043d \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_47.setText(QCoreApplication.translate("MainForm", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainForm", u"\u0418\u043d\u0436\u0435\u043d\u0435\u0440 ", None))
        self.label_52.setText(QCoreApplication.translate("MainForm", u"id", None))
        self.label_53.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_54.setText(QCoreApplication.translate("MainForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_55.setText(QCoreApplication.translate("MainForm", u"\u0418\u043c\u044f", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439", None))
        self.label_45.setText(QCoreApplication.translate("MainForm", u"id", None))
        self.label_50.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_46.setText(QCoreApplication.translate("MainForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_49.setText(QCoreApplication.translate("MainForm", u"\u0418\u043c\u044f", None))
        self.label_57.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430", None))
        self.isagreedCheckBox.setText(QCoreApplication.translate("MainForm", u"\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u043e", None))
        ___qtablewidgetitem29 = self.ZipTableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem30 = self.ZipTableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainForm", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem31 = self.ZipTableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem32 = self.ZipTableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainForm", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None));
        ___qtablewidgetitem33 = self.ZipTableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043b-\u0432\u043e", None));
        ___qtablewidgetitem34 = self.ZipTableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainForm", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem35 = self.ZipTableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430", None));
        self.label_48.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.updateWorkPlanBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), QCoreApplication.translate("MainForm", u"\u041f\u043b\u0430\u043d \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label_11.setText(QCoreApplication.translate("MainForm", u"\u0422\u0438\u043f", None))
        self.label_9.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.acceptFilterWorkStatusBtn_3.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_12.setText(QCoreApplication.translate("MainForm", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_14.setText(QCoreApplication.translate("MainForm", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.createZipBtn.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.updateZipBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem36 = self.ZipTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem37 = self.ZipTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainForm", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem38 = self.ZipTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem39 = self.ZipTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainForm", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None));
        ___qtablewidgetitem40 = self.ZipTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainForm", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem41 = self.ZipTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainForm", u"\u0417\u0418\u041f", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label_22.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.acceptFilterPriorityBtn.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.activePriorityBtn.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.inactivePriorityBtn.setText(QCoreApplication.translate("MainForm", u"\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.priorityLineEdit.setPlaceholderText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.addPriorityBtn.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.updatePriorityBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem42 = self.PriorityTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem43 = self.PriorityTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem44 = self.PriorityTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label_23.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.acceptFilterWorkPlanStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.activeWorkPlanStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.inactiveWorkPlanStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.workPlanStatusLineEdit.setPlaceholderText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.addWorkPlanStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.updateWorkPlanStatusBtn.setText(QCoreApplication.translate("MainForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem45 = self.WorkPlanStatusTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem46 = self.WorkPlanStatusTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem47 = self.WorkPlanStatusTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainForm", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("MainForm", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), "")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0443", None))
        self.label_10.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430", None))
        self.label_13.setText(QCoreApplication.translate("MainForm", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.diagramDateFilterCheckBox.setText(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u0441\u0442\u0440\u043e\u0433\u043e \u043f\u043e \u0434\u0430\u0442\u0430\u043c", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainForm", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043f\u043b\u0430\u043d\u0430 ", None))
        self.label_7.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainForm", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0435\u043d\u043e", None))
        self.label_17.setText(QCoreApplication.translate("MainForm", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainForm", u"\u0417\u0418\u041f", None))
        ___qtablewidgetitem48 = self.diagramZipTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem49 = self.diagramZipTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainForm", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem50 = self.diagramZipTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem51 = self.diagramZipTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainForm", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None));
        ___qtablewidgetitem52 = self.diagramZipTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainForm", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem53 = self.diagramZipTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainForm", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043e", None));
        self.groupBox_18.setTitle(QCoreApplication.translate("MainForm", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430\u043c ", None))
        self.label_15.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_16.setText(QCoreApplication.translate("MainForm", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))
        ___qtablewidgetitem54 = self.diagramEmployeeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainForm", u"id", None));
        ___qtablewidgetitem55 = self.diagramEmployeeTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem56 = self.diagramEmployeeTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainForm", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem57 = self.diagramEmployeeTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem58 = self.diagramEmployeeTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainForm", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None));
        self.diagramAcceptFilter.setText(QCoreApplication.translate("MainForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.diagramClearFilter.setText(QCoreApplication.translate("MainForm", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainForm", u"\u041a\u043e\u043b-\u0432\u043e \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainForm", u"% \u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u043f\u043b\u0430\u043d\u0430", None))
        self.diagramPercentFinalTask.setText(QCoreApplication.translate("MainForm", u"90%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), "")
    # retranslateUi

