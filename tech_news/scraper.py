import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
