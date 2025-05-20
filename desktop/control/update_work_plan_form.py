from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget

from api import get_all_resources, create_resource, update_resource, get_resource, delete_resource
from design.update_work_plan_form import Ui_updateWorkPlanForm


class UpdateWorkPlanFormControl(Ui_updateWorkPlanForm, QWidget):
    def __init__(self, work_plan_id, main_form, work_statuses, statuses):
        super().__init__()
        self.work_plan_id = work_plan_id
        self.main_form = main_form
        self.work_statuses = work_statuses
        self.statuses = statuses
        self.work_plan = None
        self.employee = None
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)
        self.fill_combo_box()
        self.fill()

    def connect_ui(self):
        self.updateWorkPlanBtn.clicked.connect(self.update_object)
        self.workStatusResponsibleBox.currentIndexChanged.connect(
            lambda: self.fill_employee(self.workStatusResponsibleBox, self.employeeResponsibleBox))
        self.workStatusEngineerBox.currentIndexChanged.connect(
            lambda: self.fill_employee(self.workStatusEngineerBox, self.employeeEngineerBox))
        self.zipComboBox.currentIndexChanged.connect(self.unit_change)

    def fill(self):
        self.work_plan = get_resource('work_plan', self.work_plan_id)['response'].json()
        if self.work_plan['responsible'] is not None:
            self.workStatusResponsibleBox.setCurrentIndex(
                self.workStatusResponsibleBox.findData(self.work_plan['responsible']['work_status']['id']))
            self.fill_employee(self.workStatusResponsibleBox, self.employeeResponsibleBox)
            self.employeeResponsibleBox.setCurrentIndex(
                self.employeeResponsibleBox.findData(self.work_plan['responsible']['id']))
        if self.work_plan['engineer'] is not None:
            self.workStatusEngineerBox.setCurrentIndex(
                self.workStatusEngineerBox.findData(self.work_plan['engineer']['work_status']['id']))
            self.fill_employee(self.workStatusEngineerBox, self.employeeEngineerBox)
            self.employeeEngineerBox.setCurrentIndex(
                self.employeeEngineerBox.findData(self.work_plan['engineer']['id']))
        if self.work_plan['status'] is not None:
            self.statusBox.setCurrentIndex(
                self.statusBox.findData(self.work_plan['status']['id']))
        self.startDateEdit.setDate(QDate.fromString(self.work_plan['start_date'], "yyyy-MM-dd"))
        self.endDateEdit.setDate(QDate.fromString(self.work_plan['end_date'], "yyyy-MM-dd"))
        self.tasksTextEdit.setText(self.work_plan['tasks'])
        self.notesTextEdit.setText(self.work_plan['notes'])

    def unit_change(self):
        self.unitZipEdit.setText(self.zipComboBox.currentData()['unit'])

    def fill_combo_box(self):
        self.employee = [_ for _ in get_all_resources('employee')['response'].json() if _['user']['is_active']]
        for work_status in self.work_statuses:
            self.workStatusResponsibleBox.addItem(work_status['name'], work_status['id'])
            self.workStatusEngineerBox.addItem(work_status['name'], work_status['id'])

        for status in self.statuses:
            self.statusBox.addItem(status['name'], status['id'])

        self.fill_employee(self.workStatusResponsibleBox, self.employeeResponsibleBox)
        self.fill_employee(self.workStatusEngineerBox, self.employeeEngineerBox)
        self.fill_zip()

    def fill_zip(self):
        zip_resources = [_ for _ in get_all_resources('zip')['response'].json() if _['is_active']]
        for zip in zip_resources:
            self.zipComboBox.addItem(f'[арт. {zip['article_number']}]  {zip['type']} {zip['name']}',
                                     {'id': zip['id'], 'unit': zip['unit']})

    def fill_employee(self, work_status_box, employee_box):
        employee_box.clear()
        work_status_id = work_status_box.currentData()
        employees = [_ for _ in self.employee if _['work_status']['id'] == work_status_id]
        for employee in employees:
            employee_box.addItem(
                f'[{employee['id']}] {employee['user']['last_name']} {employee['user']['first_name']} {employee['patronymic']}',
                employee['id'])

    def update_object(self):
        zip_id = self.create_zip()
        zip_resources_id = [_['id'] for _ in self.work_plan['zip_resources']]
        if zip_id is not None:
            zip_resources_id.append(zip_id)
        data = {
            "id": self.work_plan['id'],
            "responsible_id": self.employeeResponsibleBox.currentData(),
            "engineer_id": self.employeeEngineerBox.currentData(),
            "status_id": self.statusBox.currentData(),
            "zip_resources_id": zip_resources_id,
            "start_date": self.startDateEdit.date().toString("yyyy-MM-dd"),
            "end_date": self.endDateEdit.date().toString("yyyy-MM-dd"),
            "tasks": self.tasksTextEdit.toPlainText(),
            "notes": self.notesTextEdit.toPlainText(),
            "is_agreed": self.work_plan['is_agreed']
        }
        response = update_resource('work_plan', self.work_plan_id, data=data)
        if response['is_ok']:
            if response['response'].status_code == 200:
                self.main_form.show_work_plan_detail()
                self.close()
            else:
                delete_resource('zip', zip_id)
        else:
            self.errorLbl.setText(response['response'])
            delete_resource('zip', zip_id)
        pass

    def create_zip(self):
        zip_id = self.zipComboBox.currentData()['id']
        data = {
            "zip_id": zip_id,
            "quantity": self.quantityZipEdit.text(),
        }
        response = create_resource('zip_object', data=data)
        if response['is_ok']:
            if response['response'].status_code == 201:
                zip_id = response['response'].json()['id']
                return zip_id
            else:
                return None
        else:
            self.errorLbl.setText(response['response'])
