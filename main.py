import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.title = "BhrivimLab"
    page.padding = 0
    
    wv = fwv.WebView(
        url="https://www.bhrivimlab.com",  # <-- ASLI LINK ZAROOR CHECK KAREIN
        expand=True
    )
    
    page.add(wv)

ft.app(target=main)
