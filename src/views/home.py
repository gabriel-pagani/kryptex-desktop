import flet as ft


class HomeView:
    def __init__(self, page: ft.Page, user, user_key, on_logout):
        self.page = page
        self.user = user
        self.user_key = user_key
        self.on_logout = on_logout
