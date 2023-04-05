from tech_news.database import find_news


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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    news_by_title = search_by_title(
        'Versionamento de software e de código: o que é e como fazer?'
    )

    print(news_by_title)
