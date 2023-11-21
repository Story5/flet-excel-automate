import flet as ft
from sx_app import SXApp


def main(page: ft.Page):
    page.title = 'Excel自动化'
    page.add(SXApp(page))


ft.app(target=main)
