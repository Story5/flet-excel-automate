import flet as ft
import openpyxl


def get_size(size):
    units = ['Bytes', 'KB', 'MB', 'GB']
    for i in range(len(units)):
        if size < 1024:
            size_str = '%.f' % size + units[i]
            return size_str
        size = size / 1024


def main(page: ft.Page):
    wb = None
    dialog_title = '请选择库存码单excel'
    xlsx_file_path = ''

    def pick_files_result(e: ft.FilePickerResultEvent):
        if len(e.files) > 0:
            file_picker_file = e.files[0]
            selected_files.value = f'{file_picker_file.name}({get_size(file_picker_file.size)})'
            print(file_picker_file.path)
            xlsx_file_path = file_picker_file.path
            wb = openpyxl.load_workbook(xlsx_file_path)
            print(wb.active)

        else:
            selected_files.value = '已取消'
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    dialog_title,
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allowed_extensions=['xlsx'],
                        allow_multiple=False,
                        dialog_title=dialog_title
                    ),
                ),
                selected_files,
            ]
        )
    )


ft.app(target=main)
