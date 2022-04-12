from behave import given, then, when

@given(u'estar na "home page" do site')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given estar na "home page" do site')


@when(u'clicar no link de paginas "Checkboxes"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clicar no link de paginas "Checkboxes"')


@then(u'devo ser redirecionado para a tela "Checkbox"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo ser redirecionado para a tela "Checkbox"')