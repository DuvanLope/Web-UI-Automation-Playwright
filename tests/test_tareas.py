
from playwright.sync_api import Page, expect
import pytest
from pages.todo_page import TodoPage



@pytest.mark.parametrize(
    "nombre_tarea",
    [
        "Aprender Playwright",
        "Estudiar Python",
        "Practicar QA Automation"
    ]
)
def test_agregar_tarea(page: Page, nombre_tarea):
    # Crear una instancia de nuestro Page Object
    todo = TodoPage(page)

    # Abrir la aplicacion
    todo.abrir_pagina()

    # Agregar la tarea
    todo.agregar_tarea(nombre_tarea)

    # Verificar que existe una sola tarea
    expect(todo.lista_tareas).to_have_count(1)

    # Verificar que el texto es correcto
    expect(todo.lista_tareas).to_contain_text(nombre_tarea)





def test_completar_tarea(page: Page):
    todo = TodoPage(page)
    todo.abrir_pagina()

    # Crear y completar una tarea
    todo.agregar_tarea("Estudiar QA Automation")
    todo.completar_tarea("Estudiar QA Automation")

    # Validar el resultado
    expect(todo.lista_tareas).to_have_count(1)
    expect(todo.lista_tareas).to_have_class("completed")

    # Guardar evidencia visual
    page.screenshot(
        path="screenshots/tarea_completada.png",
        full_page=True
    )




def test_eliminar_tarea(page: Page):
    todo = TodoPage(page)
    todo.abrir_pagina()

    todo.agregar_tarea("Tarea para eliminar")
    todo.eliminar_tarea("Tarea para eliminar")

    expect(todo.lista_tareas).to_have_count(0)

    
def test_filtrar_tareas(page: Page):
    # Abrir TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")

    campo_tarea = page.locator(".new-todo")

    # Crear dos tareas
    campo_tarea.fill("Estudiar Playwright")
    campo_tarea.press("Enter")

    campo_tarea.fill("Estudiar Python")
    campo_tarea.press("Enter")

    # Verificar que existen dos tareas
    tareas = page.locator(".todo-list li")
    expect(tareas).to_have_count(2)

    # Marcar la primera tarea como completada
    tareas.nth(0).locator(".toggle").check()

    # Filtrar tareas activas
    page.get_by_role("link", name="Active").click()

    expect(page.locator(".todo-list li")).to_have_count(1)
    expect(page.locator(".todo-list")).to_contain_text(
        "Estudiar Python"
    )

    # Filtrar tareas completadas
    page.get_by_role("link", name="Completed").click()

    expect(page.locator(".todo-list li")).to_have_count(1)
    expect(page.locator(".todo-list")).to_contain_text(
        "Estudiar Playwright"
    )


def test_no_permitir_tarea_vacia(page: Page):
    # Abrir la aplicacion TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")

    # Localizar el campo para crear tareas
    campo_tarea = page.locator(".new-todo")

    # Intentar crear una tarea con espacios vacios
    campo_tarea.fill("   ")

    # Presionar Enter
    campo_tarea.press("Enter")

    # Verificar que no se creo ninguna tarea
    tareas = page.locator(".todo-list li")

    expect(tareas).to_have_count(0)


def test_contador_tareas_pendientes(page: Page):
    # Abrir TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")

    # Crear una tarea
    campo_tarea = page.locator(".new-todo")
    campo_tarea.fill("Aprender automatizacion web")
    campo_tarea.press("Enter")

    # Verificar que existe una tarea pendiente
    contador = page.locator(".todo-count")
    expect(contador).to_contain_text("1 item left")

    # Completar la tarea
    tarea = page.locator(".todo-list li")
    tarea.locator(".toggle").check()

    # Verificar que ya no hay tareas pendientes
    expect(contador).to_contain_text("0 items left")
