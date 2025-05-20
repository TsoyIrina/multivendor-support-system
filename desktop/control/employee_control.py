from PySide6.QtWidgets import QWidget

from api import create_resource, delete_resource, get_resource, update_resource
from design.employee_form import Ui_EmployeeForm


class EmployeeControl(Ui_EmployeeForm, QWidget):
    def __init__(self, main_form, title, work_status, employee=None):
        super().__init__()
        self.main_form = main_form
        self.title_str = title
        self.work_statuses = work_status
        self.employee = employee
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)
        self.title.setText(self.title_str)
        self.fill()

    def connect_ui(self):
        self.saveBtn.clicked.connect(self.save_object)
        self.deleteBtn.clicked.connect(self.delete_object)

    def fill(self):
        for work_status in self.work_statuses:
            self.workStatusBox.addItem(work_status['name'], work_status['id'])
        if self.employee is None:
            self.deleteBtn.hide()
        else:
            self.passwordEdit.hide()
            self.birthdateDateEdit.hide()
            self.phoneEdit.hide()
            self.label_24.hide()
            self.label_22.hide()
            self.label_27.hide()
            self.usernameEdit.setReadOnly(True)
            self.lastnameEdit.setReadOnly(True)
            self.firstnameEdit.setReadOnly(True)
            self.patronymicEdit.setReadOnly(True)
            self.loginLbl.setText('id')
            self.usernameEdit.setText(self.employee['id'])
            self.lastnameEdit.setText(self.employee['last_name'])
            self.firstnameEdit.setText(self.employee['first_name'])
            self.patronymicEdit.setText(self.employee['patronymic'])
            self.workStatusBox.setCurrentText(self.employee['work_status'])
    def save_object(self):
        if self.employee is None:
            self.create_object()
        else:
            self.update_object()

    def create_object(self):
        data = {
            "user": {
                "username": self.usernameEdit.text(),
                "password": self.passwordEdit.text(),
                "last_name": self.lastnameEdit.text(),
                "first_name": self.firstnameEdit.text(),
                "is_active": True,
                "is_superuser": False
            },
            "patronymic": self.patronymicEdit.text(),
            "work_status": self.workStatusBox.currentData(),
            "birthdate": self.birthdateDateEdit.date().toString('yyyy-MM-dd'),
            "phone": self.phoneEdit.text()
        }
        response = create_resource('employee', data=data)
        if response['is_ok']:
            self.main_form.show_employee()
            self.close()
        else:
            self.errorLbl.setText(response['response'])

    def update_object(self):
        employee = get_resource('employee', self.employee['id'])['response'].json()
        data = {
            "user": {
                "username": employee['user']['username'],
                "last_name": employee['user']['last_name'],
                "first_name": employee['user']['first_name'],
                "is_active": True,
                "is_superuser": False
            },
            "patronymic": employee['patronymic'],
            "work_status": self.workStatusBox.currentData(),
            "birthdate": employee['birthdate'],
            "phone": employee['phone']
        }
        response = update_resource('employee',self.employee['id'], data=data)
        if response['is_ok']:
            self.main_form.show_employee()
            self.close()
        else:
            self.errorLbl.setText(response['response'])

    def delete_object(self):
        response = delete_resource('employee', self.employee.get('id'))
        if response['is_ok']:
            self.main_form.show_employee()
            self.close()
        else:
            self.errorLbl.setText(response['response'])
