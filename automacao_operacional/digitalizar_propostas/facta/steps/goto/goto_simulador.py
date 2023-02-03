from playwright.sync_api import Page
from time import sleep
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    PROPOSTA_SIMULADOR
)

def goto_simulador(page: Page):
    # Vai para página simulador
    sleep(5)
    page.evaluate('(PROPOSTA_SIMULADOR) => document.querySelector(PROPOSTA_SIMULADOR).click()', PROPOSTA_SIMULADOR)
    