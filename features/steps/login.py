from behave import then, when

from modules.constants import USERS


@when(u'efetuar o login com "{user}"')
def login(context, user):
    context.page_object.login(**USERS[user])


@then(u'logim deve ser efetuado com sucesso')
def susseful_login(context):
    assert context.page_object.confirm_login()


@then(u'logim não deve ser efetuado')
def login_failed(context):
    assert not context.page_object.confirm_login()


@when(u'efetuar o logout')
def logout(context):
    context.page_object.logout()


@then(u'devo receber a mensagem "{msg}"')
def confirm_msg(context, msg):
    expected = msg
    found = context.page_object.confirm_logout()
    assert expected in found
