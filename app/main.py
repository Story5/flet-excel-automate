import flet as ft


def main(page: ft.Page):
    t = ft.Text(value="Hello,world!", color="green")
    # page.controls.append(t)
    # page.update()
    page.add(t) # 相当于 page.controls.append(t) 和 page.update()

ft.app(target=main)
