from playwright.sync_api import Page
from yuppie.steps.util.proposta_data import PropostaData
from yuppie.steps.get_values import get_values
from yuppie.steps.util.element_identifiers import (
    PROPOSTAS,
    FILTER_PROPOSTA,
    PROPOSTA
)
from time import sleep

id1 = '#sortedTable > tbody > tr:nth-child(1) > td:nth-child(2)'
id2 = '#sortedTable > tbody > tr:nth-child(1) > td:nth-child(14) > a'

ID = f'#sortedTable > tbody > tr:nth-child({0}) > td:nth-child(2)'

def propostas(page: Page):
    proposta_data: PropostaData = {}
    
    # Abre lista com propostas
    page.locator(PROPOSTAS).click(timeout=60000)

    sleep(3)

    # Filtra as propostas pelo menor valor
    page.evaluate('(FILTER_PROPOSTA) => document.querySelector(FILTER_PROPOSTA).click()', FILTER_PROPOSTA)
    
    # Abre a primeira proposta
    page.evaluate('(PROPOSTA) => document.querySelector(PROPOSTA).click()', PROPOSTA)

    # Pega os valores da proposta
    proposta_data = get_values(page)

    return proposta_data
    # i = 1
    # while(True):
    #     TR_ID = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(2)'
    #     td = page.evaluate('(TR_ID) => document.querySelector(TR_ID)', TR_ID)
        
    #     if td == None:
    #         print('Elemento não encontrado')
    #         break
        
    #     LINK_A = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(14) > a'

    #     # if page.evaluate('(TR_ID) => document.querySelector(TR_ID).innerHTML', TR_ID) == 'FACTA':
    #     ID_TD = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(10)'
    #     ID_NOME = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(8)'
    #     x = page.evaluate('(ID_TD) => document.querySelector(ID_TD).innerHTML', ID_TD)
    #     y = page.evaluate('(ID_NOME) => document.querySelector(ID_NOME).innerHTML', ID_NOME)
    #     print(x)
    #     if y == 'YAGO PEREIRA NU':
    #         print('Elemento encontrado')
    #         page.evaluate('(LINK_A) => document.querySelector(LINK_A).click()', LINK_A)

    #         proposta_data = get_values(page)
        
    #     i += 1
