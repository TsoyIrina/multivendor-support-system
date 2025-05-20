from PySide6.QtWidgets import QWidget

from api import update_resource, delete_resource, get_resource
from design.update_only_name_form import Ui_UpdateOnlyNameForm


class UpdateOnlyNameFormControl(Ui_UpdateOnlyNameForm, QWidget):
    def __init__(self, object, main_form, title, endpoint):
        super().__init__()
        self.object = object
        self.main_form = main_form
        self.title = title
        self.endpoint = endpoint
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)
        self.fill()
        self.titleLbl.setText(f'{self.title}')

    def connect_ui(self):
        self.updateBtn.clicked.connect(self.update_object)
        self.deleteBtn.clicked.connect(self.delete_object)

    def fill(self):
        self.nameLineEdit.setText(self.object.get('name'))
        if self.endpoint == 'company':
            self.updateBtn.hide()

    def update_object(self):
        data = {
            "name": self.nameLineEdit.text(),
            "is_active": True
        }
        response = update_resource(self.endpoint, self.object.get('id'), data=data)
        if response['is_ok']:
            self.main_form.show_table_with_name(self.main_form.PriorityTableWidget, 'priority')
            self.main_form.show_table_with_name(self.main_form.WorkPlanStatusTableWidget, 'work_plan_status')
            self.close()
        else:
            self.errorLbl.setText(response['response'])

    def delete_object(self):
        response = delete_resource(self.endpoint, self.object.get('id'))
        if response['is_ok']:
            self.main_form.show_table_with_name(self.main_form.PriorityTableWidget, 'priority')
            self.main_form.show_table_with_name(self.main_form.WorkPlanStatusTableWidget, 'work_plan_status')
            self.main_form.show_company()
            self.close()
        else:
            self.errorLbl.setText(response['response'])
