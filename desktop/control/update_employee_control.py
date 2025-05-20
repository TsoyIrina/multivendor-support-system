from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget

from api import update_resource
from design.update_employee_form import Ui_UpdateEmployeeForm


class UpdateEmployeeFormControl(Ui_UpdateEmployeeForm, QWidget):
    def __init__(self, employee, main_form):
        super().__init__()
        self.employee = employee
        self.main_form = main_form
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)
        self.fill()

    def connect_ui(self):
        self.updateBtn.clicked.connect(self.update)

    def fill(self):
        self.idProfileEdit.setText(f'{self.employee.get('id')}')
        self.workStatusProfileEdit.setText(self.employee.get('work_status').get('name'))
        date_joined = self.employee.get('date_joined')
        self.dateJoinedProfileEdit.setDate(QDate.fromString(date_joined, "yyyy-MM-dd"))
        self.lastnameProfileEdit.setText(self.employee.get('user').get('last_name'))
        self.firstnameProfileEdit.setText(self.employee.get('user').get('first_name'))
        self.patronymicProfileEdit.setText(self.employee.get('patronymic'))
        self.usernameProfileEdit.setText(self.employee.get('user').get('username'))
        self.permissionProfileEdit.setText(
            'Полный' if self.employee.get('user').get('is_super_user') else 'Частичный')
        birthdate = self.employee.get('birthdate')
        self.birthdateProfileEdit.setDate(QDate.fromString(birthdate, "yyyy-MM-dd"))
        self.phoneProfileEdit.setText(self.employee.get('phone'))

    def update(self):
        data = {
                "user": {
                    "username": self.usernameProfileEdit.text(),
                    "last_name": self.lastnameProfileEdit.text(),
                    "first_name": self.firstnameProfileEdit.text(),
                    "is_active": True,
                    "is_superuser": self.employee.get('work_status').get('permission')
                },
                "patronymic": self.patronymicProfileEdit.text(),
                "work_status": self.employee.get('work_status').get('id'),
                "birthdate": self.birthdateProfileEdit.date().toString('yyyy-MM-dd'),
                "phone": self.phoneProfileEdit.text()
        }
        response = update_resource('employee', self.employee.get('id'), data=data)
        if response['is_ok'] and response['response'].status_code == 200:
            self.main_form.current_user = response['response'].json()['post']
            self.main_form.show_profile()
            self.close()
        else:
            self.errorLbl.setText(response['response'])
