import requests
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url, wait=1):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=wait
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    url_list = selector.css(
        'h2 a[rel="bookmark"]::attr(href)'
        ).getall()
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css('a.next.page-numbers ::attr(href)').get()
    if next_page:
        return next_page
    else:
        return None


# Requisito 4
def get_url(selector):
    link = selector.css('link[rel="canonical"]')
    url_page = link.xpath('@href').get()
    return url_page


def get_title(selector):
    return (
        selector.css('div.entry-header-inner.cs-bg-dark h1.entry-title::text')
                .get()
                .strip()  # Remove espaços em branco no início/fim da string.
    )


def get_timestamp(selector):
    return selector.css('li.meta-date::text').get()


def get_author(selector):
    return selector.css('span.author a::text').get()


def get_reading_time(selector):
    li_text = selector.css('li.meta-reading-time::text').get()
    number = re.findall(r'\d+', li_text)  # Regex que captura somente números
    return list(map(int, number))[0]


def get_summary(selector):
    all_p_tags = (
        selector.css('div.entry-content p')
                .xpath('string()')  # Extrai somente o texto
                .getall()
    )
    return (
        all_p_tags[0].replace('\n', '')  # Substitui '\n' por ''
        .strip()
    )


def get_category(selector):
    return selector.css('a.category-style span.label::text').get()


def scrape_news(html_content):
    selector = Selector(html_content)

    return {
        'url': get_url(selector),
        'title': get_title(selector),
        'timestamp': get_timestamp(selector),
        'writer': get_author(selector),
        'reading_time': get_reading_time(selector),
        'summary': get_summary(selector),
        'category': get_category(selector)
    }


# Requisito 5
def get_tech_news(amount):
    url = 'https://blog.betrybe.com'
    html_content = fetch(url)
    url_list_first_page = scrape_updates(html_content)
    url_list = url_list_first_page
    if amount <= 12:
        return url_list_first_page[0:amount]
    else:
        while len(url_list) <= amount:
            next_page_link = scrape_next_page_link(html_content)
            html_content = fetch(next_page_link)
            url_list += scrape_updates(html_content)
        return url_list[0:amount]


if __name__ == '__main__':
    requested_amount_of_urls = get_tech_news(15)

    print(requested_amount_of_urls)
