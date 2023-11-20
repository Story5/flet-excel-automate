import flet as ft


def main(page: ft.Page):
    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
    page.update()
    page.add(ft.ElevatedButton("Choose files...",
                               on_click=lambda _: file_picker.pick_files(allow_multiple=True)))


ft.app(target=main)
