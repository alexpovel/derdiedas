import json
import random
from http import HTTPStatus
from typing import TypedDict

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, PlainTextResponse
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
        term["word"]: term["article"].casefold() for term in terms
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
    form = await request.form()

    # `FormData` doesn't define `__match_args__`, so match more primitively for now.
    match form.multi_items():
        case [
            ("article", str(a)),
            ("word", str(w)),
        ] if (article := a.casefold()) in ARTICLES and w in WORDS_TO_ARTICLES.keys():
            pass  # We gucci
        case _:
            return HTMLResponse(status_code=HTTPStatus.BAD_REQUEST)

    correct_article = WORDS_TO_ARTICLES[w]
    answered_correctly = article == correct_article

    row = f"""
    <div class="articles">
        <div class="wrong{" hidden" if answered_correctly else ""}">
            {article}
        </div>
        <div class="correct">
            {correct_article}
        </div>
    </div>
    <div class="chosen-word">
        {w}
    </div>
    <div id="word" hx-swap-oob="innerHTML">{random_word()}</div>
    """
    return HTMLResponse(content=row)


routes = [
    Route("/", home, methods=["GET"]),
    Route("/word", word, methods=["GET"]),
    Route("/choice", choice, methods=["PATCH"]),
    Mount("/static", StaticFiles(directory="static")),
]

app = Starlette(routes=routes)
