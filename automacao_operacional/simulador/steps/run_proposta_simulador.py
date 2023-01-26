from playwright.sync_api import Page
from simulador.steps.util.data import Data
from .util.element_identifiers import (
    PROPOSTA_SIMULADOR,
    DADOS_DA_SIMULACAO_INFORME_O_VALOR_SOLICITADO,
    DADOS_DA_SIMULACAO_VALOR_SOLICITADO,
    DADOS_DA_SIMULACAO_INFORME_O_PRAZO_SOLICITADO,
    PESQUISAR
)
from .simulador_dados_da_proposta import simulador_dados_da_proposta
from .simulador_dados_do_cliente import simulador_dados_do_cliente
from .simulador_dados_do_representante_legal import simulador_dados_do_representante_legal
from .simulador_dados_da_simulacao import simulador_dados_da_simulacao
from .simulador_tabela_for_operacao import simulador_tabela_for_operacao

from time import sleep

def run_proposta_simulador(page: Page, data: Data):
    page.evaluate('(PROPOSTA_SIMULADOR) => document.querySelector(PROPOSTA_SIMULADOR).click()', PROPOSTA_SIMULADOR)

    # Dados da Proposta
    simulador_dados_da_proposta(page, data)

    # Dados do Cliente
    simulador_dados_do_cliente(page, data)

    # Dados da Simulação
    simulador_dados_da_simulacao(page, data)

    # Pesquisar tabelas
    sleep(0.5)
    page.locator(PESQUISAR).click()

    # Selecionar tabelas
    sleep(2)
    simulador_tabela_for_operacao(page, data)
    