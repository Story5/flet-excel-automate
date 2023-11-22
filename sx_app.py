import flet as ft
import openpyxl
from components.sx_file_picker import SXFilePicker


class SXApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.stock_excel_path = ''
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
        self.excel_path = None
        self.wb = None

    def on_excel_path(self, path: str, type):
        print('on_excel_path:', path)
        if type == 0:  # 库存表
            print('库存表:',type)
        elif type == 1:  # 入库表
            print('入库表:',type)

    def build(self):
        self.stock_excel_picker = SXFilePicker(
            page=self.page,
            buttonText='请选择库存excel',
            on_result_path=lambda path: self.on_excel_path(path, 0)
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

        return ft.Column([
            self.stock_excel_picker,
            self.excel_view,
        ])

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if len(e.files) > 0:
            file_picker_file = e.files[0]
            print(file_picker_file.path)
            self.load_excel(file_picker_file.path)

    def load_excel(self, path):
        self.stock_excel_path = path
        self.wb = openpyxl.load_workbook(path, data_only=True)

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
