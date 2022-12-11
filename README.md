# derdiedas

A plain and simple, yet interactive and sleek website built with modern, yet [boring technology](https://mcfunley.com/choose-boring-technology):

- [htmx](https://htmx.org/)
- [CSS grid layouting](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [Python's FastAPI](https://fastapi.tiangolo.com/), served by [uvicorn](https://www.uvicorn.org/)
- [SVG animations](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animate)
- theming roughly inspired by [Material Theme](https://material-theme.com/)
- no (direct) JavaScript 😲😲😲
- some [GNU make](https://www.gnu.org/software/make/)

All this coming in at around 250 lines total.

## Setup

1. Install:
   1. Python 3.10+
   2. [poetry](https://python-poetry.org/)
   3. [make](https://www.gnu.org/software/make/)
2. Run:
   1. `poetry install`

      For best experience, issue `poetry config virtualenvs.in-project true` before this step, such that a `.venv` will be created in your current directory upon installation.
      This is generally easier for IDEs and tooling to pick up on.
   2. `make serverup`
