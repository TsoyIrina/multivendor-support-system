from PySide6.QtWidgets import QWidget

from api import create_resource, update_resource, delete_resource
from design.create_work_status import Ui_createWorkStatusForm


class CreateWorkStatusControl(Ui_createWorkStatusForm, QWidget):
    def __init__(self, main_form, title, work_status=None):
        super().__init__()
        self.main_form = main_form
        self.title = title
        self.work_status = work_status
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)
        self.label.setText(self.title)
        self.fill()

    def connect_ui(self):
        self.createBtn.clicked.connect(self.save_object)
        self.deleteBtn.clicked.connect(self.delete_object)

    def fill(self):
        if self.work_status is None:
            self.deleteBtn.hide()
        else:
            self.nameEdit.setText(self.work_status['name'])
            self.permissionCheckBox.setChecked(self.work_status['permission'])

    def save_object(self):
        if self.work_status is None:
            self.create_object()
        else:
            self.update_object()

    def create_object(self):
        data = {
            "name": self.nameEdit.text(),
            "is_active": True,
            "permission": self.permissionCheckBox.isChecked()
        }
        response = create_resource('work_status', data=data)
        if response['is_ok']:
            self.main_form.show_work_status()
            self.close()
        else:
            self.errorLbl.setText(response['response'])

    def update_object(self):
        data = {
            "name": self.nameEdit.text(),
            "is_active": True,
            "permission": self.permissionCheckBox.isChecked()
        }
        response = update_resource('work_status', self.work_status['id'], data=data)
        if response['is_ok']:
            self.main_form.show_work_status()
            self.close()
        else:
            self.errorLbl.setText(response['response'])

    def delete_object(self):
        response = delete_resource('work_status', self.work_status.get('id'))
        if response['is_ok']:
            self.main_form.show_work_status()
            self.close()
        else:
            self.errorLbl.setText(response['response'])
