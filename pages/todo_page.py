

from playwright.sync_api import Page


class TodoPage:

    URL = "https://demo.playwright.dev/todomvc/"

    def __init__(self, page: Page):
        self.page = page
        self.campo_tarea = page.locator(".new-todo")
        self.lista_tareas = page.locator(".todo-list li")

    def abrir_pagina(self):
        self.page.goto(self.URL)

    def agregar_tarea(self, nombre_tarea: str):
        self.campo_tarea.fill(nombre_tarea)
        self.campo_tarea.press("Enter")

    def completar_tarea(self, nombre_tarea: str):
        tarea = self.lista_tareas.filter(
            has_text=nombre_tarea
        )
        tarea.locator(".toggle").check()

    def eliminar_tarea(self, nombre_tarea: str):
        tarea = self.lista_tareas.filter(
            has_text=nombre_tarea
        )
        tarea.hover()
        tarea.locator(".destroy").click()
