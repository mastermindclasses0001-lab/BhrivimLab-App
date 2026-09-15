import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.title = "BhrivimLab"
    page.padding = 0
    
    wv = fwv.WebView(
        url="https://www.bhrivimlab.com", 
        expand=True
    )
    
    page.add(wv)

# Naya command jo latest Flet me use hota hai
ft.run(main)
