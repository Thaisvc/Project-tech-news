import pytest
from unittest.mock import patch
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)


mock = [
    {
        "url": "https://blog.betrybe.com/tecnologia/metadados-tudo-sobre/",
        "title": "Notícia tech",
        "writer": "thais viana",
        "summary": "teste summary",
        "reading_time": 3,
        "timestamp": "01/01/2022",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/desenvolvimento-web/angular-cli/",
        "title": "Notícia tech 2",
        "writer": "Thais cunha",
        "summary": "teste summary 2",
        "reading_time": 1,
        "timestamp": "05/02/2023",
        "category": "Tecnologia 2",
    },
    {
        "url": "https://blog.betrybe.com/linguagem-de-programacao/",
        "title": "Notícia tech 3",
        "writer": "Thais",
        "summary": "teste summary 3",
        "reading_time": 45,
        "timestamp": "04/01/2022",
        "category": "Tecnologia 3",
    },
]


def test_reading_plan_group_news():
    with patch("tech_news.analyzer.reading_plan.find_news") as mock_find:
        mock_find.return_value = mock
        news = ReadingPlanService.group_news_for_available_time(10)

        assert len(news["readable"]) == 1
        assert len(news["unreadable"]) == 1

        assert news["readable"][0]["unfilled_time"] == 5

        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(0)
