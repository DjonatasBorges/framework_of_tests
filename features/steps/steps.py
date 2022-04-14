from lib2to3.pytree import Base
from behave import given, then, when

from modules.constants import PAGE_OBJECTS
from modules.commons import check_url_suffix

from pages.base import BasePage


@given(u'acesso a aplicação')
def step_impl(context):
    context.page_object = BasePage(context.driver)

@when(u'clicar no link de paginas "{page}"')
def step_impl(context, page):
    context.page_object.select_page(page)
    context.page_object = PAGE_OBJECTS[page](context.driver)

@then(u'devo ser redirecionado para a tela "{page}"')
def step_impl(context, page):
    check_url_suffix(context.driver, page)
    context.page_object = PAGE_OBJECTS[page](context.driver)