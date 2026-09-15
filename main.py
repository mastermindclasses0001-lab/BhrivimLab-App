import flet as ft

def main(page: ft.Page):
    page.title = "BhrivimLab"
    page.padding = 0
    
    wv = ft.WebView(
        url="https://www.bhrivimlab.com", 
        expand=True
    )
    
    page.add(wv)

ft.app(target=main)
