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
    news = find_news()
    # %Y representa o ano com 4 dígitos
    # %m representa o mês com 2 dígitos
    # %d representa o dia com 2 dígitos
    try:
        formatted_date = datetime.strptime(date, '%Y-%m-%d') \
            .strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError('Data inválida')

    news_by_date = []
    for new in news:
        if new['timestamp'] == formatted_date:
            news_by_date.append((new['title'], new['url']))
    return news_by_date


# Requisito 9
def search_by_category(category):
    news = find_news()
    news_by_category = []
    for new in news:
        if category.lower() in new['category'].lower():
            news_by_category.append((new['title'], new['url']))
    return news_by_category


if __name__ == '__main__':
    news_by_category = search_by_category('Tecnologia')

    print(news_by_category)
