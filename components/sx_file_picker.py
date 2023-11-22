import flet as ft


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
        return ft.Column([
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

    def on_click_choose_excel(self, e):
        self.filePicker.pick_files(
            allowed_extensions=['xlsx'],
            allow_multiple=False,
            dialog_title=self.buttonText
        )

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if len(e.files) > 0:
            file_picker_file = e.files[0]
            self.excel_name.value = file_picker_file.name
            self.excel_path.value = f'文件路径:{file_picker_file.path}'
            self.update()
            self.on_result_path(file_picker_file.path)
