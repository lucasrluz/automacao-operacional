from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.data import Data
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    ESTADO_CIVIL,
    NOME_DO_PAI_NAO_CONSTA_NO_DOCUMENTO,
    VALOR_PRATIMONIAL,
    CLIENTE_ILETRADO_OU_IMPOSSIBILITADO_DE_ASSINAR,
    NACIONALIDADE,
    NATURALIDADE_UF,
    NATURALIDADE
)
from digitalizar_propostas.facta.steps.util.city_uf import city_uf
from time import sleep

def cadastro_dados_pessoais_informacoes_pessoais(page: Page, data: Data):
    sleep(8)
    page.locator(ESTADO_CIVIL).select_option('6') # OUTROS
    page.locator(NOME_DO_PAI_NAO_CONSTA_NO_DOCUMENTO).check() # True
    page.locator(VALOR_PRATIMONIAL).select_option('1') # Tento faz
    page.locator(CLIENTE_ILETRADO_OU_IMPOSSIBILITADO_DE_ASSINAR).select_option('N') # NÃO
    page.locator(NACIONALIDADE).select_option('1')
    page.locator(NATURALIDADE_UF).select_option(data['informacoes_pessoais_naturalidade_uf'])
    page.locator(NATURALIDADE).select_option(city_uf[data['informacoes_pessoais_naturalidade']])