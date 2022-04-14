from behave import then, when

@when(u'posicionar o "{heroe}" no "{team}"')
def step_impl(context,heroe, team):
    context.page_object.drag_and_drop(heroe, team)


@then(u'"{heroe}" estará no "{team}"')
def step_impl(context, heroe, team):
    exist = context.page_object.confirm_position_hero(heroe, team)
    assert exist
