from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = find_news()
    categories = []

    for new in news:
        categories.append(new['category'])

    top_categories = Counter(categories).most_common(5)
    # https://chat.openai.com/chat
    # prompt: "Como ordenar uma lista de tuplas de forma que os empates sejam
    # ordenados alfabeticamente"
    top_sorted_categories = sorted(top_categories, key=lambda x: (-x[1], x[0]))
    top_sorted_categories_names = []

    for category in top_sorted_categories:
        top_sorted_categories_names.append(category[0])

    return top_sorted_categories_names


if __name__ == '__main__':
    top_categories = top_5_categories()

    print(top_categories)
