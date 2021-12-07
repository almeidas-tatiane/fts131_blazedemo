import time

from behave import *
from selenium import *
from selenium.webdriver.common.by import By


@when(u'clico em Home')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href=home]').click()




@then(u'exibe a pagina de Login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Login'


@when(u'preencho o "{email}" e "{senha}"')
def step_impl(context,email,senha):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(senha)
    time.sleep(2)


@when(u'clico em Login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()



@then(u'exibe a mensagem de pagina expirada')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
