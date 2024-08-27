'''from playwright.sync_api import Page, expect
import re

# Ir para a página inicial

link_inicial = 'https://publilegal.diariodenoticias.com.br/'

def test_has_title(page: Page):
    page.goto(link_inicial)
    page.locator("xpath=/html/body/div[1]/section[4]/div/div[1]/div/section[1]/div/div/div/div[6]/div/div/div/div/div[5]/label/div/span[1]/i").click()
    texto = page.locator("xpath=/html/body/div[1]/section[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/section/div/div/div/div[1]/div/h2").inner_text
    print('teste')'''
from playwright.sync_api import sync_playwright
import pandas as pd

i = 1
titulos = []
empresas = []
datas = []
links = []
secoes = []

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://publilegal.diariodenoticias.com.br/")

    while i <= 15:
        xpath_balanco = '/html/body/div[1]/section[4]/div/div[1]/div/section[1]/div/div/div/div[6]/div/div/div/div/div[5]/label/div/span[1]'
        xpath_titulo = '/html/body/div[1]/section[4]/div/div[2]/div/div[2]/div/div/div/div['+ str(i) + ']/div/section/div/div/div/div[1]/div/h2'
        xpath_empresa = '/html/body/div[1]/section[4]/div/div[2]/div/div[2]/div/div/div/div['+ str(i) + ']/div/section/div/div/div/div[3]/div/h2'
        xpath_data = '/html/body/div[1]/section[4]/div/div[2]/div/div[2]/div/div/div/div[' + str(i) + ']/div/section/div/div/div/section[1]/div/div/div/div[2]/div'
        xpath_secao = '/html/body/div[1]/section[4]/div/div[2]/div/div[2]/div/div/div/div[' + str(i) + ']/div/section/div/div/div/section[1]/div/div/div/div[4]/div'
        xpath_link = '/html/body/div[1]/section[4]/div/div[2]/div/div[2]/div/div/div/div[' + str(i) + ']/div/section/div/div/div/section[2]/div/div/div/div[2]/div/div/a'
        page.locator(f"xpath={xpath_balanco}").click()

        titulo = page.locator(f"xpath={xpath_titulo}").inner_text()
        empresa = page.locator(f"xpath={xpath_empresa}").inner_text()
        data = page.locator(f"xpath={xpath_data}").inner_text()
        secao = page.locator(f"xpath={xpath_secao}").inner_text()
        link = page.locator(f"xpath={xpath_link}").get_attribute('href')
        titulos.append(titulo)
        empresas.append(empresa)
        datas.append(data)
        secoes.append(secao)
        links.append(link)
        i += 1
    
    print(titulos, empresas, datas, secoes, links)
    d = {'Razão Social': empresas, 'Tipo': }
    browser.close()