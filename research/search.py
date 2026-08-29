"""Tavily retrieval client. This module performs no research reasoning."""

from __future__ import annotations

from typing import Any

from tavily import TavilyClient

from research.config import MAX_SOURCE_CHARS, TAVILY_MAX_RESULTS
from research.models import Source


class SearchError(RuntimeError):
    """Raised when Tavily retrieval fails."""


class TavilySearchClient:
    def __init__(self, api_key: str, client: Any | None = None) -> None:
        self.client = client or TavilyClient(api_key=api_key)

    def search(self, query: str) -> list[Source]:
        try:
            response = self.client.search(
                query=query,
                search_depth="basic",
                topic="general",
                max_results=TAVILY_MAX_RESULTS,
                include_answer=False,
                include_raw_content="markdown",
                include_images=False,
            )
        except Exception as exc:
            raise SearchError(f"Search failed: {exc}") from exc

        if not isinstance(response, dict):
            raise SearchError("Search failed: Tavily returned an unexpected response")

        normalized: list[Source] = []
        for result in response.get("results", []):
            if not isinstance(result, dict):
                continue
            url = str(result.get("url") or "").strip()
            raw_content = str(result.get("raw_content") or "").strip()
            fallback_content = str(result.get("content") or "").strip()
            content = raw_content or fallback_content
            if not url or not content:
                continue

            score = result.get("score")
            normalized.append(
                Source(
                    id="",  # The runner assigns the stable run-level source ID.
                    title=str(result.get("title") or "").strip() or url,
                    url=url,
                    content=content[:MAX_SOURCE_CHARS],
                    score=float(score) if score is not None else None,
                )
            )
        return normalized
