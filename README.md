
# Web UI Automation Framework - Playwright


![Playwright Web UI Tests](https://github.com/DuvanLope/Web-UI-Automation-Playwright/actions/workflows/playwright-tests.yml/badge.svg)


Framework de automatización de pruebas web desarrollado con Python, Playwright y Pytest.

## Objetivo

Automatizar pruebas funcionales de aplicaciones web,
validando elementos de interfaz, interacciones del
usuario y comportamiento en diferentes navegadores.

## Tecnologías utilizadas

- Python 3.12
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Visual Studio Code

## Aplicación utilizada

TodoMVC - Playwright Demo

https://demo.playwright.dev/todomvc/

## Funcionalidades implementadas

- Automatización de navegación web
- Validación de títulos y elementos visibles
- Creación de tareas
- Marcación de tareas completadas
- Eliminación de tareas
- Validación de filtros Active y Completed
- Pruebas negativas con entradas inválidas
- Validación de contadores y estados
- Pruebas parametrizadas
- Page Object Model (POM)
- Capturas de pantalla
- Evidencias automáticas cuando falla una prueba
- Reportes HTML
- Cross-Browser Testing

## Navegadores probados

- Chromium
- Firefox
- WebKit

## Estructura del proyecto

    Web-UI-Automation-Playwright/
    |
    |-- pages/
    |   |-- todo_page.py
    |
    |-- tests/
    |   |-- test_pagina_web.py
    |   |-- test_tareas.py
    |
    |-- screenshots/
    |-- reports/
    |-- pytest.ini
    |-- README.md

## Instalación

Crear un entorno virtual:

    python -m venv .venv

Activarlo en Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Instalar las dependencias:

    python -m pip install pytest-playwright pytest-html

Instalar los navegadores:

    python -m playwright install chromium firefox webkit

## Ejecutar pruebas

Ejecutar con Chromium:

    python -m pytest

Ejecutar con navegador visible:

    python -m pytest --headed

Ejecutar en tres motores de navegador:

    python -m pytest --browser chromium --browser firefox --browser webkit

## Generar reportes HTML

    python -m pytest --html=reports/reporte_playwright.html --self-contained-html

## Evidencias de errores

    python -m pytest --screenshot=only-on-failure --output=reports/evidencias

## Resultados confirmados

- 9 casos de prueba automatizados
- 9 pruebas exitosas en Chromium
- 18 ejecuciones exitosas en Chromium y Firefox
- 27 ejecuciones exitosas en Chromium, Firefox y WebKit

## Estado del proyecto

Framework en desarrollo como parte de un portafolio
profesional de QA Automation.

Próxima integración: GitHub Actions para CI/CD.
