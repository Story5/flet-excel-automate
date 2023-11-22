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
        self.text = ft.Text()
        return ft.Row([
            ft.ElevatedButton(
                text=self.buttonText,
                icon=ft.icons.UPLOAD_FILE,
                on_click=self.on_click_choose_excel,
            ),
            self.text,
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
            self.text.value = file_picker_file.name
            self.update()
            self.on_result_path(file_picker_file.path)
