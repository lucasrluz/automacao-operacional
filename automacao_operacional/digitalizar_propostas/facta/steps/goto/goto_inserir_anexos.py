from playwright.sync_api import Page
from time import sleep
from digitalizar_propostas.facta.steps.util.element_identifiers import (    
    NEXT_PAGE_FOUR
)

def goto_inserir_anexos(page: Page):
    sleep(5)
    page.evaluate('(NEXT_PAGE_FOUR) => document.querySelector(NEXT_PAGE_FOUR).click()', NEXT_PAGE_FOUR)