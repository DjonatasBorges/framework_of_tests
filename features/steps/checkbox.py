from behave import then, when

from modules.commons import parse_context_table

@when(u'marcar o(s) checkbox(es) "{lista}"')
def select_movies(context, lista):
    movies = lista.split(', ')
    context.page_object.deselect_all_checkboxes()
    context.page_object.select_checkbox(movies)

@then(u'os seguintes filmes estarão marcados')
def step_impl(context):
    table_dict = parse_context_table(context.table.headings, context.table.rows)
    table_list = []
    expected = ''
    for row in table_dict:
        table_list.append(row)
    found = context.page_object.confirm_movies(table_list)
    assert expected in found, f'expected: {expected}, found: {found}'