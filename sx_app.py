import flet as ft
import openpyxl


class SXApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.title = '请选择库存码单excel'
        self.filePicker = ft.FilePicker(on_result=self.pick_files_result)
        self.page.overlay.append(self.filePicker)

    def build(self):
        self.view = ft.ElevatedButton(
            self.title,
            icon=ft.icons.UPLOAD_FILE,
            on_click=self.on_click_choose_excel,
        )
        return self.view

    def on_click_choose_excel(self, e):
        self.filePicker.pick_files(
            allowed_extensions=['xlsx'],
            allow_multiple=False,
            dialog_title=self.title
        )

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if len(e.files) > 0:
            file_picker_file = e.files[0]
            print(file_picker_file.path)
            xlsx_file_path = file_picker_file.path
            wb = openpyxl.load_workbook(xlsx_file_path)
            print(wb.active)
