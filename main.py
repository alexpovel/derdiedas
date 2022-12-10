import json
import random
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

Word = str
Article = str


class Term(BaseModel):
    article: Article
    word: Word


with open("data/terms.json", encoding="utf-8") as f:
    WORDS_TO_ARTICLES: dict[Word, Article] = {
        item["word"]: item["article"] for item in json.load(f)
    }
    WORDS = list(WORDS_TO_ARTICLES.keys())
    ARTICLES = set(WORDS_TO_ARTICLES.values())


@app.get("/word", response_class=PlainTextResponse)
async def word():
    return random.choice(WORDS)


@app.patch("/choice", response_class=HTMLResponse)
async def choice(choice: Term):
    current_word = choice.word
    chosen_article = choice.article.lower()

    if current_word not in WORDS or chosen_article not in ARTICLES:
        return HTMLResponse(status_code=HTTPStatus.BAD_REQUEST.value)

    correct_article = WORDS_TO_ARTICLES[choice.word].lower()

    answered_correctly = chosen_article == correct_article

    row = f"""
    <tr>
        <td class="wrong">{'' if answered_correctly else chosen_article}</td>
        <td class="correct">{correct_article}</td>
        <td>{current_word}</td>
    </tr>
    <div id="word" hx-swap-oob="innerHTML">{await word()}</div>
    """
    return HTMLResponse(content=row)


# Catch the rest, needs to be defined last:
app.mount("/", StaticFiles(directory="static", html=True), name="static")
