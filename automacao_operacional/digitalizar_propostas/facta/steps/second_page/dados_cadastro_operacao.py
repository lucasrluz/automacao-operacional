from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    BUSCAR_VENDEDOR_CPF,
    BUSCAR_VENDEDOR_LOGIN_OU_NOME,
    VENDEDOR
)
from time import sleep

def dados_cadastro_operacao(page: Page):
    while True:
        try:
            if page.locator(BUSCAR_VENDEDOR_CPF).is_visible() == True:
                page.evaluate('(BUSCAR_VENDEDOR_CPF) => document.querySelector(BUSCAR_VENDEDOR_CPF).value = "011.399.422-20"', BUSCAR_VENDEDOR_CPF)
                page.evaluate('(BUSCAR_VENDEDOR_LOGIN_OU_NOME) => document.querySelector(BUSCAR_VENDEDOR_LOGIN_OU_NOME).value = " "', BUSCAR_VENDEDOR_LOGIN_OU_NOME)
                
                page.locator(VENDEDOR).select_option('92819_ClaraB6968')
                break
        except:
            continue