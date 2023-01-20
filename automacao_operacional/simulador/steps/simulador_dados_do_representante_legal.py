from playwright.sync_api import Page
from simulador.steps.util.data import Data
from simulador.steps.util.element_identifiers import (
    DADOS_DO_REPRESENTANTE_LEGAL_CPF,
    DADOS_DO_REPRESENTANTE_LEGAL_NOME
)
from time import sleep

def simulador_dados_do_representante_legal(page: Page, data: Data):
    sleep(0.5)
    page.locator(DADOS_DO_REPRESENTANTE_LEGAL_CPF).type(data['dados_do_representante_legal_cpf'])

    sleep(0.5)
    page.locator(DADOS_DO_REPRESENTANTE_LEGAL_NOME).type(data['dados_do_representante_legal_nome'])