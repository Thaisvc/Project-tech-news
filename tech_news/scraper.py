import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_link = selector.css(".cs-overlay-link::attr(href)").getall()
    return news_link


# Requisito 3
def scrape_next_page_link(html_content):

    selector = Selector(text=html_content)
    next_page = selector.css(".next.page-numbers::attr(href)").get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    # https://stackoverflow.com/questions/68746327/find-the-canonical-link-in-a-file-type-file-beautifulsoup
    link = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    reading_time = int(
        selector.css("li.meta-reading-time::text").get().split()[0]
    )
    summary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    category = selector.css("a.category-style > span.label::text").get()

    return {
        "url": link,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
