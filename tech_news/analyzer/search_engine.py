from tech_news.database import find_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = find_news()
    news_by_title = []
    for new in news:
        if title.lower() in new['title'].lower():
            news_by_title.append((new['title'], new['url']))
    return news_by_title


# Requisito 8
def search_by_date(date):
    # %Y representa o ano com 4 dígitos
    # %m representa o mês com 2 dígitos
    # %d representa o dia com 2 dígitos
    formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    return formatted_date
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    news_by_date = search_by_date('2023-04-05')

    print(news_by_date)
