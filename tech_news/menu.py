import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12
def response_options(option, response):
    if option == '0':
        return get_tech_news(int(response))
    elif option == '1':
        return search_by_title(response)
    elif option == '2':
        return search_by_date(response)
    elif option == '3':
        return search_by_category(response)
    else:
        return top_5_categories()


def response_options_message(option):
    options = {
        '0': "Digite quantas notícias serão buscadas:",
        '1': "Digite o título:",
        '2': "Digite a data no formato aaaa-mm-dd:",
        '3': "Digite a categoria:",
        '4': "Listando top 5 categorias",
        '5': "Encerrando script\n",
    }
    if option not in options:
        return sys.stderr.write('Opção inválida\n')

    return options.get(str(option))


def analyzer_menu():
    message = "Selecione uma das opções a seguir:\n "\
                   "0 - Popular o banco com notícias;\n "\
                   "1 - Buscar notícias por título;\n "\
                   "2 - Buscar notícias por data;\n "\
                   "3 - Buscar notícias por categoria;\n "\
                   "4 - Listar top 5 categorias;\n "\
                   "5 - Sair.\n"

    # stdout - recebe informações regulares do programa
    sys.stdout.write(message)
    option = input()
    response = response_options_message(option)
    # print('olá1', response)
    sys.stdout.write(str(response))
    input_response = input()
    # print('olá', input_response)
    return response_options(option, input_response)
