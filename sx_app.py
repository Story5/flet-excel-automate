import flet as ft
import openpyxl


class SXSheetDataTable(ft.UserControl):
    def __init__(self, sheet: openpyxl.worksheet.worksheet.Worksheet):
        super().__init__()
        self.sheet = sheet
        self.max_row = self.sheet.max_row
        self.max_column = self.sheet.max_column

    def build(self):
        self.view = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(self.sheet.cell(row=1, column=column_index).value)) for column_index in range(1, self.sheet.max_column)
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(self.sheet.cell(row=row_index, column=column_index).value)) for column_index in range(1, self.sheet.max_column)
                ]) for row_index in range(2, self.sheet.max_row)
            ]
        )
        return self.view


class SXApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.title = '请选择库存码单excel'
        self.filePicker = ft.FilePicker(on_result=self.pick_files_result)
        self.page.overlay.append(self.filePicker)
        self.excel_path = None
        self.wb = None

    def build(self):
        self.choose_excel_button = ft.ElevatedButton(
            visible=True,
            text=self.title,
            icon=ft.icons.UPLOAD_FILE,
            on_click=self.on_click_choose_excel,
        )
        self.excel_view = ft.Column(
            visible=False,
        )

        self.view = ft.Column(
            controls=[
                self.choose_excel_button,
                self.excel_view,
            ]
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
            self.load_excel(file_picker_file.path)

    def load_excel(self, path):
        self.excel_path = path
        self.wb = openpyxl.load_workbook(path, data_only=True)
        self.sheet = self.wb.active
        print(type(self.sheet))

        self.choose_excel_button.visible = False
        self.excel_view.visible = True

        def on_tabs_change(e):
            sheet_str = self.sheets.tabs[self.sheets.selected_index].text
            sheet = self.wb[sheet_str]
            print('on_tabs_change:', sheet.title)
            self.on_sheet_change(sheet)

        self.sheets = ft.Tabs(
            tabs=[ft.Tab(sheet)
                  for sheet in self.wb.sheetnames],
            scrollable=True,
            on_change=on_tabs_change
        )
        self.on_sheet_change(self.sheet)

    def on_sheet_change(self, sheet: openpyxl.worksheet.worksheet.Worksheet):
        print('on_sheet_change:', sheet.title)
        self.excel_view.controls.clear()
        self.excel_view.controls.append(SXSheetDataTable(sheet))
        self.excel_view.controls.append(self.sheets)
        self.update()
