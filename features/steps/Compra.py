from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features import environment



def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(

        )


#TODO: "Desambiguar o passo com o PO"
@given('que acesso o portal Blazedemo')
@given('que acesso o site Blazedemo')
def que_acesso_o_site_Blazedemo(context):
    context.driver.get('https://www.blazedemo.com')
    print('Passo 1 - Abriu o site')


@when('pesquiso passagens de "{origem}" a "{destino}"')
def pesquiso_passagens_de_origem_a_destino(context, origem, destino):
    # Campo Origem
    elemento_origem = context.driver.find_element(By.NAME, 'fromPort')
    objeto_origem = Select(elemento_origem)
    objeto_origem.select_by_visible_text(origem)

    # Campo Destino
    elemento_destino = context.driver.find_element(By.NAME, 'toPort')
    objeto_destino = Select(elemento_destino)
    objeto_destino.select_by_visible_text(destino)

    # Clicar no botão de Pesquisar Voos
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()


@when('seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small').click()
    print('Passo 3 - Selecionou o primeiro voo')


@when('preencho os dados de pagamento')
def preencho_os_dados_de_pagamento(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('Tatiane Almeida')
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 4 - Preencheu os dados de pagamento')


@then('valido se a passagem foi emitida')
def valido_se_a_passagem_foi_emitida(context):
    # Validar se o titulo da guia exibe que está na pagina de transação confirmada
    assert context.driver.title == 'BlazeDemo Confirmation'
    print('Passo 5 - Validou se a passagem foi emitida')
