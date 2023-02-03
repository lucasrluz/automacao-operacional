from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    NEXT_PAGE_ONE
)

def goto_cadastro_propostas(page: Page):
    # Vai para a página de cadastro propostas
    page.evaluate('(NEXT_PAGE_ONE) => document.querySelector(NEXT_PAGE_ONE).click()', NEXT_PAGE_ONE)
