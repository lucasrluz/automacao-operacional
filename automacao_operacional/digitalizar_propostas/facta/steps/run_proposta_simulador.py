from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.data import Data
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    PROPOSTA_SIMULADOR,
    NEXT_PAGE_ONE,
    NEXT_PAGE_TWO,
    NEXT_PAGE_THREE,
    NEXT_PAGE_FOUR,
    DADOS_DA_SIMULACAO_INFORME_O_VALOR_SOLICITADO,
    DADOS_DA_SIMULACAO_VALOR_SOLICITADO,
    DADOS_DA_SIMULACAO_INFORME_O_PRAZO_SOLICITADO,
    PESQUISAR,
    NAO_CONTRATAR_BUTTON
)
from .first_page.simulador_dados_da_proposta import simulador_dados_da_proposta
from .first_page.simulador_dados_do_cliente import simulador_dados_do_cliente
from .first_page.simulador_dados_do_representante_legal import simulador_dados_do_representante_legal
from .first_page.simulador_dados_da_simulacao import simulador_dados_da_simulacao
from .first_page.simulador_tabela_for_operacao import simulador_tabela_for_operacao
from .third_page.informacoes_de_contato import informacoes_de_contato
from .second_page.dados_cadastro_operacao import dados_cadastro_operacao
from .fourth_page.dados_profissionais import dados_profissionais

from time import sleep

def run_proposta_simulador(page: Page, data: Data):
    page.evaluate('(PROPOSTA_SIMULADOR) => document.querySelector(PROPOSTA_SIMULADOR).click()', PROPOSTA_SIMULADOR)
    sleep(100000)
    # Dados da Proposta
    simulador_dados_da_proposta(page, data)

    # Dados do Cliente
    simulador_dados_do_cliente(page, data)

    # Dados da Simulação
    simulador_dados_da_simulacao(page, data)

    # Selecionar tabelas
    simulador_tabela_for_operacao(page, data)
    
    # Proxima página
    page.evaluate('(NEXT_PAGE_ONE) => document.querySelector(NEXT_PAGE_ONE).click()', NEXT_PAGE_ONE)

    # Seta vendedor
    dados_cadastro_operacao(page)

    # Proxíma página
    page.click(NEXT_PAGE_TWO)

    # Informações de contato
    informacoes_de_contato(page, data)

    # Proxíma página
    page.evaluate('(NEXT_PAGE_THREE) => document.querySelector(NEXT_PAGE_THREE).click()', NEXT_PAGE_THREE)
    page.evaluate('(NAO_CONTRATAR_BUTTON) => document.querySelector(NAO_CONTRATAR_BUTTON).click()', NAO_CONTRATAR_BUTTON)
    
    # Dados profissonais
    dados_profissionais(page)

    # Proxíma página
    sleep(5)
    page.evaluate('(NEXT_PAGE_FOUR) => document.querySelector(NEXT_PAGE_FOUR).click()', NEXT_PAGE_FOUR)