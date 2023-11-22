import flet as ft
import openpyxl
from components.sx_file_picker import SXFilePicker


class SXApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.stock_excel_path = ''  # 库存表excel文件路径
        self.wb = None

    def build(self):
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

        self.excel_view = ft.Column(
            visible=False,
            controls=[
                SXFilePicker(
                    page=self.page,
                    buttonText='请选择入库excel',
                    on_result_path=lambda path: self.on_excel_path(path, 1)
                ),
            ]
        )
        return ft.Column([
            SXFilePicker(
                page=self.page,
                buttonText='请选择库存excel',
                on_result_path=lambda path: self.on_excel_path(path, 0)
            ),
            ft.Divider(),
            ft.Column([
                ft.Row([
                    ft.Text('配货吨数'),
                    self.tonInput,
                ]),
                ft.Row([
                    ft.Text('换货方式'),
                    self.typeRadio,
                    self.sixCheckbox,
                ])
            ]),
            self.excel_view,
        ])

    def on_excel_path(self, path: str, type):
        print('on_excel_path:', path)
        if type == 0:  # 库存表
            print('库存表:', type)
            self.stock_excel_path = path
            self.load_excel(self.stock_excel_path)
        elif type == 1:  # 入库表
            print('入库表:', type)

    def load_excel(self, path):
        print(path)
    
