from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.data import Data
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    NEXT_PAGE_THREE,
    NEXT_PAGE_FOUR,
    NAO_CONTRATAR_BUTTON
)
from .steps.login import login
from .steps.run_simulador import run_simulador
from .steps.run_cadastro_propostas import run_cadastro_propostas
from .steps.run_cadastro_dados_pessoais import run_cadastro_dados_pessoais
from .steps.goto.goto_simulador import goto_simulador
from .steps.goto.goto_cadastro_propostas import goto_cadastro_propostas
from .steps.goto.goto_cadastro_dados_pessoais import goto_cadastro_dados_pessoais
from .steps.goto.goto_dados_complementares import goto_dados_complementares
from .steps.goto.goto_inserir_anexos import goto_inserir_anexos

from time import sleep

def run_facta(page: Page, data: Data):
    # Vai para página de login do facta
    page.goto('https://desenv.facta.com.br/sistemaNovo/login.php')
    # Executa login no facta
    login(page)

    # Vai para página simulador
    goto_simulador(page)
    
    # Executa parte do simulador
    run_simulador(page, data)
    
    # Vai para cadastro propostas
    goto_cadastro_propostas(page)

    # Executa parte de cadastro de proposta 
    run_cadastro_propostas(page)

    # Vair para parte de cadastro de dados pessoais
    goto_cadastro_dados_pessoais(page)

    # Executa parte de cadastro de dados pessoais
    run_cadastro_dados_pessoais(page, data)
    sleep(1000000)

    # Vai para parte de cadastro de dados complementares
    goto_dados_complementares(page)

    # Vai para parte de inserir anexos
    goto_inserir_anexos(page)