import flet as ft
import flet_webview as fwv


def main(page: ft.Page):
    page.title = "BhrivimLab"
    page.padding = 0
    page.spacing = 0

    page.add(
        fwv.WebView(
            url="https://www.bhrivimlab.com",
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.run(main)
