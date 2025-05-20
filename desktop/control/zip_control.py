from PySide6.QtWidgets import QWidget

from api import *
from design.zip_form import Ui_ZipForm


class ZipFormControl(Ui_ZipForm, QWidget):
    def __init__(self, zip_id=None):
        super().__init__()
        self.zip_id = zip_id
        self.setup_ui()
        self.res_form = None
        self.connect_ui()
        self.main_wnd = None

    def setup_ui(self):
        super().setupUi(self)
        self.fill()

    def connect_ui(self):
        self.saveZipBtn.clicked.connect(self.save_zip)
        self.deleteZipBtn.clicked.connect(self.delete_zip)

    def save_zip(self):
        if self.zip_id is None:
            self.create_zip()
        else:
            self.update_zip()

    def delete_zip(self):
        delete_resource('zip', self.zip_id)
        self.close()

    def fill(self):
        if self.zip_id is None:
            self.deleteZipBtn.hide()
        else:
            response = get_resource('zip', self.zip_id)
            if response['is_ok']:
                if response['response'].status_code == 200:
                    zip = response['response'].json()
                    self.typeZipEdit.setText(zip['type'])
                    self.nameZipEdit.setText(zip['name'])
                    self.articleZipEdit.setText(zip['article_number'])
                    self.unitZipEdit.setText(zip['unit'])

    def create_zip(self):
        data = {
            "type": self.typeZipEdit.text(),
            "name": self.nameZipEdit.text(),
            "article_number": self.articleZipEdit.text(),
            "unit": self.unitZipEdit.text(),
            "is_active": True
        }
        response = create_resource('zip', data=data)
        if response['is_ok']:
            if response['response'].status_code == 201:
                self.close()
            else:
                return None
        else:
            self.errorLbl.setText(response['response'])

    def update_zip(self):
        data = {
            "type": self.typeZipEdit.text(),
            "name": self.nameZipEdit.text(),
            "article_number": self.articleZipEdit.text(),
            "unit": self.unitZipEdit.text(),
            "is_active": True
        }
        response = update_resource('zip', self.zip_id, data=data)
        if response['is_ok']:
            if response['response'].status_code == 200:
                self.close()
            else:
                return None
        else:
            self.errorLbl.setText(response['response'])
