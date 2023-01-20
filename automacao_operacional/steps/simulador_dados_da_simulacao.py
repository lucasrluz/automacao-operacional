from playwright.sync_api import Page
from steps.util.data import Data
from steps.util.element_identifiers import (
    DADOS_DA_SIMULACAO_INFORME_O_PRAZO_SOLICITADO,
    DADOS_DA_SIMULACAO_VALOR_SOLICITADO,
    DADOS_DA_SIMULACAO_INFORME_O_VALOR_SOLICITADO
)
from time import sleep

valor_solicitado = {
    'Contrato': '1',
    'Parcela': '2'
}

def simulador_dados_da_simulacao(page: Page, data: Data):
    sleep(0.5)
    page.locator(DADOS_DA_SIMULACAO_INFORME_O_VALOR_SOLICITADO).type(data['dados_da_simulacao_informe_o_valor_solicitado'])

    sleep(0.5)
    page.locator(DADOS_DA_SIMULACAO_VALOR_SOLICITADO).select_option(valor_solicitado[data['dados_da_simulacao_valor_solicitado']])

    sleep(0.5)
    page.locator(DADOS_DA_SIMULACAO_INFORME_O_PRAZO_SOLICITADO).type(data['dados_da_simulacao_informe_o_prazo_solicitado'])