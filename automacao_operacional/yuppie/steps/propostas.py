from playwright.sync_api import Page
from yuppie.steps.util.proposta_data import PropostaData
from yuppie.steps.get_values import get_values
from yuppie.steps.util.element_identifiers import (
    PROPOSTAS,
)
from time import sleep

id1 = '#sortedTable > tbody > tr:nth-child(1) > td:nth-child(2)'
id2 = '#sortedTable > tbody > tr:nth-child(1) > td:nth-child(14) > a'

ID = f'#sortedTable > tbody > tr:nth-child({0}) > td:nth-child(2)'

def propostas(page: Page):
    proposta_data: PropostaData = {}
    
    page.locator(PROPOSTAS).click(timeout=60000)

    sleep(3)

    i = 1
    while(True):
        TR_ID = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(2)'
        td = page.evaluate('(TR_ID) => document.querySelector(TR_ID)', TR_ID)
        
        if td == None:
            print('Elemento não encontrado')
            break
        
        LINK_A = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(14) > a'

        # if page.evaluate('(TR_ID) => document.querySelector(TR_ID).innerHTML', TR_ID) == 'FACTA':
        if True:
            print('Elemento encontrado')
            page.evaluate('(LINK_A) => document.querySelector(LINK_A).click()', LINK_A)

            proposta_data = get_values(page)
        
        break
        # i += 1

    return proposta_data