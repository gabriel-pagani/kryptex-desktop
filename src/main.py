# import flet as ft


# def main(page: ft.Page):
#     None


# ft.run(main, assets_dir="assets")

from controllers.user import User

obj = User(username='admin', master_password='1234')
print(obj.create_user())
print(obj.delete_user())
