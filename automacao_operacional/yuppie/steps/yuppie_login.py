from playwright.sync_api import Page
from dotenv import dotenv_values
from yuppie.steps.util.element_identifiers import (
    YUPPIE_USERNAME,
    YUPPIE_PASSWORD,
    YUPPIE_BUTTON_SUBMIT
)

env = dotenv_values()

def yupie_login(page: Page):
    page.locator(YUPPIE_USERNAME).type(env['YUPPIE_USERNAME'])
    page.locator(YUPPIE_PASSWORD).type(env['YUPPIE_PASSWORD'])
    page.locator(YUPPIE_BUTTON_SUBMIT).click()