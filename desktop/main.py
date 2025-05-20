import sys

from PySide6.QtWidgets import QApplication

from control.auth_control import AuthFormControl
from control.main_control import MainFormControl

if __name__ == '__main__':
    app = QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('Fusion')
    control = AuthFormControl()
    control.show()
    status = app.exec()
    sys.exit(status)
