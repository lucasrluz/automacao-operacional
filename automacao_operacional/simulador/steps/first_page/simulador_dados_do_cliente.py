from playwright.sync_api import Page
from simulador.steps.util.data import Data
from time import sleep
from simulador.steps.util.element_identifiers import (
    DADOS_DO_CLIENTE_CPF,
    DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO,
)

def simulador_dados_do_cliente(page: Page, data: Data):
    sleep(0.5)
    page.locator(DADOS_DO_CLIENTE_CPF).fill(data['dados_do_cliente_cpf'])

    page.locator(DADOS_DO_CLIENTE_DATA_DE_NASCIMENTO).click()