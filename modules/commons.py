from typing import Iterable, List, Text

from behave.model import Row


from time import sleep

from modules.constants import URL_SUFFIXES

from selenium.webdriver.remote.webdriver import WebDriver


def parse_context_table(headers: Iterable[Text], rows: Iterable[Row], clear: bool = True) -> List[dict]: # NOQA
    """
     Analisa a tabela fornecida pelo gerenciador de contexto de comportamento.
     Args:
         headers:
             Iterável com strings para servir como chaves para cada linha.
         rows:
             Iterável com objetos de linha do módulo behavior.model.
         clear:
             Sinalizar para eliminar tipos de dados falsos da tabela

     Return:
         Uma lista com mapeamentos de todas as linhas para o cabeçalho correspondente.
         [
             {
                 'heading1': 'row1_value1',
                 'heading2': 'row1_value2'
             },
             {
                 'heading1': 'row2_value1',
                 'heading2': 'row2_value2'
             }
             [...]
         ]
    """
    if clear:
        return [{k: v for k, v in zip(headers, row) if v not in ['', None]}
                for row in rows]
    return [{k: v for k, v in zip(headers, row)} for row in rows]


def check_url_suffix(driver: WebDriver, page_name: str) -> None:
    """
     Pesquisa o URL atual para verificar se ele carrega em uma página com o
     sufixo.

     Args:
         driver:
             O webdriver de selênio remoto atual.
         page_name:
             String com o texto relativo ao nome da página
             (chave na constante URL_SUFFIXES).
    """
    for i in range(5):
        try:
            suffix = driver.current_url.split('/')[-1]
            assert suffix.startswith(URL_SUFFIXES[page_name])
            return
        except AssertionError:
            sleep(.3)
    raise AssertionError('The page suffix was unnexpected')
