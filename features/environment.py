from selenium import webdriver

# Bloco executado antes de tudo - 1 a rodar
def before_all(context):
    # Declaramos o objeto do Selenium e o instanciamos como controlador do Chrome
    context.driver = webdriver.Chrome('drivers/chrome/96/chromedriver.exe')
    # Configurar o Selenium para esperar até 30 segundos pelos elementos alvo
    # context.driver.implicitly_wait(30)

    # Esperas (Waits) em Selenium
    # "Metodos Limpos"
    # - ImplicityWait: paciência geral
    # - Wait (Explicit): espera um elemento
    # - FluentWait: sites bonitinhos, mas...
    # >>> Foco no site estar lento ou o elemento estar inacessível

    # "Método Sujo"
    # - Time.sleep: força uma pausa na thread
    # >>> Foco em parar o Selenium

# Bloco executado no final de tudo - Último a rodar
def after_all(context):
    context.driver.quit()

# Bloco executado ao final de cada step
def after_step(context,step):
    print()