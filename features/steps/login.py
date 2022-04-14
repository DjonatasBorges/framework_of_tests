from behave import then, when

from modules.constants import USERS

@when(u'efetuar o login com "{user}"')
def step_impl(context, user):
    context.page_object.login(**USERS[user])


@then(u'logim deve ser efetuado com sucesso')
def step_impl(context):
    assert context.page_object.confirm_login()


@then(u'logim não deve ser efetuado')
def step_impl(context):
    assert not context.page_object.confirm_login()

@when(u'efetuar o logout')
def step_impl(context):
    context.page_object.logout()


@then(u'devo receber a mensagem "{msg}"')
def step_impl(context, msg):
    expected = msg
    found = context.page_object.confirm_logout()
    assert expected in found
