import flet as ft
import openpyxl


class SXFilePicker(ft.UserControl):
    def __init__(
            self,
            page: ft.Page,
            buttonText: str,
            on_result_path=None,
    ):
        super().__init__()
        self.page = page
        self.buttonText = buttonText
        self.on_result_path = on_result_path

        self.filePicker = ft.FilePicker(on_result=self.pick_files_result)
        self.page.overlay.append(self.filePicker)

    def build(self):
        self.excel_name = ft.Text()
        self.excel_path = ft.Text(color=ft.colors.GREY)
        self.view = ft.Column([
            ft.Row([
                ft.ElevatedButton(
                    text=self.buttonText,
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=self.on_click_choose_excel,
                ),
                self.excel_name,
            ]),
            self.excel_path,
        ])
        return self.view

    def on_click_choose_excel(self, e):
        self.filePicker.pick_files(
            allowed_extensions=['xlsx'],
            allow_multiple=False,
            dialog_title=self.buttonText
        )

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if len(e.files) > 0:
            file_picker_file = e.files[0]
            path = file_picker_file.path

            self.excel_name.value = file_picker_file.name
            self.excel_path.value = f'文件路径:{path}'
            self.view.update()

            self.on_result_path(path)
            self.load_excel(path)

    def load_excel(self, path: str):
        self.wb = openpyxl.load_workbook(path, data_only=True)

        self.sheets_tab = ft.Tabs(
            tabs=[ft.Tab(sheet) for sheet in self.wb.sheetnames],
            scrollable=True,
            on_change=self.on_tabs_change
        )
        self.view.controls.append(self.sheets_tab)
        self.view.update()

    def on_tabs_change(self, e):
        sheet_str = self.sheets_tab.tabs[self.sheets_tab.selected_index].text
        sheetObj = self.wb[sheet_str]
        print('on_tabs_change:', sheetObj.title)
