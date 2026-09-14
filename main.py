import flet as ft

def main(page: ft.Page):
    page.title = "BhrivimLab"
    page.padding = 0
    my_url = "https://www.bhrivimlab.com/"
    wv = ft.WebView(url=my_url, expand=True)
    page.add(wv)

ft.app(target=main)
