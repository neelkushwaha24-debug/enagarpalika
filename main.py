import flet as ft
from flet_webview import WebView

def main(page: ft.Page):
    page.title = "e-Nagar Palika MP"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window.width = 400
    page.window.height = 800
    
    # WebView to load the portal
    wv = WebView(
        url="https://enagarpalika.mp.gov.in/",
        expand=True,
    )
    
    # A simple app bar for navigation and refresh
    def go_home(e):
        wv.url = "https://enagarpalika.mp.gov.in/"
        wv.update()
        
    def refresh_page(e):
        wv.reload()
        
    page.appbar = ft.AppBar(
        title=ft.Text("e-Nagar Palika", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        center_title=True,
        bgcolor=ft.Colors.BLUE_700,
        actions=[
            ft.IconButton(icon=ft.Icons.HOME, on_click=go_home, icon_color=ft.Colors.WHITE),
            ft.IconButton(icon=ft.Icons.REFRESH, on_click=refresh_page, icon_color=ft.Colors.WHITE),
        ]
    )

    page.add(wv)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
