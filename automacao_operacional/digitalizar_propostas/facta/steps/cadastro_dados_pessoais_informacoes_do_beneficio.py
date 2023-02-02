from playwright.sync_api import Page
from digitalizar_propostas.facta.steps.util.element_identifiers import (
    VALOR_BENEFICIO_OU_RENDA,
    BENEFICIO_OU_MATRICULA
)
from digitalizar_propostas.facta.steps.util.data import Data

def cadastro_dados_pessoais_informacoes_do_beneficio(page: Page, data: Data):
    valor_beneficio_ou_renda = data['informacoes_do_beneficio_valor_beneficio_ou_renda']
    page.evaluate(f'(VALOR_BENEFICIO_OU_RENDA) => document.querySelector(VALOR_BENEFICIO_OU_RENDA).value = "{valor_beneficio_ou_renda}"', VALOR_BENEFICIO_OU_RENDA)
    beneficio_ou_matricula = data['informacoes_do_beneficio_beneficio_ou_matricula']
    page.evaluate(f'(BENEFICIO_OU_MATRICULA) => document.querySelector(BENEFICIO_OU_MATRICULA).value = "{beneficio_ou_matricula}"', BENEFICIO_OU_MATRICULA)