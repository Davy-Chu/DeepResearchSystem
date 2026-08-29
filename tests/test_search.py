from research.config import MAX_SOURCE_CHARS, TAVILY_MAX_RESULTS
from research.search import TavilySearchClient


class FakeTavily:
    def __init__(self) -> None:
        self.kwargs = {}

    def search(self, **kwargs):
        self.kwargs = kwargs
        return {
            "results": [
                {
                    "title": "Raw page",
                    "url": "https://example.com/raw",
                    "content": "short fallback",
                    "raw_content": "R" * (MAX_SOURCE_CHARS + 10),
                    "score": 0.75,
                },
                {
                    "title": "Fallback page",
                    "url": "https://example.com/fallback",
                    "content": "usable fallback",
                    "raw_content": "   ",
                    "score": None,
                },
                {
                    "title": "Unusable page",
                    "url": "https://example.com/empty",
                    "content": "",
                    "raw_content": None,
                    "score": 0.1,
                },
            ]
        }


def test_search_configuration_and_content_normalization() -> None:
    fake = FakeTavily()
    results = TavilySearchClient("test-key", client=fake).search("test query")

    assert fake.kwargs == {
        "query": "test query",
        "search_depth": "basic",
        "topic": "general",
        "max_results": TAVILY_MAX_RESULTS,
        "include_answer": False,
        "include_raw_content": "markdown",
        "include_images": False,
    }
    assert len(results) == 2
    assert results[0].content == "R" * MAX_SOURCE_CHARS
    assert results[1].content == "usable fallback"
