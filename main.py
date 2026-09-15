import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.title = "BhrivimLab"
    
    wv = fwv.WebView(
        url="https://www.bhrivimlab.com",  # <-- YAHAN APNI ASLI WEBSITE KA LINK DAALEIN
        expand=True
    )
    
    page.add(wv)

# Naya command jo V1 me officially use hota hai
ft.run(main)
