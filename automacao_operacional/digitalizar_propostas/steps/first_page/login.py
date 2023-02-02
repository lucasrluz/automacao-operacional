from playwright.sync_api import Page
from dotenv import dotenv_values
from digitalizar_propostas.steps.util.element_identifiers import (
    LOGIN_USERNAME,
    LOGIN_PASSWORD,
    LOGIN_BUTTON_SUBMIT
)

env = dotenv_values()

def login(page: Page):
    page.locator(LOGIN_USERNAME).type(env['SIMULADOR_USERNAME'])
    page.locator(LOGIN_PASSWORD).type(env['SIMULADOR_PASSWORD'])
    page.locator(LOGIN_BUTTON_SUBMIT).click()
