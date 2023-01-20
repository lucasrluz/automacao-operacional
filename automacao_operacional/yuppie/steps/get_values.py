from playwright.sync_api import Page
from yuppie.steps.util.element_identifiers import (
    PROPOSTAS,
    FILTER_BANCO
)
from time import sleep

id1 = '#sortedTable > tbody > tr:nth-child(1) > td:nth-child(2)'
id2 = '#sortedTable > tbody > tr:nth-child(1) > td:nth-child(14) > a'

ID = f'#sortedTable > tbody > tr:nth-child({0}) > td:nth-child(2)'

def get_value(page: Page):
    page.locator(PROPOSTAS).click(timeout=60000)

    sleep(5)
    page.evaluate('(FILTER_BANCO) => document.querySelector(FILTER_BANCO).click()', FILTER_BANCO)

    i = 1
    while(True):
        TR_ID = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(2)'
        td = page.evaluate('(TR_ID) => document.querySelector(TR_ID)', TR_ID)
        
        if td == None:
            break
        
        LINK_A = f'#sortedTable > tbody > tr:nth-child({i}) > td:nth-child(14) > a'

        if page.evaluate('(TR_ID) => document.querySelector(TR_ID).innerHTML', TR_ID) == 'FACTA':
            element = page.evaluate('(LINK_A) => document.querySelector(LINK_A).href', LINK_A)
            print(page.evaluate('(TR_ID) => document.querySelector(TR_ID).innerHTML', TR_ID))
            print(element)
        
        i += 1
