from PySide6.QtWidgets import QWidget

from api import authenticate, get_all_resources
from control.main_control import MainFormControl
from design.auth_form import Ui_AuthForm


class AuthFormControl(Ui_AuthForm, QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)

    def connect_ui(self):
        self.authBtn.clicked.connect(self.auth)

    def auth(self):
        login = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        # login = 'user2'
        # password = 'adminpass123'
        response = authenticate(login, password)
        if response['is_ok']:
            current_user_response = response['response']
            if 'ЦК' in current_user_response['work_status']['name']:
                self.main = MainFormControl(current_user_response)
                self.main.show()
                self.close()
            else:
                self.authErrorLbl.setText('Нет доступа')
        else:
            self.authErrorLbl.setText(response['response'])
