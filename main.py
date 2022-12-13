import json
import random
from http import HTTPStatus
from typing import TypedDict

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, PlainTextResponse, Response
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

Word = str
Article = str


class Term(TypedDict):
    article: Article
    word: Word


with open("data/terms.json", encoding="utf-8") as f:
    terms: list[Term] = json.load(f)

    # For correctness checks:
    WORDS_TO_ARTICLES: dict[Word, Article] = {
        term["word"]: term["article"] for term in terms
    }

    # For random picking:
    WORDS = list(WORDS_TO_ARTICLES.keys())

    # For containment checks:
    ARTICLES = set(WORDS_TO_ARTICLES.values())

with open("index.html", encoding="utf-8") as f:
    index = f.read()


def random_word() -> str:
    return random.choice(WORDS)


async def home(request: Request) -> HTMLResponse:
    return HTMLResponse(content=index)


async def word(request: Request) -> PlainTextResponse:
    return PlainTextResponse(content=random_word())


async def choice(request: Request) -> HTMLResponse:
    # Doesn't implement `__match_args__`, so match more primitively for now.
    match request.query_params.multi_items():
        case [
            ("article", str(article)),
            ("word", str(word)),
        ] if article in ARTICLES and word in WORDS_TO_ARTICLES.keys():
            pass  # We gucci
        case _:
            return HTMLResponse(status_code=HTTPStatus.BAD_REQUEST)

    correct_article = WORDS_TO_ARTICLES[word]
    answered_correctly = article == correct_article

    row = f"""
    <div class="articles">
        <div class="incorrect{" hidden" if answered_correctly else ""}">
            {article}
        </div>
        <div class="correct">
            {correct_article}
        </div>
    </div>
    <div class="chosen-word">
        {word}
    </div>
    <div id="word" hx-swap-oob="innerHTML">{random_word()}</div>
    """
    return HTMLResponse(content=row)


class StaticCachingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        response = await call_next(request)
        if request.url.path.startswith("/static"):
            response.headers[
                "Cache-Control"
            ] = "public, max-age=604800, must-revalidate"
        return response


middleware = [
    Middleware(StaticCachingMiddleware),
    Middleware(GZipMiddleware),
]


routes = [
    Route("/", home, methods=["GET"]),
    Route("/word", word, methods=["GET"]),
    Route("/choice", choice, methods=["GET"]),
    Mount("/static", StaticFiles(directory="static")),
]

app = Starlette(routes=routes, middleware=middleware)
