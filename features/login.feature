Funcionalidade: Checkboxes

  Contexto:
    Dado acesso a aplicação
    Quando clicar no link de paginas "Login"
    Entao devo ser redirecionado para a tela "Login"

  Cenario: Login com conta válida
    Quando efetuar o login com "Usuário Correto"
    Entao logim deve ser efetuado com sucesso
    Quando efetuar o logout
    Entao devo receber a mensagem "Você saiu da área logada!"

  Cenario: Login com conta inválida
    Quando efetuar o login com "Usuário Incorreto"
    Entao logim não deve ser efetuado
