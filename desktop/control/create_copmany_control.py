from PySide6.QtWidgets import QWidget

from api import create_resource
from design.create_company import Ui_CreateCompanyForm


class CreateCompanyControl(Ui_CreateCompanyForm, QWidget):
    def __init__(self, main_form):
        super().__init__()
        self.main_form = main_form
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)

    def connect_ui(self):
        self.createBtn.clicked.connect(self.create_object)

    def create_object(self):
        data = {
            "user": {
                "username": self.usernameCompanyEdit.text(),
                "password": self.passwordCompanyEdit.text(),
                "is_active": True,
                "is_superuser": False
            },
            "name": self.nameCompanyEdit.text()
        }
        response = create_resource('company', data=data)
        if response['is_ok']:
            self.main_form.show_company()
            self.close()
        else:
            self.errorLbl.setText(response['response'])
