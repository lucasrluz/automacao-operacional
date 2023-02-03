from playwright.sync_api import Page
from .cadastro_dados_pessoais.cadastro_dados_pessoais_informacoes_pessoais import cadastro_dados_pessoais_informacoes_pessoais
from .cadastro_dados_pessoais.cadastro_dados_pessoais_informacoes_do_beneficio import cadastro_dados_pessoais_informacoes_do_beneficio
from .cadastro_dados_pessoais.cadastro_dados_pessoais_informacoes_de_contato import cadastro_dados_pessoais_informacoes_de_contato
from .util.data import Data

def run_cadastro_dados_pessoais(page: Page, data: Data):
    # Cadastro dados pessoais, informações de contato
    cadastro_dados_pessoais_informacoes_pessoais(page, data)

    # Cadastro dados pessoais, informações do benefício
    cadastro_dados_pessoais_informacoes_do_beneficio(page, data)

    # Informações de contato
    cadastro_dados_pessoais_informacoes_de_contato(page, data)