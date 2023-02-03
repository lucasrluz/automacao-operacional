from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    NEXT_PAGE_THREE,
    NAO_CONTRATAR_BUTTON
)

def goto_dados_complementares(page: Page):
    # Vair para parte de dados complementares
    page.evaluate('(NEXT_PAGE_THREE) => document.querySelector(NEXT_PAGE_THREE).click()', NEXT_PAGE_THREE)
    
    # Clica em não contratar, em popup
    page.evaluate('(NAO_CONTRATAR_BUTTON) => document.querySelector(NAO_CONTRATAR_BUTTON).click()', NAO_CONTRATAR_BUTTON)
