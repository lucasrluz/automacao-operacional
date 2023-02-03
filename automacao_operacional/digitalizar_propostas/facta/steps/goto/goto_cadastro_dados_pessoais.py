from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    NEXT_PAGE_TWO
)

def goto_cadastro_dados_pessoais(page: Page):
    # Vair para parte de cadastro de dados pessoais
    page.click(NEXT_PAGE_TWO)