from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.data import Data
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    PROPOSTA_SIMULADOR,
    NEXT_PAGE_ONE,
    NEXT_PAGE_TWO,
    NEXT_PAGE_THREE,
    NEXT_PAGE_FOUR,
    NAO_CONTRATAR_BUTTON
)
from .steps.simulador_dados_da_proposta import simulador_dados_da_proposta
from .steps.simulador_dados_do_cliente import simulador_dados_do_cliente
from .steps.simulador_dados_da_simulacao import simulador_dados_da_simulacao
from .steps.simulador_tabela_for_operacao import simulador_tabela_for_operacao
from .steps.cadastro_dados_pessoais_informacoes_de_contato import cadastro_dados_pessoais_informacoes_de_contato
from .steps.cadastro_dados_pessoais_informacoes_pessoais import cadastro_dados_pessoais_informacoes_pessoais
from .steps.cadastro_dados_pessoais_informacoes_do_beneficio import cadastro_dados_pessoais_informacoes_do_beneficio
from .steps.cadastro_propostas_dados_cadastro_operacao import cadastro_propostas_dados_cadastro_operacao
from .steps.login import login

from time import sleep

def run_facta(page: Page, data: Data):
    # Login na página facta
    login(page)

    # Vai para página de cadastro propostas
    sleep(5)
    page.evaluate('(PROPOSTA_SIMULADOR) => document.querySelector(PROPOSTA_SIMULADOR).click()', PROPOSTA_SIMULADOR)
    
    # Dados da Proposta
    simulador_dados_da_proposta(page, data)
    sleep(1000000)
    # Dados do Cliente
    simulador_dados_do_cliente(page, data)

    # Dados da Simulação
    simulador_dados_da_simulacao(page, data)

    # Selecionar tabelas
    simulador_tabela_for_operacao(page, data)
    
    # Proxima página
    page.evaluate('(NEXT_PAGE_ONE) => document.querySelector(NEXT_PAGE_ONE).click()', NEXT_PAGE_ONE)

    # Seta vendedor
    cadastro_propostas_dados_cadastro_operacao(page)

    # Proxíma página
    page.click(NEXT_PAGE_TWO)

    # Cadastro dados pessoais, informações de contato
    cadastro_dados_pessoais_informacoes_pessoais(page, data)

    # Cadastro dados pessoais, informações do benefício
    cadastro_dados_pessoais_informacoes_do_beneficio(page, data)

    # Informações de contato
    cadastro_dados_pessoais_informacoes_de_contato(page, data)
    sleep(100000)

    # Proxíma página
    page.evaluate('(NEXT_PAGE_THREE) => document.querySelector(NEXT_PAGE_THREE).click()', NEXT_PAGE_THREE)
    page.evaluate('(NAO_CONTRATAR_BUTTON) => document.querySelector(NAO_CONTRATAR_BUTTON).click()', NAO_CONTRATAR_BUTTON)
    
    # Dados profissonais
    dados_profissionais(page)

    # Proxíma página
    sleep(5)
    page.evaluate('(NEXT_PAGE_FOUR) => document.querySelector(NEXT_PAGE_FOUR).click()', NEXT_PAGE_FOUR)