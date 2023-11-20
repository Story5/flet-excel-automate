import flet as ft
import time


def main(page: ft.Page):
    t = ft.Text(value="Hello,world!", color="green")
    # page.controls.append(t)
    # page.update()
    page.add(t)  # 相当于 page.controls.append(t) 和 page.update()
    page.add(ft.Row(
        controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C"),
        ]
    ))
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    def button_clicked(e):
        page.add(ft.Text('Clicked!'))
    page.add(ft.ElevatedButton(text='Click me', on_click=button_clicked))

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(
        ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)


ft.app(target=main)
