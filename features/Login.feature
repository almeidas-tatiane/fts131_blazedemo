Feature: Login

  Scenario: Login Positivo
    Given que acesso o portal Blazedemo
    When clico em Home
    Then exibe a pagina de Login
    When preencho o "almeidas.tatiane@gmail.com" e "123456"
    And clico em Login
    Then exibe a mensagem de pagina expirada

  Scenario Outline: Vários Login com Sucesso
    Given que acesso o portal Blazedemo
    When clico em Home
    Then exibe a pagina de Login
    When preencho o "<email>" e "<senha>"
    And clico em Login
    Then exibe a mensagem de pagina expirada
    Examples:
      | email                      | senha  |
      | almeidas.tatiane@gmail.com | 123456 |
      | teste@gmail.com            | 789012 |
      | teste2@gmail.com           | abc123 |