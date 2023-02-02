from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    TIPO_DE_PROFISSAO,
    DATA_DE_ADMISSAO
)

def dados_profissionais(page: Page):
    # page.locator(TIPO_DE_PROFISSAO).select_option('0001')
    # page.locator(DATA_DE_ADMISSAO).fill('01/01/2023')
    ...