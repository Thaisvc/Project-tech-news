from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query_find = search_news({"title": {"$regex": title, "$options": "i"}})
    news = []
    for item in query_find:
        news.append((item["title"], item["url"]))
    return news


# Requisito 8
def search_by_date(date):
    try:
        date_ = datetime.strptime(date, "%Y-%m-%d")
        date_format = date_.strftime("%d/%m/%Y")

    except ValueError:
        raise ValueError("Data inválida")

    query_find = {"timestamp": date_format}
    news_db = search_news(query_find)
    list = []

    for item in news_db:
        list.append((item["title"], item["url"]))
    return list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
