from playwright.sync_api import Page
from .cadastro_propostas.cadastro_propostas_dados_cadastro_operacao import cadastro_propostas_dados_cadastro_operacao

def run_cadastro_propostas(page: Page):
    # Seta vendedor
    cadastro_propostas_dados_cadastro_operacao(page)
