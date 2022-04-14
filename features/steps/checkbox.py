from ast import literal_eval
from behave import then, when

from modules.commons import parse_context_table


@when(u'marcar o(s) checkbox(es) "{lista}"')
def select_movies(context, lista):
    movies = lista.split(', ')
    context.page_object.deselect_all_checkboxes()
    context.page_object.select_checkbox(movies)


@then(u'os seguintes filmes estarão marcados')
def confirm_selected_movies(context):
    expected = parse_context_table(context.table.headings, context.table.rows)
    found = context.page_object.confirm_movies(expected)
    assert expected == found, f'expected: {expected}, found: {found}'
