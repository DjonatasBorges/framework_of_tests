from behave import then, when

from modules.commons import parse_context_table

@when(u'marcar o(s) checkbox(es) "{lista}"')
def select_movies(context, lista):
    movies = lista.split(', ')
    context.page_object.deselect_all_checkboxes()
    context.page_object.select_checkbox(movies)

@then(u'os seguintes filmes estarão marcados')
def step_impl(context):
    expected_list = parse_context_table(context.table.headings, context.table.rows)
    found_list = context.page_object.confirm_movies(expected_list)
    for expected in expected_list:
        for found in found_list:
            assert expected in found, f'expected: {expected}, found: {found}'
