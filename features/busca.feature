#language: pt


  Funcionalidade: Realizar um agendamento de um paciente no sistema



    @busca
    Cenario: Realizar agendamento
      Dado que eu entre no site da iclinic
      E acesso o login
        | login | silas.admb@gmail.com |
        |senha  |Test2525              |
      E clicar em Entrar
      Quando eu clicar em Agenda
      E escolher um dia
      E digitar o nome do paciente
      E digitar o telefone
      E escolher um convenio
      Então quando eu clicar em salvar, o agendamento deverá ser concluido