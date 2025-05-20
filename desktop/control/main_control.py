from datetime import date

from PySide6 import QtWidgets, QtCore, QtCharts
from PySide6.QtCore import QDate, QTimer
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QCheckBox, QListWidgetItem, QLabel, QHBoxLayout, QLayout, \
    QVBoxLayout, QSpacerItem, QSizePolicy

from api import *
from control.create_copmany_control import CreateCompanyControl
from control.create_work_status_control import CreateWorkStatusControl
from control.employee_control import EmployeeControl
from control.update_employee_control import UpdateEmployeeFormControl
from control.update_only_name_control import UpdateOnlyNameFormControl
from control.update_work_plan_form import UpdateWorkPlanFormControl
from control.zip_control import ZipFormControl
from design.main_form import Ui_MainForm


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class MainFormControl(Ui_MainForm, QWidget):
    def __init__(self, current_user_response):
        super().__init__()
        self.current_user = current_user_response
        self.work_statuses = []
        self.priorities = []
        self.statuses = []
        self.work_plan_id = None
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def setup_ui(self):
        super().setupUi(self)
        self.table_widgets_custom()
        self.tab_choice(self.tabWidget.currentIndex())
        self.permission()

    def recurring_timer(self):
        self.show_chat()
        self.show_work_status()
        self.show_employee()
        self.fill_combobox()
        self.show_company()
        self.show_work_plan()
        self.fill_combobox()
        self.show_zip()
        self.show_table_with_name(self.PriorityTableWidget, 'priority')
        self.show_table_with_name(self.WorkPlanStatusTableWidget, 'work_plan_status')

    def connect_ui(self):
        self.tabWidget.currentChanged.connect(self.tab_choice)
        self.createWorkStatusBtn.clicked.connect(self.show_create_work_status)
        self.addPriorityBtn.clicked.connect(
            lambda: self.create_obj_with_name(self.priorityLineEdit, self.PriorityTableWidget, 'priority'))
        self.addWorkPlanStatusBtn.clicked.connect(
            lambda: self.create_obj_with_name(self.workPlanStatusLineEdit, self.WorkPlanStatusTableWidget,
                                              'work_plan_status'))
        self.CompanyTableWidget.itemSelectionChanged.connect(self.show_address)
        self.WorkPlanTableWidget.itemSelectionChanged.connect(self.show_work_plan_detail)
        self.WorkPlanTableWidget.itemSelectionChanged.connect(self.show_chat)
        self.acceptFilterWorkStatusBtn.clicked.connect(self.work_status_filter_accept)
        self.acceptFilterPriorityBtn.clicked.connect(self.priority_filter_accept)
        self.acceptFilterWorkPlanStatusBtn.clicked.connect(self.work_plan_status_filter_accept)
        self.updateProfileBtn.clicked.connect(self.show_update_profile_form)
        self.updateWorkStatusBtn.clicked.connect(self.show_update_work_status_form)
        self.updatePriorityBtn.clicked.connect(self.show_update_priority_form)
        self.updateWorkPlanStatusBtn.clicked.connect(self.show_update_work_plan_status_form)
        self.updateCompanyBtn.clicked.connect(self.show_update_company_form)
        self.acceptFilterCompanyBtn.clicked.connect(self.company_filter_accept)
        self.createCompanyBtn.clicked.connect(self.show_create_company_form)
        self.acceptFilterEmployeeBtn.clicked.connect(self.employee_filter_accept)
        self.createEmployeeBtn.clicked.connect(self.show_create_employee_form)
        self.updateEmployeeBtn.clicked.connect(self.show_update_employee_form)
        self.acceptWorkPlanFilterBtn.clicked.connect(self.work_plan_filter_accept)
        self.updateWorkPlanBtn.clicked.connect(self.show_update_work_plan_form)
        self.sendMesageToClientBtn.clicked.connect(
            lambda: self.send_message(self.messageToClientEdit, 'chat_with_client'))
        self.sendMessageToEmployeeBtn.clicked.connect(
            lambda: self.send_message(self.messageToEmployeeEdit, 'chat_with_employee'))
        self.createZipBtn.clicked.connect(self.create_zip_form)
        self.updateZipBtn.clicked.connect(self.update_zip_form)
        self.diagramStatusWorkComboBox.currentIndexChanged.connect(self.diagram_employee_filter_accept)
        self.diagramAcceptFilter.clicked.connect(self.diagram_date_filter_accept)
        self.diagramClearFilter.clicked.connect(self.diagram)

    def tab_choice(self, current_index_tab):
        match current_index_tab:
            case 0:
                self.show_profile()
            case 1:
                self.show_work_status()
                self.show_employee()
                self.fill_combobox()
            case 2:
                self.show_company()
            case 3:
                self.show_work_plan()
                self.fill_combobox()
            case 4:
                self.show_zip()
                self.show_table_with_name(self.PriorityTableWidget, 'priority')
                self.show_table_with_name(self.WorkPlanStatusTableWidget, 'work_plan_status')
            case 5:
                self.diagram()

    def diagram_date_filter_accept(self):
        start_date = self.diagramStartDate.date().toString("yyyy-MM-dd")
        end_date = self.diagramEndDate.date().toString("yyyy-MM-dd")
        row = self.diagramEmployeeTableWidget.currentRow()
        employee_id = int(self.diagramEmployeeTableWidget.item(row, 0).text()) if row != -1 else None
        date_check = self.diagramDateFilterCheckBox.isChecked()
        self.diagram(start_date=start_date, end_date=end_date, employee=employee_id, date_check=date_check)

    def diagram(self, start_date=None, end_date=None, employee=None, date_check=False):
        self.fill_combobox()
        self.show_employee(table_widget=self.diagramEmployeeTableWidget)
        res = get_all_resources('work_plan')
        if res['is_ok']:
            work_plans = res['response'].json()
            if start_date and end_date:
                if date_check:
                    work_plans = [_ for _ in work_plans if _['start_date'] >= start_date and _['end_date'] <= end_date]
                else:
                    work_plans = [_ for _ in work_plans if not (_['start_date'] >= end_date or _['end_date'] <= start_date)]

            if employee:
                work_plans = [_ for _ in work_plans if _['engineer']['id'] == employee or _['responsible']['id'] == employee]
            self.diagram_fill_tasks(work_plans)
            self.draw_bar_chart(work_plans)
            zips = sum([_['zip_resources'] for _ in work_plans], start=[])
            self.diagram_zip(zips)

    def draw_bar_chart(self, work_plans):
        series = QtCharts.QBarSeries()
        bar_set = QtCharts.QBarSet('Количество заявок')
        tasks_by_date = {}
        for work_plan in work_plans:
            date = f'{work_plan['application']['created_at'][:10]}'
            tasks_by_date.setdefault(date, 0)
            tasks_by_date[date] += 1

        for k in tasks_by_date.keys():
            bar_set.append(tasks_by_date[k])

        series.append(bar_set)
        series.setLabelsVisible()

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()

        axis = QtCharts.QBarCategoryAxis()
        axis.append(list(tasks_by_date.keys()))
        chart.setAxisX(axis)
        series.attachAxis(axis)

        self.diagramTasksCountChartView.setChart(chart)

    def diagram_zip(self, zips):
        zip_dict = {}
        for zip_id in zips:
            zip_dict.setdefault(f'{zip_id['zip']['id']}', {'zip': zip_id['zip'], 'quantity': 0})
            zip_dict[f'{zip_id['zip']['id']}']['quantity'] += zip_id['quantity']

        row_count = len(zip_dict)
        self.diagramZipTableWidget.setRowCount(row_count)
        for zip_id, i in zip(zip_dict.keys(), range(row_count)):
            self.diagramZipTableWidget.setItem(i, 0, QTableWidgetItem(f'{zip_dict[zip_id]['zip']['id']}'))
            self.diagramZipTableWidget.setItem(i, 1, QTableWidgetItem(f'{zip_dict[zip_id]['zip']['type']}'))
            self.diagramZipTableWidget.setItem(i, 2, QTableWidgetItem(f'{zip_dict[zip_id]['zip']['name']}'))
            self.diagramZipTableWidget.setItem(i, 3, QTableWidgetItem(f'{zip_dict[zip_id]['zip']['article_number']}'))
            self.diagramZipTableWidget.setItem(i, 4, QTableWidgetItem(f'{zip_dict[zip_id]['zip']['unit']}'))
            self.diagramZipTableWidget.setItem(i, 5, QTableWidgetItem(f'{zip_dict[zip_id]['quantity']}'))
            delegate = AlignDelegate(self.diagramZipTableWidget)
            self.diagramZipTableWidget.setItemDelegateForColumn(i, delegate)
            self.diagramZipTableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def diagram_employee_filter_accept(self):
        work_status = self.diagramStatusWorkComboBox.currentData()
        self.show_employee(work_status=work_status, table_widget=self.diagramEmployeeTableWidget)

    def diagram_fill_tasks(self, work_plans):
        final_tasks_count = len([_ for _ in work_plans if _['status']['name'] == 'Выполнено'])
        process_tasks_count = len(
            [_ for _ in work_plans if (_['status']['name'] != 'Выполнено') and (_['end_date'] or '' >= f'{date.today()}')])
        expire_tasks_count = len(
            [_ for _ in work_plans if (_['status']['name'] != 'Выполнено') and (_['end_date'] or '' < f'{date.today()}')])
        percent = f'{round(final_tasks_count / len(work_plans) * 100, 1) if len(work_plans) != 0 else 0}%'
        self.diagramFinalEdit.setText(f'{final_tasks_count}')
        self.diagramProcessEdit.setText(f'{process_tasks_count}')
        self.diagramExpireEdit.setText(f'{expire_tasks_count}')
        self.diagramPercentFinalTask.setText(percent)

    def create_zip_form(self):
        self.zip = ZipFormControl()
        self.zip.show()

    def update_zip_form(self):
        row = self.ZipTableWidget.currentRow()
        zip_id = self.ZipTableWidget.item(row, 0).text()
        self.zip = ZipFormControl(zip_id)
        self.zip.show()

    def show_chat(self):
        self.chatClientListWidget.clear()
        self.chatEmployeeListWidget.clear()
        response = get_all_resources('chat')
        if response['is_ok']:
            if response['response'].status_code == 200:
                row_index = self.WorkPlanTableWidget.currentRow()
                if row_index != -1:
                    id = self.WorkPlanTableWidget.item(row_index, 0).text()
                    self.work_plan_id = id
                    response = get_resource('work_plan', id)
                    if response['is_ok']:
                        if response['response'].status_code == 200:
                            res = response['response'].json()
                            if res.get('responsible') == self.current_user:
                                self.tab_14.show()
                                self.tab_15.show()
                                self.show_chat_with(res['chat_with_client'], self.chatClientListWidget)
                                self.show_chat_with(res['chat_with_employee'], self.chatEmployeeListWidget)
                            elif res.get('engineer') == self.current_user:
                                self.tab_14.show()
                                self.tab_15.show()
                                self.show_chat_with(res['chat_with_employee'], self.chatEmployeeListWidget)
                            else:
                                self.tab_14.hide()
                                self.tab_15.hide()

    def show_chat_with(self, chat, list_widget):
        for message in chat['message']:
            my_widget = QWidget()
            widget = QWidget()
            widget.setStyleSheet("background-color: rgb(245, 245, 245);")
            sender_txt = f'{message['sender']['last_name']} {message['sender']['first_name']}' if message['sender'][
                                                                                                      'last_name'] != "" else \
                message['sender']['username']
            sender = QLabel(sender_txt)
            sender.setStyleSheet('color: rgb(153, 153, 153); ')
            content = QLabel(message['content'])
            timestamp = QLabel(message['timestamp'][:19].replace('T', ' '))
            timestamp.setStyleSheet('color: rgb(153, 153, 153);')

            widgetLayout = QVBoxLayout()
            widgetLayout.addWidget(sender)
            widgetLayout.addWidget(content)
            widgetLayout.addWidget(timestamp)
            widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
            widget.setLayout(widgetLayout)

            my_layout = QHBoxLayout()

            if message['sender']['id'] == self.current_user['user']['id']:
                my_layout.addItem(QSpacerItem(20, 10, hData=QSizePolicy.Policy.Expanding))
                my_layout.addWidget(widget)
            else:
                my_layout.addWidget(widget)
                my_layout.addItem(QSpacerItem(20, 10, hData=QSizePolicy.Policy.Expanding))

            my_widget.setLayout(my_layout)

            itemN = QListWidgetItem()

            itemN.setSizeHint(my_widget.sizeHint())
            list_widget.addItem(itemN)
            list_widget.setItemWidget(itemN, my_widget)
        list_widget.scrollToBottom()

    def send_message(self, message_edit, chat):
        data = {
            'content': message_edit.text(),
            'sender_id': self.current_user['user']['id']
        }
        message_id = create_resource('message', data)['response'].json()['id']
        response = get_resource('work_plan', self.work_plan_id)
        chat = response['response'].json()[chat]
        messages_id = [_['id'] for _ in chat['message']]
        messages_id.append(message_id)
        data = {
            "messages_id": messages_id
        }
        update_resource('chat', chat['id'], data)
        self.show_chat()
        message_edit.clear()

    def permission(self):
        if not self.current_user['user']['is_superuser']:
            self.createEmployeeBtn.hide()
            self.updateEmployeeBtn.hide()
            self.createWorkStatusBtn.hide()
            self.updateWorkStatusBtn.hide()
            self.createCompanyBtn.hide()
            self.updateCompanyBtn.hide()
            self.groupBox_8.hide()
            self.updatePriorityBtn.hide()
            self.groupBox_10.hide()
            self.updateWorkPlanStatusBtn.hide()

    def show_update_work_plan_form(self):
        work_status = [_ for _ in self.work_statuses if _['is_active']]
        statuses = [_ for _ in self.statuses if _['is_active']]
        self.form = UpdateWorkPlanFormControl(self.work_plan_id, self, work_status, statuses)
        self.form.show()

    def work_plan_filter_accept(self):
        company = self.companyWorkPlanEdit.text()
        lastname = self.lastnameWorkPlanEdit.text()
        priority = self.priorityWorkPlanEdit.currentData()
        status = self.statusWorkPlanEdit.currentData()
        self.show_work_plan(company, lastname, priority, status)

    def show_create_employee_form(self):
        title = 'Добавление сотрудника'
        work_status = [_ for _ in self.work_statuses if _['is_active']]
        self.form = EmployeeControl(self, title, work_status)
        self.form.show()

    def show_update_employee_form(self):
        title = 'Изменение сотрудника'
        work_status = [_ for _ in self.work_statuses if _['is_active']]
        row = self.EmployeeTableWidget.currentRow()
        if row != -1:
            employee = {
                'id': self.EmployeeTableWidget.item(row, 0).text(),
                'last_name': self.EmployeeTableWidget.item(row, 1).text(),
                'first_name': self.EmployeeTableWidget.item(row, 2).text(),
                'patronymic': self.EmployeeTableWidget.item(row, 3).text(),
                'work_status': self.EmployeeTableWidget.item(row, 4).text(),
            }
            self.form = EmployeeControl(self, title, work_status, employee)
            self.form.show()

    def employee_filter_accept(self):
        work_status = self.WorkStatusBox.currentData()
        lastname = self.lastnameEdit.text()
        firstname = self.firstnameEdit.text()
        active = self.activeEmployeeCheckBox.isChecked()
        inactive = self.inactiveEmployeeCheckBox.isChecked()
        self.show_employee(lastname, firstname, work_status, active, inactive)

    def show_create_work_status(self):
        title = 'Добавление должности'
        self.form = CreateWorkStatusControl(self, title)
        self.form.show()

    def fill_combobox(self):
        self.show_work_status()
        self.show_table_with_name(self.PriorityTableWidget, 'priority')
        self.show_table_with_name(self.WorkPlanStatusTableWidget, 'work_plan_status')
        self.WorkStatusBox.clear()
        self.WorkStatusBox.addItem('Не выбран', -1)
        self.diagramStatusWorkComboBox.clear()
        self.diagramStatusWorkComboBox.addItem('Не выбран', -1)

        for obj in self.work_statuses:
            self.WorkStatusBox.addItem(obj['name'], obj['id'])
            self.diagramStatusWorkComboBox.addItem(obj['name'], obj['id'])

        self.priorityWorkPlanEdit.clear()
        self.priorityWorkPlanEdit.addItem('Не выбран', -1)
        for obj in self.priorities:
            self.priorityWorkPlanEdit.addItem(obj['name'], obj['id'])

        self.statusWorkPlanEdit.clear()
        self.statusWorkPlanEdit.addItem('Не выбран', -1)
        for obj in self.statuses:
            self.statusWorkPlanEdit.addItem(obj['name'], obj['id'])

    def show_create_company_form(self):
        self.create_company_form = CreateCompanyControl(self)
        self.create_company_form.show()

    def show_work_status(self, name_filter=None, active=True, inactive=True):
        response = get_all_resources('work_status')
        if response['is_ok']:
            if response['response'].status_code == 200:
                is_active = None if active == inactive else active
                res = [obj for obj in response['response'].json() if
                       (True if is_active is None else obj['is_active'] == is_active) and (name_filter or '') in obj[
                           'name']]
                self.work_statuses = response['response'].json()

                row_count = len(res)
                self.WorkStatusTableWidget.setRowCount(row_count)
                for i, work_status in enumerate(res):
                    self.WorkStatusTableWidget.setItem(i, 0, QTableWidgetItem(f'{work_status.get('id')}'))
                    self.WorkStatusTableWidget.setItem(i, 1, QTableWidgetItem(f'{work_status.get('name')}'))
                    perm = 'Полный' if work_status.get('permission') else 'Частичный'
                    self.WorkStatusTableWidget.setItem(i, 2, QTableWidgetItem(f'{perm}'))
                    check_box = QCheckBox('')
                    check_box.setChecked(work_status.get('is_active'))
                    self.WorkStatusTableWidget.setCellWidget(i, 3, check_box)
                    delegate = AlignDelegate(self.WorkStatusTableWidget)
                    self.WorkStatusTableWidget.setItemDelegateForColumn(i, delegate)

    def show_update_priority_form(self):
        row = self.PriorityTableWidget.currentRow()
        if row != -1:
            priority = {
                'id': self.PriorityTableWidget.item(row, 0).text(),
                'name': self.PriorityTableWidget.item(row, 1).text()
            }
            self.update_priority_form = UpdateOnlyNameFormControl(priority, self, 'Изменение приоритета', 'priority')
            self.update_priority_form.show()

    def show_update_company_form(self):
        row = self.CompanyTableWidget.currentRow()
        if row != -1:
            company = {
                'id': self.CompanyTableWidget.item(row, 0).text(),
                'name': self.CompanyTableWidget.item(row, 1).text()
            }
            self.update_form = UpdateOnlyNameFormControl(company, self, 'Изменение компании', 'company')
            self.update_form.show()

    def show_update_work_plan_status_form(self):
        row = self.WorkPlanStatusTableWidget.currentRow()
        if row != -1:
            work_plan_status = {
                'id': self.WorkPlanStatusTableWidget.item(row, 0).text(),
                'name': self.WorkPlanStatusTableWidget.item(row, 1).text()
            }
            self.update_form = UpdateOnlyNameFormControl(work_plan_status, self, 'Изменение статуса',
                                                         'work_plan_status')
            self.update_form.show()

    def show_update_work_status_form(self):
        row = self.WorkStatusTableWidget.currentRow()
        if row != -1:
            title = 'Изменение должности'
            work_status = {
                'id': self.WorkStatusTableWidget.item(row, 0).text(),
                'name': self.WorkStatusTableWidget.item(row, 1).text(),
                'permission': True if self.WorkStatusTableWidget.item(row, 2).text() == 'Полный' else False
            }
            self.form = CreateWorkStatusControl(self, title, work_status)
            self.form.show()

    def show_update_profile_form(self):
        self.update_employee = UpdateEmployeeFormControl(self.current_user, self)
        self.update_employee.show()

    def work_status_filter_accept(self):
        name_filter = self.nameWorkStatusEdit.text()
        active = self.activeWorkStatusCheckBox.isChecked()
        inactive = self.inactiveWorkStatusCheckBOx.isChecked()
        self.show_work_status(name_filter, active, inactive)

    def company_filter_accept(self):
        name_filter = self.nameCompanyFilterEdit.text()
        active = self.activeCompanyCheckBox.isChecked()
        inactive = self.inactiveCompanyCheckBox.isChecked()
        self.show_company(name_filter, active, inactive)

    def work_plan_status_filter_accept(self):
        name_filter = self.nameWorkPlanStatusEdit.text()
        active = self.activeWorkPlanStatusBtn.isChecked()
        inactive = self.inactiveWorkPlanStatusBtn.isChecked()
        self.show_table_with_name(self.WorkPlanStatusTableWidget, 'work_plan_status', name_filter, active, inactive)

    def priority_filter_accept(self):
        name_filter = self.namePriorityEdit.text()
        active = self.activePriorityBtn.isChecked()
        inactive = self.inactivePriorityBtn.isChecked()
        self.show_table_with_name(self.PriorityTableWidget, 'priority', name_filter, active, inactive)

    def show_profile(self):
        self.idProfileEdit.setText(f'{self.current_user.get('id')}')
        self.workStatusProfileEdit.setText(self.current_user.get('work_status').get('name'))
        date_joined = self.current_user.get('date_joined')
        self.dateJoinedProfileEdit.setDate(QDate.fromString(date_joined, "yyyy-MM-dd"))
        self.lastnameProfileEdit.setText(self.current_user.get('user').get('last_name'))
        self.firstnameProfileEdit.setText(self.current_user.get('user').get('first_name'))
        self.patronymicProfileEdit.setText(self.current_user.get('patronymic'))
        self.usernameProfileEdit.setText(self.current_user.get('user').get('username'))
        self.permissionProfileEdit.setText(
            'Полный' if self.current_user.get('user').get('is_super_user') else 'Частичный')
        birthdate = self.current_user.get('birthdate')
        self.birthdateProfileEdit.setDate(QDate.fromString(birthdate, "yyyy-MM-dd"))
        self.phoneProfileEdit.setText(self.current_user.get('phone'))

    def table_widgets_custom(self):
        self.work_status_table_widget(self.WorkStatusTableWidget)
        self.work_status_table_widget(self.EmployeeTableWidget)
        self.work_status_table_widget(self.addressTableWidget)
        self.work_status_table_widget(self.CompanyTableWidget)
        self.work_status_table_widget(self.ZipTableWidget)
        self.work_status_table_widget(self.PriorityTableWidget)
        self.work_status_table_widget(self.WorkPlanStatusTableWidget)
        self.work_status_table_widget(self.WorkPlanTableWidget)
        self.work_status_table_widget(self.ZipTableWidget_2)
        self.work_status_table_widget(self.diagramEmployeeTableWidget)
        self.work_status_table_widget(self.diagramZipTableWidget)

    def work_status_table_widget(self, table_widget):
        table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table_widget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

    def show_table_with_name(self, table_widget, path, name_filter=None, active=True, inactive=True):
        response = get_all_resources(path)
        if response['is_ok']:
            if response['response'].status_code == 200:
                if path == 'work_plan_status':
                    self.statuses = response['response'].json()
                elif path == 'priority':
                    self.priorities = response['response'].json()
                is_active = None if active == inactive else active
                res = [obj for obj in response['response'].json() if
                       (True if is_active is None else obj['is_active'] == is_active) and (name_filter or '') in obj[
                           'name']]
                row_count = len(res)
                table_widget.setRowCount(row_count)
                for i, work_status in enumerate(res):
                    table_widget.setItem(i, 0, QTableWidgetItem(f'{work_status.get('id')}'))
                    table_widget.setItem(i, 1, QTableWidgetItem(f'{work_status.get('name')}'))
                    check_box = QCheckBox('')
                    check_box.setChecked(work_status.get('is_active'))
                    table_widget.setCellWidget(i, 2, check_box)
                    delegate = AlignDelegate(table_widget)
                    table_widget.setItemDelegateForColumn(i, delegate)

    def create_obj_with_name(self, line_edit, table_widget, path):
        work_status_name = line_edit.text()
        data = {
            'name': work_status_name,
            'is_active': True
        }
        create_resource(path, data)
        line_edit.clear()
        self.show_table_with_name(table_widget, path)

    def show_employee(self, lastname=None, firstname=None, work_status=None, active=True, inactive=True,
                      table_widget=None, ):
        if table_widget is None:
            table_widget = self.EmployeeTableWidget
        response = get_all_resources('employee')
        if response['is_ok']:
            if response['response'].status_code == 200:
                is_active = None if active == inactive else active
                res = [obj for obj in response['response'].json() if
                       (True if is_active is None else obj['user']['is_active'] == is_active) and (firstname or '') in
                       obj['user'][
                           'first_name'] and (lastname or '') in obj['user'][
                           'last_name'] and (work_status == obj['work_status']['id'] or (work_status or -1) == -1)]
                row_count = len(res)
                table_widget.setRowCount(row_count)
                for i, item in zip(range(row_count), res):
                    table_widget.setItem(i, 0, QTableWidgetItem(f'{item.get('id')}'))
                    table_widget.setItem(i, 1, QTableWidgetItem(f'{item.get('user').get('last_name')}'))
                    table_widget.setItem(i, 2, QTableWidgetItem(f'{item.get('user').get('first_name')}'))
                    table_widget.setItem(i, 3, QTableWidgetItem(f'{item.get('patronymic')}'))
                    table_widget.setItem(i, 4, QTableWidgetItem(
                        f'{item.get('work_status').get('name')}'))
                    table_widget.setItem(i, 5, QTableWidgetItem(f'{item.get('birthdate')}'))
                    table_widget.setItem(i, 6, QTableWidgetItem(f'{item.get('phone')}'))
                    table_widget.setItem(i, 7, QTableWidgetItem(f'{item.get('date_joined')}'))
                    check_box = QCheckBox('')
                    check_box.setChecked(item.get('user').get('is_active'))
                    table_widget.setCellWidget(i, 8, check_box)
                    delegate = AlignDelegate(table_widget)
                    table_widget.setItemDelegateForColumn(i, delegate)

    def show_company(self, name_filter=None, active=True, inactive=True):
        response = get_all_resources('company')
        if response['is_ok']:
            if response['response'].status_code == 200:
                is_active = None if active == inactive else active
                res = [obj for obj in response['response'].json() if
                       (True if is_active is None else obj['user']['is_active'] == is_active) and (name_filter or '') in
                       obj[
                           'name']]
                row_count = len(res)
                self.CompanyTableWidget.setRowCount(row_count)
                for i, item in zip(range(row_count), res):
                    self.CompanyTableWidget.setItem(i, 0, QTableWidgetItem(f'{item.get('id')}'))
                    self.CompanyTableWidget.setItem(i, 1, QTableWidgetItem(f'{item.get('name')}'))
                    self.CompanyTableWidget.setItem(i, 2, QTableWidgetItem(f'{item.get('date_joined')}'))
                    check_box = QCheckBox('')
                    check_box.setChecked(item.get('user').get('is_active'))
                    self.CompanyTableWidget.setCellWidget(i, 3, check_box)
                    delegate = AlignDelegate(self.CompanyTableWidget)
                    self.CompanyTableWidget.setItemDelegateForColumn(i, delegate)

    def show_address(self):
        row_index = self.CompanyTableWidget.currentRow()
        current_company_id = self.CompanyTableWidget.item(row_index, 0).text()
        response = get_resource('company', current_company_id)
        if response['is_ok']:
            if response['response'].status_code == 200:
                res = response['response'].json().get('addresses')
                row_count = len(res)
                self.addressTableWidget.setRowCount(row_count)
                for i, item in zip(range(row_count), res):
                    self.addressTableWidget.setItem(i, 0, QTableWidgetItem(f'{item.get('id')}'))
                    self.addressTableWidget.setItem(i, 1, QTableWidgetItem(f'{item.get('street')}'))
                    self.addressTableWidget.setItem(i, 2, QTableWidgetItem(f'{item.get('house_number')}'))
                    self.addressTableWidget.setItem(i, 3, QTableWidgetItem(f'{item.get('created_date')}'))
                    check_box = QCheckBox('')
                    check_box.setChecked(item.get('is_active'))
                    self.addressTableWidget.setCellWidget(i, 4, check_box)
                    delegate = AlignDelegate(self.addressTableWidget)
                    self.addressTableWidget.setItemDelegateForColumn(i, delegate)

    def show_zip(self):
        response = get_all_resources('zip')
        if response['is_ok']:
            if response['response'].status_code == 200:
                res = response['response'].json()
                row_count = len(res)
                self.ZipTableWidget.setRowCount(row_count)
                for i, item in zip(range(row_count), res):
                    self.ZipTableWidget.setItem(i, 0, QTableWidgetItem(f'{item.get('id')}'))
                    self.ZipTableWidget.setItem(i, 1, QTableWidgetItem(f'{item.get('type')}'))
                    self.ZipTableWidget.setItem(i, 2, QTableWidgetItem(f'{item.get('name')}'))
                    self.ZipTableWidget.setItem(i, 3, QTableWidgetItem(f'{item.get('article_number')}'))
                    self.ZipTableWidget.setItem(i, 4, QTableWidgetItem(f'{item.get('unit')}'))
                    check_box = QCheckBox('')
                    check_box.setChecked(item.get('is_active'))
                    self.ZipTableWidget.setCellWidget(i, 5, check_box)

                    delegate = AlignDelegate(self.ZipTableWidget)
                    self.ZipTableWidget.setItemDelegateForColumn(i, delegate)

    def show_work_plan(self, company=None, lastname=None, priority=None, status=None, ):
        self.WorkPlanTableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        response = get_all_resources('work_plan')
        if response['is_ok']:
            if response['response'].status_code == 200:
                res = [obj for obj in response['response'].json()
                       if (company or '') in obj['application']['company']['name']
                       and (lastname or '') in (
                           obj['responsible']['user']['last_name'] if obj['responsible'] is not None else '')
                       and (priority == obj['application']['priority']['id'] or (priority or -1) == -1)
                       and (status == (obj['status']['id'] if obj['status'] is not None else '') or (
                            status or -1) == -1)]
                row_count = len(res)
                self.WorkPlanTableWidget.setRowCount(row_count)
                for i, item in zip(range(row_count), res):
                    self.WorkPlanTableWidget.setItem(i, 0, QTableWidgetItem(f'{item.get('id')}'))
                    self.WorkPlanTableWidget.setItem(i, 1, QTableWidgetItem(
                        f'{item.get('application').get('company').get('name')}'))
                    self.WorkPlanTableWidget.setItem(i, 2, QTableWidgetItem(
                        f'{item.get('application').get('priority').get('name')}'))
                    self.WorkPlanTableWidget.setItem(i, 3, QTableWidgetItem(
                        f'{item.get('responsible').get('user').get('last_name') if item['responsible'] is not None else ''}'))
                    self.WorkPlanTableWidget.setItem(i, 4, QTableWidgetItem(
                        f'{item.get('status').get('name') if item['status'] is not None else ''}'))
                    self.WorkPlanTableWidget.setItem(i, 5, QTableWidgetItem(f'{item.get('start_date', '-')}'))
                    self.WorkPlanTableWidget.setItem(i, 6, QTableWidgetItem(f'{item.get('end_date', '-')}'))
                    delegate = AlignDelegate(self.WorkPlanTableWidget)
                    self.WorkPlanTableWidget.setItemDelegateForColumn(i, delegate)

    def show_work_plan_detail(self):
        row_index = self.WorkPlanTableWidget.currentRow()
        id = self.WorkPlanTableWidget.item(row_index, 0).text()
        self.work_plan_id = id
        response = get_resource('work_plan', id)
        if response['is_ok']:
            if response['response'].status_code == 200:
                application = response['response'].json().get('application')
                self.companyApplicationEdit.setText(application.get('company').get('name'))
                self.createdApplicationEdit.setText(application.get('created_at')[:19])
                self.addressApplicationEdit.setText(
                    f'{application.get('address').get('street')}, {application.get('address').get('house_number')}')
                self.priorityApplicationEdit.setText(f'{application.get('priority').get('name')}')
                self.lastNameApplicationEdit.setText(f'{application.get('lastname')}')
                self.firstNameApplicationEdit.setText(f'{application.get('firstname')}')
                self.patronymicApplicationEdit.setText(f'{application.get('patronymic')}')
                self.emailApplicationEdit.setText(f'{application.get('email')}')
                self.phoneApplicationEdit.setText(f'{application.get('phone')}')
                self.serialNumberApplicationEdit.setText(f'{application.get('serial_number')}')
                self.equipmentNameApplicationEdit.setText(f'{application.get('equipment_name')}')
                self.locationApplicationEdit.setText(f'{application.get('location_in_room')}')
                self.IPApplicationEdit.setText(f'{application.get('ip_management_interface')}')
                self.nonOperationalApplicationCheckBox.setChecked(application.get('equipment_non_operational'))
                self.funcLimitedApplicationEdit.setText(f'{application.get('functionality_limited')}')
                self.logicalErrorsApplicationEdit.setText(f'{application.get('suspicion_of_logical_errors')}')
                self.descriptionApplicationEdit.setText(f'{application.get('fault_description')}')

                application = response['response'].json()
                if application.get('responsible') is not None:
                    self.idResponsibleLineEdit.setText(f'{application.get('responsible').get('user').get('id')}')
                    self.lastnameResponsibleLineEdit.setText(
                        f'{application.get('responsible').get('user').get('last_name')}')
                    self.firstnameResponsibleLineEdit.setText(
                        f'{application.get('responsible').get('user').get('first_name')}')
                    self.patronymicResponsibleLineEdit.setText(f'{application.get('responsible').get('patronymic')}')
                if application.get('responsible') is not None:
                    self.idSmartHandLineEdit.setText(f'{application.get('engineer').get('user').get('id')}')
                    self.lastnameSmartHandLineEdit.setText(
                        f'{application.get('engineer').get('user').get('last_name')}')
                    self.firstnameSmartHandLineEdit.setText(
                        f'{application.get('engineer').get('user').get('first_name')}')
                    self.patronymicSmartHandLineEdit.setText(
                        f'{application.get('engineer').get('patronymic')}')

                self.statusLineEdit.setText(
                    f'{application.get('status').get('name') if application.get('responsible') is not None else ''}')
                self.isagreedCheckBox.setChecked(application.get('is_agreed'))
                start_date = application.get('start_date')
                self.startDateEdit.setDate(QDate.fromString(start_date, "yyyy-MM-dd"))
                end_date = application.get('end_date')
                self.endDateEdit.setDate(QDate.fromString(end_date, "yyyy-MM-dd"))
                self.tasksTextEdit.setText(f'{application.get('tasks')}')
                self.notesTextEdit.setText(f'{application.get('notes')}')

                res = application['zip_resources']
                row_count = len(res)
                self.ZipTableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                self.ZipTableWidget_2.setRowCount(row_count)
                for i, item in zip(range(row_count), res):
                    self.ZipTableWidget_2.setItem(i, 0, QTableWidgetItem(f'{item.get('id')}'))
                    self.ZipTableWidget_2.setItem(i, 1, QTableWidgetItem(f'{item['zip']['type']}'))
                    self.ZipTableWidget_2.setItem(i, 2, QTableWidgetItem(f'{item['zip']['name']}'))
                    self.ZipTableWidget_2.setItem(i, 3, QTableWidgetItem(f'{item['zip']['article_number']}'))
                    self.ZipTableWidget_2.setItem(i, 4, QTableWidgetItem(f'{item.get('quantity')}'))
                    self.ZipTableWidget_2.setItem(i, 5, QTableWidgetItem(f'{item['zip']['unit']}'))
                    self.ZipTableWidget_2.setItem(i, 6, QTableWidgetItem(f'{item.get('created_at')}'))
