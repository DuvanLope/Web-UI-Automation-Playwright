
from playwright.sync_api import Page, expect


def test_pagina_principal(page: Page):
    # Abrir la pagina web
    page.goto("https://example.com/")

    # Verificar el titulo de la pagina
    expect(page).to_have_title("Example Domain")

    # Verificar que el enlace sea visible
    expect(
        page.get_by_role("link", name="Learn more")
    ).to_be_visible()
