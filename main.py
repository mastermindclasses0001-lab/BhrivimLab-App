import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    # App ka naam aur thodi settings
    page.title = "BhrivimLab"
    page.padding = 0  # Screen ke edges par khali space hatane ke liye
    
    # WebView widget banana
    wv = fwv.WebView(
        url="https://www.bhrivimlab.com",  # <-- YAHAN APNI WEBSITE KA ASLI LINK DAALEIN
        expand=True
    )
    
    # Screen par WebView ko dikhana
    page.add(wv)

ft.app(target=main)
