from behave import then, when


@when(u'selecionar "{name}" no Dropdown')
def select_dropdown(context, name):
    context.page_object.selector_drop_down(name)


@then(u'"{name}" deve esta como opção default')
def confirm_position_dropdown(context, name):
    resp = context.page_object.validate_element_drop_down(name)
    assert resp
