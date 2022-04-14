from behave import then, when


@when(u'selecionar "{name}" no Dropdown')
def step_impl(context, name):
    context.page_object.selector_drop_down(name)


@then(u'"{name}" deve esta como opção default')
def step_impl(context, name):
    resp = context.page_object.validate_element_drop_down(name)
    assert resp
