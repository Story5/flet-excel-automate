import flet as ft
import openpyxl


class SXApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.title = '请选择库存码单excel'
        self.filePicker = ft.FilePicker(on_result=self.pick_files_result)
        self.tonInput = ft.TextField(
            label='请输入需要配货的吨数',
            keyboard_type=ft.KeyboardType.NUMBER
        )
        self.typeRadio = ft.RadioGroup(
            value=0,
            content=ft.Row([
                ft.Radio(value=0, label='同仓库配货'),
                ft.Radio(value=1, label='交叉换货'),
            ])
        )
        self.sixCheckbox = ft.Checkbox(
            label='换60%的货',
            value=False,
        )
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
        self.user_input = ft.Column([
            ft.Row([
                ft.Text('配货吨数'),
                self.tonInput,
            ]),
            ft.Row([
                ft.Text('换货方式'),
                self.typeRadio,
                self.sixCheckbox,
            ])
        ]
        )
        self.excel_view = ft.Column(
            visible=False,
            controls=[
                self.user_input,
            ]
        )

        self.view = ft.Column([
            self.choose_excel_button,
            self.excel_view,
        ])
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

        self.choose_excel_button.visible = False
        self.excel_view.visible = True
        self.view.update()

        self.sheets_tab = ft.Tabs(
            tabs=[ft.Tab(sheet)
                  for sheet in self.wb.sheetnames],
            scrollable=True,
            on_change=self.on_tabs_change
        )
        self.excel_view.controls.append(self.sheets_tab)
        self.excel_view.update()

    def on_tabs_change(self, e):
        sheet_str = self.sheets_tab.tabs[self.sheets_tab.selected_index].text
        sheetObj = self.wb[sheet_str]
        print('on_tabs_change:', sheetObj.title)
