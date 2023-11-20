import flet as ft
import time


def main(page: ft.Page):
    t = ft.Text(value="Hello,world!", color="green")
    # page.controls.append(t)
    # page.update()
    page.add(t) # 相当于 page.controls.append(t) 和 page.update()
    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)

ft.app(target=main)
